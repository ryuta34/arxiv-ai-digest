"""Gemini 要約のテスト"""

from unittest.mock import MagicMock
from arxiv_digest.summarizer import summarize_with_gemini


def test_summarize_returns_stripped_text():
    mock_client = MagicMock()
    mock_client.models.generate_content.return_value.text = "  | 項目 | 内容 |\n  "

    result = summarize_with_gemini(mock_client, b"pdf_bytes", "https://arxiv.org/pdf/2401.00001")

    assert result == "| 項目 | 内容 |"


def test_summarize_passes_pdf_url_in_prompt():
    mock_client = MagicMock()
    mock_client.models.generate_content.return_value.text = "summary"

    pdf_url = "https://arxiv.org/pdf/2401.00001"
    summarize_with_gemini(mock_client, b"pdf_bytes", pdf_url)

    call_kwargs = mock_client.models.generate_content.call_args.kwargs
    contents = call_kwargs["contents"]
    # プロンプト文字列（contents[1]）に URL が含まれること
    assert pdf_url in contents[1]


def test_summarize_calls_correct_model():
    from arxiv_digest.config import GEMINI_MODEL

    mock_client = MagicMock()
    mock_client.models.generate_content.return_value.text = "summary"

    summarize_with_gemini(mock_client, b"pdf_bytes", "https://arxiv.org/pdf/2401.00001")

    call_kwargs = mock_client.models.generate_content.call_args.kwargs
    assert call_kwargs["model"] == GEMINI_MODEL
