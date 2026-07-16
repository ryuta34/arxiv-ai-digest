---
title: "Leveraging unlabelled data for generalizable neural population decoding"
date: 2026-07-16
arxiv_id: 2607.14086v1
url: http://arxiv.org/abs/2607.14086v1
---

# Leveraging unlabelled data for generalizable neural population decoding

| 項目 | 内容 |
|---|---|
| どんなもの？ | ニューラルスパイクデータの表現学習を効率化し、ラベルなしデータから学習できるようにした汎用的な神経人口デコーディングフレームワーク「MOJO」を提案。教師あり学習と自己教師あり学習（マスク付きオートエンコーダ）を統合することで、限られたラベル付きデータでも高精度なデコーディングを実現する。 |
| 先行研究と比べてどこがすごい？ | 既存のスパイクベースのモデル（POYO等）がラベル付きデータのみに依存していたのに対し、本手法は大量のラベルなしデータも活用可能。Few-shot学習における性能向上や、学習済みユニット埋め込みの解釈性の高さ（脳領域の分類精度等）において優れた性能を示す。 |
| 技術や手法のキモはどこ？ | スパイクのスパースな性質を考慮し、符号化された潜在変数に対して時間的なマスクを適用する「Masked AutOencoder-based JOint Pretraining (MOJO)」を採用した点。教師あり学習（行動予測）と自己教師あり学習（スパイクレートの再構成）を単一のバックボーンで統合した。 |
| どうやって有効だと検証した？ | サル（到達運動）、マウス（視覚・意思決定）、ヒト（脳皮質電位による発話）のデータセットを用いて評価。Few-shot学習、ラベルの割合を変えた学習、クロス種（サル→マウス）転移学習など、多様なタスクで教師あり学習のみのモデルを上回ることを示した。 |
| 議論はある？ | モデルがデータ駆動型であり十分なデータ量を必要とすること、またセッションごとにユニット埋め込みを再学習する必要がある点が限界。今後は、マルチモーダル学習の拡大や、埋め込みの再利用性を高める手法の開発が必要。 |
| 次に読むべき論文は？ | [13] A Unified, Scalable Framework for Neural Population Decoding (Azabou et al., 2023) / [14] Generalizable, real-time neural decoding with hybrid state-space models (Ryoo et al., 2025) |
| PDFリンク | [https://arxiv.org/pdf/2607.14086v1](https://arxiv.org/pdf/2607.14086v1) |
