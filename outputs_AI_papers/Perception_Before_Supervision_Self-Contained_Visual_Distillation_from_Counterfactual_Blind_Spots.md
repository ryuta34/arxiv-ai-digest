---
title: "Perception Before Supervision: Self-Contained Visual Distillation from Counterfactual Blind Spots"
date: 2026-08-11
arxiv_id: 2608.09931v1
url: http://arxiv.org/abs/2608.09931v1
---

# Perception Before Supervision: Self-Contained Visual Distillation from Counterfactual Blind Spots

| 項目 | 内容 |
|---|---|
| どんなもの？ | マルチモーダル大規模言語モデル（MLLM）において、外部注釈や強化学習の報酬モデルを使わずに、モデル自身の推論に基づき「視覚的な盲点」を特定・活用して自己蒸留を行うフレームワーク。画像内の細かい領域をズームした際に推論性能が向上する現象を利用し、効率的なトークンレベルの自己教師あり学習を実現する。 |
| 先行研究と比べてどこがすごい？ | 従来手法は外部のセグメンテーションモデルやGPT-4o等の強力な外部モデルによる注釈を必要としていたが、本手法はモデル単体で完結するため外部ツールが一切不要。報酬ベースの粗い学習ではなく、トークン単位のコントラスティブな学習により、細かな視覚的認識タスクで大幅な性能向上を達成している点。 |
| 技術や手法のキモはどこ？ | モデルの回答分布の変化を見る「3ゲートの反事実的盲点基準」により、モデル自身が未活用な知覚情報を保持している領域を自動発見する点。その領域を「作物（crop）」としてポジティブな教師信号とし、該当領域をぼかした「幽霊（ghost）」をネガティブな教師信号とすることで、コントラスティブな自己蒸留を行う手法。 |
| どうやって有効だと検証した？ | 12個の主要な視覚認識・推論ベンチマーク（OCRBench, MMStar等）を用いて、Qwen3-VL-8B-Instructモデルで評価。既存の自己学習手法と比較して全タスクで最高性能を記録し、特に精密な視覚的注視が必要なタスクで顕著な改善を確認した。 |
| 議論はある？ | 手法は非常に効果的だが、モデルの推論能力が一定レベルに達している必要があり、極端に性能の低いモデルでの適用性には制限がある可能性がある。また、更なる性能向上のために視覚エンコーダーの更新も検討されたが、安定性の観点から本稿では凍結したままとしている。 |
| 次に読むべき論文は？ | [37] Vision-OPD: Learning to see fine details for multimodal LLMs via on-policy self-distillation (https://arxiv.org/abs/2605.18740), [42] Self-distilled reasoner: On-policy self-distillation for large language models (https://arxiv.org/abs/2601.18734) |
| PDFリンク | https://arxiv.org/pdf/2608.09931v1 |
