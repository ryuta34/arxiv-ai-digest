---
title: "Aligning Latent Geometry for Spherical Flow Matching in Image Generation"
date: 2026-05-15
arxiv_id: 2605.15193v1
url: http://arxiv.org/abs/2605.15193v1
---

# Aligning Latent Geometry for Spherical Flow Matching in Image Generation

| 項目 | 内容 |
|---|---|
| どんなもの？ | VAE潜在空間における幾何学的な不整合（ラジアル方向の不要な変動）を解消し、生成品質を向上させる手法。潜在空間を固定半径の超球面（hypersphere）に射影し、球面上での測地線補間（slerp）を用いてフローマッチングを行う。 |
| 先行研究と比べてどこがすごい？ | 既存のVAEエンコーダーや学習済みの拡散モデルの構造を一切変更せず、補助的なエンコーダーも不要な点。デコーダーの微調整のみで実現可能でありながら、生成速度の向上（収束までのステップ数短縮）とFIDの改善を複数のモデルで達成した。 |
| 技術や手法のキモはどこ？ | 潜在トークンを半径$\sqrt{d}$の超球面上に強制的に射影し、ラジアル方向の変動を排除した点。これにより、モデルは学習時に方向（角度）成分のみに集中でき、デコーダーが敏感な方向情報と鈍感な半径情報を切り分けることで効率的な学習を実現した。 |
| どうやって有効だと検証した？ | ImageNet-256でのクラス条件付き生成タスクにおいて、FLUX.2、VA-VAE、REPA-E FLUX.1の各ファミリーで評価。FIDスコアの改善および、学習ステップ数が約2.2倍効率化されることを確認した。 |
| 議論はある？ | 現在はクラス条件付き生成に焦点を当てており、テキスト条件付き生成への拡張が今後の課題。また、より高い圧縮率を持つトークナイザーにおいて、半径情報の寄与がどう変化するかは未知数。 |
| 次に読むべき論文は？ | [14] Flow matching on general geometries (Chen & Lipman, 2023) [https://arxiv.org/abs/2302.03660], [21] REPA-E: Unlocking VAE for end-to-end tuning of latent diffusion transformers (Leng et al., 2025) [https://arxiv.org/abs/2501.07769] |
| PDFリンク | https://arxiv.org/pdf/2605.15193v1 |
