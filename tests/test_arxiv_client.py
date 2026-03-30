"""arXiv クライアントのテスト"""

from unittest.mock import MagicMock, patch
from arxiv_digest.arxiv_client import build_query, fetch_new_papers


def test_build_query_single_category():
    assert build_query(["cs.AI"]) == "cat:cs.AI"


def test_build_query_multiple_categories():
    result = build_query(["cs.AI", "cs.CL", "cs.LG"])
    assert result == "cat:cs.AI OR cat:cs.CL OR cat:cs.LG"


def _make_paper(arxiv_id: str, title: str = "Test Title") -> MagicMock:
    paper = MagicMock()
    paper.get_short_id.return_value = arxiv_id
    paper.title = title
    return paper


def test_fetch_new_papers_skips_processed_ids():
    paper_new = _make_paper("2401.00001")
    paper_processed = _make_paper("2401.00002")

    with patch("arxiv_digest.arxiv_client.arxiv.Client") as mock_client_cls, \
         patch("arxiv_digest.arxiv_client.arxiv.Search"):
        mock_client = MagicMock()
        mock_client.results.return_value = iter([paper_processed, paper_new])
        mock_client_cls.return_value = mock_client

        result = fetch_new_papers(["cs.AI"], max_results=5, processed_ids={"2401.00002"})

    assert len(result) == 1
    assert result[0].get_short_id() == "2401.00001"


def test_fetch_new_papers_respects_max_results():
    papers = [_make_paper(f"2401.{i:05d}") for i in range(10)]

    with patch("arxiv_digest.arxiv_client.arxiv.Client") as mock_client_cls, \
         patch("arxiv_digest.arxiv_client.arxiv.Search"):
        mock_client = MagicMock()
        mock_client.results.return_value = iter(papers)
        mock_client_cls.return_value = mock_client

        result = fetch_new_papers(["cs.AI"], max_results=3, processed_ids=set())

    assert len(result) == 3


def test_fetch_new_papers_returns_empty_when_all_processed():
    paper = _make_paper("2401.00001")

    with patch("arxiv_digest.arxiv_client.arxiv.Client") as mock_client_cls, \
         patch("arxiv_digest.arxiv_client.arxiv.Search"):
        mock_client = MagicMock()
        mock_client.results.return_value = iter([paper])
        mock_client_cls.return_value = mock_client

        result = fetch_new_papers(["cs.AI"], max_results=5, processed_ids={"2401.00001"})

    assert result == []


def test_fetch_new_papers_returns_empty_on_no_results():
    with patch("arxiv_digest.arxiv_client.arxiv.Client") as mock_client_cls, \
         patch("arxiv_digest.arxiv_client.arxiv.Search"):
        mock_client = MagicMock()
        mock_client.results.return_value = iter([])
        mock_client_cls.return_value = mock_client

        result = fetch_new_papers(["cs.AI"], max_results=5, processed_ids=set())

    assert result == []
