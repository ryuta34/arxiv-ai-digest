---
title: "Toward a Locally Deployable Agentic Co-Scientist: Small-Model Planning for Early-Stage Drug Discovery"
date: 2026-10-06
arxiv_id: 2610.04740v1
url: http://arxiv.org/abs/2610.04740v1
---

# Toward a Locally Deployable Agentic Co-Scientist: Small-Model Planning for Early-Stage Drug Discovery

| 項目 | 内容 |
|---|---|
| どんなもの？ | 初期段階の創薬ワークフローを効率化するため、ローカルで動作する小型言語モデル（3Bパラメータ規模）を「エージェント型コ・サイエンティスト」として活用するフレームワーク。ユーザーの要求に応じて18種類の科学ツールを統合的に計画・実行し、分子の生成から評価、 prioritizationまでを自動化する。 |
| 先行研究と比べてどこがすごい？ | 外部APIや大規模LLMへの過度な依存を避け、GPU搭載のローカル環境で機密情報を保護しつつ、構造化された「統一分子スキーマ（UMS）」を通じて異種ツール間の一貫した状態管理を可能にした点。また、ソフトウェア工学のパスカバレッジ手法を応用したデータセット構築により、小型モデルでも高い計画精度を実現した。 |
| 技術や手法のキモはどこ？ | ツール入出力の整合性を保つための「統一分子スキーマ(UMS)」、各ツールをノードとしたワークフローグラフの「パスカバレッジに基づくデータセット構築」、およびLoRAによる小型モデル（Llama 3.2-3B等）の専門特化型チューニング。 |
| どうやって有効だと検証した？ | 1,263件のクエリ・プランペアを作成し、クエリレベルおよびワークフローグループレベルの分割でテストを実施。Llama 3.2-3B等のモデルを用いて、ツール選択、実行順序、引数生成の精度（F1スコアやExact Match等）を検証。さらにCDK2標的等の具体的な創薬シナリオでの実機ケーススタディを実施。 |
| 議論はある？ | トレーニングデータに含まれない未知の複雑なワークフロー組成に対する汎化性能が課題。また、ルールベースの評価・要約層をモデルベースに置き換える余地や、より多様で実務的なデータセットへの拡張が今後の将来課題として挙げられている。 |
| 次に読むべき論文は？ | [LangGraph: Modular framework for agent AI](https://arxiv.org/abs/2412.03801)、[ChemCrow: Chemistry tool-augmented LLMs](https://arxiv.org/abs/2304.05376)、[CoScientist: Autonomous chemical research](https://www.nature.com/articles/s41586-023-06792-0) |
| PDFリンク | https://arxiv.org/pdf/2610.04740v1 |
