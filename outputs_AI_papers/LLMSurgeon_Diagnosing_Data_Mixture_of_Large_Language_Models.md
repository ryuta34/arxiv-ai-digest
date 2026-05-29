---
title: "LLMSurgeon: Diagnosing Data Mixture of Large Language Models"
date: 2026-05-29
arxiv_id: 2605.30348v1
url: http://arxiv.org/abs/2605.30348v1
---

# LLMSurgeon: Diagnosing Data Mixture of Large Language Models

| 項目 | 内容 |
|---|---|
| どんなもの？ | 大規模言語モデル（LLM）の学習データの構成比率を、モデルの重みや学習データにアクセスすることなく、生成されたテキストのみから事後的に推定する「Data Mixture Surgery (DMS)」という枠組みを提案している。 |
| 先行研究と比べてどこがすごい？ | 従来のメンバーシップ推論攻撃（MIA）は特定のデータサンプルの有無を判定するものであり、コーパス全体の分布を推定するのには不向きだった。本手法は分布推定に特化し、ドメイン間の混同を数学的に補正することで高精度な推定を実現した。 |
| 技術や手法のキモはどこ？ | 推定を「ラベルシフトを伴う逆問題」として定式化している点。外部の分類器で得られた biased な予測に対し、事前に計算した「ソフト混同行列」を用いて数学的に de-blur（補正）を行い、潜在的なドメイン混合比率を復元する。 |
| どうやって有効だと検証した？ | 学習データ構成が公開されている8つのオープンソースLLM（LLaMA-1, OLMo, StarCoder等）を用いた検証用ベンチマーク「LLMScan」を構築し、既存のMIAベースの集計手法よりも高い精度で分布を推定できることを示した。 |
| 議論はある？ | Neutral プロンプトの使用を前提とするが、RLHFなどで極端に調整されたモデルでは分布が歪む可能性がある。また、ドメイン間の意味的重複が大きい場合に逆行列計算が不安定になる限界があり、今後は階層的な推定手法などが期待される。 |
| 次に読むべき論文は？ | [DoReMi: Optimizing data mixtures speeds up language model pretraining](https://arxiv.org/abs/2305.12836), [Membership inference attacks from first principles](https://arxiv.org/abs/2112.03570) |
| PDFリンク | https://arxiv.org/pdf/2605.30348v1 |
