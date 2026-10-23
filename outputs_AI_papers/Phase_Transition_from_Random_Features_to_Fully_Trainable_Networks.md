---
title: "Phase Transition from Random Features to Fully Trainable Networks"
date: 2026-10-23
arxiv_id: 2610.31663v1
url: http://arxiv.org/abs/2610.31663v1
---

# Phase Transition from Random Features to Fully Trainable Networks

| 項目 | 内容 |
|---|---|
| どんなもの？ | 隠れ層のニューロンの一部を訓練可能、残りをランダムに固定した「P-trainableネットワーク」における近似能力と学習誤差の挙動を理論的・数値的に解析した研究。ニューラルネットワークの性能が訓練可能な割合Pに対して、Pが小さい段階で急速に向上し、その後は鈍化する「相転移」現象を明らかにしました。 |
| 先行研究と比べてどこがすごい？ | 従来は固定されたランダム特徴量モデルと完全訓練可能なネットワークという両極端なモデルが議論されてきましたが、本研究はそれらを繋ぐ中間的なP-trainableネットワークにおいて、理論的な近似誤差の評価と相転移現象の शार्p（鋭さ）を定量化しました。 |
| 技術や手法のキモはどこ？ | 訓練可能なニューロン群と固定されたニューロン群の「サンプリングのミスマッチ」を定式化し、ポリノミアルスペクトル減衰の仮定の下で、訓練可能な割合Pに依存する明示的な近似レート（O((κ_P log(m/δ)/m)^α)）を導出した点。 |
| どうやって有効だと検証した？ | 球面 biased-ReLU 特徴量を用いた理論的な評価式の導出に加え、様々なネットワーク深度や幅、対象関数を用いて数値実験を行い、理論上の相転移パターンが実際の学習誤差においても一貫して現れることを確認しました。 |
| 議論はある？ | 勾配ベースの実際の学習が、提案した理論的モデル（サンプリングベースの重み付け）とどう一致するかという接続や、より深いネットワークにおけるニューロン間の相互作用の数学的な記述が今後の課題として残されています。 |
| 次に読むべき論文は？ | [4] F. Bach, "On the equivalence between kernel quadrature rules and random feature expansions." (JMLR 2017) [32] M. Li et al., "How powerful are shallow neural networks with bandlimited random weights?" (ICML 2023) |
| PDFリンク | https://arxiv.org/pdf/2610.31663v1 |
