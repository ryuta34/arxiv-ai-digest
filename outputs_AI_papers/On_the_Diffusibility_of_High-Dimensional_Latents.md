---
title: "On the Diffusibility of High-Dimensional Latents"
date: 2026-09-24
arxiv_id: 2609.28473v1
url: http://arxiv.org/abs/2609.28473v1
---

# On the Diffusibility of High-Dimensional Latents

| 項目 | 内容 |
|---|---|
| どんなもの？ | 高次元で再構成性能を重視して調整された特徴空間（Latent Space）において、拡散モデルの学習効率を改善する手法。標準的な速度予測（v-prediction）の代わりに、クリーンなデータを直接予測する「x0-prediction」を採用することで、高次元特有の最適化の困難さを解決した。 |
| 先行研究と比べてどこがすごい？ | 再構成性能を高めるためにエンコーダを微調整すると、特徴量が低次元空間に収縮（次元の崩壊）し、標準的なv-predictionの学習効率が低下する問題を発見した。x0-predictionを用いることで、この高次元空間での無駄なノイズ成分への回帰を避け、モデルの収束を加速させ、生成品質を向上させた点。 |
| 技術や手法のキモはどこ？ | 特徴空間においてデータが低次元多様体に集中しているという性質を利用し、速度予測からクリーンデータ予測へと目的関数を切り替えた点。これにより、モデルが多様体外の無情報な直交ノイズ成分を学習する必要がなくなり、最適化が効率化される。 |
| どうやって有効だと検証した？ | 複数の強力な再構成エンコーダ（微調整済みDINOv2-L、MAE-RAE）を使用し、GenEval、DPG-Bench、COCO-30k FIDなどのベンチマークで評価した。定量的指標および視覚的な比較において、v-predictionよりも優れた生成品質と構造的整合性を示した。 |
| 議論はある？ | 再構成性能（PSNR）を追及すると理解能力（Linear Probing精度）が低下する傾向があり、両立させることは今後の研究課題である。また、非常に高次元な空間での生成は、依然として低次元ボトルネックよりも計算コストや学習難易度の課題が残る。 |
| 次に読むべき論文は？ | [1] [AlignTok: Aligning visual foundation encoders to tokenizers for diffusion models](https://arxiv.org/abs/2509.25162)<br>[2] [Scaling text-to-image diffusion transformers with representation autoencoders](https://arxiv.org/abs/2601.16208)<br>[3] [Back to basics: Let denoising generative models denoise](https://arxiv.org/abs/2511.13720) |
| PDFリンク | https://arxiv.org/pdf/2609.28473v1 |
