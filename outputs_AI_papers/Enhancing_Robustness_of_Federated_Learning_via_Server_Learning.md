---
title: "Enhancing Robustness of Federated Learning via Server Learning"
date: 2026-04-06
arxiv_id: 2604.03226v1
url: http://arxiv.org/abs/2604.03226v1
---

# Enhancing Robustness of Federated Learning via Server Learning

| 項目 | 内容 |
|---|---|
| どんなもの？ | 非IIDデータ環境下における連合学習（FL）を、Byzantine攻撃（悪意あるクライアントによる攻撃）から保護するための手法「RoFSL」を提案した論文。サーバー側で小規模なデータセットを活用し、学習の補助と悪意あるアップデートのフィルタリングを統合することで、モデルの堅牢性を大幅に向上させた。 |
| 先行研究と比べてどこがすごい？ | 従来の堅牢な集約ルール（幾何学的中央値など）だけでは、悪意あるクライアントが半数を超えると対応困難だったが、サーバー側の補助学習（Server Learning）を組み合わせることで、「正直者が過半数」という条件を緩和し、高い精度を維持できる点。 |
| 技術や手法のキモはどこ？ | サーバー側の損失関数を用いた「角度ベースのフィルタリング」および「損失ベースのフィルタリング」と、幾何学的中央値による堅牢な集約、さらにサーバー側での微小なローカル学習を組み合わせたシナジー効果。特に、サーバーデータがクライアントデータと異なっていても有効である点。 |
| どうやって有効だと検証した？ | EMNISTおよびCIFAR-10データセットを用い、Dirichlet分布でデータ非IID性を制御。標識反転（Sign-flipping）とラベル反転（Label-flipping）を混合したByzantine攻撃を加え、最大60%のクライアントが悪意を持っていても、モデル精度が維持されることを実証した。 |
| 議論はある？ | サーバー側の学習率（$\gamma$）の調整が重要であり、過度に強く学習させるとサーバーデータへの過学習のリスクがある。また、現在の手法は静的であるため、将来的には悪意あるクライアントの割合を動的に推定し、フィルタリングパラメータを適応させる必要がある。 |
| 次に読むべき論文は？ | [1] [Blanchard et al., NeurIPS 2017](https://papers.nips.cc/paper_files/paper/2017/hash/f4b9ec30ad9f68f89b29639786cb62ef-Abstract.html) (Byzantine耐性勾配降下法)<br>[3] [Xie et al., ICML 2020](https://proceedings.mlr.press/v119/xie20b.html) (Zeno++: 非同期SGDにおける堅牢性) |
| PDFリンク | https://arxiv.org/pdf/2604.03226v1 |
