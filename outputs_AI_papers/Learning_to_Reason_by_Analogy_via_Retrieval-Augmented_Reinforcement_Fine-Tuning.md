---
title: "Learning to Reason by Analogy via Retrieval-Augmented Reinforcement Fine-Tuning"
date: 2026-06-12
arxiv_id: 2606.13680v1
url: http://arxiv.org/abs/2606.13680v1
---

# Learning to Reason by Analogy via Retrieval-Augmented Reinforcement Fine-Tuning

| 項目 | 内容 |
|---|---|
| どんなもの？ | 複雑な数学的推論タスクにおいて、表面的な類似性ではなく「推論の構造的な類似性」に基づいた外部知識を検索・利用することで、モデルの回答精度を向上させる学習フレームワーク「RA-RFT」の提案。推論過程を模倣（アナロジー学習）させることで、言語モデルの推論能力を強化する。 |
| 先行研究と比べてどこがすごい？ | 従来のRAGが lexical/semantic（語彙的・意味的）な類似性に基づくのに対し、本手法は推論の有用性に特化した「推論認識型検索（reasoning-aware retrieval）」を用いる点。また、推論の過程自体を強化学習の文脈に組み込むことで、モデルが外部情報を自律的に活用する能力を直接強化できる。 |
| 技術や手法のキモはどこ？ | 強力なLLMをジャッジとして用い、検索対象とクエリが同一の推論戦略を持つかを判定する「gold-relevance distillation（金準拠の関連性蒸留）」を行い、そのラベルで retriever を対照学習（contrastive learning）させる点。その上で、推論過程を含めたプロンプトを用いて強化学習（RLVR）を行うことで、推論の足場（scaffolding）として活用させる。 |
| どうやって有効だと検証した？ | AIME 2024/2025、HMMT 2025、BrUMO 2025といった難関数学ベンチマークで検証。Qwen3-1.7Bおよび4Bモデルにおいて、ベースラインのGRPOと比較して大幅な精度向上を確認し、特に難問において効果的であることを示した。 |
| 議論はある？ | Retrieverの学習や金準拠ラベルの作成に、GPT-4o等の強力なモデルを用いた事前準備（アノテーション）コストがかかる点。一方で、一度作成すればモデルの規模やトレーニング構成を変えても再利用可能であるというトレードオフを認めている。 |
| 次に読むべき論文は？ | [DeepSeekMath (Shao et al., 2024)](https://arxiv.org/abs/2402.03300)、[QUESTA (Li et al., 2026)](https://openreview.net/forum?id=3MifB0f7qR)、[BRIGHT (Su et al., 2025)](https://openreview.net/forum?id=ykuc5q381b) |
| PDFリンク | https://arxiv.org/pdf/2606.13680v1 |
