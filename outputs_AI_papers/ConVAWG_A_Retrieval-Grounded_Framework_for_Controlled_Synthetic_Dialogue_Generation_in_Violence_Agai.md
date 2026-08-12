---
title: "ConVAWG: A Retrieval-Grounded Framework for Controlled Synthetic Dialogue Generation in Violence Against Women and Girls"
date: 2026-08-12
arxiv_id: 2608.11200v1
url: http://arxiv.org/abs/2608.11200v1
---

# ConVAWG: A Retrieval-Grounded Framework for Controlled Synthetic Dialogue Generation in Violence Against Women and Girls

| 項目 | 内容 |
|---|---|
| どんなもの？ | 対人暴力（VAWG）の動的な側面をモデル化するため、実データに基づく検索と階層的なイベント計画を組み合わせた、制御可能な合成対話生成フレームワーク「ConVAWG」の提案。被害者と加害者の関係性や時間的な虐待の推移を反映した、多幕構成のオンライン会話データセットを構築した。 |
| 先行研究と比べてどこがすごい？ | 既存研究が文レベルの毒性検知に留まっていたのに対し、本手法は会話のコンテキストや時間経過に伴う虐待の段階的なエスカレーションを、構造的なシナリオとイベントグラフを用いてモデル化できる点。 |
| 技術や手法のキモはどこ？ | ①実ケースに基づく検索（DHR知識ベース）によるシナリオ構築、②階層的なイベントグラフによる時系列計画、③ペルソナや虐待段階に応じたスタイル制御、④CAA（Contrastive Activation Addition）による、文脈的に適切な箇所への毒性（攻撃性）注入。 |
| どうやって有効だと検証した？ | 6,000以上の対話イベントを用いて、人間による評価および4つのLLM（GPT-5.2等）を評価者とした比較実験を実施。さらに毒性検知や関係性推論などの下流タスクでの有効性、およびアブレーションスタディによってフレームワークの各構成要素の妥当性を検証した。 |
| 議論はある？ | 英国の公的定義や統計に基づいているため他地域への適応性に制限がある点や、会話に現れないオフラインの虐待行動のモデル化には限界がある点を指摘している。また、データセットの性質上、悪用リスクを考慮して厳格なアクセス制限（データ使用合意）を設けている。 |
| 次に読むべき論文は？ | [PersonaHub: Large-scale Persona Generation](https://arxiv.org/abs/2406.20094)、[DiaSynth: Synthetic Dialogue Generation Framework for Low Resource Dialogue Applications](https://arxiv.org/abs/2502.16489)など。 |
| PDFリンク | https://arxiv.org/pdf/2608.11200v1 |
