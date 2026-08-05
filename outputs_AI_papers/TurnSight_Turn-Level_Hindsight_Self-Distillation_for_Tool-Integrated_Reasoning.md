---
title: "TurnSight: Turn-Level Hindsight Self-Distillation for Tool-Integrated Reasoning"
date: 2026-08-05
arxiv_id: 2608.04007v1
url: http://arxiv.org/abs/2608.04007v1
---

# TurnSight: Turn-Level Hindsight Self-Distillation for Tool-Integrated Reasoning

| 項目 | 内容 |
|---|---|
| どんなもの？ | ツール利用を伴う推論（TIR）において、実行結果に基づく「振り返り（Hindsight）」情報を活用し、ターン単位で精緻な報酬割り当てを行う自己蒸留フレームワーク「TurnSight」を提案した。強化学習の報酬伝播における課題を解決し、長距離のツール利用タスクでの性能を向上させる。 |
| 先行研究と比べてどこがすごい？ | 従来の強化学習が単一の報酬を全ターンに割り当てていたのに対し、実行状況に応じた振り返り信号を生成することで、より局所的かつタスクに即した精緻なクレジット割り当てが可能になった。外部の正解データに依存せず、実行中（on-policy）のフィードバックのみで最適化できる点が優位。 |
| 技術や手法のキモはどこ？ | 実行結果に基づく振り返り情報を複数の先行予測期間（Lookahead horizons）で構築し、それらの合意に基づき信頼性の高い信号を抽出する「方向性一貫性のある教師選択」と、グループ間で正規化した重みを用いてRLの優位性（Advantage）を動的に補正する仕組み。 |
| どうやって有効だと検証した？ | FTRL（ドメイン内）、BFCL、ToolHop（ドメイン外）という3つのベンチマークを用い、Qwen3-4Bおよび8Bモデルで評価。既存のRL手法（GRPO等）や自己蒸留手法（SDPO, RLSD等）を上回る結果を示し、特に長文脈やパラメータ欠損といった難易度の高いタスクで顕著な改善を達成した。 |
| 議論はある？ | 混合係数λや変調境界εwの設定が重要であり、過度な局所的介入は全体的なタスク解決能力を阻害する可能性がある。また、教師モデルの予測が不完全な場合のノイズへの耐性確保が今後の課題となる。 |
| 次に読むべき論文は？ | [MatchTIR](https://arxiv.org/abs/2602.04033)、[GRPO (DeepSeekMath)](https://arxiv.org/abs/2402.03300)、[ToolRL](https://arxiv.org/abs/2504.11536) |
| PDFリンク | https://arxiv.org/pdf/2608.04007v1 |
