---
title: "SpatialEvo: Self-Evolving Spatial Intelligence via Deterministic Geometric Environments"
date: 2026-04-16
arxiv_id: 2604.14144v1
url: http://arxiv.org/abs/2604.14144v1
---

# SpatialEvo: Self-Evolving Spatial Intelligence via Deterministic Geometric Environments

| 項目 | 内容 |
|---|---|
| どんなもの？ | 3D空間推論能力を向上させるための、自己進化型フレームワーク「SpatialEvo」です。モデル同士の合意に頼る従来の自己進化手法とは異なり、決定論的な幾何学的環境（DGE）から得られる物理的フィードバックを直接用いることで、ノイズのない継続的な学習を実現します。 |
| 先行研究と比べてどこがすごい？ | 従来の自己進化手法はモデル間の合意（pseudo-labels）に依存するため、モデルの誤りを強化するリスクがありました。SpatialEvoは、物理世界から算出される「真の正解」を教師信号とすることで、モデルの幾何学的な誤りを確実に修正・強化できる点に優位性があります。 |
| 技術や手法のキモはどこ？ | Deterministic Geometric Environment (DGE)の導入です。点群とカメラポーズから16種類の空間タスクの正解をプログラム的に計算し、これを報酬として活用します。また、単一のモデルが「質問者」と「解答者」を兼務し、タスク適応型スケジューラーによって苦手なタスクを重点的に学ぶカリキュラム学習を行う点も特徴です。 |
| どうやって有効だと検証した？ | 9つのベンチマーク（VSI-Bench、EmbSpatial、ViewSpatial等）で評価を行い、3Bおよび7Bスケールで最高平均スコアを達成しました。また、アブレーションスタディにより、DGEによる物理的なフィードバックが性能向上に不可欠であることを証明しました。 |
| 議論はある？ | 完全に構築された高精度な3D資産（点群データ等）が必要であり、動的な環境や屋外環境での適用には課題があります。また、言語モデルによるエンティティ抽出時の解析精度が計算結果のノイズ源となる可能性がある点を認めています。 |
| 次に読むべき論文は？ | [SpatialVLM](https://arxiv.org/abs/2406.14455)、[SpatialBot](https://arxiv.org/abs/2505.10925)、[ScanNet++](https://arxiv.org/abs/2308.06642) |
| PDFリンク | https://arxiv.org/pdf/2604.14144v1 |
