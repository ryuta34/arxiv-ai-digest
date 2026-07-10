---
title: "ZipDepth: Bringing Lightweight Zero-Shot Monocular Depth Anywhere, on Any Device"
date: 2026-07-10
arxiv_id: 2607.08771v1
url: http://arxiv.org/abs/2607.08771v1
---

# ZipDepth: Bringing Lightweight Zero-Shot Monocular Depth Anywhere, on Any Device

| 項目 | 内容 |
|---|---|
| どんなもの？ | ゼロショット汎用性と高い効率を両立させた、軽量な単眼深度推定ネットワークです。パラメータ数6.1Mという非常にコンパクトな設計ながら、大規模な教師モデル（Depth Anything v2）の知識蒸留により、多様な環境下でリアルタイムな深度推定を実現します。 |
| 先行研究と比べてどこがすごい？ | 従来手法は「高精度だが計算コストの高い大規模モデル」か「軽量だが特定ドメインに縛られ汎用性の低い自己教師ありモデル」の二極化に陥っていましたが、本手法は両者のギャップを埋め、モバイルやエッジデバイス上で実用的な精度とリアルタイム性を両立させた点です。 |
| 技術や手法のキモはどこ？ | 再構成可能な（Reparameterizable）エンコーダによる階層的な特徴抽出、ハードウェア適応型の凸型アップサンプリング（Convex Upsampling）、および大規模なマルチドメインデータセットを用いた知識蒸留手法の組み合わせです。 |
| どうやって有効だと検証した？ | 5つのゼロショット深度推定ベンチマーク（NYUv2, KITTI, ETH3D, ScanNet, DIODE）と9つのハードウェアプラットフォームを用いて評価し、計算コストに対する精度で従来の軽量モデルを圧倒する性能を示しました。 |
| 議論はある？ | 軽量モデルゆえの限界として、ビデオ入力におけるフレーム間の時間的一貫性の欠如が挙げられます。また、パラメータ数が劇的に多い基盤モデルと比較すると、絶対的な精度にはまだ差があることが認められています。 |
| 次に読むべき論文は？ | [Depth Anything v2](https://arxiv.org/abs/2406.07514), [RepVGG](https://arxiv.org/abs/2101.03697), [Depth Pro](https://arxiv.org/abs/2410.02073) |
| PDFリンク | https://arxiv.org/pdf/2607.08771v1 |
