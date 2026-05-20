---
title: "From Seeing to Thinking: Decoupling Perception and Reasoning Improves Post-Training of Vision-Language Models"
date: 2026-05-20
arxiv_id: 2605.20177v1
url: http://arxiv.org/abs/2605.20177v1
---

# From Seeing to Thinking: Decoupling Perception and Reasoning Improves Post-Training of Vision-Language Models

| 項目 | 内容 |
|---|---|
| どんなもの？ | ビジョン言語モデル（VLM）の推論性能が、実は視覚的な知覚能力の低さに起因していることを明らかにした論文。知覚と推論を段階的に分離してトレーニングする手法を提案し、精度の向上と推論コストの削減を実現した。 |
| 先行研究と比べてどこがすごい？ | 長い思考プロセスを強制する従来の手法に対し、本研究は「知覚エラーが推論の誤りを増幅させる」点に着目した。能力の種類に応じた段階的カリキュラム学習を導入し、効率的なモデル改善に成功している。 |
| 技術や手法のキモはどこ？ | 知覚・テキスト推論・視覚推論の3段階に分けたポストトレーニングの実行と、RLVR（報酬付き強化学習）による効果的な知覚学習、さらに知覚困難データを用いたフィルタリングパイプラインの構築。 |
| どうやって有効だと検証した？ | Qwen2.5-VL-7B/Qwen3-VL-8B等の複数のVLMをベースモデルとし、MathVista、WeMath、RealWorldQA等の主要な視覚的数学および知覚タスクのベンチマークを用いて評価した。 |
| 議論はある？ | 実験は7B-8B規模に留まっており、より大規模モデルへの適用や、より細かい能力分離の粒度、高品質なキャプションデータへの依存が課題として挙げられている。 |
| 次に読むべき論文は？ | [DeepSeek-R1](https://arxiv.org/abs/2501.12948) や [MathVista](https://arxiv.org/abs/2310.02255)、[LLaVA-CoT](https://arxiv.org/abs/2411.10440) などの推論・視覚基盤モデル関連論文。 |
| PDFリンク | https://arxiv.org/pdf/2605.20177v1 |
