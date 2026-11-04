---
title: "From Natural Language to Exact Cover: A Neuro-Symbolic Approach to Zebra Puzzles"
date: 2026-11-04
arxiv_id: 2611.03641v1
url: http://arxiv.org/abs/2611.03641v1
---

# From Natural Language to Exact Cover: A Neuro-Symbolic Approach to Zebra Puzzles

| 項目 | 内容 |
|---|---|
| どんなもの？ | ゼブラパズル（論理パズル）を解くための、LLMと記号ソルバー（厳密被覆問題ソルバー）を組み合わせた神経記号（neuro-symbolic）フレームワーク「NeuralExactCover」。LLMが自然言語から制約を抽出し、シンボリックソルバーが論理的な推論と検証を確実に行う仕組み。 |
| 先行研究と比べてどこがすごい？ | 従来のLLM単体やLogic-LM等の手法に対し、厳密被覆（exact cover）という数学的に厳密なモデルを採用することで、論理的整合性を保証できる点。また、解が求まらない場合にソルバーからのフィードバックを用いてLLMが自身の推論を再修正する「反復的フィードバックループ」により、高い精度を実現している。 |
| 技術や手法のキモはどこ？ | LLMがパズル情報をツール呼び出し形式に変換し、それを「Dancing Links」アルゴリズムに基づくMiniExactソルバーで解く点。また、解の成否を報酬として利用し、制約が不足・過剰な場合にツール呼び出しを再構成させるフィードバック機構。さらに、より困難なパズルを含む「ZebraExtreme」データセットを構築した点。 |
| どうやって有効だと検証した？ | 既存のZebraLogicベンチマークおよび新規構築したZebraExtremeを用い、様々なパラメータ規模（4B〜30B）や学習済みモデル（Qwen3, Devstral等）で評価。多くの設定において、既存の神経記号手法（Logic-LMやLogic.py）を上回る正解率と細胞（セル）精度を達成した。 |
| 議論はある？ | 言語モデルが「cat（猫/ペット）」のような曖昧な属性を誤ってマッピングする現象や、シンボリックな結果をテキストに逆変換する際の文字列照合エラーが失敗の主な原因である。また、パズルの規模が大きくなるとツール呼び出しの生成プロセス自体がボトルネックになる可能性がある。 |
| 次に読むべき論文は？ | [Logic.py: Bridging the gap between llms and constraint solvers](https://arxiv.org/abs/2502.15776)、[Logic-LM: Empowering large language models with symbolic solvers for faithful logical reasoning](https://arxiv.org/abs/2305.12295) |
| PDFリンク | https://arxiv.org/pdf/2611.03641v1 |
