---
title: "Generalizable Sparse-View 3D Reconstruction from Unconstrained Images"
date: 2026-05-01
arxiv_id: 2604.28193v1
url: http://arxiv.org/abs/2604.28193v1
---

# Generalizable Sparse-View 3D Reconstruction from Unconstrained Images

| 項目 | 内容 |
|---|---|
| どんなもの？ | 少ない枚数の未調整画像から、照明変化や遮蔽物に頑健な3Dシーンを即座に再構成するフィードフォワード型のフレームワーク「GenWildSplat」。最適化を必要とせず、3秒の推論時間で視点一貫性のあるレンダリングを実現する。 |
| 先行研究と比べてどこがすごい？ | 従来の最適化ベースの手法（WildGaussians等）がシーンごとに長時間かけて最適化する必要があったのに対し、本手法は推論時最適化なしで高速に実行可能。また、学習時の多様な照明・遮蔽パターンへの対応により、極めて少ない入力枚数でも高精細な3D再構成と照明制御を実現した。 |
| 技術や手法のキモはどこ？ | VGGT transformerを用いた特徴抽出による幾何学的予測と、学習済みの照明コードと各ガウス分布を組み合わせる「Appearance Adapter」による照明制御。さらに、セマンティックセグメンテーションによる遮蔽物除去と、段階的なカリキュラム学習の組み合わせが核心。 |
| どうやって有効だと検証した？ | PhotoTourismおよびMegaScenesベンチマークを用い、従来手法との定量的な比較（PSNR, SSIM, LPIPS）およびアブレーションスタディを実施。実環境における疎な視点画像から、照明変化や遮蔽を考慮した高品質なレンダリングができることを実証した。 |
| 議論はある？ | 入力画像でカバーされていない領域の幾何学的不備や、テスト時の視点が学習データから大きく離れている場合のアーティファクト、室内環境における遮蔽マスクの精度の課題などが挙げられている。また、詳細なキャストシャドウや物理的に整合したレンダリングには対応していない。 |
| 次に読むべき論文は？ | [11] Anysplat: Feed-forward 3d gaussian splatting from unconstrained views. [16] Wildgaussians: 3d gaussian splatting in the wild. [23] Dl3dv-10k: A large-scale scene dataset for deep learning-based 3d vision. |
| PDFリンク | https://arxiv.org/pdf/2604.28193v1 |
