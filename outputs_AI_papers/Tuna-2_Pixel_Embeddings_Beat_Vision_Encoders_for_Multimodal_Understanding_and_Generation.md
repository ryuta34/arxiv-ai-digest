---
title: "Tuna-2: Pixel Embeddings Beat Vision Encoders for Multimodal Understanding and Generation"
date: 2026-04-28
arxiv_id: 2604.24763v1
url: http://arxiv.org/abs/2604.24763v1
---

# Tuna-2: Pixel Embeddings Beat Vision Encoders for Multimodal Understanding and Generation

| 項目 | 内容 |
|---|---|
| どんなもの？ | 視覚エンコーダー（VAEや表現エンコーダー）を完全に排除し、生のピクセル値から直接視覚理解と生成を行う、ネイティブな統合マルチモーダルモデル「Tuna-2」を提案した研究。 |
| 先行研究と比べてどこがすごい？ | 従来のモデルが依存していたプリトレーニング済みの視覚エンコーダーを不要とし、単一のTransformerアーキテクチャで視覚理解と生成の両方を実現。特に、微細な視覚的認識タスクにおいて、従来の潜在空間モデルを上回る性能を達成した。 |
| 技術や手法のキモはどこ？ | VAEを介さず、パッチ埋め込み層を用いて画像トークンをLLMデコーダーへ直接入力するアーキテクチャ。加えて、ピクセル空間での学習の困難さを克服するための「マスキングベースの視覚特徴学習スキーム」を導入した点。 |
| どうやって有効だと検証した？ | 9つの画像理解ベンチマーク（GQA, MMVet, MMMU, OCRBench等）および画像生成ベンチマーク（GenEval, DPG-Bench）で評価。また、アテンションマップによる視覚的定性評価を行い、誤解を招く言語コンテキスト下での頑健性を実証。 |
| 議論はある？ | 生成タスクにおいては、表現エンコーダーを用いたTuna-Rの方が初期段階で安定した性能を示す場合がある。完全なエンコーダーフリー設計は、学習初期のセマンティックな事前知識の獲得において補完的なアプローチの検討が必要。 |
| 次に読むべき論文は？ | [Tuna: Taming unified visual representations for native unified multimodal models](https://arxiv.org/abs/2512.02014)（前身研究）、[JiT: Back to basics: Let denoising generative models denoise](https://arxiv.org/abs/2511.13720)（ピクセル空間生成の基礎）、[Show-o2: Improved native unified multimodal models](https://arxiv.org/abs/2506.15564) |
| PDFリンク | https://arxiv.org/pdf/2604.24763v1 |
