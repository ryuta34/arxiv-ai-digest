---
title: "Learning to Stop without Learning to Stop: Self-Supervised Confidence Training Improves Reasoning Efficiency"
date: 2026-09-29
arxiv_id: 2609.31619v1
url: http://arxiv.org/abs/2609.31619v1
---

# Learning to Stop without Learning to Stop: Self-Supervised Confidence Training Improves Reasoning Efficiency

| 項目 | 内容 |
|---|---|
| どんなもの？ | LLMの推論効率を向上させるための新しい自己教師ありファインチューニング手法「ConfSFT」を提案。推論の効率化や停止を直接目的とせず、中間推論ステップにおけるモデル自身の自信度（Confidence）を予測するように訓練することで、推論時の生成トークン数を削減する。 |
| 先行研究と比べてどこがすごい？ | 強化学習による長さへのペナルティや推論時の早期終了ルール（Early-stopping）といった明示的な効率化策を用いずに、モデル自身のメタ認知的な自信度を学習させるだけで、同等の精度を維持しつつ推論コストを最大25%削減できる点。 |
| 技術や手法のキモはどこ？ | モデルの中間推論状態における回答の尤度（自信度）を自己生成し、それを予測するようにfine-tuningを行うこと。推論効率や終了条件を最適化目標に含めず、純粋に自信度予測のみを学習させることで、結果として効率的な推論が「創発」する仕組み。 |
| どうやって有効だと検証した？ | Gemma、Qwen、Nemotron、GPT-OSSの4モデルを用い、数学（AIME等）、科学（GPQA）、コード（LiveCodeBench等）の各ベンチマークで評価。既存の効率化手法（RL等）と比較し、精度を維持しながらトークン生成数を有意に削減できることを示した。 |
| 議論はある？ | ConfSFTの効率化はあくまで推論コストの削減に留まり、特定の推論ステップの抑制ではなく全体の再構成を誘発する。また、判断ポイントとなるマーカー（Wait等）への依存性や、更なる効率化に向けた学習の安定性が今後の検討事項となる。 |
| 次に読むべき論文は？ | [Step-grpo: Internalizing dynamic early exit for efficient reasoning](https://arxiv.org/abs/2604.16890) や [Thinkprune: Pruning long chain-of-thought of llms via reinforcement learning](https://arxiv.org/abs/2504.01296) |
| PDFリンク | https://arxiv.org/pdf/2609.31619v1 |
