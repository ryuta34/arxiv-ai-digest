"""Markdown 生成のテスト"""

from arxiv_digest.markdown import build_paper_md, title_to_filename


def test_build_paper_md_contains_frontmatter():
    md = build_paper_md("Test Title", "2401.00001", "https://arxiv.org/abs/2401.00001", "summary", "2024-01-01")
    assert "---" in md
    assert "arxiv_id: 2401.00001" in md
    assert "date: 2024-01-01" in md
    assert "url: https://arxiv.org/abs/2401.00001" in md


def test_build_paper_md_contains_title_as_heading():
    md = build_paper_md("Test Title", "2401.00001", "https://arxiv.org/abs/2401.00001", "summary", "2024-01-01")
    assert "# Test Title" in md


def test_build_paper_md_contains_summary():
    md = build_paper_md("Title", "2401.00001", "https://arxiv.org/abs/2401.00001", "| 項目 | 内容 |", "2024-01-01")
    assert "| 項目 | 内容 |" in md


def test_build_paper_md_escapes_double_quotes_in_title():
    md = build_paper_md('Title with "Quotes"', "2401.00001", "https://arxiv.org/abs/2401.00001", "summary", "2024-01-01")
    # frontmatter の title フィールドにダブルクォートが含まれないこと
    frontmatter = md.split("---")[1]
    assert '"Quotes"' not in frontmatter
    assert "'Quotes'" in frontmatter


def test_title_to_filename_basic():
    assert title_to_filename("Test Paper") == "Test_Paper"


def test_title_to_filename_removes_invalid_chars():
    result = title_to_filename("Paper: A/B Study?")
    assert "/" not in result
    assert ":" not in result
    assert "?" not in result


def test_title_to_filename_truncates():
    long_title = "A" * 200
    assert len(title_to_filename(long_title)) <= 100


def test_title_to_filename_strips_edges():
    assert title_to_filename("  Paper  ") == "Paper"
