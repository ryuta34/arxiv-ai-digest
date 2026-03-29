"""メイン処理パイプライン"""

import os
import sys
import traceback
from datetime import date
from pathlib import Path

import arxiv
from google import genai

from .config import SEARCH_CATEGORIES, MAX_RESULTS
from .index import load_processed_ids, update_index
from .arxiv_client import fetch_new_papers
from .pdf_client import fetch_pdf_bytes
from .summarizer import summarize_with_gemini
from .markdown import build_paper_md

DEFAULT_OUTPUT_DIR = Path(__file__).parent.parent.parent / "outputs_AI_papers"


def process_paper(
    client: genai.Client,
    paper: arxiv.Result,
    output_dir: Path,
    index_file: Path,
    today: str,
) -> bool:
    """1論文を処理する。成功したら True を返す。"""
    arxiv_id = paper.get_short_id()
    print(f"\n処理中: [{arxiv_id}] {paper.title}")

    try:
        print("  PDF を取得中...")
        pdf_bytes = fetch_pdf_bytes(paper.pdf_url)

        print("  Gemini API で要約中...")
        summary = summarize_with_gemini(client, pdf_bytes, paper.pdf_url)

        paper_md = build_paper_md(paper.title, arxiv_id, paper.entry_id, summary, today)
        out_path = output_dir / f"{arxiv_id}.md"
        out_path.write_text(paper_md, encoding="utf-8")
        print(f"  保存: {out_path}")

        update_index(index_file, arxiv_id, paper.title, today)
        print("  index.md を更新しました。")

        return True

    except Exception as e:
        print(f"  ERROR: {arxiv_id} の処理をスキップします: {e}", file=sys.stderr)
        traceback.print_exc()
        return False


def run(output_dir: Path = DEFAULT_OUTPUT_DIR) -> None:
    """メイン処理。"""
    today = date.today().isoformat()
    index_file = output_dir / "index.md"
    output_dir.mkdir(parents=True, exist_ok=True)

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("ERROR: GEMINI_API_KEY が設定されていません。", file=sys.stderr)
        sys.exit(1)
    client = genai.Client(api_key=api_key)

    processed_ids = load_processed_ids(index_file)
    print(f"処理済み論文数: {len(processed_ids)}")

    new_papers = fetch_new_papers(SEARCH_CATEGORIES, MAX_RESULTS, processed_ids)

    if not new_papers:
        print("本日の新着論文はありませんでした。")
        return

    print(f"新着論文数: {len(new_papers)}")

    for paper in new_papers:
        process_paper(client, paper, output_dir, index_file, today)

    print("\n完了。")
