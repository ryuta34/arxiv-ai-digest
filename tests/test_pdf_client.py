"""PDF ダウンロードのテスト"""

import pytest
import requests
from unittest.mock import MagicMock, patch
from arxiv_digest.pdf_client import fetch_pdf_bytes


def test_fetch_pdf_bytes_returns_content():
    mock_resp = MagicMock()
    mock_resp.content = b"%PDF-1.4 fake content"
    mock_resp.raise_for_status.return_value = None

    with patch("arxiv_digest.pdf_client.requests.get", return_value=mock_resp) as mock_get:
        result = fetch_pdf_bytes("https://arxiv.org/pdf/2401.00001")

    assert result == b"%PDF-1.4 fake content"
    mock_get.assert_called_once_with("https://arxiv.org/pdf/2401.00001", timeout=60)


def test_fetch_pdf_bytes_uses_custom_timeout():
    mock_resp = MagicMock()
    mock_resp.content = b"data"
    mock_resp.raise_for_status.return_value = None

    with patch("arxiv_digest.pdf_client.requests.get", return_value=mock_resp) as mock_get:
        fetch_pdf_bytes("https://arxiv.org/pdf/2401.00001", timeout=30)

    mock_get.assert_called_once_with("https://arxiv.org/pdf/2401.00001", timeout=30)


def test_fetch_pdf_bytes_raises_on_http_error():
    mock_resp = MagicMock()
    mock_resp.raise_for_status.side_effect = requests.HTTPError("404 Not Found")

    with patch("arxiv_digest.pdf_client.requests.get", return_value=mock_resp):
        with pytest.raises(requests.HTTPError):
            fetch_pdf_bytes("https://arxiv.org/pdf/bad_id")
