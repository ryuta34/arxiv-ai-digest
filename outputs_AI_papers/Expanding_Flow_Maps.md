---
title: "Expanding Flow Maps"
date: 2026-07-24
arxiv_id: 2607.21585v1
url: http://arxiv.org/abs/2607.21585v1
---

# Expanding Flow Maps

| 項目 | 内容 |
|---|---|
| どんなもの？ | 生成プロセス中にデータの次元（出力サイズ）を動的に増加させる、新しい生成モデルフレームワーク「Expanding Generative Flows (EFlows)」および「Expanding Flow Maps (EFMs)」。連続および離散データの両方に対応し、変数サイズの出力生成を効率的に行う。 |
| 先行研究と比べてどこがすごい？ | 従来のフローベースモデルが固定次元のキャンバスに制限されていたのに対し、次元成長を許容することで、可変解像度の画像、可変長のテキスト、可変サイズの分子グラフ生成を実現。さらに、効率的なFew-step（1〜数ステップ）生成を可能にしている。 |
| 技術や手法のキモはどこ？ | （1）次元を成長させる「expanding interpolant」、（2）状態空間を拡張しノイズを注入する「expand operator」、（3）これらを統合した「Piecewise-Deterministic Markov Process (PDMP)」の構築。これらにより、拡張と輸送を同時に行う単一のフローマップを定義した点。 |
| どうやって有効だと検証した？ | 分子コンフォマー生成（GEOM-QM9, GEOM-Drugs）、分子グラフ生成、言語モデリング（LM1B）の3つのタスクで評価。既存の多ステップ拡散モデルやフローモデルと比較し、同等以上の性能を圧倒的に少ない計算ステップ数で達成。 |
| 議論はある？ | 現在のモデルは小〜中規模データに限定されており、より大規模な次元へのスケーリングには追加のチューニングが必要。また、現時点では「増加する次元」に限定しているが、次元を減少させる構成への拡張もPDMPの枠組みで検討可能としている。 |
| 次に読むべき論文は？ | [Stochastic interpolants: A unifying framework for flows and diffusions](https://arxiv.org/abs/2212.08072), [Flow map matching with stochastic interpolants](https://arxiv.org/abs/2312.01587), [Consistency models](https://arxiv.org/abs/2303.01469) |
| PDFリンク | https://arxiv.org/pdf/2607.21585v1 |
