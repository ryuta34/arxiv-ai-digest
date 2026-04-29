---
title: "DV-World: Benchmarking Data Visualization Agents in Real-World Scenarios"
date: 2026-04-29
arxiv_id: 2604.25914v1
url: http://arxiv.org/abs/2604.25914v1
---

# DV-World: Benchmarking Data Visualization Agents in Real-World Scenarios

| 項目 | 内容 |
|---|---|
| どんなもの？ | 現実世界のデータ可視化（DV）タスクにおいて、AIエージェントの能力を評価するための総合的なベンチマーク「DV-World」を提案している。スプレッドシートの操作、クロスモーダルなロジックの進化、および曖昧な要求に対するプロアクティブな対話インタラクションという、実務上の3つの主要な課題をカバーしている。 |
| 先行研究と比べてどこがすごい？ | 従来のベンチマークがコード生成のみに限定されていたのに対し、ネイティブなスプレッドシート環境の接地、マルチターンの曖昧な意図への対応、および現実的なエラー修復と進化といった、実際の業務フローにおける複雑性を網羅的に評価できる点。 |
| 技術や手法のキモはどこ？ | スプレッドシートのネイティブオブジェクトを操作する「DV-Sheet」、多様なプログラミング言語間でのロジックの継承を問う「DV-Evolution」、そしてユーザーシミュレータを用いて曖昧な要求への対処能力を測定する「DV-Interact」という3ドメインの統合的な評価フレームワーク。 |
| どうやって有効だと検証した？ | 260のタスクを作成し、Qwen3、Gemini、GPTシリーズなどの最先端LLMを評価。その結果、既存モデルが50%未満の性能しか達成できていないことを示し、モデルの性能が複雑な実務環境で限界に達していることを定量的に明らかにした。 |
| 議論はある？ | 多くのモデルが、データと可視化の整合性を保つ数値的推論や、プロの可視化基準を満たすレイアウト構築において「論理的な脆さ」を示していること。また、対話型プロセスにおいてユーザーの意図を汲み取れず、「対話の回避（Interactive Avoidance）」が発生する限界を指摘。 |
| 次に読むべき論文は？ | [SpreadsheetBench (Ma et al., 2024)](https://arxiv.org/abs/2403.11128), [ChartMimic (Yang et al., 2024a)](https://arxiv.org/abs/2406.09961), [SheetCopilot (Li et al., 2023)](https://arxiv.org/abs/2310.14495) |
| PDFリンク | [https://arxiv.org/pdf/2604.25914v1](https://arxiv.org/pdf/2604.25914v1) |
