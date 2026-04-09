---
title: "MoRight: Motion Control Done Right"
date: 2026-04-09
arxiv_id: 2604.07348v1
url: http://arxiv.org/abs/2604.07348v1
---

# MoRight: Motion Control Done Right

| 項目 | 内容 |
|---|---|
| どんなもの？ | 1枚の画像から、ユーザー指定の動作とカメラ移動を独立して制御し、因果関係に基づいた物理的に妥当な動画を生成するフレームワーク「MoRight」。物体動作とカメラ視点を分離した「デュアルストリーム生成」により、直感的な動画制作を可能にする。 |
| 先行研究と比べてどこがすごい？ | 従来手法はカメラと物体の動きが画素レベルで絡み合い（絡合）、かつ kinematic（運動学的）な変位に留まっていたが、本手法は両者を明示的に分離し、さらに「能動的（ユーザーの操作）」と「受動的（物理的結果）」な動作を学習することで、物理的な因果関係（例：押すと物が転がる）を再現できる点。 |
| 技術や手法のキモはどこ？ | 1. canonical 空間での物体制御と、クロスビュー注意機構によるターゲットカメラへの転写を行う「デュアルストリーム構造」。2. 学習時に動作を能動・受動に分解し、ランダムにdropoutさせることでモデルに因果関係を内省させる手法。3. 大規模な実動画データから、自動で動作因果関係を抽出・再学習するパイプライン。 |
| どうやって有効だと検証した？ | DynPose-100K、WISA、自作のCookingデータセットの3つで評価。PSNR/SSIMなどの画質指標に加え、カメラと物体の制御精度（EPE）、物理的妥当性（PC/SA）を測定。さらに、11名の被験者による定性的な知覚評価を行い、従来手法（ATI, WanMove等）よりも優れていることを証明した。 |
| 議論はある？ | 複雑な相互作用や高速なカメラ移動時には、動きの不一致や物体消失、偽物の生成（幻覚）が発生する場合がある。また、カメラ制御が滑らかな軌道に依存しており、激しいエゴモーションには弱い。 |
| 次に読むべき論文は？ | [Wan: Open and advanced large-scale video generative models](https://arxiv.org/abs/2503.20314)、[Motion prompting: Controlling video generation with motion trajectories](https://arxiv.org/abs/2412.02700)、[Physdreamer: Physics-based interaction with 3d objects via video generation](https://arxiv.org/abs/2408.06072) |
| PDFリンク | [https://arxiv.org/pdf/2604.07348v1](https://arxiv.org/pdf/2604.07348v1) |
