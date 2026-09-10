---
title: "Guiding Image-to-3D Generation with Test-Time Partial Observations"
date: 2026-09-10
arxiv_id: 2609.10531v1
url: http://arxiv.org/abs/2609.10531v1
---

# Guiding Image-to-3D Generation with Test-Time Partial Observations

| 項目 | 内容 |
|---|---|
| どんなもの？ | 既存の学習済み画像生成モデル（Image-to-3D）に対し、推論時に部分的な幾何学的情報（点群など）を外部から注入し、再学習なしで生成物の形状精度を向上させる訓練不要のガイダンスフレームワーク。 |
| 先行研究と比べてどこがすごい？ | モデルの重みを一切変更することなく、事後的なガイダンス（posterior guidance）を適用できる点。多視点画像だけでなく、点群や深度情報といった汎用的な幾何学的制約を直接組み込めるため、従来手法よりも高精度な形状再現が可能。 |
| 技術や手法のキモはどこ？ | 生成過程の速度場に、観測データに基づいた「占有率（occupancy）」と「自由空間（free-space）」のエネルギー項を追加し、事後確率を最大化するように最適化する手法。これにより、モデルが学習した事前知識と外部観測情報を整合させることができる。 |
| どうやって有効だと検証した？ | GSO-30データセットを用い、低・中・高の各観測レベルで検証を実施。Chamfer Distance（CD）やGround-truth Sided Distance（SD）の各指標において、ベースラインであるSAM 3DやMV-SAM3D、SpaceControlを大きく上回る性能を実証した。 |
| 議論はある？ | 観測データが正確かつ正規座標系にあることを前提としているため、ノイズの多いデータや未知の座標系への対応が課題。また、占有グリッド表現を用いるため、解像度がグリッドの粒度に依存してしまう限界がある。 |
| 次に読むべき論文は？ | [13] MV-SAM3D: Adaptive multi-view fusion for layout-aware 3d generation (arXiv:2603.11633), [7] SpaceControl: Introducing Test-Time Spatial Control to 3D Generative Modeling (ICLR 2026) |
| PDFリンク | https://arxiv.org/pdf/2609.10531v1 |
