---
title: "Temporal Self-Distillation: Learning Visual State Tracking in Videos Without Supervision"
date: 2026-09-04
arxiv_id: 2609.04203v1
url: http://arxiv.org/abs/2609.04203v1
---

# Temporal Self-Distillation: Learning Visual State Tracking in Videos Without Supervision

| 項目 | 内容 |
|---|---|
| どんなもの？ | 動画理解AI（Video-LLM）における「継続的な視覚状態追跡（Continuous Video State Tracking）」の精度を向上させる、教師なしの自己蒸留フレームワーク「S³T」を提案。ラベルや外部報酬モデルを一切使用せず、同一動画の異なる時間的サンプリング密度を教師・生徒として利用することで、モデル自身の能力を向上させる。 |
| 先行研究と比べてどこがすごい？ | 従来手法はラベルや外部ジャッジモデルを必要とするものが多かったが、S³Tは完全に自己完結型である点が特徴。特にアクション認識やモーメント特定ではなく、物体カウントの変化など累積的な状態追跡能力において、VSTATベンチマークで大幅な性能向上（+2.70）を実現した。 |
| 技術や手法のキモはどこ？ | 同一クリップを「スパース（12フレーム、生徒）」と「密（24フレーム、教師）」の2つの時間的密度でサンプリングし、密な方からの知識をスパースな方に蒸留する。共通のLoRAアダプターを用い、Jensen-Shannonダイバージェンスで教師の出力を生徒に模倣させることで、ラベルなしでの継続的学習を可能にした点。 |
| どうやって有効だと検証した？ | VSTATベンチマークにおいて、オープンソースの強力なベースモデルと比較。累積的な状態推論を要するタスク（Count, Sequenceなど）で精度が向上することを確認。さらに、合成動画で学習した能力がYouTube動画などの実データにも転移し、MVBench等で性能が向上することを実証した。 |
| 議論はある？ | 手法はLLaVA-OV-2-8Bでは明確な効果を示したが、検証した他の11種類のベースモデルでは一貫して成功するわけではなく、適用先モデルの特性に依存する可能性がある。また、モデルの言語デコーダーにおける推論能力のボトルネックが主要な改善ポイントであると考察されている。 |
| 次に読むべき論文は？ | [1] LLaVA-OneVision: Easy visual task transfer (arXiv:2408.03326)<br>[2] VSTAT: Benchmarking visual state tracking in multimodal video understanding (arXiv:2606.03920)<br>[3] Model soups: averaging weights of multiple fine-tuned models improves accuracy (ICML 2022) |
| PDFリンク | [https://arxiv.org/pdf/2609.04203v1](https://arxiv.org/pdf/2609.04203v1) |
