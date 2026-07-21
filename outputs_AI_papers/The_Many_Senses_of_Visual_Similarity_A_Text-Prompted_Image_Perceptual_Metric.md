---
title: "The Many Senses of Visual Similarity: A Text-Prompted Image Perceptual Metric"
date: 2026-07-21
arxiv_id: 2607.18237v1
url: http://arxiv.org/abs/2607.18237v1
---

# The Many Senses of Visual Similarity: A Text-Prompted Image Perceptual Metric

| 項目 | 内容 |
|---|---|
| どんなもの？ | 画像の類似性を、色・ポーズ・背景などの特定の側面（アスペクト）に応じて条件付けして測定できる、新しい知覚的類似性メトリクス「TPIPS」を提案している。大規模な人間による評価データセットを用いて、既存の固定的な類似性メトリクスの限界を克服した。 |
| 先行研究と比べてどこがすごい？ | 既存のLPIPSやDreamSimは、類似性を単一のスカラー値でしか表現できなかったが、本手法は「特定の側面に基づく類似性」という文脈依存の判断を可能にした。また、人間による評価データを用いてVLMを微調整することで、人間と高い一致率を示す汎用的な指標を確立した。 |
| 技術や手法のキモはどこ？ | FLUXなどの生成モデルを活用し、人間が複数の側面で評価した100万件規模の「Odd-one-out（3つから異質なものを選ぶ）」データセットを構築した点。また、VLM（Qwen3-VL）をベースに、埋め込み、中間層の活性化差、全結合の各手法を統合し、テキストプロンプトによる条件付けを実現した点。 |
| どうやって有効だと検証した？ | 提案手法（TPIPS）を用いて、未知のデータセットや様々な視覚的タスク（画像編集、コンポジット、3D生成等）における評価を行い、人間の一致率（consensus）との比較を行った。結果として、既存のVLMや従来のメトリクスを大幅に上回る性能を達成した。 |
| 議論はある？ | 計算コストが従来の手法（LPIPS等）に比べて高いことや、現在の注釈者グループのバイアスが結果に反映される可能性、また、特定の訓練データの分布に依存した類似性の曖昧さが残る点が課題として挙げられる。 |
| 次に読むべき論文は？ | [1] [DreamSim: Learning new dimensions of human visual similarity using synthetic data](https://arxiv.org/abs/2305.15065) <br> [2] [The unreasonable effectiveness of deep features as a perceptual metric](https://arxiv.org/abs/1801.03924) <br> [3] [GeneCIS: A benchmark for general conditional image similarity](https://arxiv.org/abs/2303.13524) |
| PDFリンク | https://arxiv.org/pdf/2607.18237v1 |
