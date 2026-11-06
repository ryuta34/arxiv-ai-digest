---
title: "BEAKER: An Expert-Curated Benchmark for Embodied Brains in Self-Driving Chemical Laboratories"
date: 2026-11-06
arxiv_id: 2611.06911v1
url: http://arxiv.org/abs/2611.06911v1
---

# BEAKER: An Expert-Curated Benchmark for Embodied Brains in Self-Driving Chemical Laboratories

| 項目 | 内容 |
|---|---|
| どんなもの？ | 自律化学実験室（SDCL）向けのAIモデルの性能を評価するための、専門家監修による包括的なベンチマーク「BEAKER」です。化学実験の実行に必要なアクション、知識、実験操作、推論の4つの能力を、1,000のQAサンプルを用いてオフラインで評価します。 |
| 先行研究と比べてどこがすごい？ | 既存のベンチマークが主に異常検知や安全性評価に留まっていたのに対し、BEAKERはロボットによる化学実験の遂行に必要な「実行型」の能力（操作領域の特定や軌道計画など）を体系的に評価できる点が画期的です。 |
| 技術や手法のキモはどこ？ | AI生成に頼らず、化学および具現化AI（Embodied AI）の専門家が全サンプルを独自に作成・精査した点です。さらに、Actionability、Knowledge、Experimentation、Reasoningの4軸で評価体系を構築し、実験の文脈に即した実行精度を検証する仕組みを導入しています。 |
| どうやって有効だと検証した？ | 28種類の主要なMLLM（マルチモーダル大規模言語モデル）をBEAKERで評価しました。その結果、多くのモデルが手順の把握は可能でも、微細な操作領域の接地（Actionability）やドメイン特有の認識で苦戦するという性能の限界を明らかにしました。 |
| 議論はある？ | 現在はオフライン評価にとどまっており、実際のロボットによる閉ループ制御やマルチターン対話には対応していません。また、画像やビデオの視点が特定のロボットプラットフォームと一致しない可能性がある点や、将来的にはシミュレーション環境での動的な意思決定評価への拡張を課題としています。 |
| 次に読むべき論文は？ | [10] RoboBrain, [26] SDCL Visual Anomaly Dataset, [28] LABSHIELD, [64] LabUtopia |
| PDFリンク | https://arxiv.org/pdf/2611.06911v1 |
