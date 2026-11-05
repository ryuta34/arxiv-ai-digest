---
title: "PolicyIK: High-Precision Inverse Kinematics for Robot Arms with Reinforcement Learning"
date: 2026-11-05
arxiv_id: 2611.05372v1
url: http://arxiv.org/abs/2611.05372v1
---

# PolicyIK: High-Precision Inverse Kinematics for Robot Arms with Reinforcement Learning

| 項目 | 内容 |
|---|---|
| どんなもの？ | ロボットアームの高精度な逆運動学（IK）問題を解くための、ゴール条件付き強化学習を用いた手法「PolicyIK」です。従来の数値解法では困難だった、重力や関節制限下でのミリメートル単位の精密な位置保持を実現します。 |
| 先行研究と比べてどこがすごい？ | 従来の強化学習アプローチ（通常数cm程度の誤差）を大幅に凌駕し、シミュレーションおよび実機において、一般的な古典的IKコントローラよりも高精度かつ安定した到達・保持性能を達成しました。数値的なIKソルバーを必要とせず、学習によって高精度な制御を実現した点が画期的です。 |
| 技術や手法のキモはどこ？ | 1) Joint-positionインターフェースを通じた「参照累積（Reference accumulation）」により、重力下でのオフセットを保持できること。2) 誤差の大きさに応じてステップ幅を変化させる「誤差依存のゲイン調整」および「マルチスケールな姿勢フィードバック」。3) 終端精度を重視した、進行状況と滞留を報酬化する学習設計です。 |
| どうやって有効だと検証した？ | 7自由度のOpenArmを用いたシミュレーションでの多タスク評価、および実機（OpenArmおよびxArm7）での到達・保持テストを実施。また、VLAモデル（π0.5）と組み合わせたピック＆プレイス課題において、数値ソルバーを上回る高い成功率を示しました。 |
| 議論はある？ | 実機学習における学習データ収集のコスト効率や、特定のジョイント制限に近い状況での挙動について触れています。今後はより多様なロボットへの適用や、より複雑な環境下での汎用性向上が課題となります。 |
| 次に読むべき論文は？ | [FlashSAC: Fast and Stable Off-Policy Reinforcement Learning for High-Dimensional Robot Control](https://arxiv.org/abs/2606.24049) (学習手法の基盤)、[UMI on legs: Making manipulation policies mobile with manipulation-centric whole-body controllers](https://openreview.net/forum?id=3i7j8ZPnbm) (比較対象のベースライン) |
| PDFリンク | https://arxiv.org/pdf/2611.05372v1 |
