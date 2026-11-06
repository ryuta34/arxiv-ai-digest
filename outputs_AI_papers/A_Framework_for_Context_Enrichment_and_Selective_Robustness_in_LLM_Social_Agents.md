---
title: "A Framework for Context Enrichment and Selective Robustness in LLM Social Agents"
date: 2026-11-06
arxiv_id: 2611.06914v1
url: http://arxiv.org/abs/2611.06914v1
---

# A Framework for Context Enrichment and Selective Robustness in LLM Social Agents

| 項目 | 内容 |
|---|---|
| どんなもの？ | LLMエージェントによる社会シミュレーションの妥当性を評価するための「文脈エンリッチメント（背景情報の拡充）」フレームワーク。プロンプトへの背景情報の追加方法を体系化し、特定の社会変化に対するエージェントの行動変容を測定する手法を提案した。 |
| 先行研究と比べてどこがすごい？ | 「文脈の豊かさ」と「頑健性」の定義が曖昧だった従来の研究に対し、情報を機能別に分解した制御可能なエンリッチメントと、「選択的頑健性（Selective Robustness）」という新しい評価基準を導入した点。 |
| 技術や手法のキモはどこ？ | 文脈情報を「最小限」「中立的な埋め込み」「一般的な社会的背景」「記述的決定根拠」「規範的決定根拠」の5段階に分解し、表面的なプロンプトの変化には不変でありつつ、意思決定に関連する環境変化には適切に応答する能力を定量化した点。 |
| どうやって有効だと検証した？ | SiliSocSを用いた「囚人のジレンマ」型のシミュレーションにて2つのモデル（Sol, Terra）を評価。4種類の異なるプロンプト形式（文章、箇条書き、表、代替形式）を用いて、環境変化（地域的・個別的ルール）に対する応答と表面的な安定性を分析した。 |
| 議論はある？ | 実験が単一のシナリオと同一モデル系列に限定されている点、またプロンプトへの付加情報が「決定の根拠」と「環境の顕著性」のどちらに起因する影響かを完全には分離できていない点を課題として挙げている。 |
| 次に読むべき論文は？ | [SiliSocS: A composable workbench for reproducible LLM social simulation](https://arxiv.org/abs/2605.00197) |
| PDFリンク | https://arxiv.org/pdf/2611.06914v1 |
