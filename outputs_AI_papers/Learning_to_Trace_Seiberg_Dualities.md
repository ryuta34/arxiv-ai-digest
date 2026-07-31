---
title: "Learning to Trace Seiberg Dualities"
date: 2026-07-31
arxiv_id: 2607.28628v1
url: http://arxiv.org/abs/2607.28628v1
---

# Learning to Trace Seiberg Dualities

| 項目 | 内容 |
|---|---|
| どんなもの？ | 超対称性クイーバーゲージ理論におけるザイバーグ双対関係を効率的に特定するための機械学習アプローチを提案した研究。ニューラルネットワークを用いて双対性へのパスを探索し、理論間の計算複雑性を評価する。 |
| 先行研究と比べてどこがすごい？ | 従来の有限変異タイプに限定されたアプローチに対し、組み合わせ爆発が起きるより一般的なケースを扱えるようにした点。AI手法と物理学のアルゴリズム（経路探索）を組み合わせることで、従来手法を凌駕する効率性を実現した。 |
| 技術や手法のキモはどこ？ | クイーバー間の距離を予測するDistance GNNと、最適な双対変換ノードを選択するAdviser GNNを導入し、これらをA*探索やビーム探索と融合させた「ハイブリッド・パスファインダー」という探索戦略。 |
| どうやって有効だと検証した？ | 既知の弦理論に基づいた理論データセット（ID/OOD）を用い、単純な幅優先探索（BFS）や物理学的な「共通祖先探索（LCA）」をベースラインとして、成功率や探索効率（EERなど）を指標に性能を定量評価した。 |
| 議論はある？ | NNの推論が不完全な場合に経路探索が失敗する可能性があり、その「限界点（Breaking Point）」を評価。NNモデルが未知の理論に対して完全には汎化できないケースがあることや、計算資源の比較の難しさが指摘されている。 |
| 次に読むべき論文は？ | [13] Quiver Mutations, Seiberg Duality and Machine Learning, [25] DualityCert: Verifier-Gated Language-Model Repair of Broken Duality Claims in Quantum Field Theory |
| PDFリンク | https://arxiv.org/pdf/2607.28628v1 |
