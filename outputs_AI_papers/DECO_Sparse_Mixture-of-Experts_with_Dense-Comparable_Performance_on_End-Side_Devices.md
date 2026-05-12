---
title: "DECO: Sparse Mixture-of-Experts with Dense-Comparable Performance on End-Side Devices"
date: 2026-05-12
arxiv_id: 2605.10933v1
url: http://arxiv.org/abs/2605.10933v1
---

# DECO: Sparse Mixture-of-Experts with Dense-Comparable Performance on End-Side Devices

| 項目 | 内容 |
|---|---|
| どんなもの？ | エッジデバイスでの展開に適した、高効率な疎な混合エキスパート（MoE）アーキテクチャ「DECO」を提案。同じ総パラメータ予算と学習トークン数で、密な（Dense）モデルと同等の性能を実現した。 |
| 先行研究と比べてどこがすごい？ | 従来のMoEが抱えていた計算コストとストレージ容量のトレードオフを解消し、ReLUベースのルーティングとNormSiLUの採用により、高い推論精度と最大3.00倍の高速化を両立させた点。 |
| 技術や手法のキモはどこ？ | ReLUベースの柔軟なルーティング、専門家ごとの出力規模を調整する「学習可能なエキスパート別スケーリング」、およびReLU使用時の不安定さを解消する二段階正規化手法「NormSiLU」の導入。 |
| どうやって有効だと検証した？ | 0.11B〜1.18Bの4種類のモデルスケールで、Denseモデルおよび既存のMoE手法（DeepSeek-V3等）と性能比較を実施。推論速度についてはNVIDIA RTX 4090およびJetson AGX上で評価。 |
| 議論はある？ | SFT（教師あり微調整）やRL（強化学習）段階での不安定性の可能性や、学習データの異質性が高い場合に真価を発揮するため、データ構成による性能差のさらなる検証が課題。 |
| 次に読むべき論文は？ | [DeepSeek-V3](https://arxiv.org/pdf/2412.19437)、[ReMoE](https://arxiv.org/pdf/2412.14711)、[BlockFFN](https://arxiv.org/pdf/2507.08771) |
| PDFリンク | https://arxiv.org/pdf/2605.10933v1 |
