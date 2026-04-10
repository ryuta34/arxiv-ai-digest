---
title: "When Numbers Speak: Aligning Textual Numerals and Visual Instances in Text-to-Video Diffusion Models"
date: 2026-04-10
arxiv_id: 2604.08546v1
url: http://arxiv.org/abs/2604.08546v1
---

# When Numbers Speak: Aligning Textual Numerals and Visual Instances in Text-to-Video Diffusion Models

| 項目 | 内容 |
|---|---|
| どんなもの？ | テキストで指定されたオブジェクトの個数と、動画生成モデルが生成する映像の不一致を解消する学習不要のフレームワーク「NUMINA」です。事前学習済みモデルの潜在的な空間情報を利用し、生成プロセスをガイドすることで、高い計数精度と自然な動画生成を両立します。 |
| 先行研究と比べてどこがすごい？ | 既存モデルの再学習を必要とせず、推論時に動的にアテンションヘッドを選択・制御することで、複雑な計数タスクを解決できます。従来の手法が苦手とした「オブジェクトの追加・削除」といった構造的な操作において、高い安定性と時系列一貫性を維持している点が優位です。 |
| 技術や手法のキモはどこ？ | アテンションマップを分析して「物体分離能」が高いヘッドを自動特定し、そこから得られるレイアウト情報を用いて、クロスアテンションを明示的に調整（加算・減算）する「identify-then-guide（識別してからガイドする）」アプローチにあります。 |
| どうやって有効だと検証した？ | 1〜8個のオブジェクトを含む210のプロンプトからなる新評価ベンチマーク「CountBench」を構築しました。Wan2.1やCogVideoX等の主要モデルに対し、計数精度（CountAcc）、時系列一貫性（TC）、CLIPスコアを用いて、既存のプロンプト拡張やシード探索手法と比較検証しました。 |
| 議論はある？ | 限界として、物体の一部だけを認識してしまう過剰なセグメンテーションによる誤操作が発生する場合があります。今後は、個別のインスタンスをよりホリスティック（全体的）に捉える知覚的なグループ化手法を取り入れることが将来課題とされています。 |
| 次に読むべき論文は？ | [Diffusion Transformer (DiT) [53]](https://arxiv.org/abs/2212.09748)、[Wan: Open and advanced large-scale video generative models [59]](https://arxiv.org/abs/2503.20314)、[Make it count: Text-to-image generation with an accurate number of objects [4]](https://arxiv.org/abs/2501.07720) |
| PDFリンク | https://arxiv.org/pdf/2604.08546v1 |
