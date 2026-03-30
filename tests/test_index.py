"""index.md の読み書きのテスト"""

from pathlib import Path
import pytest
from arxiv_digest.index import (
    load_processed_ids,
    build_index_row,
    update_index,
    HEADER_SEP,
)


def test_load_processed_ids_no_file(tmp_path):
    result = load_processed_ids(tmp_path / "nonexistent.md")
    assert result == set()


def test_load_processed_ids_extracts_ids(tmp_path):
    index_file = tmp_path / "index.md"
    index_file.write_text(
        "| 日付 | タイトル | arXiv ID | リンク | 概要 |\n"
        "|---|---|---|---|---|\n"
        "| 2024-01-01 | Paper A | 2401.00001 | [リンク](./Paper_A.md) | 概要A |\n"
        "| 2024-01-02 | Paper B | 2401.00002v2 | [リンク](./Paper_B.md) | 概要B |\n",
        encoding="utf-8",
    )
    result = load_processed_ids(index_file)
    assert result == {"2401.00001", "2401.00002v2"}


def test_load_processed_ids_empty_file(tmp_path):
    index_file = tmp_path / "index.md"
    index_file.write_text("# AI論文インデックス\n", encoding="utf-8")
    result = load_processed_ids(index_file)
    assert result == set()


def test_build_index_row_format():
    row = build_index_row("2401.00001", "Test Paper", "2024-01-01", "Test_Paper.md", "テストの概要")
    assert "2401.00001" in row
    assert "Test Paper" in row
    assert "2024-01-01" in row
    assert "[リンク](./Test_Paper.md)" in row
    assert "テストの概要" in row


def test_build_index_row_escapes_pipe_in_title():
    row = build_index_row("2401.00001", "Title | Subtitle", "2024-01-01", "Title_Subtitle.md", "概要")
    # タイトル部分のパイプが全角に置換されていること
    assert "Title ｜ Subtitle" in row


def test_update_index_creates_new_file(tmp_path):
    index_file = tmp_path / "index.md"
    update_index(index_file, "2401.00001", "Test Paper", "2024-01-01", "Test_Paper.md", "テストの概要")

    content = index_file.read_text(encoding="utf-8")
    assert "AI論文インデックス" in content
    assert "2401.00001" in content
    assert "Test Paper" in content
    assert "概要" in content


def test_update_index_prepends_new_entry(tmp_path):
    index_file = tmp_path / "index.md"
    update_index(index_file, "2401.00001", "First Paper", "2024-01-01", "First_Paper.md", "概要1")
    update_index(index_file, "2401.00002", "Second Paper", "2024-01-02", "Second_Paper.md", "概要2")

    content = index_file.read_text(encoding="utf-8")
    # 新しい論文がヘッダー直下（先に）来ること
    pos_first = content.find("2401.00001")
    pos_second = content.find("2401.00002")
    assert pos_second < pos_first


def test_update_index_appends_when_no_header_sep(tmp_path):
    """HEADER_SEP がない既存ファイルにも追記できること。"""
    index_file = tmp_path / "index.md"
    index_file.write_text("# 古いファイル\n", encoding="utf-8")

    update_index(index_file, "2401.00001", "Test Paper", "2024-01-01", "Test_Paper.md", "概要")

    content = index_file.read_text(encoding="utf-8")
    assert "2401.00001" in content
