---
title: "OmniVBench: A Benchmark and Large-Scale Dataset for Omni Reference-to-Video Generation"
date: 2026-09-21
arxiv_id: 2609.22069v1
url: http://arxiv.org/abs/2609.22069v1
---

# OmniVBench: A Benchmark and Large-Scale Dataset for Omni Reference-to-Video Generation

| 項目 | 内容 |
|---|---|
| どんなもの？ | 参照ベースの動画生成（R2V）モデルを評価するための広範なベンチマーク「OmniVBench」と、産業グレードのトレーニングデータセット「Omni-R2V」を提案した研究。7つのタスクファミリーと18のサブタスクをカバーし、因数分解された因子ベースの評価プロトコルを導入している。 |
| 先行研究と比べてどこがすごい？ | 既存研究がコンテンツ中心の評価にとどまっていたのに対し、本研究はモーション、スタイル、構造、物語、多重参照を含む多様な側面で細分化された評価を可能にした点。また、340K件の高品質なデータセットを提供し、モデルの性能差を明確化する評価枠組みを構築した点。 |
| 技術や手法のキモはどこ？ | 各評価ケースを「因数分解（factor-grounded）」されたチェックリストに分解し、参照因子の忠実度、命令実現能力（解きほぐしとルーティング）、動画品質の3軸で厳密に評価する手法。さらに、専門的な動画ソースを用いた自動パイプラインによる効率的なデータ構築。 |
| どうやって有効だと検証した？ | 主要なオープンソース・クローズドソースモデルを広範に評価し、性能ギャップを可視化した。また、100のケースで人手評価を行い、提案した因数分解チェックリスト評価が、従来のホリスティックな評価よりも人手による評価と高い相関を持つことを実証した。 |
| 議論はある？ | 現在のモデルはコンテンツ参照には強いが、モーションや物語性、多重参照における因子の分離とルーティング能力に依然として課題があることを明らかにした。また、特定の参照条件での成功が他へ転移するとは限らないというモデルの限界を示唆した。 |
| 次に読むべき論文は？ | 1. [OmniWeaving: Towards unified video generation with free-form composition and reasoning](https://arxiv.org/abs/2603.24458)<br>2. [Univbench: Towards unified evaluation for video foundation models](https://arxiv.org/abs/2605.25654)<br>3. [OpenS2V-Nexus: A detailed benchmark and million-scale dataset for subject-to-video generation](https://arxiv.org/abs/2506.18851) |
| PDFリンク | https://arxiv.org/pdf/2609.22069v1 |
