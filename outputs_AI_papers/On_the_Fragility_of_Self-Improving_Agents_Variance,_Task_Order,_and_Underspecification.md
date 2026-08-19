---
title: "On the Fragility of Self-Improving Agents: Variance, Task Order, and Underspecification"
date: 2026-08-19
arxiv_id: 2608.18066v1
url: http://arxiv.org/abs/2608.18066v1
---

# On the Fragility of Self-Improving Agents: Variance, Task Order, and Underspecification

| 項目 | 内容 |
|---|---|
| どんなもの？ | メモリベースの自己改善型AIエージェントの信頼性を評価した研究。Webブラウジングタスクにおいて、現状の評価手法が抱える「ランダム性への脆弱性」や「タスク順序への依存」を明らかにし、改善策を提案している。 |
| 先行研究と比べてどこがすごい？ | 従来は単一実行のみで行われていた評価を、複数回実行による分散の定量化と、タスク順序をランダム化した設定に拡張した点。自己改善型エージェントの隠れた脆弱性を初めて包括的に解明した。 |
| 技術や手法のキモはどこ？ | エージェントのメモリ生成過程における「環境とタスクの特定不足（Underspecification）」が脆弱性の主因であると特定し、評価指標や環境フィードバック、制約プロンプトをメモリ構築に統合することで性能低下を緩和する手法。 |
| どうやって有効だと検証した？ | WebArena、VisualWebArena、SCUBAの3つのベンチマークを用い、複数回実行の統計的有意差と、デフォルト順序・シャッフル順序でのパフォーマンス変化を比較検証した。 |
| 議論はある？ | 追加情報によって性能低下は一部緩和されたが、依然として課題は残存している。また、予見不可能な失敗を防ぐための人間による監視・介入インターフェースの重要性が示唆されている。 |
| 次に読むべき論文は？ | [10] Towards a science of ai agent reliability, [11] Agent workflow memory, [12] Reasoningbank: Scaling agent self-evolving with reasoning memory |
| PDFリンク | https://arxiv.org/pdf/2608.18066v1 |
