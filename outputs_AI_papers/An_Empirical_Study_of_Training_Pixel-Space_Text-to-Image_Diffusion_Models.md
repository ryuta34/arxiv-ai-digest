---
title: "An Empirical Study of Training Pixel-Space Text-to-Image Diffusion Models"
date: 2026-08-18
arxiv_id: 2608.16887v1
url: http://arxiv.org/abs/2608.16887v1
---

# An Empirical Study of Training Pixel-Space Text-to-Image Diffusion Models

| 項目 | 内容 |
|---|---|
| どんなもの？ | 潜在空間（Latent-space）ではなく画素空間（Pixel-space）で直接学習・生成を行う拡散モデルのための、効率的な学習・推論手法を提案する研究。潜在空間で獲得した学習済み事前知識を活用し、画素空間へ段階的に移行する「Latent-to-pixel」学習戦略を確立した。 |
| 先行研究と比べてどこがすごい？ | 画素空間での直接学習が抱える収束の遅さという課題に対し、適切な設計選択（重み初期化、データ構成、予測対象など）を体系的に研究。これにより、潜在空間モデルと同等の品質を維持しつつ、デコーダを排除することで3.18倍〜4.75倍の推論高速化を実現した。 |
| 技術や手法のキモはどこ？ | 潜在空間で事前学習した重みを初期値として活用し、自己生成データと実画像を組み合わせた学習を行う点。さらに、画素空間に適したDiPデコーダの採用、ノイズスケールの最適化（γ=2）、および推論効率を上げるための段階的なパッチサイズ適応とステップ蒸留を組み合わせた点。 |
| どうやって有効だと検証した？ | Z-ImageおよびFLUX2-kleinという2つの大規模モデルファミリーを用い、GenEvalやDPG等の指標で性能を評価。潜在空間モデルや既存のLatent-to-pixel手法（L2P, AsymFlow）と比較し、品質を維持しつつ推論速度が大幅に向上することを実証した。 |
| 議論はある？ | 非常に大きなパッチサイズを適用すると細部の品質が劣化する傾向があり、極端なトークン圧縮下での詳細保持が今後の重要な課題。また、画素空間への移行時における分布シフトの解消には、理論的な解析だけでなく経験的なキャリブレーションが不可欠である。 |
| 次に読むべき論文は？ | [15] L2P: Unlocking latent potential for pixel generation, [43] Back to basics: Let denoising generative models denoise, [85] Pixeldit: Pixel diffusion transformers for image generation |
| PDFリンク | https://arxiv.org/pdf/2608.16887v1 |
