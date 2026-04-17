---
title: "LeapAlign: Post-Training Flow Matching Models at Any Generation Step by Building Two-Step Trajectories"
date: 2026-04-17
arxiv_id: 2604.15311v1
url: http://arxiv.org/abs/2604.15311v1
---

# LeapAlign: Post-Training Flow Matching Models at Any Generation Step by Building Two-Step Trajectories

| 項目 | 内容 |
|---|---|
| どんなもの？ | フローマッチングモデルを人間の選好に合わせて微調整（アライメント）するための新しい手法「LeapAlign」を提案している。学習時に全ステップではなく、2ステップの「リープ軌道（leap trajectory）」を構築することで、メモリ消費を抑えつつ、モデルの初期生成段階まで効果的な勾配伝搬を可能にした。 |
| 先行研究と比べてどこがすごい？ | 従来の直接的勾配法（Direct-gradient methods）では難しかった「初期段階の生成ステップの更新」と「勾配爆発の回避」を両立している。DRTuneなどの先行研究が切り捨てていた「ネストされた勾配」を、勾配割引（gradient discounting）により適切に制御して保持することで、より高い学習効率を実現した点。 |
| 技術や手法のキモはどこ？ | 1. 2ステップのリープ軌道を構築してメモリを節約する点、2. ネストされた勾配のマグニチュードを緩和する「勾配割引（gradient discounting）」、3. リープ軌道が元の生成パスとどれだけ近いかを判定して損失に反映させる「軌道類似性重み付け（trajectory-similarity weighting）」の3点。 |
| どうやって有効だと検証した？ | FLUX.1-devモデルを用い、一般的な選好アライメント（HPDv2、MJHQ-30kなど）および構成的アライメント（GenEval）において評価した。HPSv2.1、HPSv3、PickScore、ImageReward等の指標で、既存のGRPOベースや直接的勾配法の手法を一貫して上回る性能を示した。 |
| 議論はある？ | 現在は微分可能な報酬モデルに依存している点が課題であり、非微分可能な報酬モデルへの拡張や、微分可能な価値モデル（value models）の活用が将来の課題として挙げられている。 |
| 次に読むべき論文は？ | [Flow matching for generative modeling [27]](https://arxiv.org/abs/2210.02747), [Deep reward supervisions for tuning text-to-image diffusion models [52]](https://arxiv.org/abs/2306.09341), [Directly fine-tuning diffusion models on differentiable rewards [3]](https://arxiv.org/abs/2309.17400) |
| PDFリンク | https://arxiv.org/pdf/2604.15311v1 |
