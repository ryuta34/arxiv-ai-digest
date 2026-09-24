---
title: "Contrastive Learning for Authorship Verification"
date: 2026-09-24
arxiv_id: 2609.28471v1
url: http://arxiv.org/abs/2609.28471v1
---

# Contrastive Learning for Authorship Verification

| 項目 | 内容 |
|---|---|
| どんなもの？ | 著者検証（authorship verification）タスクにおいて、分類ベースのアプローチよりも対照学習（contrastive learning）が優れていることを示した研究。ModernBERT Bi-Encoderを用いることで、PAN21のタスクにおいて98.4%という高精度を達成した。 |
| 先行研究と比べてどこがすごい？ | 従来明確でなかった「分類」と「対照学習」の比較を、モデルや学習条件を揃えた上で体系的に評価した。また、4096トークンという長いコンテキストを扱うことで、既存のState-of-the-artを上回る性能を実現した。 |
| 技術や手法のキモはどこ？ | 各テキストを独立して埋め込み、コサイン類似度で判定するBi-Encoderアーキテクチャを採用し、InfoNCE損失関数で学習させた点。また、入力のランダムテキスト回転（データ拡張）や、モデルの幅に応じた学習率の調整（μTransfer）が性能向上に寄与している。 |
| どうやって有効だと検証した？ | PAN21のデータセットを用い、TinyBERTからModernBERT-largeまでの様々なアーキテクチャで、分類モデルと対照学習モデルを比較評価した。さらに、損失関数、データ拡張、コンテキスト長の増大によるアブレーション研究を実施した。 |
| 議論はある？ | 計算の効率性やデータ拡張の有効性は確認されたが、本手法が他のタスク（著者属性予測やスタイル変化検知など）でどの程度汎用性があるかは今後の課題としている。 |
| 次に読むべき論文は？ | [SimCSE](https://aclanthology.org/2021.emnlp-main.552/)、[ModernBERT](https://aclanthology.org/2025.acl-long.127/)、[InfoNCE](https://arxiv.org/abs/1807.03748) |
| PDFリンク | https://arxiv.org/pdf/2609.28471v1 |
