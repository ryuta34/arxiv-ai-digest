---
title: "StructSplat: Generalizable 3D Gaussian Splatting from Uncalibrated Sparse Views"
date: 2026-06-29
arxiv_id: 2606.28321v1
url: http://arxiv.org/abs/2606.28321v1
---

# StructSplat: Generalizable 3D Gaussian Splatting from Uncalibrated Sparse Views

| 項目 | 内容 |
|---|---|
| どんなもの？ | カメラパラメータ（内部・外部パラメータ）が未知のスパースな画像群から、フィードフォワードかつ汎用的に3D Gaussian Splattingを再構築するフレームワーク。明示的な構造化表現を用いることで、高品質な新規視点合成を実現する。 |
| 先行研究と比べてどこがすごい？ | 従来のPose-free手法で発生しがちだった「情報のリーク（ターゲット視点の情報がソースに混入する問題）」を解決し、DL3DVなどのベンチマークでAnySplat等の既存手法を大幅に上回る性能（PSNRで+5.67dB向上など）を達成した点。 |
| 技術や手法のキモはどこ？ | ①幾何、意味、テクスチャ情報を分離して処理する「構造化表現」、②2D画像とGaussian属性を直接結びつける「ピクセルアライン・フィーチャー注入」、③学習時にソースとターゲットの情報を分離しつつ統一座標系へアラインする「カメラアライメント戦略」。 |
| どうやって有効だと検証した？ | DL3DV、ACID、RealEstate10Kの3つの大規模データセットで、既存のpose-freeおよび完全パラメータフリー手法と比較評価。L1誤差マップの可視化や、コンポーネントごとのアブレーション研究により、構造化表現とカメラアライメントの有効性を実証した。 |
| 議論はある？ | 極端に視点が少ない場合や遮蔽が激しい環境では依然として課題が残る。また、複雑な視点依存の照明効果の再現にも難しさがあり、動的シーンや大規模環境への対応を今後の課題としている。 |
| 次に読むべき論文は？ | [AnySplat](https://arxiv.org/abs/2505.23716), [Splatt3R](https://arxiv.org/abs/2408.13912), [Depth Anything 3](https://arxiv.org/abs/2511.10647) |
| PDFリンク | https://arxiv.org/pdf/2606.28321v1 |
