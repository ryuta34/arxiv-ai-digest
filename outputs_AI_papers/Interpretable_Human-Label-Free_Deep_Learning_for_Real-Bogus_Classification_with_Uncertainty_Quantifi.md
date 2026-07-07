---
title: "Interpretable Human-Label-Free Deep Learning for Real-Bogus Classification with Uncertainty Quantification"
date: 2026-07-07
arxiv_id: 2607.05393v1
url: http://arxiv.org/abs/2607.05393v1
---

# Interpretable Human-Label-Free Deep Learning for Real-Bogus Classification with Uncertainty Quantification

| 項目 | 内容 |
|---|---|
| どんなもの？ | 天文調査における過渡現象（トランジェント）とノイズ（ボガス）を識別するための、人手によるラベル付けを必要としない深層学習フレームワーク。物理ベースの注入データとノイズの多い観測データを組み合わせ、弱教師あり学習により高い精度で分類と不確実性の定量化を実現する。 |
| 先行研究と比べてどこがすごい？ | 人手によるラベル付けに依存せず、かつ survey-specific なモデルの転用問題を回避可能。また、深層学習モデルがブラックボックス化しやすい点に対し、不確実性の定量化と潜在空間の可視化を組み合わせることで、信頼性の高い科学的推論を可能にする手法を確立した。 |
| 技術や手法のキモはどこ？ | 注入されたトランジェントとノイズの多いサーベイデータを「Asym-Co-teaching（非対称共学習）」で学習する点。また、不確実性の定量化において、2つのモデルの共学習ペアにMC Dropoutを組み合わせて擬似的なアンサンブルを構築し、計算コストを抑えつつ精度を高めたハイブリッド戦略をとる点。 |
| どうやって有効だと検証した？ | HSCサーベイのデータを用いたシミュレーションおよび手動でラベル付けした評価用データセットを使用。様々なレベルのラベルノイズ（15%〜35%）に対して標準的な手法より頑健であることを示し、不確実性が信号対雑音比（SNR）や光源の明るさの変化と物理的に妥当な相関を持つことを確認した。 |
| 議論はある？ | 単一エポックの分類精度には物理的な限界（情報の曖昧さ）があり、最終的には時系列情報を統合した物体レベルの判断が必要。将来課題として、より高度な概念ベースの解釈可能性手法の導入や、クラス条件付きノイズの推定アルゴリズムの拡張が挙げられる。 |
| 次に読むべき論文は？ | Han et al. (2018) "Co-teaching: Robust Training of Deep Neural Networks with Extremely Noisy Labels" (https://arxiv.org/abs/1804.06872) |
| PDFリンク | https://arxiv.org/pdf/2607.05393v1 |
