---
title: "Personalized RewardBench: Evaluating Reward Models with Human Aligned Personalization"
date: 2026-04-09
arxiv_id: 2604.07343v1
url: http://arxiv.org/abs/2604.07343v1
---

# Personalized RewardBench: Evaluating Reward Models with Human Aligned Personalization

| 項目 | 内容 |
|---|---|
| どんなもの？ | ユーザーの過去の履歴や個人的な好みを考慮し、個別のニーズに合わせて最適化された報酬モデルを評価するための新しいベンチマーク「Personalized RewardBench」を提案しています。単なる一般的な品質の評価ではなく、ユーザーごとのRubric（規準）に基づいた厳密な選好アラインメントを測定します。 |
| 先行研究と比べてどこがすごい？ | 既存のベンチマークが一般的な回答品質に偏っているのに対し、本手法はユーザーの過去の投稿に基づいた「個人的な規準」を明示的に統合しています。また、既存手法よりも downstream タスク（BoNやPPO）でのポリシー性能と報酬モデルの評価スコアが強く相関していることを証明しました。 |
| 技術や手法のキモはどこ？ | ユーザーの履歴から「個人用プロファイル」を抽出し、それに基づいた「Rubric Aspects（ユーザーの期待事項）」を生成するプランナーモジュールを導入した点です。これにより、単なる検索ではなく、文脈に応じた個人的な嗜好を報酬モデルが正確に推論できるように設計されています。 |
| どうやって有効だと検証した？ | LaMP-QAデータセットを用いた3つの高分散ドメインで実験を行い、最新の報酬モデルの性能を比較しました。また、Best-of-NサンプリングおよびPPO強化学習を通じて、提案ベンチマークが実際にポリシーの改善に寄与するかの相関性をNDCGやSpearmanのρ等の指標で検証しました。 |
| 議論はある？ | ユーザープロファイルの抽出におけるプランナーの精度に依存する点や、さらなる高度な個性化アルゴリズムの開発が将来課題として挙げられています。また、本研究で用いた手法はDemonstration（実証）としての側面が強く、モデル自体のアーキテクチャ改良の余地があります。 |
| 次に読むべき論文は？ | 1. [RewardBench (Lambert et al., 2025)](https://arxiv.org/abs/2501.17559) <br> 2. [LaMP-QA (Salemi & Zamani, 2025)](https://arxiv.org/abs/2506.00137) <br> 3. [PersonalRewardBench (Ryan et al., 2025)](https://arxiv.org/abs/2502.08045) |
| PDFリンク | [https://arxiv.org/pdf/2604.07343v1](https://arxiv.org/pdf/2604.07343v1) |
