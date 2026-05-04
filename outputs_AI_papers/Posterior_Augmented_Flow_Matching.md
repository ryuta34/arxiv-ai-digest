---
title: "Posterior Augmented Flow Matching"
date: 2026-05-04
arxiv_id: 2605.00825v1
url: http://arxiv.org/abs/2605.00825v1
---

# Posterior Augmented Flow Matching

| 項目 | 内容 |
|---|---|
| どんなもの？ | フローマッチング（FM）の学習における疎な教師信号と高分散な勾配の問題を解決する「Posterior-Augmented Flow Matching (PAFM)」を提案した。単一のターゲットのみに依存する従来のFMを拡張し、中間状態から到達可能な複数のターゲットの事後分布に基づいた期待値で学習する手法である。 |
| 先行研究と比べてどこがすごい？ | 学習時に単一のターゲットではなく、事後確率で重み付けされた複数のターゲット集合から情報を集約するため、勾配の分散を大幅に低減できる。その結果、モデルの崩壊（flow collapse）を防ぎ、学習の安定性と生成品質（FID指標など）を大幅に向上させた。 |
| 技術や手法のキモはどこ？ | インポータンスサンプリングを用いて、中間点から導出される事後分布（条件付き確率とターゲットの尤度の積）を近似し、複数の候補ターゲットに対して同時に勾配を計算する点。追加計算コストを抑えつつ、FMの学習目的関数の不偏推定量として機能するように設計されている。 |
| どうやって有効だと検証した？ | ImageNet-1K（クラス条件付き）およびCC12M（テキスト条件付き）を用い、SiTやMMDiTといった多様なモデル構成で評価を行った。FIDスコアで最大3.4の改善が見られ、勾配分散の低減や計算オーバーヘッドが極めて小さいことを示した。 |
| 議論はある？ | テキスト条件付けにおける条件尤度の近似には簡便な手法を用いているため、より洗練された近似手法の検討が将来の課題である。また、ターゲット候補を選択するアルゴリズム（近傍探索やVAEサンプリングなど）の最適化は、アプリケーションやタスクごとに依存する。 |
| 次に読むべき論文は？ | [17] Flow matching for generative modeling (Lipman et al., 2023) [https://openreview.net/forum?id=PqvMRDCJT9t]、[19] SiT: Exploring flow and diffusion-based generative models with scalable interpolant transformers (Ma et al., 2024) [https://doi.org/10.1007/978-3-031-72980-5_2] |
| PDFリンク | https://arxiv.org/pdf/2605.00825v1 |
