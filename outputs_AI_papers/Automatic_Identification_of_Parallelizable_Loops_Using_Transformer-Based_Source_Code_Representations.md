---
title: "Automatic Identification of Parallelizable Loops Using Transformer-Based Source Code Representations"
date: 2026-04-01
arxiv_id: 2603.30040v1
url: http://arxiv.org/abs/2603.30040v1
---

# Automatic Identification of Parallelizable Loops Using Transformer-Based Source Code Representations

| 項目 | 内容 |
|---|---|
| どんなもの？ | ソースコードのループ領域が並列化可能かどうかを判定する、Transformerベースの自動分類手法。DistilBERTを用いてコードの構文的・意味的パターンを学習し、高精度な分類を実現している。 |
| 先行研究と比べてどこがすごい？ | 従来の静的解析や、トークンベースの深層学習手法が必要としていた複雑な前処理や次元削減（PCA等）を不要にした。軽量なTransformerを採用することで、計算リソースを抑えつつ、文脈を考慮した高い汎化性能と信頼性を達成した。 |
| 技術や手法のキモはどこ？ | コードをテキストとして直接処理し、DistilBERTのサブワードトークン化によってコードの文脈情報を抽出する点。また、合成データと手動アノテーション済みの実コードを組み合わせたバランスデータセットでの学習により、偽陽性を抑えた堅牢な分類モデルを構築した。 |
| どうやって有効だと検証した？ | 8,340個のサンプルからなるデータセットを用い、10分割交差検証を実施。正解率、適合率、再現率、F1スコア、および誤判定のリスクを示す偽陽性率（FPR）を評価指標として、統計的に安定した高い性能を確認した。 |
| 議論はある？ | ループレベルの解析に限定されており、ループ融合やアンロールなどの複雑な変換は対象外である点。また、データセットのプログラミングパターンや言語が限定的であるという限界がある。 |
| 次に読むべき論文は？ | [9] Le Chen et al., "Pragformer: Data-driven parallel source code classification with transformers" (2024), [10] Izavan dos S. Correia et al., "Discovering software parallelization points using deep neural networks" (2025) |
| PDFリンク | https://arxiv.org/pdf/2603.30040v1 |
