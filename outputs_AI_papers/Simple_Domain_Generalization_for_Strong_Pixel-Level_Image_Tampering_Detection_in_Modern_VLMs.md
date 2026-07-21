---
title: "Simple Domain Generalization for Strong Pixel-Level Image Tampering Detection in Modern VLMs"
date: 2026-07-21
arxiv_id: 2607.18230v1
url: http://arxiv.org/abs/2607.18230v1
---

# Simple Domain Generalization for Strong Pixel-Level Image Tampering Detection in Modern VLMs

| 項目 | 内容 |
|---|---|
| どんなもの？ | 現代の視覚言語モデル（VLM）で生成・編集された画像に対し、特定の生成器に依存せず汎用的にピクセル単位の改ざんを検出・特定する手法「PIXAR-DG」を提案した。既存の検出モデルが特定の生成器のデータに過学習してしまう課題を解決し、未知の生成器に対しても高いロバスト性を実現する。 |
| 先行研究と比べてどこがすごい？ | 従来手法（PIXARなど）よりも少ない学習データ（全体の19.2%）で、未知の生成器（GPT-Image-2.0, Gemini-3.1, FLUX.2等）に対する改ざん検出精度を大幅に向上（gIoUで26.1%、cIoUで26.8%改善）させた点。 |
| 技術や手法のキモはどこ？ | 1. 学習時の偏りを防ぐ「均衡型ミニバッチサンプリング」、2. 大規模なベースデータ学習後に少量の新しいドメインデータを注入する「遅延注入（Late-Injection）戦略」、3. 学習の過学習を防ぎ安定化させる「低学習率の定数スケジューラ」の3点。 |
| どうやって有効だと検証した？ | 6種類の生成器を用いた公開ベンチマーク（PIXAR）を使用。Qwen-ImageとGemini-2.5をベース学習データとし、他の4つの生成器を未知のドメイン（OOD）として設定し、各種メトリクス（gIoU, cIoU, F1スコア）や定性的な可視化を通じて性能を実証した。 |
| 議論はある？ | データセットの多様性や品質に性能が依存する点や、未知のドメインに対する少量のラベル付きデータが必要であること、またモデル自体の構造は既存のセグメンテーションモデルに依拠している点が挙げられる。 |
| 次に読むべき論文は？ | [PIXAR: From masks to pixels and meaning](https://arxiv.org/abs/2603.20193), [SIDA: Social media image deepfake detection, localization and explanation](https://arxiv.org/abs/2506.00902) |
| PDFリンク | https://arxiv.org/pdf/2607.18230v1 |
