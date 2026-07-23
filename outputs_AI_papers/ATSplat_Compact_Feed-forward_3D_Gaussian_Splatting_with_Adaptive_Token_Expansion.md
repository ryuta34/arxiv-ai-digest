---
title: "ATSplat: Compact Feed-forward 3D Gaussian Splatting with Adaptive Token Expansion"
date: 2026-07-23
arxiv_id: 2607.20417v1
url: http://arxiv.org/abs/2607.20417v1
---

# ATSplat: Compact Feed-forward 3D Gaussian Splatting with Adaptive Token Expansion

| 項目 | 内容 |
|---|---|
| どんなもの？ | 従来のピクセル単位のfeed-forward方式ではなく、適応的な3Dアンカートークンを用いて計算リソースをシーンの複雑さに応じて配分する、効率的でコンパクトな3D Gaussian Splatting (3DGS) 手法。シーンの複雑さに応じた適応的な能力割り当てを実現し、高速かつ高品質な新規視点合成を可能にする。 |
| 先行研究と比べてどこがすごい？ | 従来の多くの手法が画像解像度やビュー数に依存した冗長なガウス分布を生成していたのに対し、本手法は不要なガウス分布を大幅に削減（5.7倍以上）しながら、最先端のレンダリング品質を維持できる。また、推論速度の向上と計算効率の改善を両立した。 |
| 技術や手法のキモはどこ？ | Coarseなパッチ深度情報から「スパースな3Dアンカートークン」を生成し、Decoder内で「Adaptive Token Expansion (ATE)」モジュールを用いて、誤差が大きい（複雑な）領域のトークンのみを優先的に展開（増殖）させることで、リソースの集中配分を行う点。 |
| どうやって有効だと検証した？ | RealEstate10KおよびDL3DVデータセットを用い、PSNR、SSIM、LPIPS等の指標で定量評価を実施。また、ガウス分布の数、推論速度、複雑なシーンにおける定性的な比較を行い、他手法に対する優位性を確認した。 |
| 議論はある？ | 現在の手法は拡張は行うが、デコード中に冗長になったトークンを削除する機能（剪定）が未実装である。今後は、よりスケーラブルな構造への拡張や、未設定（unposed）画像への対応、剪定メカニズムの導入が課題となる。 |
| 次に読むべき論文は？ | [3D Gaussian Splatting (Kerbl et al. 2023)](https://arxiv.org/abs/2308.04079), [pixelSplat (Charatan et al. 2024)](https://arxiv.org/abs/2312.12337), [MVSplat (Chen et al. 2024a)](https://arxiv.org/abs/2403.14629) |
| PDFリンク | https://arxiv.org/pdf/2607.20417v1 |
