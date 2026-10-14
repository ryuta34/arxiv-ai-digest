---
title: "LoopWAM: Closed-Loop Generalist Policy Improvement from Deployment Rollouts"
date: 2026-10-14
arxiv_id: 2610.18873v1
url: http://arxiv.org/abs/2610.18873v1
---

# LoopWAM: Closed-Loop Generalist Policy Improvement from Deployment Rollouts

| 項目 | 内容 |
|---|---|
| どんなもの？ | 成功・失敗を含む多様な品質のデプロイメント（実世界展開）データを活用し、一般化ロボットポリシーを継続的に改善するモデル「LoopWAM」です。世界モデルと行動生成を統合し、フィードバックループを通じて自律的に性能を向上させます。 |
| 先行研究と比べてどこがすごい？ | 従来のVLA（Vision-Language-Action）モデルが成功例の模倣に偏るのに対し、LoopWAMは失敗を含む全行動スペクトルから物理的帰結を学習します。行動と未来映像を並列デノイジングで生成し、事後評価なしで直接的にポリシーを改善できる点が優位です。 |
| 技術や手法のキモはどこ？ | ソース依存のノイズサンプリング、品質ステアリング（品質に応じた条件付け）、および失敗ケースを除外・成功例を強調する「品質重み付き監督」を組み合わせた統一学習フレームワークです。 |
| どうやって有効だと検証した？ | RoboChallenge Table30-V2における3段階の反復改善実験を行い、成功率を23.67%から43.33%へと向上させました。さらにRoboTwin 2.0およびRoboCasa365でも最高精度を達成しました。 |
| 議論はある？ | 現在はカメラ映像ベースの学習ですが、より複雑な物理的因果関係の理解や、長期間にわたるエージェントのドリフト（分布変化）に対する耐性、また人間による品質アノテーションの自動化が今後の課題です。 |
| 次に読むべき論文は？ | [FACT: Failure-Aware Causal Training for World-Action Models](https://arxiv.org/abs/2608.10232)、[LingBot-VA 2.0](https://arxiv.org/abs/2607.08639) |
| PDFリンク | https://arxiv.org/pdf/2610.18873v1 |
