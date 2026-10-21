---
title: "SolarRenderer: Few-Step Generative Reference Rendering"
date: 2026-10-21
arxiv_id: 2610.28630v1
url: http://arxiv.org/abs/2610.28630v1
---

# SolarRenderer: Few-Step Generative Reference Rendering

| 項目 | 内容 |
|---|---|
| どんなもの？ | 任意の構造表現（深度、ポーズ、スケルトン等）からリアルな動画を生成する汎用的な動画レンダラー「SolarRenderer」。単一の制御LoRAと軽量なアダプターを用いることで、訓練時に見たことのない多様な構造表現にも対応可能。 |
| 先行研究と比べてどこがすごい？ | 特定のエンジンや構造表現に依存せず、かつ少ないステップ数（4ステップ）で高品質な動画を高速に生成できる。また、構造ごとのタイプ識別子を必要とせず、教師なしで多様な未知の表現に一般化できる点が優れている。 |
| 技術や手法のキモはどこ？ | 冷凍された大規模な動画基盤モデルをそのまま活用し、構造条件を「ネイティブ参照パス」へ入力する点。さらに、構造条件に基づいて教師モデルを外挿する「構造誘導型分布マッチング蒸留」により、少ない推論ステップ数で高い忠実度を実現した。 |
| どうやって有効だと検証した？ | 136Kのフレームアライメントされたクリップからなる大規模データセットを構築し、インディストリビューションおよび16種類の構造表現を用いた汎化ベンチマークで評価。Gemini 3.8 Flashを用いたペアワイズ評価や自動指標で、既存の構造条件付き生成モデルを上回る結果を示した。 |
| 議論はある？ | Causal Streaming（因果的ストリーミング）環境下では、時系列上の後のブロックが前のブロックの画質に依存し、長時間の生成時に初期フレームの色調から乖離することがある。また、非常に複雑な構造表現では依然としてフルステップの生成が好まれるケースがある。 |
| 次に読むべき論文は？ | [DMAD: Distribution Matching as Adversarial Distillation for Fast Visual Generation](https://arxiv.org/abs/2610.02188), [SolarWM: Open Data and Scalable Training for Long-Horizon Video World Models](https://arxiv.org/abs/2609.02886) |
| PDFリンク | https://arxiv.org/pdf/2610.28630v1 |
