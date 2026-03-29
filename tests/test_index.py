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
        "| 日付 | タイトル | arXiv ID | リンク |\n"
        "|---|---|---|---|\n"
        "| 2024-01-01 | Paper A | 2401.00001 | [リンク](./2401.00001.md) |\n"
        "| 2024-01-02 | Paper B | 2401.00002v2 | [リンク](./2401.00002v2.md) |\n",
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
    row = build_index_row("2401.00001", "Test Paper", "2024-01-01")
    assert "2401.00001" in row
    assert "Test Paper" in row
    assert "2024-01-01" in row
    assert "[リンク](./2401.00001.md)" in row


def test_build_index_row_escapes_pipe_in_title():
    row = build_index_row("2401.00001", "Title | Subtitle", "2024-01-01")
    # タイトル部分のパイプが全角に置換されていること
    assert "Title ｜ Subtitle" in row


def test_update_index_creates_new_file(tmp_path):
    index_file = tmp_path / "index.md"
    update_index(index_file, "2401.00001", "Test Paper", "2024-01-01")

    content = index_file.read_text(encoding="utf-8")
    assert "AI論文インデックス" in content
    assert "2401.00001" in content
    assert "Test Paper" in content


def test_update_index_prepends_new_entry(tmp_path):
    index_file = tmp_path / "index.md"
    update_index(index_file, "2401.00001", "First Paper", "2024-01-01")
    update_index(index_file, "2401.00002", "Second Paper", "2024-01-02")

    content = index_file.read_text(encoding="utf-8")
    # 新しい論文がヘッダー直下（先に）来ること
    pos_first = content.find("2401.00001")
    pos_second = content.find("2401.00002")
    assert pos_second < pos_first


def test_update_index_appends_when_no_header_sep(tmp_path):
    """HEADER_SEP がない既存ファイルにも追記できること。"""
    index_file = tmp_path / "index.md"
    index_file.write_text("# 古いファイル\n", encoding="utf-8")

    update_index(index_file, "2401.00001", "Test Paper", "2024-01-01")

    content = index_file.read_text(encoding="utf-8")
    assert "2401.00001" in content
