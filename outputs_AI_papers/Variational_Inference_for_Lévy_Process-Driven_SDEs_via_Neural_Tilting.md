---
title: "Variational Inference for Lévy Process-Driven SDEs via Neural Tilting"
date: 2026-05-12
arxiv_id: 2605.10934v1
url: http://arxiv.org/abs/2605.10934v1
---

# Variational Inference for Lévy Process-Driven SDEs via Neural Tilting

| 項目 | 内容 |
|---|---|
| どんなもの？ | レヴィ過程駆動型確率微分方程式（SDE）のベイズ推定を可能にする、新しい変分推論フレームワーク。ニューラルネットワークを用いてレヴィ測度を指数的に重み付け（ニューラル・チルト）することで、複雑なジャンプダイナミクスを扱えるようにした手法。 |
| 先行研究と比べてどこがすごい？ | 既存のガウス分布ベースの変分推論が苦手としていた、急峻な変化や極端な事象（重い裾を持つ分布）を正確にモデル化できる点。また、微分可能性を維持しつつ、スケーラブルな最適化と事後分布の推論を可能にした。 |
| 技術や手法のキモはどこ？ | レヴィ測度に対する「ニューラル・チルト（指数的重み付け）」と、それを実現するための「二次形式ニューラル・パラメータ化」。これにより、事後分布の解析的な正規化定数の算出と、サンプリングのための効率的なアルゴリズムを実現した点。 |
| どうやって有効だと検証した？ | 合成データ（Ornstein–Uhlenbeck過程およびダブルウェルポテンシャル）を用いたパラメータ復元実験と、実世界の10種の金融株価データを用いた時系列予測タスクで評価。CRPSなどの指標で、従来のガウスSDEやニューラル手法を大きく上回る性能を示した。 |
| 議論はある？ | 現在の二次形式のパラメータ化は裾の重さを制御できる一方、複雑な非対称性やマルチモーダルなジャンプ法則の表現には限界がある。また、安定性指数αをグリッドサーチで固定しているため、同時推定が将来の課題。 |
| 次に読むべき論文は？ | [25] Junteng Jia and Austin R Benson, "Neural jump stochastic differential equations", NeurIPS 2019; [18] Yuanpei Gao et al., "Neural Non-Stationary Merton Jump Diffusion for Time Series Prediction", NeurIPS 2025. |
| PDFリンク | https://arxiv.org/pdf/2605.10934v1 |
