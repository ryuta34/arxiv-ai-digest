---
title: "Inference-Time Scaling of Diffusion Models via Progressive Seed Pruning"
date: 2026-07-24
arxiv_id: 2607.21591v1
url: http://arxiv.org/abs/2607.21591v1
---

# Inference-Time Scaling of Diffusion Models via Progressive Seed Pruning

| 項目 | 内容 |
|---|---|
| どんなもの？ | 拡散モデルやフローマッチングモデルにおいて、推論時に生成途中の評価に基づいて不要な候補を早期に削除（プルーニング）することで、限られた計算リソースを有望なサンプルに集中させる手法「Progressive Seed Pruning (PSP)」を提案している。 |
| 先行研究と比べてどこがすごい？ | 従来手法（Best-of-N等）が「推論中の並列数を固定」していたのに対し、メモリ制約を緩和して探索開始時に多量のシードを生成し、動的に計算リソースを割り当てることで、同等の計算量でプロンプト整合性の高い画像を生成できる。 |
| 技術や手法のキモはどこ？ | 推論過程で得られる denoised estimate ($\hat{x}_0$) を用いて報酬を計算し、あらかじめ設定されたスケジュールに従って低スコアな候補を段階的に削除する。決定論的なサンプラーを用いるため、計算を再実行せず、キャッシュされた中間評価に基づく高速な最適化が可能である点。 |
| どうやって有効だと検証した？ | Stable Diffusion v1.5, XL, 3.5 を用いて GenEval ベンチマークで評価。自動メトリクス（IR, HPS, GenEval）および人間による評価（プロンプト整合性）において、既存のサンプリング手法（BoN, FK-Steering, DSearch, BFS 等）を上回る性能を示した。 |
| 議論はある？ | スカラー報酬に基づいたランキングに依存するため、空間的制約などが厳しい生成には工夫が必要な点。また、細部の品質が最終段階で決まるようなタスクでは、早期のプルーニングによるゲインが限定的になる可能性があると述べている。 |
| 次に読むべき論文は？ | [1] [Universal guidance for diffusion models](https://arxiv.org/abs/2402.04796) <br> [2] [Dynamic search for inference-time alignment in diffusion models](https://arxiv.org/abs/2503.02039) |
| PDFリンク | https://arxiv.org/pdf/2607.21591v1 |
