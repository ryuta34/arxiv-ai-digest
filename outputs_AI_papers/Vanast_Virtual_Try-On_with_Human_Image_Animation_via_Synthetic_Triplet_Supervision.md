---
title: "Vanast: Virtual Try-On with Human Image Animation via Synthetic Triplet Supervision"
date: 2026-04-07
arxiv_id: 2604.04934v1
url: http://arxiv.org/abs/2604.04934v1
---

# Vanast: Virtual Try-On with Human Image Animation via Synthetic Triplet Supervision

| 項目 | 内容 |
|---|---|
| どんなもの？ | 単一の人物画像、対象の衣類画像、およびポーズ動画を入力として、衣類を付け替えた状態で自然に動く人物アニメーション動画を生成する統合的なフレームワーク「Vanast」を提案した研究。従来必要とされた多段階の処理を排除し、衣類の転送と動画生成を単一のステップで高精度に実現している。 |
| 先行研究と比べてどこがすごい？ | 従来手法（画像ベースの試着＋動画生成の2段階パイプライン）で発生していた人物のアイデンティティ変化、衣類の歪み、時間的な不整合といった課題を解決した。また、大規模な「合成トリプレット（人物・衣類・動作動画）」データセットの構築パイプラインを開発し、学習を効率化している。 |
| 技術や手法のキモはどこ？ | 既存の学習済みビデオ拡散モデル（DiT）をベースに、「Human Animation Module (HAM)」と「Garment Transfer Module (GTM)」という独立した2つのモジュールを組み込む「Dual Module」構造を採用した点。これにより、ポーズの忠実な再現と衣類の精密な転送を両立し、追加の微調整なしで零知識（zero-shot）での衣類補間を可能にした。 |
| どうやって有効だと検証した？ | 提案手法を、既存の画像ベース試着モデルと動画アニメーションモデルを組み合わせた計16通りの比較用ベースラインと比較。InternetおよびViViDの2つの評価用データセットを使用し、L1、PSNR、SSIM、LPIPS、FID、VFID等の定量的指標と定性的な比較を通じて、本手法の優れた忠実度と一貫性を証明した。 |
| 議論はある？ | 現在のモデルは複数の衣服を転送できるが、オンラインショッピングサイト等の非常に限られたデータから学習しているため、極端に複雑な非日常的な環境や衣類への対応は今後の拡張課題として残る。また、データセット構築パイプラインの品質向上も継続的な改善が必要。 |
| 次に読むべき論文は？ | [13] Animate Anyone: Consistent and controllable image-to-video synthesis for character animation, [15] VACE: All-in-one video creation and editing, [33] OOTDiffusion: Outfitting fusion based latent diffusion for controllable virtual try-on |
| PDFリンク | https://arxiv.org/pdf/2604.04934v1 |
