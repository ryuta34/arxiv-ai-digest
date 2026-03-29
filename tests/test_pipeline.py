"""パイプライン処理のテスト"""

from pathlib import Path
from unittest.mock import MagicMock, patch
from arxiv_digest.pipeline import process_paper


def _make_paper(
    arxiv_id: str = "2401.00001",
    title: str = "Test Paper",
    pdf_url: str = "https://arxiv.org/pdf/2401.00001",
    entry_id: str = "https://arxiv.org/abs/2401.00001",
) -> MagicMock:
    paper = MagicMock()
    paper.get_short_id.return_value = arxiv_id
    paper.title = title
    paper.pdf_url = pdf_url
    paper.entry_id = entry_id
    return paper


def test_process_paper_creates_markdown_file(tmp_path):
    paper = _make_paper()
    client = MagicMock()

    with patch("arxiv_digest.pipeline.fetch_pdf_bytes", return_value=b"pdf"), \
         patch("arxiv_digest.pipeline.summarize_with_gemini", return_value="summary"):
        result = process_paper(client, paper, tmp_path, tmp_path / "index.md", "2024-01-01")

    assert result is True
    assert (tmp_path / "2401.00001.md").exists()


def test_process_paper_updates_index(tmp_path):
    paper = _make_paper()
    client = MagicMock()

    with patch("arxiv_digest.pipeline.fetch_pdf_bytes", return_value=b"pdf"), \
         patch("arxiv_digest.pipeline.summarize_with_gemini", return_value="summary"):
        process_paper(client, paper, tmp_path, tmp_path / "index.md", "2024-01-01")

    assert (tmp_path / "index.md").exists()
    content = (tmp_path / "index.md").read_text(encoding="utf-8")
    assert "2401.00001" in content


def test_process_paper_returns_false_on_fetch_error(tmp_path):
    paper = _make_paper()
    client = MagicMock()

    with patch("arxiv_digest.pipeline.fetch_pdf_bytes", side_effect=Exception("Network error")):
        result = process_paper(client, paper, tmp_path, tmp_path / "index.md", "2024-01-01")

    assert result is False
    assert not (tmp_path / "2401.00001.md").exists()


def test_process_paper_returns_false_on_gemini_error(tmp_path):
    paper = _make_paper()
    client = MagicMock()

    with patch("arxiv_digest.pipeline.fetch_pdf_bytes", return_value=b"pdf"), \
         patch("arxiv_digest.pipeline.summarize_with_gemini", side_effect=Exception("API error")):
        result = process_paper(client, paper, tmp_path, tmp_path / "index.md", "2024-01-01")

    assert result is False
