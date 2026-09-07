---
title: "WearableQA: A Benchmark for Health Reasoning over Real-World Wearable Data"
date: 2026-09-07
arxiv_id: 2609.05405v1
url: http://arxiv.org/abs/2609.05405v1
---

# WearableQA: A Benchmark for Health Reasoning over Real-World Wearable Data

| 項目 | 内容 |
|---|---|
| どんなもの？ | ウェアラブルデバイスの時系列データを用いた健康推論能力を評価するための新たなベンチマーク「WearableQA」です。200人の実ユーザーから得られたデータに基づき、データ処理と健康関連の解釈能力を多角的に診断します。 |
| 先行研究と比べてどこがすごい？ | 従来のベンチマークがシミュレーションデータや静的な医学知識に依存していたのに対し、本研究はノイズを含む実世界データと血中バイオマーカー、人口統計情報を組み合わせた現実的な評価環境を提供しています。 |
| 技術や手法のキモはどこ？ | 査読付き文献に基づく「文献接地（Literature-grounded）」と、大規模コホートから統計的に妥当なパターンを導き出す「集団接地（Population-grounded）」を組み合わせた「二重接地（Dual-grounding）フレームワーク」により、高品質で再現性の高い評価問題を自動生成した点です。 |
| どうやって有効だと検証した？ | 14の商用およびオープンソースLLMを対象に、16の質問タイプで性能を比較評価しました。Chain-of-Thought（CoT）の有無や入力形式、モデルサイズによる違いを細かく診断し、推論の限界を明確化しました。 |
| 議論はある？ | データ推論（数値計算）が健康解釈よりもモデルにとって困難であることや、クロスシグナル（複数信号統合）推論の難易度が高いことが判明しました。また、モデルが単純な位置バイアスや先行知識に頼るケースがある点も指摘しています。 |
| 次に読むべき論文は？ | [PHlA (Merrill et al., 2026)](https://arxiv.org/pdf/2609.05405v1) や [Time2lang (Pillai et al., 2025)](https://arxiv.org/pdf/2609.05405v1) など、ウェアラブルデータ解析に関連する先行研究。 |
| PDFリンク | https://arxiv.org/pdf/2609.05405v1 |
