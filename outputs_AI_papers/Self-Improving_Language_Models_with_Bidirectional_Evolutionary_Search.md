---
title: "Self-Improving Language Models with Bidirectional Evolutionary Search"
date: 2026-05-28
arxiv_id: 2605.28814v1
url: http://arxiv.org/abs/2605.28814v1
---

# Self-Improving Language Models with Bidirectional Evolutionary Search

| 項目 | 内容 |
|---|---|
| どんなもの？ | 大規模言語モデルやエージェントの推論能力向上を目的とした、双方向進化探索（Bidirectional Evolutionary Search, BES）フレームワークです。前方向への進化型探索と、後方向への目標分解という二つのプロセスを組み合わせることで、複雑な問題に対する効率的な探索を実現します。 |
| 先行研究と比べてどこがすごい？ | 従来のベスト・オブ・Nサンプリングや木探索が抱える「検証信号の疎さ」と「モデルの既存分布からの逸脱困難性」という二つの課題を解決しました。進化オペレーターを用いてモデルの確率分布の制約（エントロピーの殻）を打破し、目標分解によって密なフィードバックを生成することで、少ないサンプル数で高い解探索性能を達成します。 |
| 技術や手法のキモはどこ？ | 4つの進化オペレーター（組み合わせ、削除、置換、交叉）による既存軌跡の再構築と、元課題を検証可能なサブゴールに再帰的に分割する後方向探索の組み合わせです。これにより、単なる逐次拡張では到達困難な低確率領域への探索が可能になります。 |
| どうやって有効だと検証した？ | 論理推論（Knights-and-Knaves）やマルチホップ推論（MuSiQue）を用いた学習（Post-Training）実験、および円詰めやハイルブロン問題などのオープンな最適化課題における推論実験を通じて評価しました。いずれの環境でも従来の手法を大幅に上回る性能を達成しています。 |
| 議論はある？ | 客観的な報酬信号がないタスク（主観的な文章作成など）には適用が困難である点や、非常に弱いモデルでは目標分解能力が制限される点、および計算リソースの制約上8Bまでのモデルでしか検証できていない点が挙げられています。 |
| 次に読むべき論文は？ | [Tree-GRPO (Ji et al., 2026)](https://openreview.net/forum?id=ZpQwAFhU13)、[ShinkaEvolve (Lange et al., 2025)](https://arxiv.org/abs/2509.19349)、[AlphaEvolve (Novikov et al., 2025)](https://arxiv.org/abs/2506.13131) |
| PDFリンク | https://arxiv.org/pdf/2605.28814v1 |
