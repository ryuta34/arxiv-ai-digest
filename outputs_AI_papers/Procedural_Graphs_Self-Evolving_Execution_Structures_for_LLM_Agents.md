---
title: "Procedural Graphs: Self-Evolving Execution Structures for LLM Agents"
date: 2026-09-09
arxiv_id: 2609.09153v1
url: http://arxiv.org/abs/2609.09153v1
---

# Procedural Graphs: Self-Evolving Execution Structures for LLM Agents

| 項目 | 内容 |
|---|---|
| どんなもの？ | 大規模言語モデル（LLM）エージェントの行動を制御・最適化するための、自己進化型の実行構造「Procedural Graph (PG)」を提案した研究。知識グラフの考え方を応用し、手続き的な知識をグラフ構造として外部化することで、エージェントの推論の柔軟性を保ちつつ、長期的な目標達成能力やタスク遂行能力を向上させる。 |
| 先行研究と比べてどこがすごい？ | 従来の手法（記憶ベースやプロンプトによるガイド）がモデル内部の知識に依存していたのに対し、PGは手続き的知識を明示的かつ編集可能な外部グラフとして保持する点。これにより、再学習なしでグラフ構造や属性を動的に改善し、手動設計されたワークフローを上回るパフォーマンスを自律的に獲得できる。 |
| 技術や手法のキモはどこ？ | （手続き、関係、手続き）の三つ組（triplet）で構成されるグラフ構造と、(1)エージェントの現在の状況に合わせて周辺のサブグラフを抽出し、状況に応じたガイダンスを生成するオンライン推論、(2)失敗した軌跡と成功した軌跡を比較し、LLM refinerによってグラフのトポロジーや属性を編集・更新するオフライン自己進化ループの組み合わせ。 |
| どうやって有効だと検証した？ | 7つのベンチマーク（HotpotQA、MultiChallenge、GDPval、ALFWorld、τ-bench、BFCL v3、EnterpriseArena）を用い、4つの異なるLLM（Claude Sonnet 4.6, Gemini 3.1 Pro/3.5 Flash, Grok 4.1 Fast）で検証。memory-basedなベースラインと比較し、PGが全体として一貫した性能向上を達成したこと、特に長期的な計画が必要なタスクで高い耐性と効率性を示したことを実証した。 |
| 議論はある？ | ガイダンスの生成はトークン消費量を増加させるため、今後はステップ間でのガイダンスの再利用や選択的な生成が必要。また、異なる推論エンジンやツール環境間での学習済み手順の汎用性や移転性については、今後の課題として残されている。 |
| 次に読むべき論文は？ | [Sumers et al. (2023) "Cognitive architectures for language agents"](https://arxiv.org/abs/2309.02427)、[Fu et al. (2024) "AutoGuide: Automated generation and selection of context-aware guidelines for large language model agents"](https://arxiv.org/abs/2402.13264)、[Zhang et al. (2025) "AFlow: Automating agentic workflow generation"](https://arxiv.org/abs/2404.13032) |
| PDFリンク | https://arxiv.org/pdf/2609.09153v1 |
