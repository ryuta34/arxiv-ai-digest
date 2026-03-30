"""arXiv PDF のダウンロード"""

import requests


def fetch_pdf_bytes(pdf_url: str, timeout: int = 60) -> bytes:
    """arXiv PDF を取得して bytes を返す。"""
    resp = requests.get(pdf_url, timeout=timeout)
    resp.raise_for_status()
    return resp.content
