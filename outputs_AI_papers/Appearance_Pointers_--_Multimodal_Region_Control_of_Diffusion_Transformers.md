---
title: "Appearance Pointers -- Multimodal Region Control of Diffusion Transformers"
date: 2026-07-22
arxiv_id: 2607.19344v1
url: http://arxiv.org/abs/2607.19344v1
---

# Appearance Pointers -- Multimodal Region Control of Diffusion Transformers

| 項目 | 内容 |
|---|---|
| どんなもの？ | 拡散モデル（DiT）において、テキストや画像などの多様な入力（マルチモーダル）を領域ごとに指定して、高精度に生成・編集するための「Appearance Pointers」を提案した研究。ユーザーが指定した領域マスクに基づき、局所的な制御を単一のデノイジングパスで実現する。 |
| 先行研究と比べてどこがすごい？ | テキストのみや画像のみといった単一モダリティに制約されていた従来手法に対し、本手法はモダリティ非依存なインターフェースを提供し、同一シーン内で画像とテキストを組み合わせて同時に制御できる点。また、大規模な再学習なしに既存のDiTベースモデルに統合可能なモジュール性を有する。 |
| 技術や手法のキモはどこ？ | リージョン（領域）に対応する信号をコンパクトなトークンに集約・変換する「Region Correspondence Transformer」と、複数の領域情報を効率的に統合する「Region Aggregation Transformer」。これにより、計算コストを抑えつつ空間的な整合性を保つ。 |
| どうやって有効だと検証した？ | 独自の合成データセット「Appearance Pointers-37K」を作成し、CLIPスコア、DINO-I、MIoUなどの指標を用いて既存手法と比較。また、実データセット（SACap）での評価や、生成物の定性的比較、アブレーションスタディを実施して各モジュールの有効性を実証。 |
| 議論はある？ | 人間の顔など、極めて詳細な識別情報の保持には課題が残る点。また、領域数が10個を超えるような非常に複雑なシーンでは、アーティファクトの発生や領域指定の精度低下が見られることがある。 |
| 次に読むべき論文は？ | [Flux.1: Official inference repository](https://github.com/black-forest-labs/flux)や[DreamRenderer](https://arxiv.org/abs/2503.12885)、[Seg2Any](https://arxiv.org/abs/2506.00596)などが比較対象として挙げられる。 |
| PDFリンク | https://arxiv.org/pdf/2607.19344v1 |
