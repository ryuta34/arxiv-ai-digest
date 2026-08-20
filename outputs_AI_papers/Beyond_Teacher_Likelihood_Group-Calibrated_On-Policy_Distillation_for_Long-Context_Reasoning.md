---
title: "Beyond Teacher Likelihood: Group-Calibrated On-Policy Distillation for Long-Context Reasoning"
date: 2026-08-20
arxiv_id: 2608.19181v1
url: http://arxiv.org/abs/2608.19181v1
---

# Beyond Teacher Likelihood: Group-Calibrated On-Policy Distillation for Long-Context Reasoning

| 項目 | 内容 |
|---|---|
| どんなもの？ | 長文コンテキストにおける推論タスクにおいて、教師モデルの指示と検証器（Verifier）による評価の不一致（Teacher-Verifier Disagreement）を解消し、モデル性能を向上させる手法「GC-OPD」を提案する論文。教師モデルのログ確率に基づく従来のOn-Policy Distillation（OPD）に、検証器からの報酬をグループ単位で調整して組み込むことで、推論精度の改善を図る。 |
| 先行研究と比べてどこがすごい？ | 従来のOPD手法が教師モデルの選好のみに依存していたのに対し、検証器のフィードバックをそのまま加算するのではなく、グループ単位での相対的な不一致を正規化して「残差」として活用する点。これにより、モデル全体の強みを維持しつつ、タスクの正誤判定に基づいた微細な軌道修正が可能となった。 |
| 技術や手法のキモはどこ？ | 検証器報酬と軌道レベルのOPDスコアをグループ内で個別に標準化（Zスコア正規化）し、その差分を「署名付きの不一致残差」として算出する点。さらに、Relative-advantage-based credit assignment (RACA) を用い、各トークンの相対的な重要度に応じてこの残差を分配する仕組み。 |
| どうやって有効だと検証した？ | GoLongRLから抽出した9,527件のプロンプトを用いた学習環境を構築し、5つの長文ベンチマーク（DocMath, Frames, MRCR, CorpusQA, LBv1QA）で検証。Qwen3-4Bおよび8Bモデルにおいて、既存のOPD手法を上回る平均スコアを達成し、特に構造的推論や証拠集約タスクで顕著な改善を確認した。 |
| 議論はある？ | 長文コンテキストにおいて入力長が伸びるほど教師と検証器の乖離が拡大することを確認したが、この傾向はタスクに依存する。また、フレームワークの改善は全体としては有効だが、特定のベンチマーク（Frames等）ではモデルによる差異があることや、評価指標の選定に依存する可能性があること。 |
| 次に読むべき論文は？ | [1] On-policy distillation of language models: Learning from self-generated mistakes (Agarwal et al., 2024) <br> [5] LongRLVR: Long-context reinforcement learning requires verifiable context rewards (Chen et al., 2026) <br> [36] SCOPE: Signal-calibrated on-policy distillation enhancement with dual-path adaptive weighting (Zheng et al., 2026) |
| PDFリンク | https://arxiv.org/pdf/2608.19181v1 |
