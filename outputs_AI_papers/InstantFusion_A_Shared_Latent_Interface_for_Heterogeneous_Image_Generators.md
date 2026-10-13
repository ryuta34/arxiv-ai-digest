---
title: "InstantFusion: A Shared Latent Interface for Heterogeneous Image Generators"
date: 2026-10-13
arxiv_id: 2610.13944v1
url: http://arxiv.org/abs/2610.13944v1
---

# InstantFusion: A Shared Latent Interface for Heterogeneous Image Generators

| 項目 | 内容 |
|---|---|
| どんなもの？ | 異なるアーキテクチャを持つ複数の画像生成モデル間で、中間的な潜在状態やデノイズ過程を相互に転送・接続するための軽量な共有潜在インターフェース「InstantFusion」です。これにより、モデル間の組成、加速、知識蒸留、報酬最適化などが可能になります。 |
| 先行研究と比べてどこがすごい？ | 既存手法がモデルペアごとの専用マッピングを必要とし、動的な生成プロセスを考慮していなかったのに対し、モデル非依存の共通表現空間を構築することで、複数の異種モデルを柔軟に連結できます。 |
| 技術や手法のキモはどこ？ | モデルごとに固有のLatent AutoEncoder (LAE)を導入し、潜在状態を共通空間に投影・デコードする点と、潜在状態の整合性だけでなく、デノイズ速度（局所的な動特性）を明示的に同期させる学習手法にあります。 |
| どうやって有効だと検証した？ | SD3、FLUX.1、Qwen-Imageなどの代表的な生成モデルを用いた大規模な実験を行い、生成加速、クロスアーキテクチャ蒸留、マルチ報酬の組成において、ベースラインを上回る性能や効率的な推論を実現することを示しました。 |
| 議論はある？ | 現在は共通のVAEと時間パラメータ設定に依存しており、今後は異なるVAE間への拡張や、モデルの動的ロードに伴う計算リソースのオーバーヘッド削減が課題とされています。 |
| 次に読むべき論文は？ | [Flow Matching for generative modeling](https://arxiv.org/abs/2210.02747)、[T-stitch: Accelerating sampling in pre-trained diffusion models with trajectory stitching](https://arxiv.org/abs/2501.06103) |
| PDFリンク | https://arxiv.org/pdf/2610.13944v1 |
