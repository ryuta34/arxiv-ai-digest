---
title: "Adaptive Critical Token-Aware Retrieval for Repository-Level Code Generation"
date: 2026-09-02
arxiv_id: 2609.01601v1
url: http://arxiv.org/abs/2609.01601v1
---

# Adaptive Critical Token-Aware Retrieval for Repository-Level Code Generation

| 項目 | 内容 |
|---|---|
| どんなもの？ | リポジトリレベルのコード生成において、生成プロセス中に「決定的なミスを誘発しやすいトークン（クリティカル・トークン）」を動的に特定し、その時点で必要なコンテキストのみをターゲットとして取得（Retrieval）する適応型フレームワーク「ACTOR」を提案した。 |
| 先行研究と比べてどこがすごい？ | 従来のRAGが生成前に静的かつ一括でコンテキストを取得していたのに対し、ACTORは生成途中の隠れ状態から重要箇所を特定し、必要な時だけ動的に再検索を行うため、より高精度で効率的かつ適応性の高い生成を実現した。 |
| 技術や手法のキモはどこ？ | モデルの隠れ状態から「トークンの不一致」「不確実性（エントロピー）」「後続トークンへの注目度」を基にクリティカル・トークンを特定する手法、および取得したコンテキストの重要度を前後端で重み付けする「Position-Aware Weighting」手法。 |
| どうやって有効だと検証した？ | RepoExecおよびCoderEvalという2つのリポジトリレベルのコード生成ベンチマークを使用し、複数のLLM（DeepSeek-Coder、CodeLlama）で実験。ベースラインを大幅に上回る性能（最大15.4%の改善）を確認した。 |
| 議論はある？ | クリティカル・トークンの判定はあくまで予測に基づくため、一部の決定的な箇所を見逃す可能性があることや、動的な検索に伴うKVキャッシュ再計算等の計算オーバーヘッドを将来的に最適化する必要があるとしている。 |
| 次に読むべき論文は？ | [10] RepoCoder: Repository-level code completion through iterative retrieval and generation, [14] Repository-level prompt generation for large language models of code |
| PDFリンク | https://arxiv.org/pdf/2609.01601v1 |
