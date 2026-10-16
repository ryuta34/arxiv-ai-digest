---
title: "Which Tokens to Merge? Diffusion Dynamics for Efficient Image Generation"
date: 2026-10-16
arxiv_id: 2610.22370v1
url: http://arxiv.org/abs/2610.22370v1
---

# Which Tokens to Merge? Diffusion Dynamics for Efficient Image Generation

| 項目 | 内容 |
|---|---|
| どんなもの？ | 拡散モデルを用いた画像生成において、推論コストを削減するための「学習不要」なトークンマージングフレームワーク「DaTMe」を提案する論文。拡散モデルのデノイジングプロセスにおける「動的な生成変化」と「構造的な重要性」を考慮し、画質劣化を抑えつつ効率的な推論を実現する。 |
| 先行研究と比べてどこがすごい？ | 従来のCFG（分類器フリーガイダンス）ベースの手法が、プロンプトに明示された物体以外（背景や細部）の保護を苦手としていたのに対し、本手法は拡散の動的プロセスを活用することで、画像全体にわたる構造的整合性を高度に維持できる。 |
| 技術や手法のキモはどこ？ | Tweedie推定量を用いた「時間的変化マップ（M_temp）」と「空間的構造マップ（M_spat）」を組み合わせた「ダイナミクス認識型重要度マップ」を定義。これに基づき、重要トークンをアンカーとして保護しつつ、安定した背景領域などを効率的にマージする動的な役割割り当てを行う。 |
| どうやって有効だと検証した？ | PixArt-αおよびFLUXを用いた実験で、CLIPスコア、FID、SSIM、PSNR等を測定。加えて、32名の被験者によるユーザースタディを行い、視覚的忠実度とプロンプト整合性において他手法を上回る結果を示した。 |
| 議論はある？ | 極めて複雑なシーンや背景が入り組んだ画像では、過度な圧縮により必要なトークンが削除され、画質が劣化する可能性がある。また、DiTアーキテクチャのレイヤーごとの役割分担については未解明であり、今後の探索課題としている。 |
| 次に読むべき論文は？ | [9] Wu et al., "Importance-based token merging for efficient image and video generation" (ICCV 2025) <br> [10] Bolya & Hoffman, "Token merging for fast stable diffusion" (CVPR 2023) |
| PDFリンク | https://arxiv.org/pdf/2610.22370v1 |
