---
title: "Think Harder Where It Matters: Item-Level Adaptive Recursion for Sequential Recommendation"
date: 2026-10-22
arxiv_id: 2610.30128v1
url: http://arxiv.org/abs/2610.30128v1
---

# Think Harder Where It Matters: Item-Level Adaptive Recursion for Sequential Recommendation

| 項目 | 内容 |
|---|---|
| どんなもの？ | 逐次レコメンデーションにおいて、全アイテムを一律の深さで処理するのではなく、アイテムごとの計算需要に応じて適応的に計算量を割り当てる手法「LoopRec」を提案した。各アイテムに対し、重み共有ブロックと軽量なゲートを用いて、早期終了または継続の判断を逐次的に行う。 |
| 先行研究と比べてどこがすごい？ | 従来は全アイテムに対し固定の計算量を課していたが、本手法はアイテムごとの異質な計算需要（重要度や複雑さの差）を学習し、計算リソースをより重要なアイテムに集中させることで、精度向上と計算効率化を両立させた点。 |
| 技術や手法のキモはどこ？ | 単一の重み共有ブロックを再帰的に適用するアーキテクチャと、各再帰境界に配置された学習可能な「バイナリ・ルーティング・ゲート」である。これにより、補助的なラベルなしで、アイテムごとに適応的な停止判断を可能にした。 |
| どうやって有効だと検証した？ | Amazonのデータセット（Software, Office, Patio）を用いて、SASRecやBSARec等の4つのバックボーンで実験。固定深さモデルと比較して一貫した精度改善（NDCG@20等）を確認し、ルーティングパターンが「稀なアイテム」や「直近のアイテム」に深い計算を割り当てていることを示した。 |
| 議論はある？ | 計算上の節約は可能だが、必ずしもGPU等のハードウェアにおける実時間（壁時計時間）の短縮に直結しない場合があること。また、最大再帰回数の設定が現状では固定であること。 |
| 次に読むべき論文は？ | [1] Mixture-of-recursions: Learning dynamic recursive depths for adaptive token-level computation (Bae et al., 2026), [41] Scaling latent reasoning via looped language models (Zhu et al., 2025) |
| PDFリンク | https://arxiv.org/pdf/2610.30128v1 |
