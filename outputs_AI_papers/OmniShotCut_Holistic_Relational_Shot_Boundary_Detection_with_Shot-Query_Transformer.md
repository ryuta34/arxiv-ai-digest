---
title: "OmniShotCut: Holistic Relational Shot Boundary Detection with Shot-Query Transformer"
date: 2026-04-28
arxiv_id: 2604.24762v1
url: http://arxiv.org/abs/2604.24762v1
---

# OmniShotCut: Holistic Relational Shot Boundary Detection with Shot-Query Transformer

| 項目 | 内容 |
|---|---|
| どんなもの？ | 従来のショット境界検出（SBD）の曖昧さや限定的な定義を克服し、ショット内の関係性とショット間の関係性を統合的に予測する新しいショット境界検出モデル「OmniShotCut」を提案した論文。高品質な学習データセットを構築するための完全合成型のトランジション生成パイプラインと、現代の動画制作の多様性を反映した評価ベンチマーク「OmniShotCutBench」を導入している。 |
| 先行研究と比べてどこがすごい？ | 従来の3D CNNベースの手法が苦手としていた、急なカット（Sudden Jump）の検出や漸進的なトランジション（溶解、フェード等）の正確な境界定位において、State-of-the-art（SOTA）の性能を達成した。また、ショットの境界だけでなく、ショットの性質や前後関係を構造的に出力する点が新規。 |
| 技術や手法のキモはどこ？ | ショット境界検出をフレームインデックスの離散的な分類問題として再定式化し、クエリベースのビデオTransformerを用いることで、ショット範囲、ショット内関係、ショット間関係を単一の隠れ状態で統合的に最適化した点。また、大規模かつ正確なラベル付けが不要な合成学習データ生成戦略を採用した点。 |
| どうやって有効だと検証した？ | 提案したOmniShotCutBenchを用い、PySceneDetectやTransNetV2、AutoShotといった既存の代表的な手法と比較評価。特にトランジションのIoUとSudden Jumpの精度、分類の正確性において、提案手法が顕著に優れた性能を示すことを定量・定性的に証明した。 |
| 議論はある？ | 現在の合成生成パイプラインでは対応できない高度に芸術的・動的なトランジションが存在する点。また、複雑な映画的トランジションの表現には、より大規模な業界レベルのテンプレートコレクションが必要であり、それらが公開されていないことが限界であると述べている。 |
| 次に読むべき論文は？ | [TransNet V2](https://arxiv.org/abs/1906.03363)、[AutoShot](https://arxiv.org/abs/2303.02247)、[CoTracker3](https://arxiv.org/abs/2502.06013) |
| PDFリンク | https://arxiv.org/pdf/2604.24762v1 |
