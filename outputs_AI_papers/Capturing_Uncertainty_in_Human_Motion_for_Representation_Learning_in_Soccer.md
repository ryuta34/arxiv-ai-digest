---
title: "Capturing Uncertainty in Human Motion for Representation Learning in Soccer"
date: 2026-08-12
arxiv_id: 2608.11203v1
url: http://arxiv.org/abs/2608.11203v1
---

# Capturing Uncertainty in Human Motion for Representation Learning in Soccer

| 項目 | 内容 |
|---|---|
| どんなもの？ | サッカーの3Dスケルトンデータを用いた自己教師あり表現学習フレームワーク。将来の動作予測を学習目標とすることで、タスク間で転移可能な表現を獲得し、アクション認識やイベント検知などの下流タスクの精度を向上させる。 |
| 先行研究と比べてどこがすごい？ | 従来の決定論的な回帰予測に対し、離散的なコードブックを用いて将来の動作を確率分布としてモデル化することで、人間の動作に伴う不確実性とマルチモーダル性を効果的に学習できる。また、フレーム単位での密な教師信号を与えることで、フレーム単位の精度が求められるタスクでの汎用性を高めている。 |
| 技術や手法のキモはどこ？ | バランスの取れたKD木を用いて3D動作空間を離散化し、将来の動作を分類タスクとして予測する「Discrete Distribution Learning (DDL)」モジュールを導入した点。また、Graph Transformer Network (GTN) を backbone に採用し、空間的および時間的な依存関係を効率的に学習させている。 |
| どうやって有効だと検証した？ | WorldPoseおよびProSoccerのサッカー選手トラッキングデータセットを用いて評価。動作予測におけるMPJPE（平均関節位置誤差）でベースラインを上回ったほか、アクション認識（WorldPoseAR/SoccerAR）およびショット検知（イベント検知）において、Random初期化や他の自己教師あり学習手法（MAMP）よりも優れた性能を達成した。 |
| 議論はある？ | 現在は個々の選手の動作に焦点を当てているため、将来の課題として、ボールや他の選手との相互作用を考慮したマルチエージェントおよびボール認識を含む包括的な表現学習への拡張を挙げている。 |
| 次に読むべき論文は？ | [15] MSR-GCN: Multi-Scale Residual Graph Convolution Networks for Human Motion Prediction, [48] Learning Trajectory Dependencies for Human Motion Prediction, [52] Masked Motion Predictors are Strong 3D Action Representation Learners |
| PDFリンク | https://arxiv.org/pdf/2608.11203v1 |
