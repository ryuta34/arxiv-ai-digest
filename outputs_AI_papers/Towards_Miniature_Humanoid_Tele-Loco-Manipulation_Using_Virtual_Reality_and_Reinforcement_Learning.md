---
title: "Towards Miniature Humanoid Tele-Loco-Manipulation Using Virtual Reality and Reinforcement Learning"
date: 2026-07-23
arxiv_id: 2607.20399v1
url: http://arxiv.org/abs/2607.20399v1
---

# Towards Miniature Humanoid Tele-Loco-Manipulation Using Virtual Reality and Reinforcement Learning

| 項目 | 内容 |
|---|---|
| どんなもの？ | 小型ヒューマノイドロボット（ROBOTIS OP3）を対象とした、仮想現実（VR）による遠隔操作と強化学習（RL）による歩行制御を組み合わせた全身遠隔操作フレームワーク。遠隔地からロボットを操り、歩行と物体操作を同時に行う「Tele-Loco-Manipulation」を実現した。 |
| 先行研究と比べてどこがすごい？ | 高価な大型ロボットに限定されがちだった遠隔操作技術を、入手容易な小型ヒューマノイドへ適用した点。強化学習を用いたロバストな歩行制御と、独自のトルク制御スタックを組み合わせることで、小型機でも全身の協調動作を可能にした。 |
| 技術や手法のキモはどこ？ | DYNAMIXELサーボに対する独自のPDベースインピーダンス制御と、Isaac Labを用いたドメインランダム化によるSim2Real（シミュレーションから実機への移行）。また、視覚的な遅延を軽減するためのEMAフィルタや、物理的な遅延を補償するVR視点の回転制御を実装した点。 |
| どうやって有効だと検証した？ | 腕の動作追従性に関する円軌道トレース実験、ランダムな外力下での歩行安定性試験、および実機を用いた「5m歩行して40gの立方体を箱に運ぶ」という一連のブロック移動実験により評価した。 |
| 議論はある？ | 現在の課題として、通信・処理遅延（約220ms）、ロボットの歩行時の足上げ高さ不足、テザー（電源コード）の制約、およびアクチュエータモデルの単純さが挙げられる。今後は重力・摩擦補償の追加や、KAT WALKトレッドミルとの統合による没入感向上が必要。 |
| 次に読むべき論文は？ | [17] M. Seo et al., "Deep Imitation Learning for Humanoid Loco-manipulation Through Human Teleoperation" (https://doi.org/10.1109/Humanoids57100.2023.10375203) <br> [24] H. Shi et al., "ToddlerBot: Open-Source ML-Compatible Humanoid Platform for Loco-Manipulation" (https://doi.org/10.48550/arXiv.2502.00893) |
| PDFリンク | https://arxiv.org/pdf/2607.20399v1 |
