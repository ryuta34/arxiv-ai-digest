"""
arXiv AI論文の取得・Gemini APIによる日本語要約・Markdown生成スクリプト
"""

import arxiv
import base64
import os
import re
import sys
import traceback
from datetime import date
from pathlib import Path

import requests
from google import genai
from google.genai import types


# ---- 定数 ----------------------------------------------------------------
SEARCH_CATEGORIES = ["cs.AI", "cs.CL", "cs.CV", "cs.LG"]
MAX_RESULTS = 5
OUTPUT_DIR = Path(__file__).parent.parent / "outputs_AI_papers"
INDEX_FILE = OUTPUT_DIR / "index.md"

SUMMARY_PROMPT = """
以下の論文PDFを読み、日本語で要約してください。
必ず下記のMarkdown表形式のみで回答し、余分な文章は出力しないでください。

| 項目 | 内容 |
|---|---|
| どんなもの？ | （概要を2〜3文で） |
| 先行研究と比べてどこがすごい？ | （新規性・優位性） |
| 技術や手法のキモはどこ？ | （核心的なアイデア） |
| どうやって有効だと検証した？ | （実験・評価方法） |
| 議論はある？ | （限界・課題・将来課題） |
| 次に読むべき論文は？ | （関連論文をリンク付きで） |
| PDFリンク | {pdf_url} |
"""

GEMINI_MODEL = "gemini-2.0-flash"


# ---- ヘルパー関数 ---------------------------------------------------------

def load_processed_ids() -> set[str]:
    """index.md から処理済み arXiv ID を取得する。"""
    if not INDEX_FILE.exists():
        return set()
    content = INDEX_FILE.read_text(encoding="utf-8")
    # テーブル行の arXiv ID 列（例: | 2024.01234 | ...）を抽出
    ids = set(re.findall(r"\|\s*([\d]{4}\.\d{4,5}(?:v\d+)?)\s*\|", content))
    return ids


def fetch_pdf_base64(pdf_url: str) -> bytes:
    """arXiv PDF を取得して bytes を返す（base64 エンコードは genai が行う）。"""
    resp = requests.get(pdf_url, timeout=60)
    resp.raise_for_status()
    return resp.content


def summarize_with_gemini(client: genai.Client, pdf_bytes: bytes, pdf_url: str) -> str:
    """Gemini API に PDF を渡して日本語要約表を取得する。"""

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=[
            types.Part.from_bytes(data=pdf_bytes, mime_type="application/pdf"),
            SUMMARY_PROMPT.format(pdf_url=pdf_url),
        ],
    )
    return response.text.strip()


def build_paper_md(paper: arxiv.Result, summary: str, today: str) -> str:
    """個別論文の Markdown 文字列を構築する。"""
    arxiv_id = paper.get_short_id()
    return f"""---
title: "{paper.title.replace('"', "'")}"
date: {today}
arxiv_id: {arxiv_id}
url: {paper.entry_id}
---

# {paper.title}

{summary}
"""


def update_index(paper: arxiv.Result, today: str) -> None:
    """index.md にエントリを追記（新しい順）する。存在しなければ新規作成。"""
    arxiv_id = paper.get_short_id()
    safe_title = paper.title.replace("|", "｜")
    new_row = f"| {today} | {safe_title} | {arxiv_id} | [リンク](./{arxiv_id}.md) |"
 
    if INDEX_FILE.exists():
        content = INDEX_FILE.read_text(encoding="utf-8")
        header_sep = "|---|---|---|---|"
        if header_sep in content:
            content = content.replace(
                header_sep,
                header_sep + "\n" + new_row,
                1,
            )
        else:
            content += "\n" + new_row + "\n"
    else:
        content = (
            "# AI論文インデックス\n\n"
            "| 日付 | タイトル | arXiv ID | リンク |\n"
            "|---|---|---|---|\n"
            f"{new_row}\n"
        )
 
    INDEX_FILE.write_text(content, encoding="utf-8")
 
 
# ---- メイン処理 -----------------------------------------------------------
 
def main() -> None:
    today = date.today().isoformat()
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
 
    # Gemini クライアント初期化
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("ERROR: GEMINI_API_KEY が設定されていません。", file=sys.stderr)
        sys.exit(1)
    client = genai.Client(api_key=api_key)
 
    # 処理済み ID の読み込み
    processed_ids = load_processed_ids()
    print(f"処理済み論文数: {len(processed_ids)}")
 
    # arXiv 検索クエリ
    query = " OR ".join(f"cat:{c}" for c in SEARCH_CATEGORIES)
    search = arxiv.Search(
        query=query,
        max_results=MAX_RESULTS,  # FIX: 3倍取得をやめてレート制限を回避
        sort_by=arxiv.SortCriterion.SubmittedDate,
        sort_order=arxiv.SortOrder.Descending,
    )
 
    new_papers: list[arxiv.Result] = []
    client_arxiv = arxiv.Client(delay_seconds=5, num_retries=3)  # FIX: レート制限対策
 
    for paper in client_arxiv.results(search):
        arxiv_id = paper.get_short_id()
        if arxiv_id in processed_ids:
            print(f"スキップ（処理済み）: {arxiv_id}")
            continue
        new_papers.append(paper)
        if len(new_papers) >= MAX_RESULTS:
            break
 
    if not new_papers:
        print("本日の新着論文はありませんでした。")
        return
 
    print(f"新着論文数: {len(new_papers)}")
 
    for paper in new_papers:
        arxiv_id = paper.get_short_id()
        print(f"\n処理中: [{arxiv_id}] {paper.title}")
 
        pdf_url = paper.pdf_url
        out_path = OUTPUT_DIR / f"{arxiv_id}.md"
 
        try:
            print("  PDF を取得中...")
            pdf_bytes = fetch_pdf_base64(pdf_url)
 
            print("  Gemini API で要約中...")
            summary = summarize_with_gemini(client, pdf_bytes, pdf_url)
 
            paper_md = build_paper_md(paper, summary, today)
            out_path.write_text(paper_md, encoding="utf-8")
            print(f"  保存: {out_path}")
 
            update_index(paper, today)
            print("  index.md を更新しました。")
 
        except Exception as e:
            print(f"  ERROR: {arxiv_id} の処理をスキップします: {e}", file=sys.stderr)
            traceback.print_exc()
            continue
 
    print("\n完了。")

if __name__ == "__main__":
    try:
        main()
    except Exception:
        traceback.print_exc()
        sys.exit(1)
