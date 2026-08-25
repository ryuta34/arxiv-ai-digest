---
title: "How to Train a Critic Stably and Efficiently"
date: 2026-08-25
arxiv_id: 2608.23566v1
url: http://arxiv.org/abs/2608.23566v1
---

# How to Train a Critic Stably and Efficiently

| 項目 | 内容 |
|---|---|
| どんなもの？ | 大規模言語モデル（LLM）の強化学習において、不安定になりがちな「クリティック（価値関数）」の学習を安定化・効率化する手法「BPCO (Best-Practice Critic Optimization)」を提案した論文。単一の応答サンプルで高い学習性能を実現し、グループベースの手法（GRPO等）に代わる信頼性の高い代替手段を提供します。 |
| 先行研究と比べてどこがすごい？ | 従来は critic の学習不安定さを避けるために複数回答をサンプリングする「グループベース手法」が主流でしたが、本作は critic 自身を正しく訓練することで単一応答での効率的な強化学習を可能にしました。特に、報酬範囲への値の制限や、学習時のみ参照可能な補助情報を与えることで、性能と安定性を両立させています。 |
| 技術や手法のキモはどこ？ | ①DPPOの採用、②報酬範囲内への価値予測の制限（スケーリングした逆正接関数の使用）、③バイアスのないモンテカルロターゲットへの回帰、④バッチ正規化の廃止、⑤長さ適応型GAEの導入、⑥訓練時のみ参照可能な補助情報（正解や rubric 等）の critic への入力を組み合わせた点。 |
| どうやって有効だと検証した？ | 1,460問の数学データセットを用いたサンリティチェック、40.3K問のDeepScaleRデータセット、30Bパラメーター超のMoEモデル、およびrubric（評価指標）を用いた報酬設定などで評価。多くのベースラインに対して安定した報酬向上と、AIME 2025ベンチマークにおける高い推論精度を示しました。 |
| 議論はある？ | 数学・rubricタスクに検証が限定されている点。また、報酬範囲を事前に知る必要があることや、criticの訓練により計算コストとメモリ消費が増加する点が課題として挙げられています。さらに、補助情報の導入は過学習を招く可能性も示唆されています。 |
| 次に読むべき論文は？ | [Deepseek-r1: Incentivizing reasoning capability in llms via reinforcement learning](https://arxiv.org/abs/2501.12948)、[Rethinking the trust region in llm reinforcement learning](https://arxiv.org/abs/2602.04879)、[Vapo: Efficient and reliable reinforcement learning for advanced reasoning tasks](https://arxiv.org/abs/2504.05118) |
| PDFリンク | https://arxiv.org/pdf/2608.23566v1 |
