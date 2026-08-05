---
title: "PAST-Bench: Benchmarking the Foundations of Recursive Self-Improvement in Personal Agents"
date: 2026-08-05
arxiv_id: 2608.04003v1
url: http://arxiv.org/abs/2608.04003v1
---

# PAST-Bench: Benchmarking the Foundations of Recursive Self-Improvement in Personal Agents

| 項目 | 内容 |
|---|---|
| どんなもの？ | パーソナルAIエージェントが過去の経験を保持し、再利用して自己改善する能力（オンライン自己進化）を評価するためのベンチマーク「PAST-Bench」を提案した。エージェントのパフォーマンス向上を、モデルやランタイムの寄与から分離して正しく帰属させることを目的とする。 |
| 先行研究と比べてどこがすごい？ | 従来手法が単発タスクのスコアに依存していたのに対し、タスクファミリー内の「順序付きエピソード」を用いる。また、経験の保持・未保持を切り替えるマッチドコントロール（対照実験）とトレースレベルの診断を組み合わせ、改善が意図したpersistence（持続性）メカニズムによるものかを証明できる点。 |
| 技術や手法のキモはどこ？ | タスクファミリー内での「記憶」「手続きの再利用」「情報収集」「更新」という4つの能力軸と、それらを評価するための「persistence-on/off」の対照設定。さらに、エージェントの処理ループに介入する5つの診断・改善メカニズム（Plan, Render, Route, Gate, Close）を実装した「Hermes+」フレームワーク。 |
| どうやって有効だと検証した？ | 7つのモデルと4つのフレームワークを用いて、オンライン自己進化のパフォーマンスギャップ（Δ）と、意図した経路での改善かを示す「メカニズム・エビデンススコア」の両面から評価。さらに、Hermes+の各メカニズムを個別に無効化するアブレーションスタディを実施。 |
| 議論はある？ | 持続的な改善効果はモデルや能力に依存し、汎用的なものではない。また、経験の保持は必ずしも改善に直結せず、かえって古い情報がノイズとなる場合もある。将来は、より長期間や複雑なドメイン間での転移、メカニズムの因果関係をより強固に証明する手法が課題。 |
| 次に読むべき論文は？ | [AgentBench (Liu et al., 2024)](https://arxiv.org/abs/2402.04003)、[SkillsBench (Li et al., 2026a)](https://arxiv.org/abs/2602.12670)、[AgentArch (Bogavelli et al., 2025)](https://arxiv.org/abs/2509.10769) |
| PDFリンク | https://arxiv.org/pdf/2608.04003v1 |
