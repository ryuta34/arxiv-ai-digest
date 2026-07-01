---
title: "GEAR: Guided End-to-End AutoRegression for Image Synthesis"
date: 2026-07-01
arxiv_id: 2606.32039v1
url: http://arxiv.org/abs/2606.32039v1
---

# GEAR: Guided End-to-End AutoRegression for Image Synthesis

| 項目 | 内容 |
|---|---|
| どんなもの？ | 画像生成モデルにおいて、VQトークナイザーと自己回帰（AR）生成器をエンドツーエンドで学習する「GEAR」という手法。従来の手法とは異なり、学習中のトークナイザーをAR生成器が最適化するように導くことで、生成の高速化と品質向上を実現した。 |
| 先行研究と比べてどこがすごい？ | 従来はトークナイザーを固定して生成器を学習するのが一般的だったが、GEARはARモデルの生成目的に合わせてトークナイザーを能動的に調整できる。これにより、LlamaGen-REPAと比較してImageNetでの収束速度を最大10倍高速化し、より局所的で空間的一貫性のあるパッチレベルの学習が可能になった。 |
| 技術や手法のキモはどこ？ | 非微分な離散インデックスによる勾配消失問題を、ハード（離散）とソフト（連続・温度付き）の二重読み出し構造で解決した点。ソフトブランチを経由して表現アライメント損失を流すことで、生成器の性能を最大化するようなインデックスの分布へとトークナイザーを誘導できる。 |
| どうやって有効だと検証した？ | ImageNet-1Kにおけるクラス条件付き画像生成および、GPICデータセットを用いたテキスト・トゥ・イメージ生成で検証。gFID（生成FID）の収束速度や品質、またモデルサイズを変えた際のスケール則や各種量子化器（VQVAE, LFQ, IBQ）での汎用性について広範な比較実験を行った。 |
| 議論はある？ | トークナイザーの再構成性能（画質）と、ARモデルの生成のしやすさのトレードオフが存在する。また、現状のVQ-ARパイプラインは圧縮率とシーケンス長が固定されているため、今後はより柔軟なパッチ化やマルチトークン予測を取り入れ、シーケンス長を抑えつつ再構成精度を高める必要がある。 |
| 次に読むべき論文は？ | [LlamaGen: Autoregressive model beats diffusion](https://arxiv.org/abs/2406.06525)、[REPA: Representation alignment for generation](https://arxiv.org/abs/2410.06940)、[VQ-VAE: Neural discrete representation learning](https://arxiv.org/abs/1711.00937) |
| PDFリンク | https://arxiv.org/pdf/2606.32039v1 |
