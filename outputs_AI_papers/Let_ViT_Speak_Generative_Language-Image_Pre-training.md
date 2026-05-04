---
title: "Let ViT Speak: Generative Language-Image Pre-training"
date: 2026-05-04
arxiv_id: 2605.00809v1
url: http://arxiv.org/abs/2605.00809v1
---

# Let ViT Speak: Generative Language-Image Pre-training

| 項目 | 内容 |
|---|---|
| どんなもの？ | 大規模言語モデル（MLLM）のための、シンプルでスケーラブルな視覚エンコーダ学習フレームワーク「GenLIP」を提案した論文。従来の複雑な2タワー型やエンコーダ・デコーダ構造を排し、単一のTransformerを用いたミニマリストな生成型学習を実現している。 |
| 先行研究と比べてどこがすごい？ | 対照学習や複雑なテキストデコーダを必要とせず、標準的な言語モデリング目的のみで視覚エンコーダを直接学習する。これにより、少ない学習データでも既存の強力なベースラインと同等以上の性能を達成し、特にOCRや図表理解などの詳細な視覚タスクで高い優位性を示す。 |
| 技術や手法のキモはどこ？ | 「Let ViT Speak directly」という設計思想に基づき、視覚トークンから直接言語トークンを生成する単一モデルを採用した点。また、視覚トークンへの過度な注目集中（Attention Sink）を防ぎ、学習を安定させるための「Gated Attention（ゲート付き注意機構）」を導入した点が重要。 |
| どうやって有効だと検証した？ | Recap-DataComp-1B等のデータセットで最大8Bサンプルを用いて学習を行い、LLaVA-NeXT設定での冷凍視覚表現評価や、ImageNet/ADE20Kでの識別能力評価を実施。複数のモデルスケールにおいて、既存の対照学習手法や生成型手法を上回る性能を多角的に検証した。 |
| 議論はある？ | 現在の検証は学術規模のMLLM設定に留まっている点、1.0B〜8.0Bスケールでの学習に限定されている点、および高品質なキャプションデータへの依存による獲得コストが課題として挙げられている。 |
| 次に読むべき論文は？ | [LLaVA-NeXT: Improved reasoning, ocr, and world knowledge](https://arxiv.org/abs/2401.12599), [SigLIP: Sigmoid loss for language image pre-training](https://arxiv.org/abs/2303.15343) |
| PDFリンク | https://arxiv.org/pdf/2605.00809v1 |
