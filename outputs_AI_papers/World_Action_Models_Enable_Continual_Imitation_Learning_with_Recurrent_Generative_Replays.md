---
title: "World Action Models Enable Continual Imitation Learning with Recurrent Generative Replays"
date: 2026-06-26
arxiv_id: 2606.27374v1
url: http://arxiv.org/abs/2606.27374v1
---

# World Action Models Enable Continual Imitation Learning with Recurrent Generative Replays

| 項目 | 内容 |
|---|---|
| どんなもの？ | 過去のタスクのデモンストレーションを保存せずに、ワールドアクションモデル（WAM）自身の生成能力を用いて擬似的な学習データを再生成し、継続学習時の破滅的忘却を緩和するフレームワーク「REGEN」を提案した。 |
| 先行研究と比べてどこがすごい？ | 従来手法が過去の学習データをバッファに保存する必要があったのに対し、本手法はモデル自体が過去のタスクを「想像」してリプレイするため、メモリ制約がある環境や実環境で非常に実用的である点。 |
| 技術や手法のキモはどこ？ | タスクの言語指示と現在の観察状態からWAMを条件付けし、自身の生成した未来の視覚観察を再帰的に入力し続けることで、過去のタスクの完全な擬似軌道を生成する手法。 |
| どうやって有効だと検証した？ | LIBEROベンチマーク（シミュレーション）およびxArm7実機を用いたピック＆プレースタスクで評価し、逐次ファインチューニングと比較して忘却を50%以上低減し、実データを保存する手法に近い性能を達成した。 |
| 議論はある？ | 長期間の再帰的な生成による視覚的品質の劣化や、生成された視覚情報と実際のロボット動作の不整合（アクションと観察の乖離）がボトルネックであり、これらが性能向上の余地となっている。 |
| 次に読むべき論文は？ | [Cosmos policy: Fine-tuning video models for visuomotor control and planning](https://arxiv.org/abs/2601.16163) (本研究のベースモデル), [LIBERO: Benchmarking knowledge transfer for lifelong robot learning](https://arxiv.org/abs/2310.08864) |
| PDFリンク | https://arxiv.org/pdf/2606.27374v1 |
