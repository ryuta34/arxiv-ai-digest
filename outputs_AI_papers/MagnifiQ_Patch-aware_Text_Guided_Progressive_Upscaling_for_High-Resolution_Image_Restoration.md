---
title: "MagnifiQ: Patch-aware Text Guided Progressive Upscaling for High-Resolution Image Restoration"
date: 2026-08-17
arxiv_id: 2608.14543v1
url: http://arxiv.org/abs/2608.14543v1
---

# MagnifiQ: Patch-aware Text Guided Progressive Upscaling for High-Resolution Image Restoration

| 項目 | 内容 |
|---|---|
| どんなもの？ | 低品質な画像から最大32倍のアップスケーリングを行い、4Kの高解像度画像を生成するテキストガイド付き画像復元フレームワーク。拡散モデル（SDXL）を基盤とし、パッチ単位でのきめ細やかな復元を実現する。 |
| 先行研究と比べてどこがすごい？ | 従来手法（StableSR等）が抱えていた計算コストの高さや、高解像度化時のテクスチャの繰り返し・不整合を解決した。パッチレベルのテキストプロンプトを導入することで、グローバルな構造を保持しつつ、局所的な細部を詳細に復元できる点が優位。 |
| 技術や手法のキモはどこ？ | SDXLの自己注意層（self-attention）を効率的な畳み込みベースのPADRe層に置き換え計算量を削減した点と、進化的アップスケーリング過程でLLaVAを用いた「パッチ単位のテキストプロンプト」を cross-attention に注入する「PACA (Patch-Aware Cross-Attention)」モジュール。 |
| どうやって有効だと検証した？ | 50枚のAesthetic-4KデータセットやDIV2Kデータセットを用い、MANIQA、CLIP-IQA、LAION-Aesthetic等の指標で定量評価を実施。また、10名の参加者によるブラインドA/Bユーザーテストを行い、他手法よりも高い選好度（75%）を獲得した。 |
| 議論はある？ | 現状の手法は大規模な生成モデルに依存しており、建築物など特定の被写体で稀にハルシネーション（非現実的なテクスチャの生成）が発生する。また、完全なリアルタイム処理ではなく、さらなる高速化（1ステップ復元など）が将来課題。 |
| 次に読むべき論文は？ | [17] Letourneau et al., "PADRe: A unifying polynomial attention drop-in replacement for efficient vision transformer"、[37] Yu et al., "Scaling up to excellence: Practicing model scaling for photo-realistic image restoration in the wild" |
| PDFリンク | https://arxiv.org/pdf/2608.14543v1 |
