---
title: "Code2LoRA: Hypernetwork-Generated Adapters for Code Language Models under Software Evolution"
date: 2026-06-07
arxiv_id: 2606.06492v1
url: http://arxiv.org/abs/2606.06492v1
---

# Code2LoRA: Hypernetwork-Generated Adapters for Code Language Models under Software Evolution

| 項目 | 内容 |
|---|---|
| どんなもの？ | ソフトウェア開発の進化（コードの変更）に適応可能な、リポジトリ特化型のLoRAアダプターを生成するハイパーネットワークフレームワーク「Code2LoRA」を提案。推論時のトークンオーバーヘッドなしに、リポジトリごとの知識をモデルの重みに直接注入する。 |
| 先行研究と比べてどこがすごい？ | 既存のRAG等のコンテキスト注入手法が抱える推論時のコストやコンテキスト制限を解決し、さらに従来の静的なファインチューニングやLoRAが困難だった「進化するコードベース」への追従を、GRNを用いた再帰的なアダプター更新により実現した点。 |
| 技術や手法のキモはどこ？ | リポジトリのコンテキストを固定サイズの埋め込みベクトルに圧縮し、それをハイパーネットワークでLoRA重みに変換する仕組み。特に「Code2LoRA-Evo」では、コードの差分をGRUで処理してアダプターを順次更新し、時間変化するコードベースに動的に適応する。 |
| どうやって有効だと検証した？ | 604件のPythonリポジトリで構成される新ベンチマーク「RepoPeftBench」を構築。静的なリポジトリ解析を行う「Static track」と、コミット履歴に基づきコードの進化を追う「Evolution track」の両面から評価し、既存のベースラインを大幅に上回る性能を実証した。 |
| 議論はある？ | 評価対象がPythonのみであること、ベースモデルが1.5B規模であること、およびOOD評価におけるターゲットの短さに起因するスコア上昇の可能性がある点を認めている。また、LoRA生成用ハイパーネットワークがパラメータ量の大半を占める。 |
| 次に読むべき論文は？ | [Doc2LoRA](https://arxiv.org/abs/2602.15902)、[Text2LoRA](https://arxiv.org/abs/2506.05176)、[Zhyper](https://arxiv.org/abs/2510.19733) |
| PDFリンク | https://arxiv.org/pdf/2606.06492v1 |
