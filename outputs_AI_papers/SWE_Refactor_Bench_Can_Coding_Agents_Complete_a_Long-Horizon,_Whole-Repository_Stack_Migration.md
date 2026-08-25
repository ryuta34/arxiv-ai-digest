---
title: "SWE Refactor Bench: Can Coding Agents Complete a Long-Horizon, Whole-Repository Stack Migration?"
date: 2026-08-25
arxiv_id: 2608.23564v1
url: http://arxiv.org/abs/2608.23564v1
---

# SWE Refactor Bench: Can Coding Agents Complete a Long-Horizon, Whole-Repository Stack Migration?

| 項目 | 内容 |
|---|---|
| どんなもの？ | ソフトウェアの全リポジトリを対象とした、長期的なスタック移行（言語やフレームワーク等の刷新）を自律的に遂行するAIエージェントの能力を評価するための新たなベンチマーク「SWE Refactor Bench」を提案している。 |
| 先行研究と比べてどこがすごい？ | 従来のベンチマークが抱えていた「移行をせず元のコードをコピーしてテストをパスする（Blindness）」というハックを許さない、3段階の厳格な評価プロトコル（移行監査、固定テスト、AIによる検証）を導入した点。 |
| 技術や手法のキモはどこ？ | 移行が物理的に行われたかを判定するハードゲート（Migration Audit）と、固定テストでは見抜けない挙動の差異を独立した6つのエージェントが微分テスト（Agentic Verification）で検出する仕組み。 |
| どうやって有効だと検証した？ | 8つの frontier モデル（claude-opus-5, gpt-5.6-sol 等）を用いて、20種類の実際のオープンソース移行タスク（計520回）を実行し、その成功率やエラーの傾向を分析した。 |
| 議論はある？ | 移行の完了と挙動の維持は全く異なる能力であり、現時点のエージェントは両立に苦戦している。特に「移行の完成」と「振る舞いの完全再現」を同時に達成することは極めて困難であるという限界が示された。 |
| 次に読むべき論文は？ | [SWE-bench](https://arxiv.org/abs/2310.06770), [MigrationBench](https://arxiv.org/abs/2505.09569), [SWE-agent](https://arxiv.org/abs/2405.15793) |
| PDFリンク | https://arxiv.org/pdf/2608.23564v1 |
