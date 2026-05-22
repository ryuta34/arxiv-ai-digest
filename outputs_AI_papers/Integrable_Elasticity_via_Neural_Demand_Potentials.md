---
title: "Integrable Elasticity via Neural Demand Potentials"
date: 2026-05-22
arxiv_id: 2605.22820v1
url: http://arxiv.org/abs/2605.22820v1
---

# Integrable Elasticity via Neural Demand Potentials

| 項目 | 内容 |
|---|---|
| どんなもの？ | 高次元の小売データにおいて、予測精度と経済学的な妥当性を両立させる、統合可能な価格弾力性推定のためのニューラルネットワークモデル「ICDN (Integrable Context-Dependent Demand Network)」を提案した論文。 |
| 先行研究と比べてどこがすごい？ | 従来の深層学習モデルが個別に弾力性を学習して数学的整合性を欠くことがあったのに対し、対数需要関数を滑らかな面として学習し、その微分として弾力性を導出することで、数学的な整合性と解釈可能性を保証した点。 |
| 技術や手法のキモはどこ？ | 需要関数をスプライン基底と文脈条件付きの係数で構成し、弾力性を解析的に微分可能な形で導出する「Demand-first」設計。また、疎な注意機構を用いた隣接製品の選択により、高次元な多製品間での交差弾力性推定をスケーラブルに実現した点。 |
| どうやって有効だと検証した？ | Dominick’s Finer Foodsのビール販売データを用い、従来の対数対数（log-log）回帰ベンチマークとの比較を実施。予測精度の向上（MAE/RMSEの改善）に加え、ブートストラップ法を用いた弾力性推定の安定性と信頼区間の狭さを実証した。 |
| 議論はある？ | 実験は観測データに基づいているため因果推論を完全には保証できない点、および弾力性の不確実性のキャリブレーションに課題が残る点。将来課題として、より高度な因果識別手法の導入や、実務的な価格最適化への応用が挙げられている。 |
| 次に読むべき論文は？ | Berry et al. (1995) "Automobile prices in market equilibrium" および Acuna-Agost et al. (2021) "Price elasticity estimation for deep learning-based choice models" |
| PDFリンク | https://arxiv.org/pdf/2605.22820v1 |
