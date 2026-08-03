---
title: "ExtractBench: A Benchmark for Schema-Guided Enterprise Document Extraction"
date: 2026-08-03
arxiv_id: 2607.29677v1
url: http://arxiv.org/abs/2607.29677v1
---

# ExtractBench: A Benchmark for Schema-Guided Enterprise Document Extraction

| 項目 | 内容 |
|---|---|
| どんなもの？ | 企業向けドキュメントにおけるスキーマ駆動型データ抽出のための包括的ベンチマーク「ExtractBench」を提案した論文。文書の抽出精度、データの接地性（グラウンディング）、およびコストを総合的に評価する初の枠組みを提供している。 |
| 先行研究と比べてどこがすごい？ | 従来手法が固定的なテンプレートや単一の評価軸に限定されていたのに対し、本手法は4,869ページ、370文書、8ドメインにわたる実データを用い、長大なレコードの網羅性、スキャン・手書き対応、コスト効率を包括的に測定できる点。 |
| 技術や手法のキモはどこ？ | 独立した5つの評価軸（タスク難易度、認識難易度、表構造、長さ、ビジネスドメイン）によるタグ付けと、モデルアンサンブル、プログラム生成、人間による検証を組み合わせた高品質な教師データ作成パイプラインを構築したこと。 |
| どうやって有効だと検証した？ | 商用VLM、OSSパイプライン、コーディングエージェントなど計14種類のシステムを比較評価。LlamaExtract Agentic Plusが精度とコストのバランスにおいて最も優れていることを実証した。 |
| 議論はある？ | 最高の精度を誇るシステムでも、テキスト情報の正確な根拠（ワードレベルの接地性）を提示する能力は依然として50%未満であり、自動抽出の完全な信頼性確保にはまだ課題が残っている。 |
| 次に読むべき論文は？ | [12] ExtractBench: A benchmark and evaluation methodology for complex structured extraction (https://arxiv.org/abs/2602.12247) |
| PDFリンク | https://arxiv.org/pdf/2607.29677v1 |
