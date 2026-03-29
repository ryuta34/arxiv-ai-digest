# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Project Does

`arxiv-ai-digest` is an automated daily digest system that fetches recent AI/ML papers from arXiv, generates Japanese summaries using Google Gemini, and stores them as markdown files. It runs on a daily GitHub Actions schedule and commits the output back to the repository, designed to integrate with an Obsidian vault via obsidian-git.

## Running the Script

```bash
# Install dependencies
pip install -r requirements.txt

# Set API key
export GEMINI_API_KEY="your_api_key_here"

# Run
python scripts/fetch_and_summarize.py
```

## Running Tests

```bash
# Run all tests
pytest tests/ -v

# Run a single test file
pytest tests/test_index.py -v

# Run a single test
pytest tests/test_index.py::test_load_processed_ids_extracts_ids -v
```

## Architecture

```
src/arxiv_digest/        # パッケージ本体
  config.py              # 定数（SEARCH_CATEGORIES, MAX_RESULTS, GEMINI_MODEL, SUMMARY_PROMPT）
  index.py               # index.md の読み書き（load_processed_ids, update_index）
  arxiv_client.py        # arXiv API 検索（build_query, fetch_new_papers）
  pdf_client.py          # PDF ダウンロード（fetch_pdf_bytes）
  summarizer.py          # Gemini API 要約（summarize_with_gemini）
  markdown.py            # Markdown 生成（build_paper_md）
  pipeline.py            # 処理統合（process_paper, run）
scripts/
  fetch_and_summarize.py # エントリポイント（run() を呼ぶだけ）
tests/                   # 各モジュール対応のユニットテスト
conftest.py              # pytest 用 sys.path 設定（src/ を追加）
```

**処理フロー:**
1. `index.md` を読んで処理済み arXiv ID を取得（重複排除）
2. arXiv API で `cs.AI / cs.CL / cs.CV / cs.LG` の最新論文を検索
3. 未処理論文の PDF を取得し Gemini 2.0 Flash で日本語要約を生成
4. `outputs_AI_papers/{arxiv_id}.md` に保存、`index.md` を更新

**GitHub Actions:**
- `test.yml`: push / PR 時に `pytest tests/` を自動実行
- `daily_digest.yml`: 毎日 21:00 UTC に論文取得スクリプトを実行し結果をコミット

## Key Configuration Constants (in `src/arxiv_digest/config.py`)

- `MAX_RESULTS = 5` — 1回の実行で取得する論文数（arXiv レート制限対策）
- `GEMINI_MODEL = "gemini-2.0-flash"`
- `SEARCH_CATEGORIES = ["cs.AI", "cs.CL", "cs.CV", "cs.LG"]`

## Output Format

- `outputs_AI_papers/{arxiv_id}.md` — YAML frontmatter + Gemini 生成の日本語要約表
- `outputs_AI_papers/index.md` — 全論文のインデックス（新しい順）

## Secrets

- `GEMINI_API_KEY` を GitHub repository secrets に設定する必要あり
