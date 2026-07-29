---
title: "Re-thinking Mammography Transfer Learning: The Dataset-Informed Transfer Learning (DITL) Framework for Breast Cancer Screening and Lesion Diagnosis"
date: 2026-07-29
arxiv_id: 2607.26043v1
url: http://arxiv.org/abs/2607.26043v1
---

# Re-thinking Mammography Transfer Learning: The Dataset-Informed Transfer Learning (DITL) Framework for Breast Cancer Screening and Lesion Diagnosis

| 項目 | 内容 |
|---|---|
| どんなもの？ | マンモグラフィの乳がん検診から病変診断までを網羅する、データセット固有の特性を取り入れた転移学習フレームワーク「DITL」。自己教師あり学習の知見を基に、サンプルごとの難易度と近傍関係を学習プロセスに統合することで、分類性能を向上させる。 |
| 先行研究と比べてどこがすごい？ | 従来の不変的な重み付けや固定マージンを用いた手法とは異なり、データセットサイズに応じて適応的に重みやマージンを調整できる点。また、ハイパーパラメータ調整が不要で、かつ計算負荷が無視できるほど小さい点。 |
| 技術や手法のキモはどこ？ | SSLによる特徴空間での近傍分析に基づき、(i)各サンプルの近傍ラベル純度に基づく適応的難易度重み付け（A-DWCE）と、(ii)近傍の同じクラスの平均と遠い別のクラスの平均を対比させる適応的近傍表現トリプレット損失（A-NR-Triplet）を統合した点。 |
| どうやって有効だと検証した？ | 大規模なVinDR-Mammoデータセット（乳房密度・BI-RADS）および、CESM、CBIS-DDSM（Mass/Calcification）などの小規模ROIデータセットを用いて評価。従来手法（CE、Focal Loss等）との比較で、精度、F1スコア、AUCにおいて有意な（p < 0.0001）向上を確認した。 |
| 議論はある？ | 現在はマンモグラフィに特化しているが、胸部X線など他モダリティへの拡張性が課題。また、今後はコントラスティブ言語-画像事前学習や、より高度なカリキュラム学習と組み合わせることで、さらに適応的なパイプラインを構築することが将来課題。 |
| 次に読むべき論文は？ | [18] Panambur et al., "Enhancing downstream classification of breast abnormalities in contrast enhanced spectral mammography using a neighborhood representation loss" (前身となるDWNR手法) |
| PDFリンク | https://arxiv.org/pdf/2607.26043v1 |
