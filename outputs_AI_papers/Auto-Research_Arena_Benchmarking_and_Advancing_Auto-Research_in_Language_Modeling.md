---
title: "Auto-Research Arena: Benchmarking and Advancing Auto-Research in Language Modeling"
date: 2026-10-28
arxiv_id: 2610.35866v1
url: http://arxiv.org/abs/2610.35866v1
---

# Auto-Research Arena: Benchmarking and Advancing Auto-Research in Language Modeling

| 項目 | 内容 |
|---|---|
| どんなもの？ | 自律的な研究エージェント（Auto-Research）を評価するための、言語モデルの事前学習に関するマルチターゲットベンチマーク「Auto-Research Arena」。モデル、データ、学習、推論という様々な側面において、品質制約下での最適化能力を横断的に評価する枠組みを提案している。 |
| 先行研究と比べてどこがすごい？ | 既存のベンチマークが特定の指標やタスクに偏っていたのに対し、Arenaは共通の実験環境下で9つの異なる効率化目標（パラメータ数、学習FLOPs、推論レイテンシ等）を統一的に評価できる点。また、単なる評価にとどまらず、発見されたアイデアを再利用してモデル品質を向上させるプロセスを体系化している。 |
| 技術や手法のキモはどこ？ | 「Admissibility（許容性）」と「Improvement（改善）」を分離する制約付き最適化問題としての定式化。品質閾値（バリデーションBPB）をクリアした上で、特定のリソース指標を最小化するという枠組みにより、多様な研究目標を共通の基準で比較可能にした点。 |
| どうやって有効だと検証した？ | 7つの研究ハーネス（AutoScientists, Sequential Search等）と2つの基盤モデルを用いて実験を行い、ハーネス間の性能差を明らかにするとともに、発見された32のアイデアを再統合してモデル品質（BPB）の向上を実証した。また、検索ホライゾンを超えた発見の転移性も検証済み。 |
| 議論はある？ | 言語モデルの自律的検索に特化しており、全自動的な科学的研究プロセス全体をカバーしているわけではないこと。また、システム測定のノイズによる微小な差の解釈には注意が必要であると述べている。 |
| 次に読むべき論文は？ | [GEAR: Genetic AutoResearch for agentic code evolution](https://arxiv.org/abs/2605.13874)、[AutoScientists: Self-organizing agent teams for long-running scientific experimentation](https://arxiv.org/abs/2605.28655)、[AIDE: AI-driven exploration in the space of code](https://arxiv.org/abs/2502.13138) |
| PDFリンク | https://arxiv.org/pdf/2610.35866v1 |
