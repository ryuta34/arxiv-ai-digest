---
title: "Weight Tying Biases Token Embeddings Towards the Output Space"
date: 2026-03-30
arxiv_id: 2603.26663v1
url: http://arxiv.org/abs/2603.26663v1
---

# Weight Tying Biases Token Embeddings Towards the Output Space

| 項目 | 内容 |
|---|---|
| どんなもの？ | 言語モデルにおける「重み共有（Weight Tying）」が、学習ダイナミクスに与える負の影響を解明した研究。共有された埋め込み行列が出力層の勾配によって強くバイアスされ、入力表現としての性能が犠牲になっていることを明らかにした。 |
| 先行研究と比べてどこがすごい？ | 重み共有が性能低下を招くという経験的事実に対し、学習初期の勾配の不均衡というメカニズムによる理論的説明を提供した点。さらに勾配スケーリングによる因果的検証を行い、なぜ「 untying（非共有）」が大規模モデルで推奨されるのかを裏付けた。 |
| 技術や手法のキモはどこ？ | 学習初期において出力層からの勾配が入力層よりも支配的であり、それが共有行列を「出力予測」に特化させてしまうという発見。勾配フックを用いて入力層の勾配をスケーリングし、埋め込み行列の構造が意図的に変化することを示した点。 |
| どうやって有効だと検証した？ | OLMo、Pythia、Qwen3等の複数モデルに対し、埋め込み行列の類似性分析、Tuned Lensによる層ごとのKLダイバージェンス測定、勾配流の追跡、および入力勾配を強化する因果アブレーション実験を実施した。 |
| 議論はある？ | 勾配スケーリングによって入力表現の質を改善しても、出力予測性能とのトレードオフにより、下流タスクでの一貫した性能向上には至らなかった。また、実験は特定のアーキテクチャに限定されており、混合エキスパートモデル等への汎化性は未知数である。 |
| 次に読むべき論文は？ | [Chung et al. (2020) "Rethinking embedding coupling in pre-trained language models"](https://arxiv.org/abs/2010.12821)、[Press and Wolf (2017) "Using the output embedding to improve language models"](https://arxiv.org/abs/1608.05859) |
| PDFリンク | https://arxiv.org/pdf/2603.26663v1 |
