---
title: "Verifier-Backed Hard Problem Generation for Mathematical Reasoning"
date: 2026-05-08
arxiv_id: 2605.06660v1
url: http://arxiv.org/abs/2605.06660v1
---

# Verifier-Backed Hard Problem Generation for Mathematical Reasoning

| 項目 | 内容 |
|---|---|
| どんなもの？ | 数学問題生成における「報酬ハッキング」を防ぐため、セッター（問題生成者）とソルバー（解法者）の対話に独立した検証器（Verifier）を導入した「VHG（Verifier-Backed Hard Problem Generation）」という3者間自律学習フレームワーク。検証器により、妥当性が確認された問題のみを難易度評価に使用することで、高品質かつ困難な数学問題の生成を可能にした。 |
| 先行研究と比べてどこがすごい？ | 従来の自己対話型手法は、ソルバーの誤答を難易度向上と見なして報酬を与えるため、無効な問題を生成する報酬ハッキングが課題であった。VHGは検証器による「妥当性の保証」を報酬計算に組み込むことで、問題の「妥当性」と「難易度」を分離し、より信頼性の高いトレーニングデータの生成を実現した点。 |
| 技術や手法のキモはどこ？ | セッターの報酬関数を「検証器による正当性評価」と「ソルバーによる難易度評価」の積で定義した点。検証器が「不合格」と判断すれば、ソルバーが解けなくてもセッターには報酬が与えられない設計により、無効な問題の生成を物理的に遮断したこと。 |
| どうやって有効だと検証した？ | 不定積分（SymPyによる厳密な検証）と一般数学（LLM-as-a-judgeによる検証）の2つのドメインで実験。AntiderivBenchやMATH、AMC、AIME等の標準的ベンチマークにおいて、既存の最高性能モデル（R-Zero等）を大きく上回る推論精度の向上を確認。 |
| 議論はある？ | ガイダンスの質は検証器の性能に完全に依存する点。特にLLMベースのソフト検証器は、厳密な数学的保証が難しく、微細なエラーを見逃す可能性がある。また、ベンチマークへの過学習や、検証器の前提条件が不明確な場合のリスクについても言及されている。 |
| 次に読むべき論文は？ | [R-Zero: Self-evolving reasoning LLM from zero data](https://openreview.net/forum?id=96apU6YzSO) / [DeepSeek-R1: Incentivizing reasoning capability in LLMs via reinforcement learning](https://arxiv.org/abs/2501.12948) / [LLMs gaming verifiers: RLVR can lead to reward hacking](https://arxiv.org/abs/2604.15149) |
| PDFリンク | https://arxiv.org/pdf/2605.06660v1 |
