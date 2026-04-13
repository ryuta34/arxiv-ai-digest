---
title: "ANTIC: Adaptive Neural Temporal In-situ Compressor"
date: 2026-04-13
arxiv_id: 2604.09543v1
url: http://arxiv.org/abs/2604.09543v1
---

# ANTIC: Adaptive Neural Temporal In-situ Compressor

| 項目 | 内容 |
|---|---|
| どんなもの？ | 科学技術計算における大規模な偏微分方程式（PDE）シミュレーションデータを、時空間の両面から効率的に圧縮するin-situ（オンライン）フレームワーク「ANTIC」を提案した。物理現象の重要度に基づいた適応的な時間サンプリングと、ニューラルフィールドの継続的学習（CFT）による空間圧縮を組み合わせることで、ストレージ要件を大幅に削減する。 |
| 先行研究と比べてどこがすごい？ | 従来の圧縮手法と異なり、物理的な変化（enstrophyやWeyl scalarなど）を監視することで、計算シミュレーション中の重要な過渡現象のみを優先的に保持する。また、ニューラルフィールドの重みに対する低ランク適応（LoRA）を用いた継続的学習により、高い圧縮率を維持しつつ、トレーニング時間の大幅な短縮（10倍以上）を実現した点。 |
| 技術や手法のキモはどこ？ | 物理量に基づいて適応的に時間ステップを制御する「Physics-aware Temporal Selector (PATS)」と、時間的に連続するスナップショット間の差分（residual）をニューラルフィールドの重み更新として学習する「Spatial Neural Compression」の二段構成。 |
| どうやって有効だと検証した？ | 2D Kolmogorov乱流と3Dブラックホール連星合体シミュレーションを用い、ストレージ効率、空間的な忠実度（物理的再現性）、および計算スループットを評価した。特にBSSN法による複雑な3Dシミュレーションにおいて、最大6807倍という極めて高い圧縮率を達成した。 |
| 議論はある？ | 現在の手法では計算負荷が依然としてソルバーより高く、リアルタイム処理にはさらなるレイテンシ低減が必要である。また、物理指標の設計が対象PDEに依存している点や、グリッド外でのデータ補完性能の検証が今後の課題として挙げられている。 |
| 次に読むべき論文は？ | ・[LoRA: Low-rank adaptation of large language models](https://arxiv.org/abs/2106.09685)<br>・[Neural fields for visual computing](https://arxiv.org/abs/2301.07767)<br>・[JAX: Composable transformations of Python+NumPy programs](https://arxiv.org/abs/1803.00245) |
| PDFリンク | https://arxiv.org/pdf/2604.09543v1 |
