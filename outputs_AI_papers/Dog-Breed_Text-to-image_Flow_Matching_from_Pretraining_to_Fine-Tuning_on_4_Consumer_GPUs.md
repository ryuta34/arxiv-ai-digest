---
title: "Dog-Breed Text-to-image Flow Matching from Pretraining to Fine-Tuning on 4 Consumer GPUs"
date: 2026-10-14
arxiv_id: 2610.18870v1
url: http://arxiv.org/abs/2610.18870v1
---

# Dog-Breed Text-to-image Flow Matching from Pretraining to Fine-Tuning on 4 Consumer GPUs

| 項目 | 内容 |
|---|---|
| どんなもの？ | 消費者向けGPU（RTX 3090 × 4枚）を用いて、約1時間で犬種のテキスト・トゥ・イメージ（T2I）モデルを事前学習、さらに15分でファインチューニングを完遂する軽量フレームワーク「MiniDog」。リソース制限のある研究者でもT2I学習パイプライン全体を体験可能にする教育的・実践的なリソース。 |
| 先行研究と比べてどこがすごい？ | 巨大な計算資源を要するT2Iモデルの学習を、事前計算された画像・テキスト特徴量（キャッシング）と効率的なアーキテクチャ（LightningDiT、E2E-INVAE）の組み合わせにより、極めて短時間かつ低コストで実現可能にした点。 |
| 技術や手法のキモはどこ？ | 学習データを固定・キャッシュして再利用する仕組みに加え、表現学習を高速化するiREPA（中間層の空間構造転送）の採用、および特定のVAE（E2E-INVAE）と効率的な拡散トランスフォーマーの統合。 |
| どうやって有効だと検証した？ | ImageNetの犬画像26k枚による事前学習と、FLUX.1-schnellで生成した2k枚によるSFTを行い、gFID、PSNR、HPSv2、PickScoreを用いて定量評価を実施。また、様々なエンコーダーや手法（REPA vs iREPA）の比較実験を詳細に行い、手法の有効性を立証。 |
| 議論はある？ | 技術的な新規性は主張しておらず、汎用的な大規模T2Iモデルではなくドッグイメージ生成に特化した最小限のプロジェクトである点。SFTを行うと高画質なデータに過剰適合し、FIDが悪化する場合があることなどが述べられている。 |
| 次に読むべき論文は？ | [LightningDiT](https://arxiv.org/abs/2407.16900)、[REPA-E](https://arxiv.org/abs/2505.02237)、[DiffusionBench](https://arxiv.org/abs/2606.24888) |
| PDFリンク | https://arxiv.org/pdf/2610.18870v1 |
