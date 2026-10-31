---
title: "Read, Allocate, Route: Role-Coupled Tokenization for Pixel-Space Generative Transformers"
date: 2026-10-31
arxiv_id: 2610.40647v1
url: http://arxiv.org/abs/2610.40647v1
---

# Read, Allocate, Route: Role-Coupled Tokenization for Pixel-Space Generative Transformers

| 項目 | 内容 |
|---|---|
| どんなもの？ | 画素空間での画像生成を行うTransformerにおいて、トークンを「空間アンカー」と「スペクトルスロット」に分離することで、計算コストを抑えつつ高精細な生成を可能にする手法。出力の詳細度とグローバルな通信量を独立して制御できるのが特徴。 |
| 先行研究と比べてどこがすごい？ | 従来手法（JiT等）では、パッチサイズを小さくするとトークン数が増え、グローバルアテンションの計算コストが二次的に増大していた。本手法では、低周波成分（グローバルな構造）のみをグローバル通信させ、高周波成分（局所的な詳細）はローカルで処理するため、計算効率を大幅に向上させつつ高品質な生成を実現した点。 |
| 技術や手法のキモはどこ？ | Read、Allocate、Routeの3段階による構成。空間アンカーで入力を読み取り、各アンカーを複数のスペクトルスロットに展開し、最低周波数のスロットのみをグローバル通信（キャリア）として扱い、それ以外はローカル処理する「GGLL（Global-Global-Local-Local）アテンション」を採用したこと。 |
| どうやって有効だと検証した？ | ImageNet-256/512およびテキスト画像生成において評価。JiT等のベースラインと比較し、同等のFLOPsでより低いFIDスコアを達成し、特に高解像度での改善幅が大きいことを確認。また、サンプリング速度の向上も実証。 |
| 議論はある？ | K（スペクトルスロット数）を増やすと、教師強制によるフィッティングは改善するが、必ずしも情報量が増えるわけではないという「割り当てのスイートスポット」が存在する。また、空間アンカー密度とスペクトル細分化の最適なバランスは今後も探求が必要。 |
| 次に読むべき論文は？ | [1] [Back to basics: Let denoising generative models denoise](https://arxiv.org/abs/2511.13720), [9] [Show the signal, hide the noise: Spectral forcing for pixel-space diffusion](https://arxiv.org/abs/2606.15236), [13] [Flow straight and fast: Learning to generate and transfer data with rectified flow](https://arxiv.org/abs/2209.03003) |
| PDFリンク | https://arxiv.org/pdf/2610.40647v1 |
