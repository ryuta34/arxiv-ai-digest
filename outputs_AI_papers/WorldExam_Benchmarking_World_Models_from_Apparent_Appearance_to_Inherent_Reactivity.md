---
title: "WorldExam: Benchmarking World Models from Apparent Appearance to Inherent Reactivity"
date: 2026-08-04
arxiv_id: 2608.02603v1
url: http://arxiv.org/abs/2608.02603v1
---

# WorldExam: Benchmarking World Models from Apparent Appearance to Inherent Reactivity

| 項目 | 内容 |
|---|---|
| どんなもの？ | 動画生成モデルを「世界モデル」として評価するための包括的な診断ベンチマーク「WorldExam」を提案した研究。見かけの映像品質だけでなく、シーン状態から推論される反応性（Inherent Reactivity）までを4段階のレベルで多角的に評価する。 |
| 先行研究と比べてどこがすごい？ | 従来は視覚的品質や明示的な指示の遵守（layout controlなど）に留まっていたのに対し、本研究ではモデルが明示的に指示されていないシーン条件に応じた反応や、目標達成のための詳細な実行プロセスまでを「世界モデル」の能力として定義し、包括的に評価する点。 |
| 技術や手法のキモはどこ？ | 1,474のテストケースを「Visual Quality」「Control Adherence」「Spatial Consistency」「World Reactivity」という4つの階層的レベルで構造化した点。また、カメラ・アクション・言語という異なる制御インターフェースを「atomic control units（原子的な制御単位）」にマッピングし、統一的なパイプラインで評価する仕組みを構築した点。 |
| どうやって有効だと検証した？ | カメラ駆動、アクション駆動、言語駆動の計20モデルを対象に、静的シーンと動的インタラクションの2トラックで評価。さらにVLM（GPT-5.5）を用いたチェックリスト評価の人間との相関（Spearman’s ρ=0.8614）を示すことで、評価指標の妥当性を検証した。 |
| 議論はある？ | 現在のベンチマーク能力はモデルインターフェースの制約に依存しており、動画生成器が内部的な因果表現を獲得しているかまでは検証できていない。また、商用モデルによるプロンプト増強が評価に影響する可能性も指摘されている。 |
| 次に読むべき論文は？ | [10] WorldScore: A unified evaluation benchmark for world generation, [14] VBench: Comprehensive benchmark suite for video generative models, [51] WorldRoamBench: An open-world benchmark for long-horizon stability of interactive world models |
| PDFリンク | https://arxiv.org/pdf/2608.02603v1 |
