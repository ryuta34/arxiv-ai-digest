---
title: "GaussiAnimate: Reconstruct and Rig Animatable Categories with Level of Dynamics"
date: 2026-04-10
arxiv_id: 2604.08547v1
url: http://arxiv.org/abs/2604.08547v1
---

# GaussiAnimate: Reconstruct and Rig Animatable Categories with Level of Dynamics

| 項目 | 内容 |
|---|---|
| どんなもの？ | 4Dガウススプラッティング(4DGS)等で再構成された動的な3D形状を、関節構造と非剛体変形を分離してモデル化することで、直感的な制御と高い変形忠実度を両立させる「Skelebones」 riggingシステム。 |
| 先行研究と比べてどこがすごい？ | テンプレートを用いない「テンプレートフリー」なアプローチでありながら、内側の kinematic スケルトンと外側の自由形状ボーンを分離して扱うことで、従来手法の「制御のしやすさ」と「変形精度」のトレードオフを解消した点。 |
| 技術や手法のキモはどこ？ | ①ガウス分布を圧縮した自由形状ボーン、②平均曲率骨格を用いた動的適応型スケルトン、③骨格とボーンをパーツ単位でマッチング・ブレンドする非パラメトリックなPartwise Motion Matching (PartMM)。 |
| どうやって有効だと検証した？ | 合成データセット(D-NeRF, DG-Mesh)および実写データセット(DNA-Rendering, ActorHQ, VTO, D4D)を用い、既存のLBS、BoB、ニューラル手法と比較してPSNR等のレンダリング品質とRMSE等の変形精度で評価。 |
| 議論はある？ | 現在はリアルタイム処理ではない点や、複雑な衣服（スカートなど）で関節位置が解剖学的な期待から逸脱する可能性がある点、レンダリング時に穴が生じる可能性がある点が挙げられている。 |
| 次に読むべき論文は？ | [RigGS](https://arxiv.org/abs/2501.14937), [BanMo](https://arxiv.org/abs/2112.12753), [DressRecon](https://arxiv.org/abs/2412.00000)（※URLは論文中の引用文献に基づいた推定） |
| PDFリンク | https://arxiv.org/pdf/2604.08547v1 |
