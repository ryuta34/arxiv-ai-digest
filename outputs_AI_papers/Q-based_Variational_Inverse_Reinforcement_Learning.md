---
title: "Q-based Variational Inverse Reinforcement Learning"
date: 2026-08-18
arxiv_id: 2608.16888v1
url: http://arxiv.org/abs/2608.16888v1
---

# Q-based Variational Inverse Reinforcement Learning

| 項目 | 内容 |
|---|---|
| どんなもの？ | 逆強化学習（IRL）において、報酬関数だけでなく最適なQ値に対する事後分布をベイズ的に推定する手法「QVIRL」を提案。変分推論を用いることで、従来手法の課題であったスケーラビリティと不確実性の定量化を両立させ、高次元かつ raw pixel 入力にも対応した。 |
| 先行研究と比べてどこがすごい？ | MCMCに基づく手法が抱えていた計算コストの問題を解決し、スケーラビリティを確保した。また、従来のスケーラブルな手法（AVRIL等）が点推定にとどまり適切な不確実性評価ができないのに対し、QVIRLはQ値の事後分布を直接モデル化することで、安全性の高い学習や能動学習に適した不確実性評価が可能になった点。 |
| 技術や手法のキモはどこ？ | 報酬そのものではなく、最適なQ値の事後分布を変分推論で推定する点。逆ベルマン方程式を用いてQ値から報酬を導出し、Clarkの近似を用いることで、最大化演算を含む非線形な変換をガウス分布の閉形式として効率的に処理する点。 |
| どうやって有効だと検証した？ | 100種類のランダムなグリッドワールド（MCMCによる真の事後分布を算出可能）での近似品質評価。Lunar Lander、Highway環境、およびATARIゲーム（Pong, Space Invaders）を用いた学習性能と能動学習（Active IRL）の有用性の検証。 |
| 議論はある？ | ガウス分布の仮定による制約があり、非ガウス的な複雑な事後分布を扱うにはさらなる工夫（ワープ処理等）が必要。また、ハイパーパラメータλの設定や、補助データを用いた損失計算の最適化が性能に影響を与える可能性がある。 |
| 次に読むべき論文は？ | 1. [Scalable Bayesian Inverse Reinforcement Learning (Chan & van der Schaar, 2021)](https://arxiv.org/abs/2106.03856) <br> 2. [Walking the Values in Bayesian Inverse Reinforcement Learning (Bajgar et al., 2024)](https://arxiv.org/abs/2402.05191) |
| PDFリンク | https://arxiv.org/pdf/2608.16888v1 |
