---
title: "Neuron Populations Exhibit Divergent Selectivity with Scale"
date: 2026-06-03
arxiv_id: 2606.03990v1
url: http://arxiv.org/abs/2606.03990v1
---

# Neuron Populations Exhibit Divergent Selectivity with Scale

| 項目 | 内容 |
|---|---|
| どんなもの？ | ニューラルネットワークの「Rosetta Neurons（異なる独立した学習モデル間で共通して現れるニューロン）」が、モデルのスケール拡大に伴いどのように進化するかを調査した研究。モデルサイズが大きくなるにつれて、これらの共通ニューロンがどのように数、選択性、専門性を変化させるかを明らかにした。 |
| 先行研究と比べてどこがすごい？ | 従来の性能指標（損失関数など）のスケール則とは異なり、モデル内部の表現組織である「ニューロン単位」でのスケール則を確立した点。また、モデルのスケール拡大が、ニューロンをより選択的かつ専門的な「Rosetta」集団と、polysemantic（多義的）な背景集団へと分極させる「Neuron Polarization Effect」を初めて特定した。 |
| 技術や手法のキモはどこ？ | モデル間でニューロンの応答類似度を計算し、相互近傍マッチングによって「Rosetta Neurons」を特定する手法。また、特徴量の重要度とニューロン容量の制限に基づく統計的な容量配分モデルを提案し、Rosetta Neuronsの数がサブ線形的なべき乗則に従うことを理論的に導出した点。 |
| どうやって有効だと検証した？ | 言語モデル（最大30Bパラメータ）と視覚モデル（最大5Bパラメータ）の双方で大規模な実験を行い、予測通りのサブ線形的な増大と分極効果を観測した。さらに、特定のコード領域を識別するRosetta Neuronを用いたデータフィルタリング実験を行い、その実用的な性能を証明した。 |
| 議論はある？ | Rosetta Neuronsがモデル内部の全共有計算を網羅しているわけではない点（アテンションヘッドなどは対象外）。また、単一ニューロンの解釈性の測定にはモダリティ固有のプロキシ（指標）に頼っているため、評価手法の普遍性には改善の余地がある。 |
| 次に読むべき論文は？ | [Dravid et al., 2023 "Rosetta neurons: Mining the common units in a model zoo"](https://arxiv.org/abs/2305.15340) および [Elhage et al., 2022 "Toy models of superposition"](https://arxiv.org/abs/2209.10652) |
| PDFリンク | https://arxiv.org/pdf/2606.03990v1 |
