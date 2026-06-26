---
title: "Ask, Solve, Generate: Self-Evolving Unified Multimodal Understanding and Generation via Self-Consistency Rewards"
date: 2026-06-26
arxiv_id: 2606.27376v1
url: http://arxiv.org/abs/2606.27376v1
---

# Ask, Solve, Generate: Self-Evolving Unified Multimodal Understanding and Generation via Self-Consistency Rewards

| 項目 | 内容 |
|---|---|
| どんなもの？ | 視覚理解と画像生成を統合したモデル（LMM）において、人間によるラベル付けや外部報酬モデルを用いず、ラベルなし画像のみを用いて自律的に両能力を改善する「自己進化型（Self-Evolving）」学習フレームワーク。 |
| 先行研究と比べてどこがすごい？ | 外部の教師データや報酬モデルに依存せず、Proposer（質問生成）、Solver（解答・評価）、Generator（画像生成）という3つの役割をLoRAで実装することで、アーキテクチャ（拡散モデル、Rectified-Flow、自己回帰）を問わず汎用的に適用・改善可能である点。 |
| 技術や手法のキモはどこ？ | 自己整合性（Self-Consistency）に加え、解答生成時の予測不確実性を捉える「Solver Token Entropy (STE)」を用いた難易度調整、および理解モデルが生成モデルの評価を担う「Solver-mediated」な結合ループ。 |
| どうやって有効だと検証した？ | BLIP3o-8B、BAGEL、VARGPT-v1.1という3種類の異なる基盤モデルに対し、MMMU等の8つの理解ベンチマークとGenEval生成ベンチマークを用いて、ベースラインに対する精度向上（MMMUで最大+3.5%等）を実証した。 |
| 議論はある？ | LoRAベースの適応学習であるため、基盤モデルが本来持たない新しい視覚概念をゼロから獲得するものではない点や、改善幅がSolver（理解モデル）の品質に依存する限界がある点。 |
| 次に読むべき論文は？ | [10] UniCorn: Towards self-improving unified multimodal models through self-generated supervision, [12] SUDER: Self-improving unified large multimodal models for understanding and generation with dual self-rewards, [34] ILLUME: Illuminating your LLMs to see, draw, and self-enhance |
| PDFリンク | https://arxiv.org/pdf/2606.27376v1 |
