"""
arXiv AI論文の取得・Gemini APIによる日本語要約・Markdown生成スクリプト
"""
import sys
import traceback
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from arxiv_digest.pipeline import run

if __name__ == "__main__":
    try:
        run()
    except Exception:
        traceback.print_exc()
        sys.exit(1)
