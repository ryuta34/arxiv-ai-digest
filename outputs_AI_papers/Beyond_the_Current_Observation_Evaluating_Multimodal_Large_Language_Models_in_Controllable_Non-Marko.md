---
title: "Beyond the Current Observation: Evaluating Multimodal Large Language Models in Controllable Non-Markov Games"
date: 2026-06-18
arxiv_id: 2606.19338v1
url: http://arxiv.org/abs/2606.19338v1
---

# Beyond the Current Observation: Evaluating Multimodal Large Language Models in Controllable Non-Markov Games

| 項目 | 内容 |
|---|---|
| どんなもの？ | マルチモーダル大規模言語モデル（MLLM）の「非マルコフ型ゲーム」における推論能力と記憶保持能力を評価するための新たなベンチマーク「RNG-Bench」を提案した研究。エージェントが過去の観察結果を長期的に記憶し、それを現在の行動に反映させる「Remember-to-act」能力を測定する。 |
| 先行研究と比べてどこがすごい？ | 既存ベンチマークが記憶能力と他のスキル（探索や推論）を混在させていたのに対し、本手法は隠れた状態を制御可能な環境で隔離し、記憶の欠落と意思決定の失敗を「Memory Gap」という指標で切り分けることができる点。 |
| 技術や手法のキモはどこ？ | 静的な情報記憶を要する「Matching Pairs（神経衰弱）」と、動的な空間地図構築を要する「3D Maze」の2種類のゲームを用意し、難易度をグリッドサイズや視覚パターンで精緻に制御したこと。また、真の隠れ状態を注入するオラクル条件と比較することで、性能低下の原因を特定したこと。 |
| どうやって有効だと検証した？ | GPT-5.4やGemini-3.1-Pro等の主要MLLMを対象に性能を測定した。また、Qwen3.5-9Bを最適戦略のシミュレーターログで追加学習（SFT）させることで、ターゲットとした推論能力が向上し、他の外部ベンチマークへも汎化することを示した。 |
| 議論はある？ | 対象としたゲーム環境の制限や、モデルの種類、視覚スタイルが限定的であること。また、Memory Gap指標がモデルの内部構造を完全に説明するものではないという限界を指摘している。 |
| 次に読むべき論文は？ | [40] Emembench: Interactive benchmarking of episodic memory for vlm agents (arXiv:2601.16690) |
| PDFリンク | https://arxiv.org/pdf/2606.19338v1 |
