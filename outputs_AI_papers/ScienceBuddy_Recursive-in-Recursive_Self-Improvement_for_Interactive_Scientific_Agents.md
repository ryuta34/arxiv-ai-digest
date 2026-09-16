---
title: "ScienceBuddy: Recursive-in-Recursive Self-Improvement for Interactive Scientific Agents"
date: 2026-09-16
arxiv_id: 2609.17523v1
url: http://arxiv.org/abs/2609.17523v1
---

# ScienceBuddy: Recursive-in-Recursive Self-Improvement for Interactive Scientific Agents

| 項目 | 内容 |
|---|---|
| どんなもの？ | 科学研究のワークフローに統合され、研究者との対話を通じて継続的に改善される科学エージェント向けの対話型ワークスペース。エージェントの操作手順（ハーネス）とモデル自体の能力を相互に強化する「再帰的自己改善」パラダイムを導入している。 |
| 先行研究と比べてどこがすごい？ | 個別の会話内での修正に留まらず、研究者のフィードバックから実行可能なタスクと評価指標を自動生成し、ハーネスの進化とモデルの強化学習を循環的に組み合わせることで、長期的な能力向上を実現した点。 |
| 技術や手法のキモはどこ？ | 内側のループで補助モデルを用いてハーネス（手順）を改善し、外側のループでそのハーネスの下で強化学習（GRPO）を行いモデル自体を訓練する、入れ子状の「再帰的自己改善」プロセス。 |
| どうやって有効だと検証した？ | 4つの科学的タスクファミリー（文献読解、データベース判定、プロトコル診断、遺伝子解析）を用いたベンチマークで評価。ハーネス適応のみ、モデル学習のみ、および両方の組み合わせによる改善効果をそれぞれ検証。 |
| 議論はある？ | 個々のスキルやフィードバックが最終的な性能改善にどう寄与したかの因果関係の特定が難しいこと、また、実験は特定の専門領域（バイオメディカル）に特化していることなどが挙げられる。 |
| 次に読むべき論文は？ | [16] Shinn et al., Reflexion: Language Agents with Verbal Reinforcement Learning [URL](https://arxiv.org/abs/2303.11366) |
| PDFリンク | https://arxiv.org/pdf/2609.17523v1 |
