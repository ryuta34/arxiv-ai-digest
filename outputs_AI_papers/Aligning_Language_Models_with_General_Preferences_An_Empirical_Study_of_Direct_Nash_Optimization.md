---
title: "Aligning Language Models with General Preferences: An Empirical Study of Direct Nash Optimization"
date: 2026-11-05
arxiv_id: 2611.05373v1
url: http://arxiv.org/abs/2611.05373v1
---

# Aligning Language Models with General Preferences: An Empirical Study of Direct Nash Optimization

| 項目 | 内容 |
|---|---|
| どんなもの？ | Direct Nash Optimization (DNO) を用いた言語モデルのアライメント手法「DNO-Prct」の独立した再実装と、異なるモデルファミリーに対する有効性を検証した実証研究。オンポリシーのサンプリング、LLMによる評価、強化学習的なペア選択を繰り返すことで、モデルの応答性能を向上させる。 |
| 先行研究と比べてどこがすごい？ | 従来はモデル単体や特定のモデルファミリーに限定されていたDNOの検証を、Llama 3.1 8BやMistral 7Bといった複数のオープンウェイトモデルで実施。GPT-4oなどのプロプライエタリなモデルだけでなく、同ファミリーのモデルを評価者（アノテーター）に用いても高い性能向上を確認した。 |
| 技術や手法のキモはどこ？ | 強化学習の Nash 均衡を近似するために、オンポリシーのサンプルと教師モデルのゴールドレスポンスを組み合わせた「LLMベースの評価とペア構築」を行う点。さらに、過去のイテレーションのデータを再利用する「データルックバック」や、特定のスコア差に基づいた大規模マージンフィルタリングを組み合わせている。 |
| どうやって有効だと検証した？ | AlpacaEval 2.0ベンチマークを用い、Llama 3.1 8B InstructとMistral 7B Instruct v0.1に対し、GPT-4oおよび同ファミリーモデルを評価者として適用。長さ制御された勝率（LC win rate）を指標とし、SFTや標準的なDPOとの比較、および各設計要素の重要性を検証する網羅的なアブレーションスタディを実施。 |
| 議論はある？ | 長い応答が評価スコアを押し上げている可能性や、評価者であるGPT-4oと生成モデルの親和性（評価の偏り）、および単一の実行結果であることによる確率的変動が課題。また、大規模なモデルへの追い上げには成功したが、報酬ハッキングや分布シフトに対する頑健性については更なる検証が必要。 |
| 次に読むべき論文は？ | [Direct Nash Optimization: Teaching language models to self-improve with general preferences](https://arxiv.org/abs/2404.03715), [Iterative length-regularized direct preference optimization](https://arxiv.org/abs/2406.11817), [A minimaximalist approach to reinforcement learning from human feedback](https://arxiv.org/abs/2401.04056) |
| PDFリンク | https://arxiv.org/pdf/2611.05373v1 |
