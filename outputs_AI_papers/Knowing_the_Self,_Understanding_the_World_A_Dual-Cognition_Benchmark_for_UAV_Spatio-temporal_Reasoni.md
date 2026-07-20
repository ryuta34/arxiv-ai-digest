---
title: "Knowing the Self, Understanding the World: A Dual-Cognition Benchmark for UAV Spatio-temporal Reasoning with MLLMs"
date: 2026-07-20
arxiv_id: 2607.16193v1
url: http://arxiv.org/abs/2607.16193v1
---

# Knowing the Self, Understanding the World: A Dual-Cognition Benchmark for UAV Spatio-temporal Reasoning with MLLMs

| 項目 | 内容 |
|---|---|
| どんなもの？ | UAV（無人航空機）の視点移動や運動を伴う環境下での、自己の状態認識と環境認識を統合的に評価する「Dual-Cognition（二重認知）」ベンチマークである。画像および動画タスクを通じて、MLLMの空間的・時間的推論能力を詳細に測定できる。 |
| 先行研究と比べてどこがすごい？ | 既存のUAVベンチマークが主に「環境理解」や「タスク完了」に特化していたのに対し、本研究は「自己の状態（姿勢・飛行行動）」と「外部環境」を不可分な認知対象として同時に評価する枠組みを導入した点。また、バウンディングボックスや時間区間などの構造的な出力による厳密なグラウンディング評価を可能にした。 |
| 技術や手法のキモはどこ？ | シーンレベルのセマンティック点群を用いた高度に自動化されたデータ構築パイプライン（UAV-DualCog）。これを用い、飛行行動と環境の相互作用を考慮した多様なマルチビュー推論タスクを生成し、マルチモーダルLLMの認知能力を自己・環境の二側面から評価可能にした点。 |
| どうやって有効だと検証した？ | 多様な軽量MLLMを対象に網羅的な性能評価を実施。さらに、思考プロセスの導入（Thinking model）、人間によるベースライン比較、失敗事例の分析、および「UAV-DualCog-Train」を用いた強化学習（GRPO）による性能向上を確認する最適化プローブを通じて、ベンチマークとしての有効性を立証した。 |
| 議論はある？ | 現在のMLLMは環境認識に比べ自己認識が著しく弱く、空間的な接地（Grounding）と回答精度に乖離があることを指摘。また、動画タスクにおける時間的一貫性の確保や、シミュレーション環境から現実世界へのドメインギャップが依然として課題であるとしている。 |
| 次に読むべき論文は？ | [63] Zhishan Zou et al., "Self in Space: Benchmarking Self-Awareness and Spatial Cognition in UAV Embodied Intelligence" (arXiv:2607.12477) |
| PDFリンク | https://arxiv.org/pdf/2607.16193v1 |
