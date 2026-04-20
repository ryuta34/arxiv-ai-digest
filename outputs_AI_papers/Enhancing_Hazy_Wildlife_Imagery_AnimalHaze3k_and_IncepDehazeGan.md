---
title: "Enhancing Hazy Wildlife Imagery: AnimalHaze3k and IncepDehazeGan"
date: 2026-04-20
arxiv_id: 2604.16284v1
url: http://arxiv.org/abs/2604.16284v1
---

# Enhancing Hazy Wildlife Imagery: AnimalHaze3k and IncepDehazeGan

| 項目 | 内容 |
|---|---|
| どんなもの？ | 野生動物の画像における大気ヘイズ（霧）除去を目的とした、合成データセット「AnimalHaze3k」と、新しいGANベースの画像復元モデル「IncepDehazeGan」を提案する研究。野生動物モニタリング等のコンピュータビジョンタスクの精度向上を支援する。 |
| 先行研究と比べてどこがすごい？ | 野生動物に特化したヘイズ除去データセットの希少性を解消した点。IncepDehazeGanは、既存手法と比較してSSIMで6.27%、PSNRで10.2%高い性能を達成し、下游タスクである動物検出（YOLOv11）のmAPを112%向上させた。 |
| 技術や手法のキモはどこ？ | インセプションブロックと残差スキップ接続を統合したエンコーダ・デコーダ構造の採用。また、HybridDepthを用いて高精度な深度推定を行い、物理モデルに基づいた写実的な合成ヘイズ画像を生成するパイプラインを構築した点。 |
| どうやって有効だと検証した？ | NTLNPデータセットから生成した3,477枚の画像を用い、FD-GAN、FFA-Net、DehazeFormer等の最先端モデルと定量評価（SSIM, PSNR, FSIM, LPIPS）で比較。さらにYOLOv11による動物検出性能の向上を確認した。 |
| 議論はある？ | 実環境での多様な気象条件の網羅性や、野生動物の行動データへの長期的な影響については今後の検討課題。また、物理モデルの仮定が適用できない複雑な照明環境下での性能検証が挙げられる。 |
| 次に読むべき論文は？ | [9] HybridDepth: Robust metric depth fusion by leveraging depth from focus and single-image priors (arXiv:2407.18443) |
| PDFリンク | https://arxiv.org/pdf/2604.16284v1 |
