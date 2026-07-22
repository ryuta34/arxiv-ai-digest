---
title: "Copy Less, Ground More: Overcoming Repetitive Copying in Long-Context Reasoning via Evidence-Aware Reinforcement Learning"
date: 2026-07-22
arxiv_id: 2607.19345v1
url: http://arxiv.org/abs/2607.19345v1
---

# Copy Less, Ground More: Overcoming Repetitive Copying in Long-Context Reasoning via Evidence-Aware Reinforcement Learning

| 項目 | 内容 |
|---|---|
| どんなもの？ | 長文脈推論を行う大規模言語モデル（LLM）において、入力プロンプトを無差別にコピーしてしまう「反復的コピー（Repetitive Copying）」という失敗モードを特定し、それを抑制するための強化学習手法「GEAR」を提案した研究。 |
| 先行研究と比べてどこがすごい？ | 従来手法が単なる正確性のみを報酬としていたのに対し、本手法は「証拠への接地（Grounding）」という観点を導入。タスクに関連する証拠への報酬と、無関係な文脈へのペナルティを組み合わせることで、推論の正確性を高めつつ、過剰な推論長を大幅に短縮した点。 |
| 技術や手法のキモはどこ？ | n-gram統計を用いた「GEAR報酬（Grounding Evidence-Aware Reward）」の導入。重要な証拠との重なりには報酬を与え、無関係な文脈（ディストラクター）との重なりにはペナルティを課すという報酬設計により、モデルに選択的な証拠抽出を学習させる点。 |
| どうやって有効だと検証した？ | GSM-Infinite等の長文脈ベンチマークを用い、Qwen3.5シリーズ等で検証。標準的な強化学習手法と比較して、平均で最大+4.6ポイントの精度向上を達成し、訓練時よりも4倍長い文脈に対しても高い汎用性を示した。 |
| 議論はある？ | 証拠のアノテーションがない自然言語データに対しては、自動構築パイプラインで対応しているものの、アノテーションの質や多様性に依存する可能性がある。また、非常に高い報酬を与えすぎた場合に、逆にモデルの推論行動が歪む可能性があることも示唆されている。 |
| 次に読むべき論文は？ | [DeepSeek-R1 (Guo et al., 2025)](https://arxiv.org/abs/2501.12948)、[LongRLVR (Chen et al., 2026)](https://arxiv.org/abs/2412.21187)、[GSM-Infinite (Zhou et al., 2025)](https://arxiv.org/abs/2502.05252) |
| PDFリンク | https://arxiv.org/pdf/2607.19345v1 |
