---
title: "Decoupling Exploration from Optimization in RLVR"
date: 2026-10-09
arxiv_id: 2610.10536v1
url: http://arxiv.org/abs/2610.10536v1
---

# Decoupling Exploration from Optimization in RLVR

| 項目 | 内容 |
|---|---|
| どんなもの？ | 強化学習における探索と最適化を分離する「Exploration-Distillation (ExpDis)」というフレームワーク。探索用に報酬に新規性ボーナスを加えたモデルを別途訓練し、そこから得られた高品質な推論軌跡のみを抽出して学生モデルに蒸留させることで、モデルの質を低下させずに探索能力を向上させる手法。 |
| 先行研究と比べてどこがすごい？ | 従来の強化学習(RLVR)では探索ボーナスを加えるとモデルの汎用能力が低下する「知識の劣化」が課題だったが、本手法は探索担当と最適化担当を分けることで、能力低下を防ぎつつ従来手法（DAPO等）を上回る数学的推論性能を実現した点。 |
| 技術や手法のキモはどこ？ | 新規性ボーナスを付与した探索用ポリシー(explorer)と、純粋な正解報酬のみで学習する学生ポリシー(student)を分離した設計。探索用モデルの出力を、正解性・トークン予算・反復ループの有無でフィルタリングし、厳選された推論軌跡のみを教師データとして蒸留する「拒絶サンプリング(Rejection sampling)」のプロセス。 |
| どうやって有効だと検証した？ | 7つの数学的推論ベンチマーク（AIME24, MATH500等）において、Qwen3およびMinistralモデルを用いて検証。従来手法であるDAPOに対し、同一の壁時計時間・計算予算でPass@kの大幅な改善を確認。また、一般知識のベンチマークにおいても劣化がないことを実証。 |
| 議論はある？ | 現在の実験では主に数学的推論に焦点を当てており、今後より広範なエージェントタスクや未踏の科学的課題へ適用できる可能性がある。また、新規性ボーナスの最適化手法には改善の余地があり、より攻撃的な探索メカニズムを可能にする潜在性を指摘。 |
| 次に読むべき論文は？ | [1] [DAPO: An open-source llm reinforcement learning system at scale](https://arxiv.org/abs/2610.113222) (ベースライン手法) <br> [2] [DeepSeek-R1: Incentivizing reasoning capability in llms via reinforcement learning](https://arxiv.org/abs/2501.12948) <br> [3] [Exploration by random network distillation](https://arxiv.org/abs/1810.12894) (新規性ボーナスの基礎) |
| PDFリンク | https://arxiv.org/pdf/2610.10536v1 |
