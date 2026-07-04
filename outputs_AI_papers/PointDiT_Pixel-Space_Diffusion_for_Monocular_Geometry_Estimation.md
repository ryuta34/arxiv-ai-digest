---
title: "PointDiT: Pixel-Space Diffusion for Monocular Geometry Estimation"
date: 2026-07-04
arxiv_id: 2607.02515v1
url: http://arxiv.org/abs/2607.02515v1
---

# PointDiT: Pixel-Space Diffusion for Monocular Geometry Estimation

| 項目 | 内容 |
|---|---|
| どんなもの？ | 単一のRGB画像から高精細な3Dポイントマップを予測する、ミニマリストなピクセル空間拡散Transformerモデル。VAEなどの複雑なアーキテクチャや損失関数を排除し、単純なViTベースの拡散モデルで高品質な幾何学的再構成を実現した。 |
| 先行研究と比べてどこがすごい？ | VAEによる潜在空間への圧縮を行わないため、情報の損失を防ぎ、特に透明な物体や薄い構造物に対して非常に鋭い幾何学的境界を生成できる。また、推論時に1ステップで competitive な結果が得られ、既存の潜在拡散モデルより計算効率が高い。 |
| 技術や手法のキモはどこ？ | 学習済みのDINOv3を条件付け（コンディショニング）に利用し、ピクセル空間で直接拡散モデルを訓練する設計。特に、推論安定性と画質向上に寄与する「clean point map（x-prediction）」を直接予測する目的関数と、スカイ処理や相対的な点誤差損失の導入が鍵。 |
| どうやって有効だと検証した？ | DIODE、KITTI、NYUv2など7つの実世界のデータセットを用いたゼロショット評価を実施。従来の決定論的回帰モデルや潜在拡散モデル（GeometryCrafter等）と比較し、BF1（境界の鋭さ）などで最高性能を達成した。 |
| 議論はある？ | 現在は固定解像度での学習に限定されていることや、一部の屋外シーンで回帰ベースの既存手法に劣る場合がある。今後は混合解像度学習への対応や、より多様な屋外データを用いたスケーリングが課題。 |
| 次に読むべき論文は？ | [JiT: Back to basics: Let denoising generative models denoise (Li & He, 2026)](https://arxiv.org/abs/2601.12345 ※想定リンク) や、[GeometryCrafter (Xu et al., 2025b)](https://arxiv.org/abs/2501.00000 ※想定リンク) |
| PDFリンク | https://arxiv.org/pdf/2607.02515v1 |
