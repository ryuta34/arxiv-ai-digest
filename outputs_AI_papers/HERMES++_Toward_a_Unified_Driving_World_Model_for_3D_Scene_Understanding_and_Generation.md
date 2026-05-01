---
title: "HERMES++: Toward a Unified Driving World Model for 3D Scene Understanding and Generation"
date: 2026-05-01
arxiv_id: 2604.28196v1
url: http://arxiv.org/abs/2604.28196v1
---

# HERMES++: Toward a Unified Driving World Model for 3D Scene Understanding and Generation

| 項目 | 内容 |
|---|---|
| どんなもの？ | 3Dシーン理解と将来の幾何学的進化予測を統合した、自律走行のための世界モデル「HERMES++」を提案した論文。LLMの推論能力とBEV表現の空間認識能力を融合し、環境の記述・質問応答と将来の3D点群生成を単一の枠組みで実現している。 |
| 先行研究と比べてどこがすごい？ | 従来モデルが「理解」または「生成」のどちらかに特化していたのに対し、本手法は両者をシームレスに統合した点。特に、BEV表現を用いることでマルチビュー情報の空間整合性を保ちつつ、既存の専用手法を上回る3D生成精度（Chamfer Distanceの改善など）とシーン理解性能を両立した。 |
| 技術や手法のキモはどこ？ | BEV表現をLLMと互換性のあるトークンに変換する手法、LLMの推論知識を将来生成に転送する「世界クエリ（World Queries）」、および明示的な幾何学的制約と潜在空間での暗黙的正則化を組み合わせた「共同幾何最適化戦略」が核心。 |
| どうやって有効だと検証した？ | NuScenesおよびOmniDrive-nuScenesデータセットを用い、生成タスク（Chamfer Distance）と理解タスク（CIDEr等）の両面から既存手法と比較。さらに、アブレーションスタディを通じて、BEV表現の有効性や提案コンポーネント（Joint Geometric Optimization等）の寄与を詳細に分析した。 |
| 議論はある？ | 現在はカメラ入力に依存しているが、将来的にはマルチモーダルな入力への拡張や、より多様な環境・モダリティへの適用が必要であると述べている。また、事前学習済みの大規模モデルのセマンティックな事前知識をBEV入力に活かす方法の深掘りが課題。 |
| 次に読むべき論文は？ | [15] OmniDrive: A holistic vision-language dataset for autonomous driving (CVPR 2025), [18] DriveX: Omni scene modeling for learning generalizable world knowledge in autonomous driving (ICCV 2025) |
| PDFリンク | https://arxiv.org/pdf/2604.28196v1 |
