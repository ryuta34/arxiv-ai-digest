---
title: "CausalCine: Real-Time Autoregressive Generation for Multi-Shot Video Narratives"
date: 2026-05-13
arxiv_id: 2605.12496v1
url: http://arxiv.org/abs/2605.12496v1
---

# CausalCine: Real-Time Autoregressive Generation for Multi-Shot Video Narratives

| 項目 | 内容 |
|---|---|
| どんなもの？ | リアルタイムかつインタラクティブなマルチショット動画生成を実現する自己回帰フレームワーク「CausalCine」。ショット境界を越えて一貫性のある物語を生成し、生成途中でのプロンプト更新にも対応する。 |
| 先行研究と比べてどこがすごい？ | 短い動画の延長にとどまりがちな従来の自己回帰モデルに対し、複数のショットをまたぐ物語の連続性、ビューポイントの変化、長期的なエンティティの一貫性を保持できる点。 |
| 技術や手法のキモはどこ？ | 長期文脈を効率的に保持する「Content-Aware Memory Routing (CAMR)」によるKVキャッシュの動的ルーティングと、動画のマルチショット構造を事前に学習させる教師強制の統合。 |
| どうやって有効だと検証した？ | 100のプロンプトを用いたベンチマークで、視覚的品質、ショット間の整合性、ショットカット精度などを評価し、既存の自己回帰ベースラインを上回り、双方向モデルに匹敵する性能を実証した。 |
| 議論はある？ | 高度な物理的整合性（微細な物体の動きや接触など）の保持には限界がある。また、大規模なモデル基盤（14Bパラメータ）を使用するため、動作にはハイエンドなGPUリソースが必要。 |
| 次に読むべき論文は？ | [Self Forcing: Bridging the Train-Test Gap in Autoregressive Video Diffusion](https://arxiv.org/abs/2506.08009) |
| PDFリンク | https://arxiv.org/pdf/2605.12496v1 |
