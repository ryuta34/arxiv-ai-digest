---
title: "FuseReg: Regularizing Layer Fusion Mitigates the Reconstruction-Generation Gap in Representation Autoencoders"
date: 2026-09-29
arxiv_id: 2609.31620v1
url: http://arxiv.org/abs/2609.31620v1
---

# FuseReg: Regularizing Layer Fusion Mitigates the Reconstruction-Generation Gap in Representation Autoencoders

| 項目 | 内容 |
|---|---|
| どんなもの？ | 表現オートエンコーダ（RAE）における層の融合戦略の硬直性を解消し、復元と生成の性能差（Gap）を縮小する「FuseReg」という学習手法。事前学習済みエンコーダを固定したまま、多様な層のサブセットを学習させることで、デコーダと生成モデルの汎用性と堅牢性を高めている。 |
| 先行研究と比べてどこがすごい？ | 従来手法は特定の固定された層融合に依存しており、復元（浅い層重視）と生成（深い層重視）の嗜好の不一致を解決できなかった。FuseRegは学習時に層をランダムにサンプリングして正規化することで、単一のデコーダで多様な融合構成に対応し、モデルの再学習なしに復元と生成の品質を大幅に向上させた。 |
| 技術や手法のキモはどこ？ | 学習時に層のサブセットをランダムに抽出し、その平均を常に保持しつつ「層間の不一致」を正規化項としてペナルティ化する手法。理論的に、このランダムサブセットサンプリングは各層の重みのモーメントにおいて決定論的な融合手法では到達不可能な特性を持ち、学習モデルの汎化能力を直接的に高める。 |
| どうやって有効だと検証した？ | ImageNet-256データセットとDINOv3-Lエンコーダを用い、フル/スパース/単一層の各融合構成で復元精度（PSNR/SSIM）を評価。さらにDiT（Diffusion Transformer）を用いた生成実験において、gFIDスコアの改善と、デコーダ・生成モデルの両ステージにおけるjoint regularizationの効果を定量的に示した。 |
| 議論はある？ | 線形モデルを用いた理論解析は非線形な実機モデルの挙動を直接予測するものではない点。また、デコーダと生成モデルは異なる最適化目標を持つため、ハイパーパラメータ（pdec, pdit）の選択を個別に行う必要があり、モデル規模やタスクに応じた最適なレート設定の一般化が今後の課題である。 |
| 次に読むべき論文は？ | [Diffusion transformers with representation autoencoders (Zheng et al., 2025)](https://arxiv.org/abs/2510.11690) および [Improved baselines with representation autoencoders (Singh et al., 2026)](https://arxiv.org/abs/2605.18324) |
| PDFリンク | https://arxiv.org/pdf/2609.31620v1 |
