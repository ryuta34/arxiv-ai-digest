---
title: "PerturbRx: Learning Treatment-Conditioned Latent Transitions for Patient Drug Response Prediction"
date: 2026-08-24
arxiv_id: 2608.21349v1
url: http://arxiv.org/abs/2608.21349v1
---

# PerturbRx: Learning Treatment-Conditioned Latent Transitions for Patient Drug Response Prediction

| 項目 | 内容 |
|---|---|
| どんなもの？ | 単一細胞の摂動データを用いて薬物投与による分子状態の「潜在的な遷移」を学習し、それを患者の治療前分子プロファイルに転移させることで、がん患者の薬物応答を予測するフレームワーク「PerturbRx」を提案した論文。 |
| 先行研究と比べてどこがすごい？ | 既存手法は治療前の分子プロファイルのみを用いて予測を行っていたが、本手法は薬物による分子の「変化の方向と大きさ」を明示的にモデル化して予測に組み込むことで、予測性能を大幅に向上させた点。 |
| 技術や手法のキモはどこ？ | 薬物と用量に条件付けられた遷移予測器を、コンテキストが一致した未対の単一細胞の対照・処置群データから事前学習し、学習済みモデルを凍結した状態で患者データに適用する二段階フレームワークを採用している点。 |
| どうやって有効だと検証した？ | TCGA（臨床）および患者由来異種移植（PDX）の3つのベンチマークを用いて評価し、ベースラインと比較して最高性能を達成。また、アブレーションスタディにより、予測された遷移情報が予測性能向上に寄与していることを確認した。 |
| 議論はある？ | 薬物ごとの予測性能に不均一性があることや、化学的な類似性が必ずしも予測性能の向上に直結しないこと、および単一細胞データと臨床用RNA-seqの間のドメインギャップなどが課題として挙げられている。 |
| 次に読むべき論文は？ | [Tahoe-100M (Zhang et al., 2025)](https://arxiv.org/pdf/2502.xxxx), [DeepSADR (Zhang et al., 2026)](https://openreview.net/forum?id=jrFJWpDZvq), [WISER (Shubham et al., 2024)](https://arxiv.org/abs/2405.04078) |
| PDFリンク | https://arxiv.org/pdf/2608.21349v1 |
