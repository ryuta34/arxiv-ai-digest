---
title: "MeanFlowNFT: Bringing Forward-Process RL to Average-Velocity Generators"
date: 2026-07-17
arxiv_id: 2607.15273v1
url: http://arxiv.org/abs/2607.15273v1
---

# MeanFlowNFT: Bringing Forward-Process RL to Average-Velocity Generators

| 項目 | 内容 |
|---|---|
| どんなもの？ | 少ないステップ数で高品質な生成を可能にするMeanFlowモデルに対し、報酬に基づく強化学習（RL）を適用するためのフレームワーク「MeanFlowNFT」を提案した論文。既存の拡散モデル用RL手法を、平均速度を扱うMeanFlowの特性を損なわずに適応させた。 |
| 先行研究と比べてどこがすごい？ | 既存のRL手法（DiffusionNFT等）は瞬時速度の最適化に依存していたが、MeanFlowNFTは平均速度を保ったまま最適化を実現した。これにより、Few-step生成の効率性を維持しつつ、学習済みモデルの品質をRLで大幅に向上させ、Multi-step生成モデルをも凌駕する性能を達成した。 |
| 技術や手法のキモはどこ？ | MeanFlowのIdentity式を用いて、平均速度を扱うネットワークから「誘起された瞬時速度予測器」を構成した点。この誘起された予測器に対してDiffusionNFTの目的関数を適用することで、推論時のサンプリング手順を変えずに報酬最適化を可能にした。 |
| どうやって有効だと検証した？ | SD3.5-Mを用いた画像生成とWan2.1を用いた動画生成において実験。複数の評価指標（ImageReward, CLIPScore, HPSv2, VBench等）で比較し、4ステップのサンプリングでも50ステップの強化学習済みモデルや他の手法を上回る性能を実証した。 |
| 議論はある？ | 現在はDiffusionNFTスタイルのRL手法に限定しており、他のRL手法（RAMやAWM）への適用は今後の課題。また、MeanFlowモデルという特定の枠組みに基づいているが、他のフローマップモデルやConsistency Trajectoryモデルへも拡張可能であると示唆されている。 |
| 次に読むべき論文は？ | [DiffusionNFT: Online diffusion reinforcement with forward process](https://openreview.net/forum?id=VJZ477R89F) および [Mean flows for one-step generative modeling](https://arxiv.org/abs/2605.10759) |
| PDFリンク | https://arxiv.org/pdf/2607.15273v1 |
