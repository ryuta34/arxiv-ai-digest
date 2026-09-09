---
title: "ReCite: Agentic Reasoning for Faithful Citation"
date: 2026-09-09
arxiv_id: 2609.09156v1
url: http://arxiv.org/abs/2609.09156v1
---

# ReCite: Agentic Reasoning for Faithful Citation

| 項目 | 内容 |
|---|---|
| どんなもの？ | 学術論文の引用プロセスを「検索」から「推論」へと再定義し、正確かつ論理的に裏付けられた引用を自動生成するエージェントフレームワーク「ReCite」を提案した。既存のモデルが抱える、単なる意味的類似性による引用の不整合（ミスアトリビューション）を解消する。 |
| 先行研究と比べてどこがすごい？ | 従来手法が単一の生成パイプラインに依存していたのに対し、本手法は「場所認識」「意図認識」「 reflective（省察的）検証」をデカップル（分離）したエージェント設計を採用。これにより、検索結果が不適切な場合に自己修正を行うことが可能となり、引用の忠実性を大幅に向上させた。 |
| 技術や手法のキモはどこ？ | Qwen3-4Bをベースに、CiteLocator（位置特定）、QueryPlanner（検索クエリ生成）、Master Brain（ワークフロー制御）の3モジュールを構築した点。特にGRPOを用いた強化学習により、検索失敗を分析し適切なクエリへ修正する「reflective re-retrieval loop」が核心的。 |
| どうやって有効だと検証した？ | arXivから収集した約1万件の論文に基づく大規模データセットを構築。既存のLLMやエージェントと比較し、厳格な引用正確性（Strict F1）および学術的な妥当性を評価するLenient評価の両面で、ベースラインを大きく上回る性能を実証した。 |
| 議論はある？ | 4Bという軽量モデルであるため大規模LLMと比較して推論能力に限界がある点、現在はテキストのみのユニモーダルな検証である点、CS分野に特化した訓練データであるため他分野への一般化には追加検証が必要な点が挙げられる。 |
| 次に読むべき論文は？ | [ALCE: Large Language Models for Academic Writing](https://arxiv.org/abs/2309.07056) (引用精度の評価基準となるALCEベンチマーク), [Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366) (自己修正エージェントの基礎) |
| PDFリンク | https://arxiv.org/pdf/2609.09156v1 |
