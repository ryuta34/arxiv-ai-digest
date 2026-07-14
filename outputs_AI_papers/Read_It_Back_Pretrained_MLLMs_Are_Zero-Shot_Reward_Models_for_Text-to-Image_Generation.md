---
title: "Read It Back: Pretrained MLLMs Are Zero-Shot Reward Models for Text-to-Image Generation"
date: 2026-07-14
arxiv_id: 2607.11886v1
url: http://arxiv.org/abs/2607.11886v1
---

# Read It Back: Pretrained MLLMs Are Zero-Shot Reward Models for Text-to-Image Generation

| 項目 | 内容 |
|---|---|
| どんなもの？ | 訓練不要で、事前学習済みMLLM（マルチモーダル大規模言語モデル）を画像生成の報酬モデルとして活用する手法「SpectraReward」を提案。さらに、Unified Multimodal Model（UMM）自身の理解ブランチを報酬モデルとする自己改善フレームワーク「Self-SpectraReward」を実現した。 |
| 先行研究と比べてどこがすごい？ | 従来の強化学習で必要だった、報酬モデルの追加学習や大規模な人間による選好データの収集、複雑な推論パイプラインを排除。訓練不要かつオフラインで利用可能であり、報酬モデルの規模を拡大するよりも、ポリシーモデルとの分布整合性を高める方が有効であることを実証した。 |
| 技術や手法のキモはどこ？ | 画像を入力条件とし、元のプロンプトをトークン単位で予測する際の「画像条件付きプロンプト尤度」を報酬として算出する点。これにより、モデルが持つ既存の画像・テキストのアライメント能力を直接報酬として再利用できる。 |
| どうやって有効だと検証した？ | 2つの拡散モデル、3つの強化学習アルゴリズム、4B〜235Bパラメータの9つの報酬モデルを用い、5つのドメイン外ベンチマーク（GenEval, TIIF-Bench, DPG-Bench, WISE, GenEval2）で包括的な評価を実施。 |
| 議論はある？ | 報酬モデルのベースとなるMLLMの推論能力に依存する点や、安全性・美学的観点の最適化が直接的ではないという限界がある。また、より強固な安全性フィルタやバイアス監査が必要であると言及。 |
| 次に読むべき論文は？ | [17] Runhui Huang et al., "AlphaGRPO: Unlocking self-reflective multimodal generation in unified multimodal models via decompositional verifiable reward." (ICML 2026) |
| PDFリンク | https://arxiv.org/pdf/2607.11886v1 |
