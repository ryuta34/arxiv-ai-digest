---
title: "Early Stopping for Large Reasoning Models via Confidence Dynamics"
date: 2026-04-07
arxiv_id: 2604.04930v1
url: http://arxiv.org/abs/2604.04930v1
---

# Early Stopping for Large Reasoning Models via Confidence Dynamics

| 項目 | 内容 |
|---|---|
| どんなもの？ | 大規模推論モデルにおいて、推論過程の信頼度（Confidence）の動的な変化を監視することで、推論を早期終了させる手法「CoDE-Stop」を提案した論文。学習不要かつ推論時に適用可能な手法で、計算コストを大幅に削減しつつ精度を維持する。 |
| 先行研究と比べてどこがすごい？ | 既存の早期終了手法が単一ステップの信頼度のみを見るのに対し、本手法は推論過程全体の「不安定さ」を累積的に捉える。これにより、信頼度が高い場合だけでなく、推論が停滞・迷走している不安定なケースも効果的に検出し、精度低下を抑えつつ25〜50%のトークン削減を実現した点。 |
| 技術や手法のキモはどこ？ | 推論ステップごとの信頼度と、その変化率から算出した「変性スコア（Degeneration score）」の組み合わせ。特に、初期の推論ステップをより重視する対数的な重み付けを行うことで、 unproductive（生産性の低い）な推論軌道を早期に見極める設計。 |
| どうやって有効だと検証した？ | Qwen3（4B/14B）、DeepSeek-R1-Distill-Llama-8B、Llama-3.1-Nemotron-8Bといったモデルを用い、AIME、MATH500、GSM8K、GPQA-Diamond等の多様なベンチマークで評価。既存の早期終了手法（DEER、EAT等）と比較し、精度と計算コストのトレードオフにおいてパレート最適であることを示した。 |
| 議論はある？ | 推論ステップの区切り文字（"Wait"等）の選択に対する頑健性を検証したが、本質的にはモデルの出力から得られるヒューリスティックな信号に基づいている。より深い内部表現を直接活用することが、今後の重要な発展の方向性であると示唆されている。 |
| 次に読むべき論文は？ | [Yang et al. (2025) - Dynamic early exit in reasoning models](https://arxiv.org/abs/2504.15895), [Liu & Wang (2025) - Answer convergence as a signal for early stopping](https://arxiv.org/abs/2506.02536), [Wei et al. (2026) - The evolution of thought](https://arxiv.org/abs/2508.17627) |
| PDFリンク | https://arxiv.org/pdf/2604.04930v1 |
