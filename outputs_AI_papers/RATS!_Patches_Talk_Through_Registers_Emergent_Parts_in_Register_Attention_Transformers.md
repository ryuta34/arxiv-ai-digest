---
title: "RATS! Patches Talk Through Registers: Emergent Parts in Register Attention Transformers"
date: 2026-06-15
arxiv_id: 2606.14701v1
url: http://arxiv.org/abs/2606.14701v1
---

# RATS! Patches Talk Through Registers: Emergent Parts in Register Attention Transformers

| 項目 | 内容 |
|---|---|
| どんなもの？ | 画像内の物体を「パーツ（部品）」の集合体として自律的に学習する、新しいVision Transformerアーキテクチャ「RATS」を提案した論文。パーツアノテーション等の教師データを使用せず、自己教師あり学習のみで高精度なパーツ分割と意味的構造の獲得を実現している。 |
| 先行研究と比べてどこがすごい？ | 既存のViTは画像を単なるパッチの集合として扱うためパーツレベルの構造を捉えにくいが、RATSはパーツに特化した「レジスタートークン」を導入することで、5つのセグメンテーションベンチマークにおいて従来比でmIoUを平均12ポイント向上させ、SOTAを達成した。 |
| 技術や手法のキモはどこ？ | Transformerブロック内に「compress（集約）- communicate（通信）- broadcast（拡散）」という3ステップのレジスターボトルネックを導入した点。レジスタートークンをアテンションヘッドごとに独立させることで、各ヘッドが特定の部分構造（パーツ）を専門的に学習する仕組みとなっている。 |
| どうやって有効だと検証した？ | COCO、ADE20K、ImageNet等5つのデータセットでセグメンテーション性能を評価。また、学習済みレジスターを用いて「パーツ辞書」を構築し、異なるカテゴリ間でのパーツ共有や機能的な類似性の定性分析、さらにMask2Formerへの転移学習による性能向上を実証した。 |
| 議論はある？ | ボトルネック構造は低ランクアテンションであるため、高解像度の精密なタスクには追加の全ランクパスが必要になる点。また、学習は視覚的な共起に基づくため、人間が定義する分類概念と厳密に一致しない場合があることを指摘している。 |
| 次に読むべき論文は？ | [1] [DINOv2: Learning robust visual features without supervision](https://arxiv.org/abs/2304.07193)<br>[2] [Vision transformers need registers](https://arxiv.org/abs/2309.16588)<br>[3] [GroupViT: Semantic segmentation emerges from text supervision](https://arxiv.org/abs/2111.13788) |
| PDFリンク | https://arxiv.org/pdf/2606.14701v1 |
