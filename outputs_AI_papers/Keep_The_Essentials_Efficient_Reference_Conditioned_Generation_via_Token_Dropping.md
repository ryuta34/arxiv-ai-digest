---
title: "Keep The Essentials: Efficient Reference Conditioned Generation via Token Dropping"
date: 2026-06-23
arxiv_id: 2606.23682v1
url: http://arxiv.org/abs/2606.23682v1
---

# Keep The Essentials: Efficient Reference Conditioned Generation via Token Dropping

| 項目 | 内容 |
|---|---|
| どんなもの？ | 参照画像ベースの拡散モデルにおける、入力参照画像のトークン数を削減することで推論の効率化を図る手法「Sparse Context」を提案。参照画像を疎なトークン集合として表現し、計算コストを大幅に削減しつつ高品質な生成を維持する。 |
| 先行研究と比べてどこがすごい？ | 従来のモデルが参照画像を密なグリッドとして扱うため計算コストが二次的に増大していたのに対し、本手法は推論時に必要なトークンのみを優先的に選択する動的なトークン削減を実現。単一参照で2倍、複数参照で最大4倍の推論高速化を達成している点。 |
| 技術や手法のキモはどこ？ | 推論時のトークン削減に備えて学習時にランダムなトークン脱落（Token Dropping）を行うことで、モデルに疎な表現に対する頑健性を学習させる点。また、タスクに応じてCannyエッジや顕著性マップを用いたタスク認識型のトークン選択を行う点。 |
| どうやって有効だと検証した？ | FLUX.2-Klienモデルを用い、PIE-Bench（画像編集）やSubject-200K/CustomDiffusion-105（パーソナライズ生成）等のデータセットで評価。LPIPS、CLIP-I、DINO等の指標を用いて品質を測定し、従来の手法と比較して効率と品質のトレードオフを改善したことを実証した。 |
| 議論はある？ | タスク（スタイライズかオブジェクト置換かなど）によって最適なトークン選択ヒューリスティックが異なる点。特定の選択手法（エッジベース等）が、背景の保持に悪影響を及ぼす場合があるという限界が指摘されている。 |
| 次に読むべき論文は？ | [Flux.1: Flow matching for in-context image generation](https://arxiv.org/abs/2506.00000)（ベースモデル関連）、[Token merging for fast stable diffusion](https://arxiv.org/abs/2303.17604)（トークン削減の先行研究） |
| PDFリンク | https://arxiv.org/pdf/2606.23682v1 |
