---
title: "Patch Policy: Efficient Embodied Control via Dense Visual Representations"
date: 2026-07-21
arxiv_id: 2607.18236v1
url: http://arxiv.org/abs/2607.18236v1
---

# Patch Policy: Efficient Embodied Control via Dense Visual Representations

| 項目 | 内容 |
|---|---|
| どんなもの？ | 既存のロボット学習用政策において、画像全体を単一のグローバルなトークンに圧縮する手法に代わり、事前学習済みVision Transformer（ViT）の「高解像度なパッチ特徴量」を直接利用する手法。軽量かつ高速なモデルアーキテクチャ「PATCH POLICY」を提案し、精緻な操作が必要なロボットタスクにおける性能向上を実現した。 |
| 先行研究と比べてどこがすごい？ | 巨大なVision-Language-Actionモデル（VLA）をファインチューニングすることなく、事前学習済みViTの凍結されたパッチ特徴量を利用することで、数％のパラメータ数で同等以上の性能を達成。また、グローバル特徴量に依存する手法と比べて、空間的詳細情報を保持できるため、多物体操作や微細な作業（例：ケーブル挿入）で高い精度を誇る。 |
| 技術や手法のキモはどこ？ | 画像のパッチ情報を直接ポリシーに入力する「観察トランク」と、時間的な因果関係を保ちつつ複数パッチへの注意を可能にする「ブロック因果アテンションマスク（Block-causal attention mask）」の導入。これにより、推論速度（約11ms〜）を犠牲にすることなく、高密度な視覚情報を直接利用できる。 |
| どうやって有効だと検証した？ | 4つのシミュレーション環境（Push-T, LIBERO Goal等）と3つの実世界ロボットタスク（ケーブル挿入、ペン収集、ツール吊り下げ）を用いて評価。従来手法との比較や、空間圧縮が性能に与える影響の分析、異なる事前学習済みバックボーン（DINOv2, WebSSL, V-JEPA2等）を用いた網羅的なベンチマーク実験を行った。 |
| 議論はある？ | 現在は行動模倣（Behavior Cloning）のみに焦点を当てており、強化学習への拡張が今後の課題。また、高密度のトークンはシーケンス長を増加させるため、FlashAttention等の最適化技術の導入が検討されるべきとしている。端的な視覚表現の質が性能の主要なボトルネックであることも指摘している。 |
| 次に読むべき論文は？ | [1] [An image is worth 16x16 words: Transformers for image recognition at scale](https://api.semanticscholar.org/CorpusID:225039882) <br> [6] [Dinov2: Learning robust visual features without supervision](https://api.semanticscholar.org/CorpusID:258170077) <br> [22] [Diffusion policy: Visuomotor policy learning via action diffusion](https://doi.org/10.15607/RSS.2023.XIX.026) |
| PDFリンク | https://arxiv.org/pdf/2607.18236v1 |
