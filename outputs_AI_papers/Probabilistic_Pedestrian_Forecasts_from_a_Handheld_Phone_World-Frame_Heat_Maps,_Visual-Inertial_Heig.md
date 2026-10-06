---
title: "Probabilistic Pedestrian Forecasts from a Handheld Phone: World-Frame Heat Maps, Visual-Inertial Height Drift, and Evaluation without Ground Truth"
date: 2026-10-06
arxiv_id: 2610.04736v1
url: http://arxiv.org/abs/2610.04736v1
---

# Probabilistic Pedestrian Forecasts from a Handheld Phone: World-Frame Heat Maps, Visual-Inertial Height Drift, and Evaluation without Ground Truth

| 項目 | 内容 |
|---|---|
| どんなもの？ | ハンドヘルド型のスマートフォンを用いた、歩行者の将来位置を予測するシステム。単眼カメラとVisual-Inertial Odometry (VIO)のみを使用し、重力に整合したメートル単位のワールドフレームで歩行者の移動を確率マップとして予測する。 |
| 先行研究と比べてどこがすごい？ | 従来の固定カメラやロボット用データセットに頼らず、移動するスマホという過酷な条件下で、独自手法によるVIOドリフト対策を施し、実世界での実用的な予測を試みた点。また、正解ラベルのない実環境での評価プロトコルを確立した。 |
| 技術や手法のキモはどこ？ | VIOの垂直ドリフトが地面の位置推定を歪ませる問題に対し、低域通過フィルタを通したカメラ高度を使用し、地面を固定せずに常にカメラからの相対高さを一定に保つことで、正確な地面投影を実現した点。 |
| どうやって有効だと検証した？ | 既存の公開ベンチマーク（SDD, EgoTraj-Bench）での精度評価に加え、ADVIOデータセットを用いた実環境での事前登録済みプロトコルに基づく評価を実施。トラッカー自身の後続測定値との整合性をスコア化する手法で検証。 |
| 議論はある？ | 地面の平坦性の仮定（傾斜や階層の移動）や、スマホの姿勢推定の精度に依存する。また、実環境での検証はシステム自身の測定値に基づく「自己整合性」の評価であり、独立した絶対的な正解データとの比較ではない点。 |
| 次に読むべき論文は？ | [33] Karttikeya Mangalam et al., "From goals, waypoints & paths to long term human trajectory forecasting", ICCV 2021. [7] Santiago Cortés et al., "ADVIO: An authentic dataset for visual-inertial odometry", ECCV 2018. |
| PDFリンク | https://arxiv.org/pdf/2610.04736v1 |
