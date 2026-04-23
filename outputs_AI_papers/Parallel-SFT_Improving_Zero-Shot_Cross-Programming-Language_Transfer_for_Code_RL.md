---
title: "Parallel-SFT: Improving Zero-Shot Cross-Programming-Language Transfer for Code RL"
date: 2026-04-23
arxiv_id: 2604.20835v1
url: http://arxiv.org/abs/2604.20835v1
---

# Parallel-SFT: Improving Zero-Shot Cross-Programming-Language Transfer for Code RL

| 項目 | 内容 |
|---|---|
| どんなもの？ | プログラミング言語（PL）間でのコードRL（強化学習）のゼロショット転移性能を向上させる手法「Parallel-SFT」を提案した論文。異なる言語間で機能的に等価なコード（パラレルプログラム）をSFTデータに組み込むことで、言語の垣根を超えた転移性能を改善する。 |
| 先行研究と比べてどこがすごい？ | 従来のLLMでは、ある言語でRL学習しても他の言語への転移が限定的あるいは性能低下を招くという課題に対し、モデルの潜在空間を機能中心（functionality-centric）に調整することで、未知の言語への高い汎化性能と、一部では言語特化型oracleを凌駕する転移性能を実現した点。 |
| 技術や手法のキモはどこ？ | 同一の自然言語による指示に対して、機能的に等価な複数のプログラミング言語のコードをペアにした「パラレルプログラム」をSFTデータに含める点。これにより、構文レベルではなく機能レベルでコードの共通表現を獲得させる。 |
| どうやって有効だと検証した？ | CodeForcesデータセットを用いたコード生成およびコード検証タスクで評価。Llama-3.1-8B-Instructをベースに、3つのターゲット言語（Go, PHP, Ruby）へのゼロショット転移性能を測定し、内部表現の解析（検索精度や余弦類似度）を通じて機能的なクラスタリングを確認した。 |
| 議論はある？ | SFTデータフォーマットや学習比率の網羅的な探索は未実施である点や、現在の実験は基本的なコード生成/検証タスクに留まっている点が挙げられる。より複雑なエージェント推論や大規模なモデルへの適用については将来課題としている。 |
| 次に読むべき論文は？ | [Llama 3 Herd of Models](https://arxiv.org/abs/2407.21783), [Tulu 3: Pushing frontiers in open language model post-training](https://arxiv.org/abs/2411.15124), [Code Llama: Open foundation models for code](https://arxiv.org/abs/2308.12950) |
| PDFリンク | https://arxiv.org/pdf/2604.20835v1 |
