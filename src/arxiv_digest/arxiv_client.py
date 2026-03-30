"""arXiv API からの論文取得"""

import arxiv


def build_query(categories: list[str]) -> str:
    """カテゴリリストから arXiv 検索クエリ文字列を構築する。"""
    return " OR ".join(f"cat:{c}" for c in categories)


def fetch_new_papers(
    categories: list[str],
    max_results: int,
    processed_ids: set[str],
) -> list[arxiv.Result]:
    """arXiv から未処理の論文を最大 max_results 件取得する。"""
    query = build_query(categories)
    search = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.SubmittedDate,
        sort_order=arxiv.SortOrder.Descending,
    )
    client = arxiv.Client(delay_seconds=5, num_retries=3)

    new_papers: list[arxiv.Result] = []
    for paper in client.results(search):
        if paper.get_short_id() in processed_ids:
            print(f"スキップ（処理済み）: {paper.get_short_id()}")
            continue
        new_papers.append(paper)
        if len(new_papers) >= max_results:
            break

    return new_papers
