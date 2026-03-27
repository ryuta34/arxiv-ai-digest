# arxiv-ai-digest

arXiv から毎日最新の AI 論文（最大5本）を自動取得し、Gemini API で日本語要約して Markdown ファイルを生成するリポジトリです。

## ディレクトリ構成

```
arxiv-ai-digest/
├── .github/
│   └── workflows/
│       └── daily_digest.yml   # GitHub Actions ワークフロー
├── scripts/
│   └── fetch_and_summarize.py # メインスクリプト
├── outputs_AI_papers/
│   ├── index.md               # 論文一覧インデックス
│   └── <arxiv_id>.md          # 論文ごとの要約ファイル
├── requirements.txt
└── README.md
```

---

## セットアップ手順

### 1. Gemini API キーの取得

1. [Google AI Studio](https://aistudio.google.com/app/apikey) にアクセス
2. 「Create API key」をクリックしてキーを発行
3. 発行された API キーをコピーしておく

### 2. GitHub Secrets への登録

1. このリポジトリの **Settings** → **Secrets and variables** → **Actions** を開く
2. 「New repository secret」をクリック
3. 以下を入力して保存:
   - **Name**: `GEMINI_API_KEY`
   - **Secret**: 手順1でコピーした API キー

### 3. GitHub Actions の有効化

リポジトリを GitHub に push すると、毎日 JST 06:00 に自動実行されます。

---

## 手動実行方法

### GitHub Actions から手動実行

1. リポジトリの **Actions** タブを開く
2. 左サイドバーから **Daily AI Paper Digest** を選択
3. 「Run workflow」ボタンをクリック → 「Run workflow」で実行

### ローカルで実行

```bash
# 依存ライブラリのインストール
pip install -r requirements.txt

# API キーを環境変数にセット
export GEMINI_API_KEY="your_api_key_here"

# スクリプト実行
python scripts/fetch_and_summarize.py
```

---

## Obsidian との連携 (obsidian-git プラグイン)

Obsidian の Vault 内にこのリポジトリをサブフォルダとして取り込み、論文要約を Obsidian で閲覧できます。

### 設定手順

1. **Community Plugins** から `obsidian-git` をインストール・有効化

2. Vault のルートまたは任意のフォルダ内で、このリポジトリをクローン:

   ```bash
   # 例: Vault 直下に "arxiv-ai-digest" フォルダとしてクローン
   cd /path/to/your/obsidian/vault
   git clone https://github.com/<your-username>/arxiv-ai-digest.git
   ```

3. Obsidian を再起動（または「Reload vault」）すると、`arxiv-ai-digest/outputs_AI_papers/` 内のファイルが Obsidian から参照できるようになります。

4. obsidian-git の設定で **Custom base path** を `arxiv-ai-digest` に設定し、自動 Pull 間隔（例: 60分）を指定しておくと、GitHub に push された最新要約が自動同期されます。

> **Tip**: `outputs_AI_papers/index.md` をホームノートやダッシュボードにリンクしておくと、一覧から各論文へ素早くアクセスできます。

---

## 生成されるファイルの例

### `outputs_AI_papers/<arxiv_id>.md`

```markdown
---
title: "Attention Is All You Need"
date: 2026-03-27
arxiv_id: 1706.03762
url: https://arxiv.org/abs/1706.03762
---

# Attention Is All You Need

| 項目 | 内容 |
|---|---|
| どんなもの？ | ... |
| 先行研究と比べてどこがすごい？ | ... |
...
```

### `outputs_AI_papers/index.md`

```markdown
# AI論文インデックス

| 日付 | タイトル | arXiv ID | リンク |
|---|---|---|---|
| 2026-03-27 | Attention Is All You Need | 1706.03762 | [リンク](./1706.03762.md) |
```
