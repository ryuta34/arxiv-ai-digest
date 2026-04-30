---
title: "Hyper Input Convex Neural Networks for Shape Constrained Learning and Optimal Transport"
date: 2026-04-30
arxiv_id: 2604.26942v1
url: http://arxiv.org/abs/2604.26942v1
---

# Hyper Input Convex Neural Networks for Shape Constrained Learning and Optimal Transport

| 項目 | 内容 |
|---|---|
| どんなもの？ | 凸関数を学習するために設計された、新しいニューラルネットワークアーキテクチャ「Hyper Input Convex Neural Networks (HyCNNs)」の提案。ICNN（Input Convex Neural Networks）の利点である入力に対する凸性を維持しつつ、深層化による表現能力の向上と学習の安定性を実現している。 |
| 先行研究と比べてどこがすごい？ | 従来のICNNは深層化しても表現能力が十分に向上しにくいという問題があったが、HyCNNは隠れ層の構造を改良することで、深さに対して指数関数的に近似誤差が減少することを理論的に証明した。また、実験において、凸回帰タスクや高次元の最適輸送（OT）マップ学習において、既存のICNNやMLPを上回る予測性能を示した。 |
| 技術や手法のキモはどこ？ | Maxoutユニットの概念をICNNに組み込み、各層で2つの行列演算レーンを持つ構造を採用した点。これにより、単純なICNNよりも区分的アフィン近似の区分数を倍増させることができる。また、深層ネットワークの学習を安定させるための、非負制約を考慮した独自の初期化手法を開発した。 |
| どうやって有効だと検証した？ | 50次元の凸回帰タスクにおけるMSE測定と、4iデータセットを用いた単一細胞RNAシーケンスデータへの適用実験（OTマップ学習）を行った。学習コストの異なる複数の設定で評価し、HyCNNが従来のICNNベースの手法よりも高い精度かつ効率的に動作することを明らかにした。 |
| 議論はある？ | HyCNNは滑らかで強制的な凸関数に対して帰納的バイアスを持つため、これらから逸脱する設定では学習が制限される可能性がある。また、実験では計算リソースの制約から、さらなる大規模な研究が将来の課題として挙げられている。 |
| 次に読むべき論文は？ | [Amos et al. (2017): Input convex neural networks](https://arxiv.org/abs/1703.00467)、[Makkuva et al. (2020): Optimal transport mapping via input convex neural networks](https://arxiv.org/abs/2006.06327)、[Bunne et al. (2023): Learning single-cell perturbation responses using neural optimal transport](https://www.nature.com/articles/s41592-023-02047-w) |
| PDFリンク | https://arxiv.org/pdf/2604.26942v1 |
