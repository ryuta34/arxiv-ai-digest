---
title: "DIRECT: When and Where Should You Allocate Test-Time Compute in Embodied Planners?"
date: 2026-06-11
arxiv_id: 2606.12402v1
url: http://arxiv.org/abs/2606.12402v1
---

# DIRECT: When and Where Should You Allocate Test-Time Compute in Embodied Planners?

| 項目 | 内容 |
|---|---|
| どんなもの？ | 視覚言語モデル（VLM）をロボットのプランナーとして利用する際に、タスクの難易度に応じて動的に最適なモデルや計算量を割り当てるルーティングフレームワーク「DIRECT」を提案。無駄な高コスト計算を抑えつつ、 frontierレベルの性能と低レイテンシの両立を目指す。 |
| 先行研究と比べてどこがすごい？ | 従来手法は特定のモデルに固定されがちだが、DIRECTはタスクごとの認知負荷をシーンと指示から推論する。これにより、単純な作業には軽量モデルを、複雑な作業には高性能モデルを割り当てることで、最大65%のレイテンシ低減を実現した。 |
| 技術や手法のキモはどこ？ | タスクの指示とシーン画像を軽量なエンコーダで埋め込み、その文脈に基づいて、事前に定義した複数のプランナー（思考の深さ、モデルサイズ、メモリ構成の異なるもの）から最適なものを動的に選択するルーティングアルゴリズム。 |
| どうやって有効だと検証した？ | VLABenchやRoboMMEといったベンチマークでのシミュレーションに加え、実機のFrankaアームを用いたDROID環境での実験を行い、固定モデルよりも優れた性能とコスト効率（パレートフロンティアの改善）を達成した。 |
| 議論はある？ | ルーター自体は訓練済みモデルの固定プールに依存しており、プランナーの種類を変更するには再学習が必要となる。また、各ステージごとの依存関係を考慮しない per-call な意思決定を行っている。 |
| 次に読むべき論文は？ | [RouteLLM: Learning to route LLMs with open models](https://arxiv.org/abs/2408.06195)、[FrugalGPT: How to use large language models more efficiently while reducing cost and latency](https://arxiv.org/abs/2305.05176) |
| PDFリンク | https://arxiv.org/pdf/2606.12402v1 |
