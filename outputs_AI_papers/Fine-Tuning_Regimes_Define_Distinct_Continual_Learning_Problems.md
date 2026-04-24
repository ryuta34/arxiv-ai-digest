---
title: "Fine-Tuning Regimes Define Distinct Continual Learning Problems"
date: 2026-04-24
arxiv_id: 2604.21927v1
url: http://arxiv.org/abs/2604.21927v1
---

# Fine-Tuning Regimes Define Distinct Continual Learning Problems

| 項目 | 内容 |
|---|---|
| どんなもの？ | 継続学習（CL）において、これまで固定されがちだった「ファインチューニングの対象範囲（適応レジーム）」を、モデル性能やアルゴリズムの優位性を左右する重要な変数として再定義した研究。異なるパラメータの深さで学習を行うと、手法間の相対的なランキングが逆転することを示した。 |
| 先行研究と比べてどこがすごい？ | 従来は学習順序やアルゴリズムの選定が重視されていたが、本研究は「学習させる層の深さ」そのものが塑性・安定性のトレードオフに直接関与し、比較実験の結論を根本から変えうることを初めて体系的に実証した点。 |
| 技術や手法のキモはどこ？ | 学習プロセスを「固定された部分空間における射影勾配の最適化」として定式化し、深さが変わることで適応可能な勾配方向が制限され、保持すべき知識と新しい課題への適応の競合関係が変化することを理論的に説明した点。 |
| どうやって有効だと検証した？ | 5つのデータセット（MNIST系4種、CIFAR-100）に対し、5段階の深さの適応レジームと4つの代表的なCL手法（EWC, LwF, SI, GEM）を組み合わせ、Kendallの$\tau$を用いたランキング相関分析と、勾配ノルムと忘却の関係性分析を実施した。 |
| 議論はある？ | ハイパーパラメータを全レジームで固定していること、ResNet-18という単一のアーキテクチャに限定していること、また最適化観点の分析が完全なメカニズム説明というよりは解釈のレンズに留まっている点が限界として挙げられる。 |
| 次に読むべき論文は？ | [Schwarz et al., "Progress & Compress" (2018)](https://arxiv.org/abs/1805.06370)、[Lopez-Paz & Ranzato, "Gradient episodic memory" (2022)](https://arxiv.org/abs/1706.08840)、[Kumar et al., "Fine-tuning can distort pretrained features" (2022)](https://arxiv.org/abs/2202.10054) |
| PDFリンク | https://arxiv.org/pdf/2604.21927v1 |
