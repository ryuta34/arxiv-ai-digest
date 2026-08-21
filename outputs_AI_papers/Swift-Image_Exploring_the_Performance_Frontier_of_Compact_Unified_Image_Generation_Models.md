---
title: "Swift-Image: Exploring the Performance Frontier of Compact Unified Image Generation Models"
date: 2026-08-21
arxiv_id: 2608.20334v1
url: http://arxiv.org/abs/2608.20334v1
---

# Swift-Image: Exploring the Performance Frontier of Compact Unified Image Generation Models

| 項目 | 内容 |
|---|---|
| どんなもの？ | テキストからの画像生成、単一・複数画像の編集を統一的に扱う、計算リソースを抑えた軽量な高性能画像生成モデル「Swift-Image」を提案。6Bパラメータのモデルを中心に、推論効率に優れた3Bモデルや数ステップで生成可能な高速版も提供する。 |
| 先行研究と比べてどこがすごい？ | 巨大なバックボーンに依存せず、243K GPU時間という限られた計算リソースで、既存のオープンソースモデルを凌駕する性能を実現した点。また、プロンプト強化器（Prompt Enhancer）による意図理解とレンダリングの分離により、複雑な編集タスクで高い適応能力を発揮する。 |
| 技術や手法のキモはどこ？ | 高度な推論を行う「Prompt Enhancer」と、効率的な「6B単一ストリームDiT」の分離。さらに、進化的学習パイプライン、並列専門家による強化学習（RL）、マルチティーチャー型ポリシー蒸留（OPD）を組み合わせ、タスク間の干渉を抑制しつつ各専門スキルを統合した点。 |
| どうやって有効だと検証した？ | GEdit-Bench、ImgEdit-Bench、REDEdit-Benchといった標準的な編集ベンチマークに加え、独自指標CPI-BenchmarkやQwen-Image-Benchなどを用い、プロンプト強化の有無やモデルサイズによる比較評価を実施した。 |
| 議論はある？ | 複雑な要求に対する「推論とレンダリングの分離」の効果を強調しているが、非常に単純なタスクではこの分離によるオーバーヘッドが無視できない可能性がある。また、モデルの蒸留やプルーニングにおいて、特定のタスク間での干渉を完全には排除しきれない場合がある。 |
| 次に読むべき論文は？ | [DiffusionNFT (Zheng et al., 2025)](https://arxiv.org/abs/2509.16117)、[Flow-GRPO (Liu et al., 2025)](https://arxiv.org/abs/2505.05470)、[PromptEnhancer (Wang et al., 2025)](https://arxiv.org/abs/2509.04545) |
| PDFリンク | https://arxiv.org/pdf/2608.20334v1 |
