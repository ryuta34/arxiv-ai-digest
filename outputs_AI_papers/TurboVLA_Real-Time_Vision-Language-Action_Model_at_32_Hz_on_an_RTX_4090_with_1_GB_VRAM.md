---
title: "TurboVLA: Real-Time Vision-Language-Action Model at 32 Hz on an RTX 4090 with <1 GB VRAM"
date: 2026-07-30
arxiv_id: 2607.27205v1
url: http://arxiv.org/abs/2607.27205v1
---

# TurboVLA: Real-Time Vision-Language-Action Model at 32 Hz on an RTX 4090 with <1 GB VRAM

| 項目 | 内容 |
|---|---|
| どんなもの？ | 大規模言語モデル（LLM）を中心とした従来のVLA（Vision-Language-Action）モデルのボトルネックを解消する、リアルタイムかつ効率的なロボット操作モデル「TurboVLA」を提案。視覚情報と言語指示を直接相互作用させることで、わずか0.2Bのパラメータ数で32Hzの推論速度と低メモリ消費を実現した。 |
| 先行研究と比べてどこがすごい？ | LLMを介さない直接的な「V+L→A」のマッピングにより、従来のLLM中心型と比較して大幅な低遅延（31.2ms）とモデル軽量化（0.9GB VRAM）を達成した。LIBERO等のベンチマークで既存の大型モデルを凌駕または匹敵する性能を実証した。 |
| 技術や手法のキモはどこ？ | LLMという汎用的な生成モデルを排除し、軽量なテキストエンコーダ（BERT）とビジョンエンコーダ、および双方向クロスアテンションによる「Vision-Language Interaction Module」を用いた点。これにより、タスク固有の視覚・言語特徴を直接統合し、並列的な行動チャンク生成を行う。 |
| どうやって有効だと検証した？ | LIBERO（単腕マニピュレーション）およびRoboTwin 2.0（双腕マニピュレーション）環境で評価を実施。実世界においてもAgileX Piperロボットを用いた実証実験を行い、精度とリアルタイム性の両立を証明した。 |
| 議論はある？ | 高度な推論やオープンエンドな言語生成が必要な高次タスクには不向きであり、現状は実行レベルの指示に特化している。将来的な課題として、LLMの持つ高次計画能力と本手法の効率的な実行経路を組み合わせた階層的システムの構築が挙げられている。 |
| 次に読むべき論文は？ | [ACT: Learning fine-grained bimanual manipulation with low-cost hardware](https://arxiv.org/abs/2304.13705)、[π0.5: a vision-language-action model with open-world generalization](https://arxiv.org/abs/2410.01092) |
| PDFリンク | https://arxiv.org/pdf/2607.27205v1 |
