---
title: "TerraZero: Procedural Driving Simulation for Zero-Demonstration Self-Play at Scale"
date: 2026-07-15
arxiv_id: 2607.13028v1
url: http://arxiv.org/abs/2607.13028v1
---

# TerraZero: Procedural Driving Simulation for Zero-Demonstration Self-Play at Scale

| 項目 | 内容 |
|---|---|
| どんなもの？ | ゼロから強化学習で自律走行エージェントを訓練するための、高速かつ高忠実度な手続き型シミュレーションエンジン。既存のデータセットの地図情報のみを利用し、多様な交通シナリオを自動生成することで、人間による実演なし（ゼロ・デモンストレーション）での自己対戦学習を実現している。 |
| 先行研究と比べてどこがすごい？ | CPU/GPU間のゼロコピーデータ転送やNUMA最適化により、既存のオブジェクトレベルシミュレータを大きく上回る最大2.8M agent-steps/秒という圧倒的なスループットを達成した。また、ルールベースの交通制御やヘテロジニアスなエージェント構成を維持しつつ、学習効率と汎化性能を両立した点が優れている。 |
| 技術や手法のキモはどこ？ | 地図データのみを入力とし、手続き型生成（初期化、目標割り当て、NPC生成）により無限のシナリオを生み出す点。さらに、学習環境に依存しない報酬・力学パラメータのドメインランダマイゼーションと、PPOベースの強化学習においてサリエンシー優先度付きサンプリングやV-trace、PopArt等の安定化手法を統合した点。 |
| どうやって有効だと検証した？ | nuPlan val14およびInterPlanベンチマークを用いたプランナー評価、およびWaymo Open Sim Agents Challenge (WOSAC) におけるシムエージェントのリアリズム評価を実施。いずれの指標でも最先端の手法を上回るか同等の性能を示し、データセットや都市をまたぐ汎化性能についても確認した。 |
| 議論はある？ | 高解像度の地図と車線情報を必要とするため、それらが未整備の地域には適用できない。また、Visual Perception（カメラ/LiDAR入力）を直接扱わないオブジェクトレベルの抽象化を採用しているため、エンドツーエンドの知覚パイプラインには直接利用できないという限界がある。 |
| 次に読むべき論文は？ | [13] Robust Autonomy Emerges from Self-Play (ICML 2025), [46] Nocturne: A Scalable Driving Benchmark (NeurIPS 2022), [7] SPACeR: Self-Play Anchoring with Centralized Reference Models (ICLR 2026) |
| PDFリンク | https://arxiv.org/pdf/2607.13028v1 |
