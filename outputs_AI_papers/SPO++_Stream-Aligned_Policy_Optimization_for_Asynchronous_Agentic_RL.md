---
title: "SPO++: Stream-Aligned Policy Optimization for Asynchronous Agentic RL"
date: 2026-08-27
arxiv_id: 2608.24870v1
url: http://arxiv.org/abs/2608.24870v1
---

# SPO++: Stream-Aligned Policy Optimization for Asynchronous Agentic RL

| 項目 | 内容 |
|---|---|
| どんなもの？ | 非同期エージェント強化学習における「SPO (Single-stream Policy Optimization)」の効率と安定性を改善する手法「SPO++」を提案した論文。プロンプト単位の価値推定と学習プロセスを最適化することで、ツール使用など長時間のタスクにおけるオンライン学習効率を向上させる。 |
| 先行研究と比べてどこがすごい？ | 従来手法のSPOで見られた「学習順序（受信順）への依存性」と「報酬の標準化と損失計算の尺度不一致」という2つの問題を解決した点。これにより、異なるモデル規模やタスク設定においても一貫して学習効率を改善し、特にアクショントークンに基づく正規化が性能向上に大きく寄与することを示した。 |
| 技術や手法のキモはどこ？ | 1. 学習の進捗を個別の「ポリシーイベント」で管理し、システムのタイミング（受信順）に依存しない「イベント時間プロンプトメモリ」の導入。2. 報酬の標準化を、 actor loss（トークン平均）と同じ「アクショントークン尺度」に合わせることで、軌道長による中心化のズレを解消したこと。 |
| どうやって有効だと検証した？ | ALFWorld（Qwen3.5 0.8B/2Bモデル）およびMath-TIR環境において、SPOとSPO++の性能を比較評価。学習曲線下の面積（AUC）および最終的な報酬の改善幅を確認し、アブレーションスタディによって正規化手法の重要性を実証した。 |
| 議論はある？ | 実験が比較的小規模なモデルと限定的な予算で行われている点や、今回の改善が複数の要素（トラッキング、正規化、Dual-Clip等）を組み合わせたものであるため、個別の寄与度を完全に分離しきれていない点を課題として挙げている。 |
| 次に読むべき論文は？ | [17] Xu and Ding, "Single-stream policy optimization" (SPOの原論文), [19] Yu et al., "DAPO: An open-source LLM reinforcement learning system at scale" |
| PDFリンク | https://arxiv.org/pdf/2608.24870v1 |
