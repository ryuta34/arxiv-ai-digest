---
title: "Discriminative World Models for Web Agents"
date: 2026-09-03
arxiv_id: 2609.02885v1
url: http://arxiv.org/abs/2609.02885v1
---

# Discriminative World Models for Web Agents

| 項目 | 内容 |
|---|---|
| どんなもの？ | ウェブエージェントの意思決定を支援する新しい世界モデル（World Model）の訓練手法。指定された行動が引き起こす結果を、他の代替行動による結果と明確に区別できるように表現を学習させる。 |
| 先行研究と比べてどこがすごい？ | 従来の固定フォーマット（HTMLやアクセシビリティツリー等）の再現を求める学習と異なり、行動の帰結を「識別する」ことに最適化された表現を生成できる。また、少ない計算リソースとデータ量で既存手法を上回る精度を実現した。 |
| 技術や手法のキモはどこ？ | 特定のフォーマットを強制しない「Predicted-state matching」という学習目的の導入。WebArenaから分岐（Branching）したデータセットを構築し、生成された表現が「正解の状態」を「代替の状態」から判別できるかを判定する仕組みを採用した。 |
| どうやって有効だと検証した？ | 独自の「predicted-state matching」ベンチマークで高い識別精度を確認し、WebPRMBenchを用いたアクションランキングのタスクで性能向上を実証。さらにWebArena-Lite上でのエージェントのタスク成功率改善を評価した。 |
| 議論はある？ | 評価が言語モデルによる判断（ジャッジ）に依存している点や、分岐データが網羅的ではない点が挙げられる。また、モデルの評価はベンチマーク環境に限定されており、実環境での安全性や汎用性については今後の課題としている。 |
| 次に読むべき論文は？ | [Web-Shepherd: Advancing PRMs for Reinforcing Web Agents](https://arxiv.org/abs/2505.15277), [WebWorld: A Large-scale World Model for Web Agent Training](https://arxiv.org/abs/2602.14721) |
| PDFリンク | https://arxiv.org/pdf/2609.02885v1 |
