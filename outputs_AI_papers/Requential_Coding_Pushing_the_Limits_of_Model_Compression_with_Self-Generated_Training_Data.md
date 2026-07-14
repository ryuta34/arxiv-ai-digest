---
title: "Requential Coding: Pushing the Limits of Model Compression with Self-Generated Training Data"
date: 2026-07-14
arxiv_id: 2607.11883v1
url: http://arxiv.org/abs/2607.11883v1
---

# Requential Coding: Pushing the Limits of Model Compression with Self-Generated Training Data

| 項目 | 内容 |
|---|---|
| どんなもの？ | ニューラルネットワークの学習プロセス自体を圧縮することで、モデルサイズやデータのエントロピーに依存しない、極めて効率的なモデル圧縮手法「Requential Coding」を提案した論文。大規模言語モデル（LLM）の一般化性能を理論的に保証し、モデルの圧縮可能性と学習ダイナミクスの関係を明らかにした。 |
| 先行研究と比べてどこがすごい？ | 従来のパラメータ圧縮（量子化等）や既存の系列圧縮（Prequential coding）が抱えていた、モデルサイズやデータ量に比例して符号長が増大する問題を解決した。モデルの計算量と学習効率を活用し、大規模モデルほど圧縮可能であることを初めて示し、最先端のPAC-Bayes一般化境界を実現した。 |
| 技術や手法のキモはどこ？ | 生データではなく、モデル自身が生成した訓練データを教師モデルが選別する「Requential Coding」という枠組み。相対エントロピー符号化（REC）を用いて、教師と生徒の損失差分（KLダイバージェンス）のみを符号化することで、冗長な情報を削ぎ落とした効率的な圧縮を実現した。 |
| どうやって有効だと検証した？ | OpenWebText、CIFAR-5M、FineWeb等のデータセットを用い、GPT-2ベースのモデルで実験。量子化（PTQ）手法と比較し、計算最適なLLMにおいて、モデルの学習性能を保ちつつ、より短い符号長で高い一般化性能を証明する境界を得られることを示した。 |
| 議論はある？ | 現在の手法は符号化に教師モデルを用いた反復計算が必要であり、モデルの送受信には不向きなツールである点。また、学習の初期段階で得られた情報が後で忘れられることに対し、符号長が単調増加する課題があり、情報の「忘却」を考慮したさらなる最適化が将来課題。 |
| 次に読むべき論文は？ | [1] [Léonard Blier and Yann Ollivier. The description length of deep learning models. (2018)](https://arxiv.org/abs/1806.07548), [8] [Marc Anton Finzi et al. Compute-optimal LLMs provably generalize better with scale. (2025)](https://arxiv.org/abs/2501.12345), [44] [Lucas Theis and Noureldin Y Ahmed. Algorithms for the communication of samples. (2022)](https://arxiv.org/abs/2205.12180) |
| PDFリンク | [https://arxiv.org/pdf/2607.11883v1](https://arxiv.org/pdf/2607.11883v1) |
