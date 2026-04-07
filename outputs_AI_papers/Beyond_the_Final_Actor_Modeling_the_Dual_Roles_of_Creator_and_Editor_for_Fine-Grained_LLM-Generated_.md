---
title: "Beyond the Final Actor: Modeling the Dual Roles of Creator and Editor for Fine-Grained LLM-Generated Text Detection"
date: 2026-04-07
arxiv_id: 2604.04932v1
url: http://arxiv.org/abs/2604.04932v1
---

# Beyond the Final Actor: Modeling the Dual Roles of Creator and Editor for Fine-Grained LLM-Generated Text Detection

| 項目 | 内容 |
|---|---|
| どんなもの？ | LLM生成テキストの検出において、コンテンツの「作成者（Creator）」と「編集者（Editor）」の役割を分離してモデル化する手法「RACE」を提案。人間とLLMが混在する複雑な4クラス分類（人間作成、LLM生成、LLM洗練、人間による人間化）を高精度に識別するフレームワークです。 |
| 先行研究と比べてどこがすごい？ | 従来のバイナリや3クラス分類では困難だった、人間とLLMの協働プロセスにおける微妙なスタイルの違い（洗練 vs 人間化）を捉えられる点。作成者の論理構成と編集者の言語スタイルという二つのレンズで分析することで、既存の12のベースライン手法を上回る低誤警報率を実現しました。 |
| 技術や手法のキモはどこ？ | Rhetorical Structure Theory (RST)を用いてテキストを論理グラフとして構築し、Rhetoric-Guided Message Passing（修辞学誘導型のメッセージ伝達）を行う点。Elementary Discourse Unit (EDU)レベルの言語特徴と、RSTツリーによる論理構造を分離・抽出して統合するモデルアーキテクチャが核心です。 |
| どうやって有効だと検証した？ | HARTベンチマークデータセットを使用し、4クラス分類タスクにおいて、12の学習ベースおよび指標ベースの手法と比較。TPR@1%FPRなどの指標を用いて、RACEが最も高い識別能力を持ち、特に短いテキストやドメイン外（OOD）データに対しても頑健であることを示しました。 |
| 議論はある？ | 現在はHARTデータセットのみで評価されており、他言語や未知のドメインへの適用範囲が限定的であること。また、完璧な検出器ではないため、商用利用時には人間による手動確認が不可欠であり、将来的な「論理的な難読化」に対する防御策が必要であるとしています。 |
| 次に読むべき論文は？ | [Bao et al., 2025 (HART)](https://arxiv.org/abs/2503.00258), [Abassy et al., 2024 (DetectAIve)](https://aclanthology.org/2024.emnlp-demo.30/), [Liu et al., 2023 (CoCo)](https://aclanthology.org/2023.emnlp-main.1022/) |
| PDFリンク | [https://arxiv.org/pdf/2604.04932v1](https://arxiv.org/pdf/2604.04932v1) |
