---
title: "Sensorimotor Alignment: A Platonic Proxy for Embodied Policy Success"
date: 2026-10-23
arxiv_id: 2610.31670v1
url: http://arxiv.org/abs/2610.31670v1
---

# Sensorimotor Alignment: A Platonic Proxy for Embodied Policy Success

| 項目 | 内容 |
|---|---|
| どんなもの？ | ロボット学習モデルの性能を、高コストな実機やシミュレーション評価なしで予測する指標「Sensorimotor Alignment (S²)」を提案した論文。モデルの感覚表現（画像・テキスト特徴量）が物理的な行動軌跡の構造といかに整合しているかを測ることで、タスク成功率を offline で予測可能にする。 |
| 先行研究と比べてどこがすごい？ | 従来の指標（VQAスコアや動画品質メトリクス）が受動的な認識能力しか測れなかったのに対し、S²は「行動」に直結する表現の整合性を測定する。タスク成功率と高い正の相関を示し、VLAの設計choices（凍結したエンコーダーの限界や各レイヤーの重要性など）に対して表現レベルでの説明性を提供できる点。 |
| 技術や手法のキモはどこ？ | Platonic Representation Hypothesis (PRH) をロボット工学に応用し、感覚表現と運動軌跡をそれぞれ近傍探索（k-nearest neighbors）で比較する点。動的な軌跡の差異を考慮するためにDynamic Time Warping (DTW) を導入し、感覚表現と運動表現の共通する近傍集合の重なりを指標化（S²）した点。 |
| どうやって有効だと検証した？ | 12種類のVLA、8種類のVLM、6種類のWAM、および実機ロボットポリシーを対象に広範な実験を実施。SimplerEnvやRoboTwinなどの環境で、S²と各モデルのタスク成功率が強い正の相関（r=+0.6〜0.8以上）を持つことを示した。また、アーム構成が合わないデータセットを用いた負の制御実験により、指標の妥当性も検証した。 |
| 議論はある？ | 現在は相関関係を示している段階であり、学習プロセスに直接組み込んで成功率を向上させる手法としては未検証である。また、異なるモデル間ではS²値が同じでも成功率が異なる場合があるため、あくまで高コストなテスト前の有望モデル絞り込みツールとしての利用が推奨される。 |
| 次に読むべき論文は？ | [20] M. Huh et al., "The Platonic representation hypothesis", ICML 2024. (本手法の理論的基礎) |
| PDFリンク | https://arxiv.org/pdf/2610.31670v1 |
