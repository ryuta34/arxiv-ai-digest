---
title: "Geometric regularization of autoencoders via observed stochastic dynamics"
date: 2026-04-20
arxiv_id: 2604.16282v1
url: http://arxiv.org/abs/2604.16282v1
---

# Geometric regularization of autoencoders via observed stochastic dynamics

| 項目 | 内容 |
|---|---|
| どんなもの？ | 非線形多様体上で進展する確率微分方程式（SDE）を、観測されたデータから学習するための幾何学的正則化付きオートエンコーダ。疎なデータ環境においても、多様体の幾何学的構造を維持しつつ、ドリフト項や拡散項を安定的に推定する手法。 |
| 先行研究と比べてどこがすごい？ | 既存のATLAS法が抱える「次元の呪い」や「再投影のコスト」を克服し、オートエンコーダのデコーダヤコビアンのヘッセ行列に依存しない、幾何学的に整合性のとれたSDE係数の推定を実現した点。特に、未知の多様体上のSDEを、幾何学的に正則化された単一の非線形チャートで直接学習できる。 |
| 技術や手法のキモはどこ？ | 観測されたアンビエント空間の共分散行列$\Lambda$が接空間情報を保持している点に着目し、タンジェント束に対するペナルティ（$\rho$-metric）を設計したこと。また、Itôの公式を用いたエンコーダ・プルバックターゲットにより、デコーダのヘッセ行列なしで正確な潜伏ドリフトを推定可能にしたこと。 |
| どうやって有効だと検証した？ | パラボロイドやクォーティクドームなど4つの曲面上で、回転力学とミュラー・ブラウン・ランジュバン力学を用いた実験を実施。ベースラインおよび先行手法と比較し、MFPT（平均初通過時間）の誤差を50〜70%削減し、かつアンビエント空間における係数推定誤差を大幅に低減したことで検証した。 |
| 議論はある？ | 現在の理論は単一チャート設定に基づいており、複数チャートを用いたアトラスへの拡張や、より一般的な非線形マニホールドへの適応が今後の課題。また、理論的な経路誤差の境界（Pathwise bound）は緩く、実際の精度改善を完全には説明しきれない点がある。 |
| 次に読むべき論文は？ | [12] Crosskey & Maggioni, "ATLAS: a geometric approach to learning high-dimensional stochastic systems near manifolds." (ベースとなる手法) <br> [46] Yang & He, "Deeper or wider: A perspective from optimal generalization error with sobolev loss." (本手法の一般化誤差理論の基礎) |
| PDFリンク | https://arxiv.org/pdf/2604.16282v1 |
