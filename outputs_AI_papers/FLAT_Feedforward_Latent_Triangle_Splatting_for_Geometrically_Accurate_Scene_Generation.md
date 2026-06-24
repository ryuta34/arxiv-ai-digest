---
title: "FLAT: Feedforward Latent Triangle Splatting for Geometrically Accurate Scene Generation"
date: 2026-06-24
arxiv_id: 2606.24876v1
url: http://arxiv.org/abs/2606.24876v1
---

# FLAT: Feedforward Latent Triangle Splatting for Geometrically Accurate Scene Generation

| 項目 | 内容 |
|---|---|
| どんなもの？ | 単一の画像から、高品質でレンダリング可能な「三角形スプラット」による3Dシーンを直接生成するモデル「FLAT」です。従来のボリュメトリック（容積型）な表現とは異なり、ゲームエンジンで直接利用可能な幾何学的に正確な表面プリミティブを出力します。 |
| 先行研究と比べてどこがすごい？ | 従来の3D Gaussian Splatting（3DGS）等の手法が抱えていた「表面が不透明ではなく、グラフィックスパイプラインとの互換性が低い」という課題を解決しました。高品質な生成品質を維持しつつ、後処理によるメッシュ変換が容易で、幾何学的な正確さにおいて既存手法を大きく上回ります。 |
| 技術や手法のキモはどこ？ | 1. 安定した学習のための「レイ中心の三角形パラメータ化（Cholesky分解を用いた形状変換と残差回転の予測）」、2. 勾配流を改善するための「新しいプロダクト窓関数」を用いた微分可能なレンダリング手法、3. 既存のビデオ生成モデルのデコーダを再利用した軽量な設計。 |
| どうやって有効だと検証した？ | RealEstate10KおよびDL3DVデータセットを用い、既存の3DGSや2DGS手法と同一の学習条件下で比較を行いました。PSNR/SSIMといった画像品質評価に加え、法線マップの精度評価（コサイン類似度）を行い、幾何学的な忠実度において優位であることを示しました。 |
| 議論はある？ | 三角形プリミティブはPSNR等の画質指標の最適化が3DGSより難しく、非常に薄い物体や半透明領域のモデリングには依然として限界があります。また、生成されるメッシュは完全な閉曲面（Watertight）ではないため、今後より複雑な環境への拡張や幾何学的整合性の向上が課題です。 |
| 次に読むべき論文は？ | [Meshsplatting [24]](https://arxiv.org/abs/2512.06818)、[Wonderland [38]](https://arxiv.org/abs/2501.07166)、[3D Gaussian Splatting [33]](https://arxiv.org/abs/2308.04079) |
| PDFリンク | https://arxiv.org/pdf/2606.24876v1 |
