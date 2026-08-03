---
title: "Toward Robust and 3D-Aware RGB-NIR Imaging in the Dark"
date: 2026-08-03
arxiv_id: 2607.29684v1
url: http://arxiv.org/abs/2607.29684v1
---

# Toward Robust and 3D-Aware RGB-NIR Imaging in the Dark

| 項目 | 内容 |
|---|---|
| どんなもの？ | 低照度環境において、Near-Infrared (NIR) 画像とノイズの多いRGB画像を融合し、きれいなRGB画像を復元する3D認識技術。教師データとしてきれいなRGB画像を一切必要とせず、ボリュームレンダリングと神経暗黙的モデルを活用してノイズを抑制し、鮮明な画像を生成する。 |
| 先行研究と比べてどこがすごい？ | 既存の教師あり学習手法が「きれいなRGB画像」を学習に必要とするのに対し、本手法は不要であり、ノイズレベルや環境変化に対して高い汎用性と堅牢性を備える点。また、3D空間内での整合性を考慮することで、従来の手法よりも高精細な構造・テクスチャ復元を可能にした。 |
| 技術や手法のキモはどこ？ | NIR画像による構造ガイダンスに基づいた「NIR条件付きMLP構造」と、Checkerboardアーティファクトを抑制する「NIRベースの位置エンコーディング」、さらにNIR-RGB間の色曖昧さを解決する「Color Code MLP（C.C. MLP）」の3点。 |
| どうやって有効だと検証した？ | Mitsuba3を用いて生成した合成データセット（ROVER）と、JAI FS-3200T10GE-NNCカメラで撮影した実環境データセット（SAKANA）を用いた定量的・定性的な評価。PSNR, SSIM, LPIPS等の指標および人間による主観評価を実施。 |
| 議論はある？ | 静止シーンのみを対象としており、動的な環境には適用できない点。また、RGBカメラとNIRカメラが完全に整列していない場合、正確なカメラポーズの取得が困難であり、今後の課題としている。 |
| 次に読むべき論文は？ | [1] Ben Mildenhall et al., "NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis" (2021) <br> [2] Ben Mildenhall et al., "Nerf in the dark: High dynamic range view synthesis from noisy raw images" (2022) |
| PDFリンク | https://arxiv.org/pdf/2607.29684v1 |
