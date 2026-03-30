"""index.md の読み書き"""

import re
from pathlib import Path

HEADER_SEP = "|---|---|---|---|---|"
INDEX_HEADER = (
    "# AI論文インデックス\n\n"
    "| 日付 | タイトル | arXiv ID | リンク | 概要 |\n"
    f"{HEADER_SEP}\n"
)


def load_processed_ids(index_file: Path) -> set[str]:
    """index.md から処理済み arXiv ID を取得する。"""
    if not index_file.exists():
        return set()
    content = index_file.read_text(encoding="utf-8")
    return set(re.findall(r"\|\s*([\d]{4}\.\d{4,5}(?:v\d+)?)\s*\|", content))


def build_index_row(arxiv_id: str, title: str, today: str, filename: str, overview: str) -> str:
    """index.md に追加する1行を生成する。"""
    safe_title = title.replace("|", "｜")
    safe_overview = overview.replace("|", "｜")
    return f"| {today} | {safe_title} | {arxiv_id} | [リンク](./{filename}) | {safe_overview} |"


def update_index(index_file: Path, arxiv_id: str, title: str, today: str, filename: str, overview: str) -> None:
    """index.md にエントリをヘッダー直下（新しい順）に追記する。なければ新規作成。"""
    new_row = build_index_row(arxiv_id, title, today, filename, overview)

    if index_file.exists():
        content = index_file.read_text(encoding="utf-8")
        if HEADER_SEP in content:
            content = content.replace(HEADER_SEP, HEADER_SEP + "\n" + new_row, 1)
        else:
            content += "\n" + new_row + "\n"
    else:
        content = INDEX_HEADER + new_row + "\n"

    index_file.write_text(content, encoding="utf-8")
