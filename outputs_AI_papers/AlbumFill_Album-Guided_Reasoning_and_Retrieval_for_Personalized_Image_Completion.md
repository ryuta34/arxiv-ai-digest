---
title: "AlbumFill: Album-Guided Reasoning and Retrieval for Personalized Image Completion"
date: 2026-05-05
arxiv_id: 2605.02892v1
url: http://arxiv.org/abs/2605.02892v1
---

# AlbumFill: Album-Guided Reasoning and Retrieval for Personalized Image Completion

| 項目 | 内容 |
|---|---|
| どんなもの？ | パーソナルアルバム内の写真から、Occlusion（欠損部）を持つ画像に対して、個人を特定しつつ自然に画像を修復する「AlbumFill」というトレーニング不要のフレームワーク。VLMを用いて欠損部分のセマンティックな内容を推論し、アルバム内から最適な参照画像を自動検索して補完する手法。 |
| 先行研究と比べてどこがすごい？ | 従来手法はユーザーによる明示的な参照画像の指定が必要だったが、本研究はアルバム全体を検索対象として自動でアイデンティティの一致する画像を特定できる。また、VLMによる推論を介在させることで、アルバム内の多様な画像から「欠損内容」と「個人特性」の両方に合致した最適な参照画像を高精度に取得できる点。 |
| 技術や手法のキモはどこ？ | ①VLMによる「Masked Visual Reasoning」で欠損部の内容を推論、②それに基づいた「Composed Query Embedding」によるアルバム内検索、③UniReal等の参照型インペインティングモデルへの統合という3段階のパイプライン。特定の学習を必要としないモジュール型設計。 |
| どうやって有効だと検証した？ | CUFEDデータセットを加工し、53,294枚の画像から構成される「AlbumFill Benchmark」を構築。CIR（画像検索）性能をRecall@KやmAP@Kで評価し、画像補完性能をCLIP/DINO類似度、LPIPS、PSNR等の指標を用いて既存手法と比較。さらにマスク比率による性能変化の検証を実施。 |
| 議論はある？ | マスク領域が大きい場合には参照画像が適切であっても補完が困難になる場合がある。また、現在の手法はアルバム内のアイデンティティの一致には強いが、極端に異なる照明環境やポーズでの検索精度向上には将来的な改善の余地がある。 |
| 次に読むべき論文は？ | CompleteMe [49], UniReal [9], LinCIR [18], BrushNet [25] |
| PDFリンク | https://arxiv.org/pdf/2605.02892v1 |
