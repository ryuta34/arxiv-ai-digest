---
title: "SignRR: Retrieve and Refine Real Motion for Sign Language Production"
date: 2026-09-01
arxiv_id: 2608.28568v1
url: http://arxiv.org/abs/2608.28568v1
---

# SignRR: Retrieve and Refine Real Motion for Sign Language Production

| 項目 | 内容 |
|---|---|
| どんなもの？ | 手話生成のための「retrieve-and-refine（検索・洗練）」パラダイムを提案したフレームワーク「SignRR」。既存の生成モデルと検索ベース手法の弱点を補い、リアルな手話表現とシーケンス全体の整合性を両立させる。 |
| 先行研究と比べてどこがすごい？ | ゼロからの生成（ノイズやPriorから）で生じる不自然な手話動作と、単純な検索・連結で生じるリズムやスタイルの不整合という、二大パラダイムの課題を解決した点。 |
| 技術や手法のキモはどこ？ | Gloss（手話の単語ラベル）に基づき辞書から実際のセグメントを検索し、動的計画法で最適化した初期シーケンスを生成した後、「part-aware（部位ごとの）」Residual VQ-VAEを用いて全体の整合性を再洗練させる点。 |
| どうやって有効だと検証した？ | PHOENIX14TおよびCSL-Dailyデータセットを用い、逆翻訳（back-translation）メトリクス（WER, BLEU, ROUGE等）およびPose品質メトリクスで評価。既存のSOTA手法を上回る結果を示した。 |
| 議論はある？ | 現在は身体と手のみを扱っており、手話の文法的・語彙的意味を持つ表情や非手動信号を考慮できていない。今後は顔のストリーム追加や、Photorealisticなアバターへの統合を目指す。 |
| 次に読むべき論文は？ | [Sign Stitching](https://papers.bmvc2024.org/0721.pdf), [Sign-IDD](https://arxiv.org/abs/2502.13961), [G2P-DDM](https://arxiv.org/abs/2402.09117) |
| PDFリンク | https://arxiv.org/pdf/2608.28568v1 |
