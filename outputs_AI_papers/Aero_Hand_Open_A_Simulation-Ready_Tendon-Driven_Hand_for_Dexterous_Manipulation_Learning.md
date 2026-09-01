---
title: "Aero Hand Open: A Simulation-Ready Tendon-Driven Hand for Dexterous Manipulation Learning"
date: 2026-09-01
arxiv_id: 2608.28578v1
url: http://arxiv.org/abs/2608.28578v1
---

# Aero Hand Open: A Simulation-Ready Tendon-Driven Hand for Dexterous Manipulation Learning

| 項目 | 内容 |
|---|---|
| どんなもの？ | 3Dプリンタで製作可能な低コストかつ高い把持能力を持つ、腱駆動式の五指ロボットハンド「Aero Hand Open」とそのシミュレーション・学習環境。実機で調整することなく、シミュレーションで学習したモデルをゼロショットで転移できる再現性を実現した。 |
| 先行研究と比べてどこがすごい？ | 腱駆動ハンドの難点であった「シミュレータと実機の伝達機構の乖離」を、物理的なルーティング形状に基づいた高精度なシミュレーションモデルと、入出力の線形写像によって解決した点。また、製作費用約314ドルという低コスト性も特徴。 |
| 技術や手法のキモはどこ？ | CADデータに基づき、ケーブルが滑車を回る経路を空間腱（spatial tendon）としてMuJoCo上に忠実に再現した点。また、 thumb（親指）の複雑な結合を識別モデルを用いて補完し、ハードウェア側で計測可能な信号のみを用いた観察空間を設計した点。 |
| どうやって有効だと検証した？ | 134秒間の実機とシミュレータの同期検証による動的性能の確認と、MuJoCo PlaygroundおよびPPOアルゴリズムを用いた「インハンド・キューブ回転タスク」の学習を実施。実機へのゼロショット転移による継続的な安定回転の実現で評価した。 |
| 議論はある？ | サム（親指）のフレックス（屈曲）における物理モデルとシミュレーションの結合部の乖離が残る。現時点ではソフトウェア側の写像補正でカバーしているが、さらなるモデル精度の向上が将来的な課題。 |
| 次に読むべき論文は？ | [1] [The GRASP taxonomy of human grasp types](https://doi.org/10.1109/THMS.2015.2470657), [14] [Leap Hand: Low-cost, efficient, and anthropomorphic hand for robot learning](https://www.roboticsproceedings.org/rss19/p045.html), [25] [Learning dexterous in-hand manipulation](https://doi.org/10.1177/0278364919887447) |
| PDFリンク | https://arxiv.org/pdf/2608.28578v1 |
