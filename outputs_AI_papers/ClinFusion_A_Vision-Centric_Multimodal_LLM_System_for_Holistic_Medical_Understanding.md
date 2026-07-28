---
title: "ClinFusion: A Vision-Centric Multimodal LLM System for Holistic Medical Understanding"
date: 2026-07-28
arxiv_id: 2607.24743v1
url: http://arxiv.org/abs/2607.24743v1
---

# ClinFusion: A Vision-Centric Multimodal LLM System for Holistic Medical Understanding

| 項目 | 内容 |
|---|---|
| どんなもの？ | 医療画像（2D・3D）を包括的に理解し、正確な放射線レポートを作成するための視覚中心型マルチモーダル大規模言語モデル（MLLM）「ClinFusion」の提案。エージェント機能によるツール利用や、臨床の実践に基づいた評価手法を統合し、実用的な臨床アシスタントとしての機能を備えている。 |
| 先行研究と比べてどこがすごい？ | 単一のエンコーダーに依存する従来手法に対し、構成的な視覚エンコーダーを採用することで、2Dと3Dの医療データを統合的に処理できる。また、臨床現場の医師の判断と相関が高い「RoI（関心領域）ベースの評価手法」と、指示追従能力を測る「MedIF-Bench」を導入し、既存の表面的な評価手法の限界を克服している。 |
| 技術や手法のキモはどこ？ | 2Dエンコーダーのアンサンブルと3Dエンコーダーを「Cascade Spatial-Aware Locality (CaSL) Fusion」により段階的に統合する設計。また、RAG（検索増強生成）や専門知覚ツールを活用するエージェント型ワークフローと、臨床的な文脈を考慮した「RoI-Grounded」な評価フレームワークが核心となっている。 |
| どうやって有効だと検証した？ | 2D/3Dの多様な公開ベンチマークでSOTAを達成したほか、6名の放射線科医による300症例のブラインド評価を実施。提案手法のレポートが臨床的有用性や正確性において最も高く評価され、開発した自動評価指標が専門家の判断と最も強い相関を示すことを確認した。 |
| 議論はある？ | 現在のエージェント機能はツールセットが限定的であること、知識集約型のベンチマークでは依然として強力な独自モデルとの差があることを認めている。また、今後は臨床現場への統合に向けて、ワークフロー内での人間による検証と規制への対応が必要となる。 |
| 次に読むべき論文は？ | [1] [Qwen3-VL technical report](https://arxiv.org/abs/2511.21631) <br> [2] [Cambrian-1: A fully open, vision-centric exploration of multimodal llms](https://arxiv.org/abs/2406.16860) <br> [3] [Lingshu: A generalist foundation model for unified multimodal medical understanding and reasoning](https://arxiv.org/abs/2506.07044) |
| PDFリンク | https://arxiv.org/pdf/2607.24743v1 |
