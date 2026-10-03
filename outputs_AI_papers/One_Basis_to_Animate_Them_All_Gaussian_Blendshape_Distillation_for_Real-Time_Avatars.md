---
title: "One Basis to Animate Them All: Gaussian Blendshape Distillation for Real-Time Avatars"
date: 2026-10-03
arxiv_id: 2610.02207v1
url: http://arxiv.org/abs/2610.02207v1
---

# One Basis to Animate Them All: Gaussian Blendshape Distillation for Real-Time Avatars

| 項目 | 内容 |
|---|---|
| どんなもの？ | 既存の複雑なニューラル3D Gaussianアバターモデルの推論を高速化し、モバイルデバイス上でリアルタイム（60fps）でのアニメーションを可能にする蒸留手法「GALA」を提案した論文です。重いニューラルデコーダを、計算コストの低い線形ブレンド形状（Blendshape）ベースの表現に置き換えます。 |
| 先行研究と比べてどこがすごい？ | 個別の対象に対してモデルを最適化する従来の手法と異なり、学習済みモデルから身元（ID）非依存のブレンド形状基底を抽出し、未知の人物に対しても再利用可能です。これにより、CPUのアニメーション計算コストを最大3桁削減しつつ、元のレンダリング品質をほぼ維持できます。 |
| 技術や手法のキモはどこ？ | 学習済みモデルから残差を抽出し、レンダリング品質を考慮した指標に基づく「レンダリング重視のブロック局所PCA」を用いてブレンド形状基底を構築する点です。さらに、軽量なMLPを用いて、入力の表情・姿勢パラメータから適切な係数を予測することで、リアルタイム性を実現しています。 |
| どうやって有効だと検証した？ | 3つの既存のホストモデル（AGORA、FlexAvatar、DynaAvatar）に適用し、FFHQや4D-Dress等のベンチマークで定量・定性評価を行いました。また、モバイルブラウザ上で60fpsで動作するデモを通じて、計算効率とレンダリング品質のトレードオフを検証しています。 |
| 議論はある？ | 現在は空間分割が固定（32ブロック）されており、係数予測の精度に改善の余地があるとしています。また、将来的にアバターモデル自体を最初からID共通のブレンド形状基底を組み込んで学習するアプローチの可能性を示唆しています。 |
| 次に読むべき論文は？ | [3D Gaussian Splatting (Kerbl et al., 2023)](https://arxiv.org/abs/2308.04079), [FlexAvatar (Kirschstein et al., 2026)](https://arxiv.org/abs/2601.xxxx), [DynaAvatar (Kwon et al., 2026)](https://arxiv.org/abs/2601.xxxx) |
| PDFリンク | https://arxiv.org/pdf/2610.02207v1 |
