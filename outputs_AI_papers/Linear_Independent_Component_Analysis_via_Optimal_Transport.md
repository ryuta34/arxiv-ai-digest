---
title: "Linear Independent Component Analysis via Optimal Transport"
date: 2026-07-16
arxiv_id: 2607.14081v1
url: http://arxiv.org/abs/2607.14081v1
---

# Linear Independent Component Analysis via Optimal Transport

| 項目 | 内容 |
|---|---|
| どんなもの？ | 独立成分分析（ICA）において、従来の近似的な対比関数（非ガウス性の指標）に代わり、最適な輸送理論に基づく「Wasserstein距離」を用いた新しいICAアルゴリズム（OT-ICA）を提案した研究です。分布に対する事前の仮定を置かずに、信号源を分離することに成功しました。 |
| 先行研究と比べてどこがすごい？ | 従来のFastICAやJADE等は対比関数の近似に依存しており、特定の分布で精度が低下したりヘッセ行列が不安定になる欠点がありました。本手法は真の距離指標であるWasserstein距離を利用することで、複雑な混合分布に対しても頑健で高い分離精度を達成しました。 |
| 技術や手法のキモはどこ？ | 非ガウス性の尺度として「標準ガウス分布との間のWasserstein距離」を直接最適化対象とし、勾配降下法を用いて非ガウス性を最大化する行列を探索する点です。特に、離散的な分布に対してもガウス・ディザリング（Gaussian Dithering）を用いることで微分可能なコスト関数を実現しています。 |
| どうやって有効だと検証した？ | 合成データを用いた5つの異なる混合環境（連続・混合・離散等）において、FastICA等のベースライン手法とAmari性能指数を用いて比較評価しました。また、EEG信号のアーチファクト除去や、金融時系列データを用いた価格発見プロセスへの実応用を行い、実効性を確認しました。 |
| 議論はある？ | 次元の増大に伴い、限られたサンプル数では状態空間を網羅できず性能が低下する「次元の呪い」が課題です。また、離散分布において階段状の分布関数が勾配の停滞を招くことや、計算コストが既存の固定点反復手法よりも高い点が挙げられます。 |
| 次に読むべき論文は？ | 1. Cardoso (2022) [Independent component analysis in the light of information geometry](https://doi.org/10.3390/e24030377)<br>2. Peyré & Cuturi (2019) [Computational optimal transport](https://doi.org/10.1561/2200000073)<br>3. Ablin et al. (2018) [Faster independent component analysis by preconditioning with Hessian approximations](https://ieeexplore.ieee.org/document/8316773) |
| PDFリンク | https://arxiv.org/pdf/2607.14081v1 |
