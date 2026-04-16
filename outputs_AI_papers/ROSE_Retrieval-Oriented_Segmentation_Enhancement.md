---
title: "ROSE: Retrieval-Oriented Segmentation Enhancement"
date: 2026-04-16
arxiv_id: 2604.14147v1
url: http://arxiv.org/abs/2604.14147v1
---

# ROSE: Retrieval-Oriented Segmentation Enhancement

| 項目 | 内容 |
|---|---|
| どんなもの？ | マルチモーダル大規模言語モデル（MLLM）の学習データカットオフ後の新規・新興エンティティに対するセグメンテーション能力を評価するタスク（NEST）と、それを解決するプラグアンドプレイ型のフレームワーク「ROSE」を提案した。 |
| 先行研究と比べてどこがすごい？ | 従来のモデルは学習済み知識に依存するため、最近の出来事や新規製品を正確にセグメンテーションできないという課題があった。ROSEはリアルタイムのインターネット検索を統合することで、モデルの知識を更新し、19.2%という大幅なgIoU向上を実現した。 |
| 技術や手法のキモはどこ？ | インターネットからの情報取得（IRAG）、テキストプロンプトによる補強（TPE）、検索画像を用いた視覚的プロンプトによる誤認識の修正（VPE）、および検索の必要性を判断する「WebSense」モジュールの4つの構成要素。 |
| どうやって有効だと検証した？ | 自動生成された1,500以上のサンプルを含むNESTベンチマークを構築し、既存のセグメンテーションモデル（LISA等）と、GPT-4o/Gemini 2.0を用いた検索ベースのベースラインに対して比較実験を行った。 |
| 議論はある？ | 自動生成された評価データセットの質や、検索クエリの複雑性への対応、またWebSenseが常に完璧に検索の必要性を判断できるわけではない点が課題として挙げられる。 |
| 次に読むべき論文は？ | [19] LISA: Reasoning Segmentation via Large Language Model, [31] Gemini: a family of highly capable multimodal models, [21] SearchLVLMs: A plug-and-play framework for augmenting large vision-language models by searching up-to-date internet knowledge. |
| PDFリンク | https://arxiv.org/pdf/2604.14147v1 |
