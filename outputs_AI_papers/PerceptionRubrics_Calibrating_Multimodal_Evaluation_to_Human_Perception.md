---
title: "PerceptionRubrics: Calibrating Multimodal Evaluation to Human Perception"
date: 2026-06-29
arxiv_id: 2606.28322v1
url: http://arxiv.org/abs/2606.28322v1
---

# PerceptionRubrics: Calibrating Multimodal Evaluation to Human Perception

| 項目 | 内容 |
|---|---|
| どんなもの？ | マルチモーダル大規模言語モデル（MLLM）の視覚的認識能力を評価するための、ルブリック（評価基準）に基づく新しいベンチマークフレームワーク「PERCEPTIONRUBRICS」。既存のベンチマークが抱えるリーダーボードの飽和やモデルの脆弱性といった課題を解決し、人間が感じる知覚の厳密さに合わせた評価を実現する。 |
| 先行研究と比べてどこがすごい？ | 従来の単一スコアによる評価とは異なり、必須項目（Must-Right）と細かな詳細（Easy-Wrong）という二層のルブリックを導入した点。また、必須条件に失敗するとスコアがゼロになる「ゲート付きスコアリング（Gated Scoring）」により、局所的な幻覚を許容せず、人間の知覚の非線形な厳しさを反映できる点。 |
| 技術や手法のキモはどこ？ | 1,038枚の超高密度情報画像に対し、複数のトップモデルによる「Circular Peer-Review」で検証済みのゴールデンキャプションを生成し、そこから12,000以上の原子的な評価ルブリックを自動生成したこと。さらに、これらを用いてモデルの「認識の正確性」だけでなく「空間的・論理的な一貫性」を厳格に評価する仕組み。 |
| どうやって有効だと検証した？ | 25種類の主要なプロプライエタリおよびオープンソースモデルを評価。既存ベンチマーク（DOCCI, DetailCaps）と比較して、Vision Arenaの人間による順位付けと高い相関（Pearson 0.916）があることを実証し、モデルの推論能力と認識能力の間に「Reliability Gap（信頼性のギャップ）」が存在することを明らかにした。 |
| 議論はある？ | 現在のトップモデルであっても、高密度なGUI画面等の認識において依然として明確な性能限界や脆弱性があることを指摘。また、ベンチマークの評価がルブリックの質と量に依存するため、人間による検証の介入と自動生成のバランスが重要であり、今後さらなる洗練が求められる。 |
| 次に読むべき論文は？ | 1. [DOCCI: Descriptions of connected and contrasting images](https://arxiv.org/abs/2405.19092)<br>2. [DetailCaps: Benchmarking and improving detail image caption](https://arxiv.org/abs/2405.19092)<br>3. [MM-Vet: Evaluating large multimodal models for integrated capabilities](https://arxiv.org/abs/2308.02490) |
| PDFリンク | https://arxiv.org/pdf/2606.28322v1 |
