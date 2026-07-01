---
title: "PointSplat: Compact Gaussian Splatting via Human-Centric Prediction"
date: 2026-07-01
arxiv_id: 2606.32036v1
url: http://arxiv.org/abs/2606.32036v1
---

# PointSplat: Compact Gaussian Splatting via Human-Centric Prediction

| 項目 | 内容 |
|---|---|
| どんなもの？ | 入力画像から高精度かつ軽量な3D Gaussian Splatting（3DGS）表現をリアルタイムで生成する、人間を中心としたフィードフォワード型再構成手法。視点中心の表現で生じる多視点間の冗長性を排除し、効率的なレンダリングを実現する。 |
| 先行研究と比べてどこがすごい？ | 視点ごとに計算を行う従来手法に対し、3D空間上で直接予測を行うため冗長性が低い。計算負荷を大幅に抑えつつ、入力視点数や解像度の変化に対して頑健な高い品質での新規視点合成が可能である点。 |
| 技術や手法のキモはどこ？ | Space Carving（空間彫り込み）による粗な幾何学的プロキシの推定と、レイキャスティングを用いた不要な内部点の除去および2D-3D対応付けの確立。さらに「Point-Image Transformer」を用いて、外観と幾何学的特徴を統合し、Gaussianパラメータを一度の推論で生成する点。 |
| どうやって有効だと検証した？ | DNA-Rendering、ActorsHQ、PKU-DyMVHumansなどの複数の実写および合成データセットを用いて検証。PSNR、SSIM、LPIPS等の指標に加え、Gaussianの総数と推論速度を比較し、従来手法を凌駕する効率と品質を証明した。 |
| 議論はある？ | フィードフォワード手法であるため、メモリ制限により境界のない（unbounded）シーンの取り扱いが困難な場合がある。また、時間的な一貫性を備えた4D表現への拡張が今後の課題である。 |
| 次に読むべき論文は？ | [17] 3D Gaussian Splatting for real-time radiance field rendering (https://arxiv.org/abs/2308.04079) <br> [52] GS-LRM: Large reconstruction model for 3D Gaussian Splatting (https://arxiv.org/abs/2403.14621) |
| PDFリンク | https://arxiv.org/pdf/2606.32036v1 |
