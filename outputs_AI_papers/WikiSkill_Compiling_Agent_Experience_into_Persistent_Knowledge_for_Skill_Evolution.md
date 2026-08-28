---
title: "WikiSkill: Compiling Agent Experience into Persistent Knowledge for Skill Evolution"
date: 2026-08-28
arxiv_id: 2608.27454v1
url: http://arxiv.org/abs/2608.27454v1
---

# WikiSkill: Compiling Agent Experience into Persistent Knowledge for Skill Evolution

| 項目 | 内容 |
|---|---|
| どんなもの？ | AIエージェントのスキルを進化させるためのフレームワーク「WikiSkill」を提案。エージェントの実行ログから得られた経験を構造化されたナレッジベース（Wiki）に蓄積し、それを基にスキルを反復的に改善する。 |
| 先行研究と比べてどこがすごい？ | 従来のスキル進化手法（EvoSkill, SkillOpt等）は進化の過程で得られた知見が散逸しがちであったが、WikiSkillはWiki層を設けることで経験を永続的な知識として蓄積・再利用する。これにより、スキル進化の信頼性と性能が向上し、モデルの性能を補完する効果も確認された。 |
| 技術や手法のキモはどこ？ | エージェントのワークスペースを「Raw Layer（実行トレース）」「Wiki Layer（構造化された知識）」「Skill Layer（進化する手続き）」の3層で構成した点。Wiki層が過去の成功・失敗パターン、拒否された提案、進化の過程を記録・保持し、それに基づいてSkill Proposerが次なる改善を提案するループを回す。 |
| どうやって有効だと検証した？ | 数学的推論、Web検索、表計算操作、長文QA、具体的操作（ALFWorld）の5つのベンチマークにおいて、5つの異なるLLMを用いて検証。既存手法を上回る性能を達成し、モデルの規模にかかわらずスキル進化が有効であることや、スキルがモデル間で転移可能であることを示した。 |
| 議論はある？ | 現在はスキルをプロンプトに注入する設定だが、スキル数が増加した際のスケーラビリティや検索・トリガーの課題がある。また、現在Wikiの自動剪定機能が欠如しており、検証のための厳格なゲート基準が中間的な成果を排除する可能性がある。 |
| 次に読むべき論文は？ | [EvoSkill (Alzubi et al., 2026)](https://arxiv.org/abs/2603.02766), [SkillOpt (Yang et al., 2026)](https://arxiv.org/abs/2605.23904), [Trace2Skill (Ni et al., 2026)](https://arxiv.org/abs/2603.25158) |
| PDFリンク | https://arxiv.org/pdf/2608.27454v1 |
