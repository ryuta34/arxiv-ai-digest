---
title: "From Corpora to Co-Evolving Capabilities: Capability-Centric Data Design for Generalist Image Generation"
date: 2026-08-19
arxiv_id: 2608.18076v1
url: http://arxiv.org/abs/2608.18076v1
---

# From Corpora to Co-Evolving Capabilities: Capability-Centric Data Design for Generalist Image Generation

| 項目 | 内容 |
|---|---|
| どんなもの？ | 一般的な画像生成モデルに向けた、能力主導型（Capability-Centric）のデータ構築インフラストラクチャを提案する論文。タスク固有の独立したデータセットを構築する従来手法とは異なり、生成能力の依存関係に基づいた専門的なデータエンジンと、段階的なカリキュラム学習を組み合わせた統合的なパイプラインを実現している。 |
| 先行研究と比べてどこがすごい？ | 個別のデータセット作成ではなく、「能力の獲得順序」に基づいたデータ設計に焦点を当てた点。T2I生成、画像編集、知識グラウンディングを相互運用可能なエンジンで管理し、共通のキャプション手法によりタスク間で概念を転用することで、小規模なデータセットでも効率的に一般化能力を向上させる。 |
| 技術や手法のキモはどこ？ | ①T2I、編集、知識という3つの専門的かつ相互運用可能なデータエンジン、②モデルの能力進化と連動してタスク構成や解像度を動的に制御する5段階のカリキュラム学習、③失敗ケースを評価して次ステップのデータ構築にフィードバックするアクティブ学習ループ。 |
| どうやって有効だと検証した？ | 3Bおよび6BスケールのMM-DiTモデルをスクラッチで学習し、実画像編集ベンチマーク「CPI-Bench」での定量的評価を実施。また、多様な画像生成および編集タスクを通じた定性的評価により、広範な視覚的網羅性と、タスクを跨いだ効果的な転移学習の有効性を実証した。 |
| 議論はある？ | データ構築の自動化には成功しているが、依然として高品質な合成データやエキスパートによる微調整が必要であり、特定のドメイン知識への偏りが生じる可能性がある。また、フィードバックループにおいて計算リソースの最適化が今後の課題となる。 |
| 次に読むべき論文は？ | [13] Emerging properties in unified multimodal pretraining, [26] Seedream 4.0: Toward next-generation multimodal image generation, [37] Dreamomni: Unified image generation and editing |
| PDFリンク | https://arxiv.org/pdf/2608.18076v1 |
