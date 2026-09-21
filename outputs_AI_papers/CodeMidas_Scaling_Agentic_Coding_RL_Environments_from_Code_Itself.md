---
title: "CodeMidas: Scaling Agentic Coding RL Environments from Code Itself"
date: 2026-09-21
arxiv_id: 2609.22068v1
url: http://arxiv.org/abs/2609.22068v1
---

# CodeMidas: Scaling Agentic Coding RL Environments from Code Itself

| 項目 | 内容 |
|---|---|
| どんなもの？ | ソースコードそのものから自動的にタスクを作成し、強化学習（RL）環境を構築するパイプライン「CodeMidas」を提案した論文。既存の開発成果物（Issueやコミット等）に依存せず、多様なコードベースから高品質なトレーニングデータと検証用環境をスケーラブルに生成する。 |
| 先行研究と比べてどこがすごい？ | 従来のパイプラインがIssueやコミットなどの開発履歴に依存していたのに対し、ソースコードのみを入力としてタスクを構築できるため、格段に高い拡張性を持つ。フィルタリングプロセスにより、データ量だけでなくデータの質も担保し、既存手法を上回るベンチマーク性能を達成した点。 |
| 技術や手法のキモはどこ？ | コードベースから機能単位を特定し、実行可能なテストを構築するだけでなく、post-rollout filtering（事後ロールアウトフィルタリング）を導入した点。具体的には、リーク検知、検証器の妥当性評価、ロールアウトの成否を用いた選別を行い、低品質なタスクを排除してRL環境の信頼性を高めている。 |
| どうやって有効だと検証した？ | 生成された5,545のタスクを用いて「MiMo-V2.5」をGRPOで学習させ、5つの外部ベンチマーク（SWE-bench Pro, DeepSWE, ProgramBench等）で評価した。その結果、全ベンチマークで改善が見られ、特にProgramBenchで17%の大幅なスコア向上を達成した。 |
| 議論はある？ | タスク生成における自動化パイプラインのフィルタリング精度がモデルの初期能力に依存している可能性。また、極めて複雑なリポジトリ構造や特殊な依存関係を持つプロジェクトに対するタスク化の限界については明示的な議論が少ない。 |
| 次に読むべき論文は？ | [SWE-bench Pro](https://openreview.net/forum?id=uEVTdoAbnK)、[DeepSeekMath](https://arxiv.org/abs/2402.03300)、[R2E](https://proceedings.mlr.press/v235/jain24c.html) |
| PDFリンク | https://arxiv.org/pdf/2609.22068v1 |
