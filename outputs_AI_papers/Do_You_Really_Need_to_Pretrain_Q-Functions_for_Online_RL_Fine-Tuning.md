---
title: "Do You Really Need to Pretrain Q-Functions for Online RL Fine-Tuning?"
date: 2026-07-30
arxiv_id: 2607.27203v1
url: http://arxiv.org/abs/2607.27203v1
---

# Do You Really Need to Pretrain Q-Functions for Online RL Fine-Tuning?

| 項目 | 内容 |
|---|---|
| どんなもの？ | オンライン強化学習によるファインチューニングにおいて、Q関数をオフラインデータで事前学習することが必ずしも有効ではないという問題を指摘し、その解決策として多様なポリシーを用いたQ関数初期化手法（IPE）を提案した論文。 |
| 先行研究と比べてどこがすごい？ | 一般的な「Q関数も事前学習すべき」という通説に反し、事前学習されたQ関数がオンライン学習で収束する最適Q関数と根本的に不一致であることを解明した点。また、その不一致を解消するために多様なポリシーから収集したロールアウトでQ関数をブートストラップする簡潔かつ強力な手法（IPE）を提案した点。 |
| 技術や手法のキモはどこ？ | 単一の事前学習済みポリシーのみで学習を行うとアクション分布が限定的になり、Q関数が最適値に収束しない（collapseする）問題に対し、同一のデータ分布から異なる複数のポリシーを学習させ、それらの出力をプールしてQ関数の学習に使用することで、アクション空間への多様なカバー率を確保した点。 |
| どうやって有効だと検証した？ | Robomimic（lift, can, square）およびOGBench（cube, scene, puzzle）の6つの連続制御タスクにおいて、単純なQ関数事前学習や事前学習なしの場合と比較し、平均26%の性能向上を実証した。 |
| 議論はある？ | IPEはQ関数を学習するためのデータ収集において、単一ポリシーの場合よりも追加のオーバーヘッドが必要となる。また、本研究はオフラインからオンラインへの強化学習に特化しており、オンポリシー手法への適用やデータ効率のさらなる改善が将来課題である。 |
| 次に読むべき論文は？ | [EXPO: Stable reinforcement learning with expressive policies](https://arxiv.org/abs/2507.07986) および [Cal-ql: Calibrated offline rl pre-training for efficient online fine-tuning](https://arxiv.org/abs/2303.05479) |
| PDFリンク | https://arxiv.org/pdf/2607.27203v1 |
