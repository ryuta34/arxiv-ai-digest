---
title: "FVAttn: Adaptive Sparse Attention with Runtime Load Balancing for Video Generation"
date: 2026-07-20
arxiv_id: 2607.16190v1
url: http://arxiv.org/abs/2607.16190v1
---

# FVAttn: Adaptive Sparse Attention with Runtime Load Balancing for Video Generation

| 項目 | 内容 |
|---|---|
| どんなもの？ | ビデオ生成用Diffusion Transformer（DiT）の推論における、適応的疎注意（Adaptive Sparse Attention）特有の負荷不均衡を解消する推論システム「FVAttn」です。マルチGPUのシーケンス並列環境下で、動的な負荷分散と余剰計算リソースの有効活用を実現し、ビデオ生成の推論を高速化します。 |
| 先行研究と比べてどこがすごい？ | 既存の静的な負荷分散やプロファイルベースの手法と異なり、実行時の動的なマスク情報に基づき、低オーバーヘッドなP2Pヘッド移動でランク間の計算負荷を即座に平準化します。さらに、余った計算リソースを高品質なブロックの追加計算に再投資することで、精度と速度の両立において従来手法を上回るパレートフロンティアを達成しました。 |
| 技術や手法のキモはどこ？ | ①「Runtime Load Balancing (RLB)」：マスク生成後に各ランクの負荷を特定し、最小限の通信で過負荷なヘッドを移動させる。②「Slack-Aware Sparse Augmentation (SASA)」：負荷分散後の余剰時間を利用し、重要度の高いブロックを計算することでモデルの推論精度を向上させる。③「Overlapped Execution」：スケジューリングや通信を既存の量子化プロセス等とオーバーラップさせ、オーバーヘッドを最小化する。 |
| どうやって有効だと検証した？ | Wan2.2 I2V, Wan2.2 Animate, Wan2.1 T2Vなどの大規模ビデオ生成モデルを用い、NVIDIA H20 GPU 8基の環境で評価しました。FlashAttentionと比較して最大4.41倍の注意計算の高速化、およびDiT推論全体で2倍以上の高速化を達成し、VBenchを用いた品質評価でも競合手法より優れた結果を示しました。 |
| 議論はある？ | 長い時空間シーケンス生成に最適化されており、画像生成のような疎性が低いタスクや、GPU間通信帯域が制限される環境では効果が限定的になる可能性があります。また、現在の実装はUlyssesシーケンス並列に依存しており、他の並列手法への拡張が今後の課題です。 |
| 次に読むべき論文は？ | [2] db-sp: Accelerating sparse attention for visual generative models with dual-balanced sequence parallelism、[10] Dsa: Efficient inference for video generation models via distributed sparse attention、[23] Spargeattn: Accurate sparse attention accelerating any model inference |
| PDFリンク | https://arxiv.org/pdf/2607.16190v1 |
