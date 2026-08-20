---
title: "Finetuning Strategies for Querying Sounds by Vocal Imitation"
date: 2026-08-20
arxiv_id: 2608.19174v1
url: http://arxiv.org/abs/2608.19174v1
---

# Finetuning Strategies for Querying Sounds by Vocal Imitation

| 項目 | 内容 |
|---|---|
| どんなもの？ |  AES-AIMLA 2025 ChallengeにおけるQuery by Vocal Imitation（声の模倣による音響検索）の優勝手法を報告した技術レポート。二つの異なるニューラルネットワークベースの微調整戦略を提案し、音声模倣と参照音の橋渡しを実現した。 |
| 先行研究と比べてどこがすごい？ | 既存のMobileNetV3ベースの手法を強化し、学習済みのCED（Consistent Ensemble Distillation）モデルの活用や、VocalSketchデータセットを用いた「半硬ネガティブ（semi-hard negative）」の三つ組学習（triplet learning）を導入することで、検索精度を大幅に向上させた。 |
| 技術や手法のキモはどこ？ | 手法1では凍結したCEDエンコーダーによる軽量な微調整、手法2ではMobileNetV3を用いた対照学習と三つ組学習のハイブリッド構成を採用。特に三つ組学習において、学習の不安定化を防ぐための動的な重み付け戦略と、クラスラベルに基づいたネガティブサンプリングを導入した点。 |
| どうやって有効だと検証した？ | QVIM 2025の公式検証セット（qvim-dev）を用い、MRR（Mean Reciprocal Rank）とNDCG指標で評価。ベースライン（Greif et al.）と比較し、提案手法が検索性能で上回ることを実証した。 |
| 議論はある？ | 本報告では手法の有効性が示されたが、異なるデータセットへの汎用性や、極めて短時間あるいは未知の音響クラスに対する堅牢性の向上などが、今後の課題として示唆されている。 |
| 次に読むべき論文は？ | [1] J. Greif et al., "[Improving query-by-vocal imitation with contrastive learning and audio pretraining](https://arxiv.org/abs/2406.19174)" (本手法のベースライン) |
| PDFリンク | https://arxiv.org/pdf/2608.19174v1 |
