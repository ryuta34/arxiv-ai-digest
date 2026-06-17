---
title: "Future Dynamic 3D Reconstruction: A 3D World Model with Disentangled Ego-Motion"
date: 2026-06-17
arxiv_id: 2606.18250v1
url: http://arxiv.org/abs/2606.18250v1
---

# Future Dynamic 3D Reconstruction: A 3D World Model with Disentangled Ego-Motion

| 項目 | 内容 |
|---|---|
| どんなもの？ | 単眼画像入力から、将来の動的な3Dシーン構成を予測する世界モデル「FR3D」。エゴモーション（自己運動）と環境の動的変化を3D潜在空間内で分離してモデル化することで、長期にわたる一貫した3D予測を実現した。 |
| 先行研究と比べてどこがすごい？ | 従来の2D動画生成モデルが抱えていた、エゴモーションとシーン変化の混同による物理的矛盾（オブジェクトの歪み等）を解決した。また、大規模な学習コストを回避し、既存の3D再構成モデルを用いた教師あり蒸留により、高いゼロショット汎化性能を達成した点。 |
| 技術や手法のキモはどこ？ | エゴモーション（カメラの軌跡）と環境の動的変化（3Dシーン構造）を、共通の3D潜在空間で明示的に分離して予測する二つの専用トランスフォーマー（Pose/Spatial Masked Transformer）を導入し、互いに情報を共有（クロスアテンション）させた点。 |
| どうやって有効だと検証した？ | Waymo Open Datasetで学習し、KITTIおよびnuScenesデータセットを用いたゼロショット評価を実施。深さ推定とポーズ推定の指標で、Copy LastやDINO-Foresightなどのベースラインを上回る精度（2秒先まで）を実証した。 |
| 議論はある？ | 長期予測時にスケールドリフトが発生する点や、縦方向の動きには強い一方、横方向の移動に対しては動きを混合してしまう偏りがある。より多様なデータでの学習や、さらなる幾何学的制約の導入が課題。 |
| 次に読むべき論文は？ | [CUT3R (Wang et al., 2025b)](https://arxiv.org/abs/2501.03575) / [DINO-Foresight (Karypidis et al., 2025a)](https://arxiv.org/abs/2512.11225) |
| PDFリンク | https://arxiv.org/pdf/2606.18250v1 |
