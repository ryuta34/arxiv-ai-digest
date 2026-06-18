---
title: "Learning User Simulators with Turing Rewards"
date: 2026-06-18
arxiv_id: 2606.19336v1
url: http://arxiv.org/abs/2606.19336v1
---

# Learning User Simulators with Turing Rewards

| 項目 | 内容 |
|---|---|
| どんなもの？ | ユーザーの過去の履歴や人格に基づいて、人間らしく自然な対話を生成するユーザーシミュレーターを構築する手法「Turing-RL」を提案する論文。特定の正解応答を模倣するのではなく、人間が書いたものと区別できない（Indistinguishable）応答の生成を目指す。 |
| 先行研究と比べてどこがすごい？ | 従来手法は対話のログ確率最大化や類似性報酬に依存しており、模倣は得意だが人間らしさに欠けていた。本手法はLLM Judgeを用いた「Turing報酬」を導入することで、内容の正確さを犠牲にすることなく、より人間らしい応答を生成できる点。 |
| 技術や手法のキモはどこ？ | 強化学習における報酬関数として、LLM Judgeが「人間による正解」と「モデルの生成物」を比較し、どちらがより人間らしいかを1-7の尺度でスコアリングする「Turing報酬」を採用したこと。また、GRPO（Group Relative Policy Optimization）を用いて学習する。 |
| どうやって有効だと検証した？ | 多対話チャット（PRISM）とRedditのフォーラム議論という2つの異なるドメインで評価。LLM-as-a-judgeおよび人間による比較評価を行い、従来手法（Sim-RLやLogprob-RL）と比較して高いWin Rateを達成したことで有効性を示した。 |
| 議論はある？ | 現在はQwen3-8Bベースだが、より大規模なモデルへのスケーラビリティや、評価用LLM Judgeのバイアスへの依存、悪用（なりすまし等）のリスク、モデルの思考プロセスが人間と一致しているかの検証が残された課題である。 |
| 次に読むべき論文は？ | [HumanLM: Simulating users with state alignment beats response imitation](https://arxiv.org/abs/2603.03303), [Learning to simulate human dialogue](https://arxiv.org/abs/2601.04436) |
| PDFリンク | https://arxiv.org/pdf/2606.19336v1 |
