---
title: "A Chosen Future Can Still Be Rewritten: Causal Writability in Video Models"
date: 2026-09-15
arxiv_id: 2609.15980v1
url: http://arxiv.org/abs/2609.15980v1
---

# A Chosen Future Can Still Be Rewritten: Causal Writability in Video Models

| 項目 | 内容 |
|---|---|
| どんなもの？ | 動画生成モデルが物理的に不正確な動画を生成する際、正しい物理法則を学習していないのではなく、モデル内部に知識があるにもかかわらず活用できていないことを示した研究。介入（アクティベーション編集）により、モデルが本来持っている物理的な動きを強制的に引き出せることを明らかにしました。 |
| 先行研究と比べてどこがすごい？ | 「モデルが正しい動きを知っているか」という潜在的な知識の有無と、「それが生成に制御されているか」という制御可能性を理論的に分離した点。また、学習が進むにつれて特定の介入が効かなくなる「コミットメント（Commitment）」の境界を特定しました。 |
| 技術や手法のキモはどこ？ | 物理的に対立するデータ（例：赤い物体はゆっくり動くべきなのに速く動いている）に対して、モデル内部の潜在表現を編集する「因果的書き込み可能性（Causal Writability）」を提案。層ごとの介入や、物理パラメータに基づく編集コントローラーの実装が鍵となっています。 |
| どうやって有効だと検証した？ | 制御されたスプリング・マス運動のシミュレーション動画を用い、物体や背景の色によるショートカット学習を誘発。編集介入がデコードされた動画の周波数や色に与える影響を測定し、1.3BパラメータのWan 1.3Bモデルでも同様の現象を再現しました。 |
| 議論はある？ | 現時点では合成データによる限定的な環境下での検証に留まっており、より広範な世界モデルの訓練データで生じるショートカット学習に対して、同様の介入が普遍的に適用できるかは今後の課題です。 |
| 次に読むべき論文は？ | [Shortcut learning in deep neural networks (Geirhos et al., 2020)](https://arxiv.org/abs/2004.07780), [Video diffusion models (Ho et al., 2022)](https://arxiv.org/abs/2204.03458), [Locating and editing factual associations in GPT (Meng et al., 2022)](https://arxiv.org/abs/2202.05262) |
| PDFリンク | https://arxiv.org/pdf/2609.15980v1 |
