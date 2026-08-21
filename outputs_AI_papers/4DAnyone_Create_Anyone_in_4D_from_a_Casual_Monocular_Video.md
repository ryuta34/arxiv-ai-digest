---
title: "4DAnyone: Create Anyone in 4D from a Casual Monocular Video"
date: 2026-08-21
arxiv_id: 2608.20335v1
url: http://arxiv.org/abs/2608.20335v1
---

# 4DAnyone: Create Anyone in 4D from a Casual Monocular Video

| 項目 | 内容 |
|---|---|
| どんなもの？ | カジュアルな単一視点の動画から、再構築に適した高品質な多視点動画を生成し、4D Gaussian Splatting（4DGS）を用いて動的な4D人間アバターを生成するフレームワーク。 |
| 先行研究と比べてどこがすごい？ | 従来手法が抱えていた「コンテキスト長制限による一貫性の低下」と「グループ間の構造的ドリフト」という二つのボトルネックを解消した。これにより、カメラパラメータが不明な環境下でも、安定した多視点動画と高精度な4D再構築を実現している。 |
| 技術や手法のキモはどこ？ | 生成したビューを圧縮して固定長で管理する「Reference Context Packing (RCP)」と、生成過程の高ノイズステップでグループ間を循環的に入れ替えることで構造的整合性を保つ「Target Context Routing (TCR)」の2点。 |
| どうやって有効だと検証した？ | DNA-RenderingおよびDyMVHumansデータセットを用い、生成動画の一貫性、4DGS再構築品質、視覚的なNovel View合成品質の観点で比較評価を実施。従来手法を上回るPSNR、SSIM等のスコアを達成。 |
| 議論はある？ | 衣服が大きく体に密着しない場合の表現の不安定さや、HMR（人体ポーズ推定）の精度に生成結果が依存するため、ポーズ推定を誤ると一貫して誤ったポーズが生成されるといった限界がある。 |
| 次に読むべき論文は？ | [FreeTimeGS](https://arxiv.org/abs/2501.12781), [Wan-Animate](https://arxiv.org/abs/2509.14055), [FramePack](https://arxiv.org/abs/2503.11195) |
| PDFリンク | https://arxiv.org/pdf/2608.20335v1 |
