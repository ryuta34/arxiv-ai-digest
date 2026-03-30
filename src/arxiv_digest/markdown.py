"""論文 Markdown ファイルの生成"""


def build_paper_md(title: str, arxiv_id: str, entry_id: str, summary: str, today: str) -> str:
    """個別論文の Markdown 文字列を構築する。"""
    safe_title = title.replace('"', "'")
    return f"""---
title: "{safe_title}"
date: {today}
arxiv_id: {arxiv_id}
url: {entry_id}
---

# {title}

{summary}
"""
