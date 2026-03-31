---
title: "Gen-Searcher: Reinforcing Agentic Search for Image Generation"
date: 2026-03-31
arxiv_id: 2603.28767v1
url: http://arxiv.org/abs/2603.28767v1
---

# Gen-Searcher: Reinforcing Agentic Search for Image Generation

| 項目 | 内容 |
|---|---|
| どんなもの？ | 画像生成モデルが苦手とする知識集約型や最新情報の反映が必要なプロンプトに対し、エージェントがマルチホップのWeb検索と推論を行って情報を収集し、接地（グラウンディング）された画像を生成する「Gen-Searcher」を提案した研究。モデルのトレーニングにエージェント型強化学習（Agentic RL）を導入し、画像生成の品質と正確性を大幅に向上させている。 |
| 先行研究と比べてどこがすごい？ | 従来のRAGベース手法やプロンプト駆動のワークフローが抱えていた「動的知識への対応不足」や「手動プロンプトの最適化不足」を解決した点。また、単なるテキスト検索にとどまらず、視覚的なリファレンス画像を収集して活用する点が画期的。 |
| 技術や手法のキモはどこ？ | Gemini 3 Proを用いたデータ生成パイプラインと、SFTおよびGRPO（グループベース強化学習）による2段階学習。特に、画像生成の不安定さを考慮し、テキストと画像の双方から報酬を得る「デュアル報酬フィードバック設計」を採用したことで、検索と推論プロセスの安定した最適化を実現した点。 |
| どうやって有効だと検証した？ | 知識集約的な検索ベース画像生成を評価するための新ベンチマーク「KnowGen」を構築し、K-Scoreを用いて評価。Qwen-Image等のベースモデルに対し、KnowGenで約16ポイント、WISEで約15ポイントの大幅な改善を示した。さらに、複数の生成モデルに対する強力な転移性能を実証した。 |
| 議論はある？ | 生成画像が検索情報と合致していても、下流の画像生成モデル自体の性能限界（一貫性の欠如、テキスト描画能力の低さ等）に依存する場合がある。今後はベースとなる画像生成モデルの強化も課題となる。また、画像報酬とテキスト報酬の重みづけ調整が必要である。 |
| 次に読むべき論文は？ | [Simpledeepsearcher: Deep information seeking via web-powered reasoning trajectory synthesis](https://arxiv.org/abs/2505.16834)、[Agentic reinforced policy optimization](https://arxiv.org/abs/2507.19849) |
| PDFリンク | https://arxiv.org/pdf/2603.28767v1 |
