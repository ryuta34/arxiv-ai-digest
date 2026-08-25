---
title: "ReWorld: An Interactive World Model with Long-Horizon Memory"
date: 2026-08-25
arxiv_id: 2608.23565v1
url: http://arxiv.org/abs/2608.23565v1
---

# ReWorld: An Interactive World Model with Long-Horizon Memory

| 項目 | 内容 |
|---|---|
| どんなもの？ | インタラクティブな環境で、ユーザーの操作に従いながら長期的な空間記憶を保持し、リアルタイムでストリーミング生成を行う世界モデル「ReWorld」を提案した論文。訓練時の制約と推論時のKVキャッシュ管理を分離することで、長時間のロールアウトでも安定した一貫性を実現している。 |
| 先行研究と比べてどこがすごい？ | 従来手法では短期間の制御と長期的な記憶が競合していたが、本手法は訓練時に「窓サイズ」を分ける学習と、推論時にポーズベースで検索可能なランドマークバンクを用いることで、固定メモリ予算内で長距離の一貫性を大幅に向上させた。 |
| 技術や手法のキモはどこ？ | 混合窓アテンション（Mixed per-head attention windows）による制御と記憶の分離学習、ランダムヘッドルーティングによる能力の汎化、およびカメラポーズで索引付けされたランドマークバンクによる、疎で非連続な履歴からの効率的なKVキャッシュ復元が核心。 |
| どうやって有効だと検証した？ | 40の開始画像と6種類の軌道を組み合わせたカメラ操作性ベンチマークと、回文軌道を用いた「わらの中の針（NIAH）」プロトコルによる長期記憶テストを実施。6つのベースラインモデルと比較し、制御誤差の低減と長距離の再訪精度において最高性能を達成した。 |
| 議論はある？ | 現在のメモリはカメラポーズのみに依存しているため、動的なシーンや非ナビゲーション的な対話シーンへの拡張が今後の課題として挙げられている。 |
| 次に読むべき論文は？ | [LongLive-2.0: An nvfp4 parallel infrastructure for long video generation](https://arxiv.org/abs/2605.18739)、[Worldplay: Towards long-term geometric consistency for real-time interactive world modeling](https://arxiv.org/abs/2512.14614) |
| PDFリンク | https://arxiv.org/pdf/2608.23565v1 |
