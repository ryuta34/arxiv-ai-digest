---
title: "Differentially Private Nonparametric Modal Learning with Applications to Regression and Clustering"
date: 2026-08-03
arxiv_id: 2607.29675v1
url: http://arxiv.org/abs/2607.29675v1
---

# Differentially Private Nonparametric Modal Learning with Applications to Regression and Clustering

| 項目 | 内容 |
|---|---|
| どんなもの？ | 差分プライバシーを保証しつつ、多変量分布のモード（局所最大値）をノンパラメトリックに推定する手法「DP-GRAMS」を提案した論文。回帰やクラスタリングといった下流タスクへの応用も可能であり、理論的な収束レートやミニマックス最適性も示されている。 |
| 先行研究と比べてどこがすごい？ | 既存の差分プライバシー下でのモード推定が単一モードやk近傍法ベースの手法に限定されていたのに対し、本手法はカーネルベースの勾配上昇法を用いることで、滑らかな高次カーネルを活用し、複数のモードを効率的かつ統計的に精度良く推定できる。 |
| 技術や手法のキモはどこ？ | 勾配上昇を安定させるための「勾配クリッピングと密度床（density floor）付きのスコア推定器」、高密度領域を効率的に探索しモードをカバーする「密度認識型プライベート初期化（DAP）」、そして複数の初期値間でノイズを相関させる「相関ノイズ機構」の組み合わせ。 |
| どうやって有効だと検証した？ | 合成データ（4モードのガウス混合、5モードのt分布混合）および実データ（MNIST、Cancer RNA-Seq）を用いて、プライバシー予算（ε）と推定精度（MSE）のトレードオフを検証。非公開データに対する平均シフト法やk-meansベースのプライベート手法と比較し、優れた性能を示した。 |
| 議論はある？ | 高次元データにおけるDAPグリッドの計算コストの増大、およびRDP（Rényi DP）やzCDPなどのよりタイトなプライバシー会計手法の導入可能性について今後の課題として挙げている。 |
| 次に読むべき論文は？ | [Chen et al. (2016a)](https://doi.org/10.1214/15-AOS1373)、[Pacchiano et al. (2021)](https://arxiv.org/abs/2102.04633)、[Tsybakov (2008)](https://link.springer.com/book/10.1007/978-0-387-79078-7) |
| PDFリンク | https://arxiv.org/pdf/2607.29675v1 |
