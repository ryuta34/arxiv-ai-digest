---
title: "From Noisy Traces to Root Causes: Structural Trajectory Analysis and Causal Extraction for Agent Optimization"
date: 2026-07-09
arxiv_id: 2607.07702v1
url: http://arxiv.org/abs/2607.07702v1
---

# From Noisy Traces to Root Causes: Structural Trajectory Analysis and Causal Extraction for Agent Optimization

| 項目 | 内容 |
|---|---|
| どんなもの？ | 長期的なタスクを実行するAIエージェントの最適化フレームワーク「STRACE」。実行ログを単なるテキストではなく因果関係のグラフとして捉えることで、エラーの根本原因を特定し、効率的かつ効果的なプロンプト最適化を実現する。 |
| 先行研究と比べてどこがすごい？ | 従来手法（全文のプロンプト利用や単純な要約・切り捨て）では、ノイズが多すぎて偽の相関を学習したり、因果的に重要な過去の情報を捨ててしまったりするという「コンテキストとノイズのトレードオフ」を解決した点。 |
| 技術や手法のキモはどこ？ | エージェントの構造から実行依存関係グラフを構築し、失敗パターンを分析して代表的なトレースを選別後、因果グラフ上で遡及的にスライスを行うことで、ノイズを除去した「最小因果コンテキスト」を抽出する点。 |
| どうやって有効だと検証した？ | HotpotQA、WebArena、VeruSAGE-Benchの3つのベンチマークで評価。特に複雑なformal verificationタスクにおいて、ベースライン比で16.0%の成功率向上（42.5%→58.5%）を達成した。 |
| 議論はある？ | システムの実装や harness（枠組み）に対する十分な可視性を前提としているため、完全にブラックボックスなエージェントへの適用は将来課題。また、実運用時のトレースに含まれる機密情報の取り扱いに注意が必要。 |
| 次に読むべき論文は？ | [GEPA: Reflective prompt evolution can outperform reinforcement learning](https://arxiv.org/abs/2507.19457)、[AgentRx: Diagnosing AI agent failures from execution trajectories](https://arxiv.org/abs/2602.02475) |
| PDFリンク | https://arxiv.org/pdf/2607.07702v1 |
