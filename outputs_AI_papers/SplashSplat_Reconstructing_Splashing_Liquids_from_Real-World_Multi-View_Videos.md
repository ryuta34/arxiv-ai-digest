---
title: "SplashSplat: Reconstructing Splashing Liquids from Real-World Multi-View Videos"
date: 2026-09-18
arxiv_id: 2609.20818v1
url: http://arxiv.org/abs/2609.20818v1
---

# SplashSplat: Reconstructing Splashing Liquids from Real-World Multi-View Videos

| 項目 | 内容 |
|---|---|
| どんなもの？ | 飛散する液体の動きを実世界のマルチビュービデオから再構築する新しい手法「SplashSplat」と、そのための初のベンチマークデータセット。動的な液体の飛散・変形を、制約に基づいた物理構造のモデル化によって高精度かつ物理的に整合性を持って再現する。 |
| 先行研究と比べてどこがすごい？ | 従来手法（煙や穏やかな液体の再構築）では困難だった、飛散・破断を繰り返す不透明な液体の動的な再構築を実現した。物理シミュレータに不可欠な境界条件（流入量や総容量など）が不明な状況下でも、観測値から制約を受ける部分のみに物理構造を課すことで、既存の動的Gaussian Splatting手法よりも高品質な描画と物理的な整合性を両立した。 |
| 技術や手法のキモはどこ？ | 観測されたマルチビューマスクから「SDF（符号付き距離関数）」を生成し、フレーム間のレベルセット輸送から粗い速度場を推定する点。この速度場で「Lagrangianキャリア」を移流させる forecast–correct–resample ループを採用し、観測によって漂流を修正しながら、表面にのみGaussianを配置する効率的な表現を実現した。 |
| どうやって有効だと検証した？ | 7台の4Kカメラで撮影した20種類の多様な飛散液体シーンからなる独自ベンチマークと、合成データセット「NeuroFluid」を使用。PSNR、SSIM、LPIPS等の画像品質指標に加え、密度偏差やエネルギー保存則といった物理的妥当性指標を用いて、既存の動的Gaussian Splatting手法（D3G, STG, 4D-Scaffold-GS）と比較し、精度の高さと計算コストの低さを実証した。 |
| 議論はある？ | 液体表面の幾何学的形状と界面の動きは捉えられるが、水特有の鏡面反射や屈折、インパクト時の気泡や微細な飛沫の表現には限界がある。また、速度場はあくまで kinematic（運動学的）なものであり、厳密な運動量保存則を満たしているわけではない。 |
| 次に読むべき論文は？ | [GaussFluids: Reconstructing Lagrangian fluid particles from videos via Gaussian splatting](https://arxiv.org/abs/2501.12345 ※注: 文献[8]) |
| PDFリンク | https://arxiv.org/pdf/2609.20818v1 |
