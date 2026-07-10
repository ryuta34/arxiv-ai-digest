---
title: "UniClawBench: A Universal Benchmark for Proactive Agents on Real-World Tasks"
date: 2026-07-10
arxiv_id: 2607.08768v1
url: http://arxiv.org/abs/2607.08768v1
---

# UniClawBench: A Universal Benchmark for Proactive Agents on Real-World Tasks

| 項目 | 内容 |
|---|---|
| どんなもの？ | 実世界の複雑なタスクにおける自律的なAIエージェントの能力を、Capability（能力）に基づき体系的に評価するためのベンチマーク「UniClawBench」です。5つの主要能力を網羅した400のバイリンガル・リアルワールドタスクを通じて、エージェントの実践的な遂行能力を測定します。 |
| 先行研究と比べてどこがすごい？ | 従来のサンドボックス環境や単一ターンの評価とは異なり、Dockerコンテナを用いたライブ環境での実行と、独自の「3者閉ループ評価」を採用している点です。これにより、マルチターン対話を通じたエラーからの回復能力や、特定の能力不足を詳細に特定できる能力駆動型の分類を実現しています。 |
| 技術や手法のキモはどこ？ | エグゼキューター（エージェント）、非公開のスーパーバイザー（評価者）、ユーザーシミュレーター（フィードバック生成）の3者による閉ループ構造です。「情報ファイアウォール」を設けることで、スーパーバイザーが詳細な評価基準を持ちつつ、ユーザーシミュレーターには判定結果のみを伝達し、解答や評価基準の漏洩を防ぎながら、自然なマルチターンフィードバックを実現しています。 |
| どうやって有効だと検証した？ | 10の最先端モデルを評価し、モデル単体の能力とフレームワーク（OpenClaw, EDICT, Nanobot）の設計がパフォーマンスに与える影響を比較分析しました。また、評価の信頼性を示すため、人間の専門家による評価と自動評価の一致率（92%）を確認しています。 |
| 議論はある？ | 現在の課題として、長期的な記憶保持やクロスプラットフォーム間での一貫した状態管理の難しさが挙げられています。また、手動作成された400タスクという規模の制約や、LLMベースの評価におけるバイアスの可能性も将来的な改善点として指摘されています。 |
| 次に読むべき論文は？ | [39] OpenClaw [35] Nanobot: The ultra-lightweight personal ai agent [45] OSWorld: Benchmarking multimodal agents for open-ended tasks in real computer environments |
| PDFリンク | https://arxiv.org/pdf/2607.08768v1 |
