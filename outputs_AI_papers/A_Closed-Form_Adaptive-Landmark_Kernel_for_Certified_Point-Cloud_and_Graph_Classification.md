---
title: "A Closed-Form Adaptive-Landmark Kernel for Certified Point-Cloud and Graph Classification"
date: 2026-05-06
arxiv_id: 2605.04046v1
url: http://arxiv.org/abs/2605.04046v1
---

# A Closed-Form Adaptive-Landmark Kernel for Certified Point-Cloud and Graph Classification

| 項目 | 内容 |
|---|---|
| どんなもの？ | persistence diagram（持続的ホモロジーの出力）を用いたグラフ・点群分類のためのデータ適応型かつ閉形式（closed-form）のカーネル手法であるPALACEを提案。従来の手法と異なり、勾配学習や保持データ（held-out data）を用いたハイパーパラメータ調整を必要とせず、理論的な保証と予測ごとの正当性証明を両立させている。 |
| 先行研究と比べてどこがすごい？ | 固定グリッドを用いる従来手法（PLACE）に対し、クラス適応的なランドマーク配置を行うことで、データが集中する領域に計算コストを集中させつつ、同じ理論的保証を維持できる。また、カーネルSVMを用いることで非線形な識別性能を高めつつ、閉形式の構成により精度・堅牢性・計算効率において既存の図式ベース手法を上回る結果を示した。 |
| 技術や手法のキモはどこ？ | クラス適応的な遠方点サンプリング（FPS）によるランドマーク配置と、Lebesgue数に基づいたカバー理論による非一様歪み保証。また、個々のランドマークに対する加法的なカーネル（additive landmark kernel）の導入と、分類の信頼性を評価する閉形式の正規化マージン（Score statistic）の提案。 |
| どうやって有効だと検証した？ | Orbit5k点群データおよび5つの化学グラフベンチマークを用い、固定グリッドベースライン（PLACE）やDeep Learningベースの競合手法（Persformer等）との分類精度を比較。また、ドメイン膨張実験により、データ集中時における予算削減効果（(D/L)^2の低減）を実証した。 |
| 議論はある？ | 非干渉条件（non-interference condition）が化学グラフ等の実データでは構造的な仮定として機能する点や、計算コストがグラム行列の計算に依存するため、大規模データへのスケーリングには制限がある。また、極端にラベル情報が支配的なデータセットでは、構造的な記述子を用いるグラフニューラルネットワーク等に劣る場合がある。 |
| 次に読むべき論文は？ | [PLACE: A closed-form persistence-landmark pipeline for certified point-cloud and graph classification](https://arxiv.org/abs/2605.02836), [Geometric embeddings of spaces of persistence diagrams with explicit distortions](https://arxiv.org/abs/2401.05298) |
| PDFリンク | https://arxiv.org/pdf/2605.04046v1 |
