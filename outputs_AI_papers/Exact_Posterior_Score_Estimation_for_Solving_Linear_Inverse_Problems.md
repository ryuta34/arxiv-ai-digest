---
title: "Exact Posterior Score Estimation for Solving Linear Inverse Problems"
date: 2026-06-16
arxiv_id: 2606.17048v1
url: http://arxiv.org/abs/2606.17048v1
---

# Exact Posterior Score Estimation for Solving Linear Inverse Problems

| 項目 | 内容 |
|---|---|
| どんなもの？ | 線形逆問題（インペインティング、超解像、デブラリング等）を解くための、高精度かつ効率的な事後分布サンプリング手法。拡散モデルの学習済みデノイザーを直接利用しつつ、線形ガウス逆問題の事後分布スコアを正確に推定する。 |
| 先行研究と比べてどこがすごい？ | 勾配ベースの近似手法（DPS等）が抱える近似誤差を排除し、厳密な事後分布スコアを導出した点。学習済みモデルの入力を変更するだけで済むため、追加の勾配計算や投影が不要で、極めて少ないサンプリングステップ数（NFE）で高品質な結果を得られる。 |
| 技術や手法のキモはどこ？ | 線形ガウス逆問題における事後分布のスコアが、測定結果を考慮した「事後分布のピボット（$\mu_\star$）」と「異方性ノイズ共分散（$\Sigma_\star$）」を用いたデノイジング問題に帰着することを示した「Exact Posterior Score (EPS)」の導出。 |
| どうやって有効だと検証した？ | ImageNet-64およびFFHQ-64を用いた5つの線形逆問題で、DPS、DDNM、Palette等の既存手法と比較評価。PSNR、FID、CRPS等の指標において、少ないサンプリング計算量（NFE）で一貫して優れた性能を達成した。 |
| 議論はある？ | 線形観測モデルとガウスノイズを前提としているため、非線形オペレーターへの適用には工夫が必要。また、学習時のノイズ統計量とテスト時のノイズレベルが大きく乖離する場合、ピボットの精度が低下する可能性がある。 |
| 次に読むべき論文は？ | [17] Karras et al., "Elucidating the design space of diffusion-based generative models" (本手法のバックボーン) <br> [18] Chung et al., "Diffusion posterior sampling for general noisy inverse problems" (代表的な比較対象手法) |
| PDFリンク | https://arxiv.org/pdf/2606.17048v1 |
