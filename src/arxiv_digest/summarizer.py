"""Gemini API による論文要約"""

from google import genai
from google.genai import types

from .config import GEMINI_MODEL, SUMMARY_PROMPT


def summarize_with_gemini(client: genai.Client, pdf_bytes: bytes, pdf_url: str) -> str:
    """Gemini API に PDF を渡して日本語要約表を取得する。"""
    prompt = SUMMARY_PROMPT.format(pdf_url=pdf_url)
    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=[
            types.Part.from_bytes(data=pdf_bytes, mime_type="application/pdf"),
            prompt,
        ],
    )
    return response.text.strip()
