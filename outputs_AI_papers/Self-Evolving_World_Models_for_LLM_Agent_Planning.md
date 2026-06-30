---
title: "Self-Evolving World Models for LLM Agent Planning"
date: 2026-06-30
arxiv_id: 2606.30639v1
url: http://arxiv.org/abs/2606.30639v1
---

# Self-Evolving World Models for LLM Agent Planning

| 項目 | 内容 |
|---|---|
| どんなもの？ | 大規模言語モデル（LLM）エージェント向けの、推論時に自己進化する世界モデルフレームワーク「WORLDEVOLVER」です。モデルの重みを更新せず、エピソード記憶とセマンティック記憶を動的に更新することで、環境変化に対する予測精度とプランニング性能を向上させます。 |
| 先行研究と比べてどこがすごい？ | 従来の強化学習やオフライン学習によるモデル更新と比較して、学習コストがかからず、環境の分布変化に柔軟に適応できます。また、信頼性の低い予測をフィルタリングする仕組みにより、誤った情報によるプランニングの悪化を防ぎます。 |
| 技術や手法のキモはどこ？ | ①実体験を蓄積する「エピソード記憶」、②予測と観測の不一致から永続的なヒューリスティック・ルールを抽出する「セマンティック記憶」、③予測の自信度に応じてエージェントへの入力を制限する「選択的フォーサイト」の3つのモジュールを統合した点です。 |
| どうやって有効だと検証した？ | Word2Worldベンチマークを用いた世界モデルの予測精度評価と、ALFWorldおよびScienceWorldにおけるAgentBoardを用いたエージェントのタスク成功率評価を行いました。多様なバックボーンモデルでベースラインを上回る性能を示しました。 |
| 議論はある？ | 現在はテキストベースの環境に限定されており、より広範な領域への拡張が課題です。また、予測の自信度と正確性の相関がモデルや環境によって変動する可能性があり、より堅牢な信頼性推定手法が必要とされています。 |
| 次に読むべき論文は？ | [ReAct: Synergizing reasoning and acting in language models](https://arxiv.org/abs/2210.03629), [World models](https://arxiv.org/abs/1803.10122), [AgentBoard: An analytical evaluation board of multi-turn LLM agents](https://arxiv.org/abs/2401.13158) |
| PDFリンク | https://arxiv.org/pdf/2606.30639v1 |
