---
title: "Critical-State RL: Diagnosing Trainable States for Multi-Turn Tool Use"
date: 2026-09-22
arxiv_id: 2609.24985v1
url: http://arxiv.org/abs/2609.24985v1
---

# Critical-State RL: Diagnosing Trainable States for Multi-Turn Tool Use

| 項目 | 内容 |
|---|---|
| どんなもの？ | マルチターンツール使用における、学習に最適な「決定（State）」を自動診断・選択する強化学習手法「Critical-State RL」。 trajectory（軌跡）レベルの報酬ではなく、行動に依存した局所的な学習シグナルを抽出することで、効率的なモデルのファインチューニングを実現する。 |
| 先行研究と比べてどこがすごい？ | 従来の強化学習は軌跡全体に報酬を適用するためノイズが多く、どのステップの改善が重要か特定できなかった。本手法は、Nested Samplingを用いて、事後のランダムな事象と現在の行動に起因する報酬変動を切り分けることで、学習すべき最適なポイント（Critical State）をピンポイントで特定できる点に優位性がある。 |
| 技術や手法のキモはどこ？ | タスク固有の構造に基づいた「候補となる行動」に対し、 nested sampling で報酬の分散を分解し、行動依存の変動（action-dependent reward variation）が最大となる箇所を選択する点。また、選択した行動のみにRL損失を適用し、他はコンテキストとして扱うことで、学習効率を高める点。 |
| どうやって有効だと検証した？ | Berkeley Function Calling Leaderboard (BFCL) v4の「missing-function」や「missing-argument」等のタスクで、Gemma-4-26Bモデル等を用いて検証。診断に基づき選択したターンの学習が、他と比較して大幅な精度向上（missing-functionで約14ポイント等）をもたらすことを示した。 |
| 議論はある？ | 現在の手法はカテゴリーごとの選択に留まっており、各ステップの分散の大きさに基づいた厳密な閾値設定には課題がある。また、学習によるモデル更新が他の未学習ターンに予期せぬ影響（drift）を与える可能性があり、その影響範囲を理論的に評価している。 |
| 次に読むべき論文は？ | [1] [PivotRL: High accuracy agentic post-training at low compute cost](https://arxiv.org/abs/2603.21383)、[49] [Verified critical step optimization for LLM agents](https://arxiv.org/abs/2608.13179)、[50] [Group-in-group policy optimization for LLM agent training](https://arxiv.org/abs/2505.11821) |
| PDFリンク | https://arxiv.org/pdf/2609.24985v1 |
