---
title: "Geometry-aware similarity metrics for neural representations on Riemannian and statistical manifolds"
date: 2026-03-31
arxiv_id: 2603.28764v1
url: http://arxiv.org/abs/2603.28764v1
---

# Geometry-aware similarity metrics for neural representations on Riemannian and statistical manifolds

| 項目 | 内容 |
|---|---|
| どんなもの？ | ニューラルネットワークの内部表現を、従来の「埋め込み空間における幾何学」ではなく、リーマン幾何学を用いた「内在的幾何学」の観点から比較・評価する新しい枠組み「Metric Similarity Analysis (MSA)」を提案した論文。異なるアーキテクチャや学習手法を持つモデル間の計算メカニズムの差異を、より本質的に明らかにすることを目的としている。 |
| 先行研究と比べてどこがすごい？ | 従来の手法（CKA、RSA、Procrustesなど）は状態空間内の extrinsic（外在的）な幾何学を比較するが、これらは本質的な計算の違いを捉えられない場合がある。MSAは「多様体仮説」に基づき、pullback metricを用いて内在的幾何学を直接比較することで、外在的には似ていても計算戦略が異なるモデル（例：Rich vs Lazy学習 regime）を明確に区別できる。 |
| 技術や手法のキモはどこ？ | 入力データが構成する多様体上の「プルバック計量（pullback metric）」をネットワークの計算の定義とし、それらを比較するためにSPD（正定値対称）行列に対する新しい距離尺度「スペクトル比（Spectral Ratio）」を導入した点。これにより、座標変換や状態空間の回転に対して不変な、数学的に厳密な類似性評価が可能になった。 |
| どうやって有効だと検証した？ | 1) Rich/Lazy学習 regimeの違いの識別、2) 再帰型ニューラルネットワーク（RNN）と状態空間モデル（SSM）によるワーキングメモリ課題での計算メカニズムの解析、3) 大規模テキスト・画像生成モデル（StableDiffusionXL）におけるガイダンスが潜在空間に与える影響の分析、の3つの実験で有効性を実証した。 |
| 議論はある？ | 入力データ多様体の事前定義（または学習による推定）が必要であることや、最終層のデコーダーによる情報利用の仕方が考慮されていない点（後段のタスクへの依存性）が挙げられる。また、本手法はあくまで幾何学的なレンズを通じた相関的な解析であり、因果関係を直接示すものではない点に留意が必要。 |
| 次に読むべき論文は？ | [1] [Klabunde et al. (2025). Similarity of neural network models: A survey of functional and representational measures.](https://dl.acm.org/doi/10.1145/3697914) <br> [2] [Brandon, Angus Chadwick, and Pellegrino (2025). Emergent Riemannian geometry over learning discrete computations on continuous manifolds.](https://arxiv.org/abs/2512.00196) |
| PDFリンク | https://arxiv.org/pdf/2603.28764v1 |
