---
title: "UniSHARP: Universal Sharp Monocular View Synthesis"
date: 2026-06-08
arxiv_id: 2606.07514v1
url: http://arxiv.org/abs/2606.07514v1
---

# UniSHARP: Universal Sharp Monocular View Synthesis

| 項目 | 内容 |
|---|---|
| どんなもの？ | 単一の画像から多様なカメラシステム（広角、魚眼、パノラマ、透視投影）に対応した新規視点生成を行うフィードフォワード型3Dガウススプラッティング手法。カメラモデルの依存性を排除し、未知のカメラ環境でも一貫した品質でレンダリング可能。 |
| 先行研究と比べてどこがすごい？ | 従来のSHARP等の手法がピンホールカメラ前提の制約を受けていたのに対し、UniSHARPはカメラ共通の「光線・距離空間（ray-distance space）」を採用。カメラ固有の制限なしに、広視野角から全方位パノラマまでを単一モデルで処理でき、高い一般化性能を実現した。 |
| 技術や手法のキモはどこ？ | 1. 投影によらない「光線・距離ベースのユニバーサル表現」の導入。2. 2Dセマンティック特徴と3D空間特徴を統合する「Feature Conditioned Gaussian residuals」。3. パノラマ歪みに対応した「緯度依存の確率的ドロップアウト」と、カメラパラメータがない場合でも予測可能な「ポーズフリー推論」のサポート。 |
| どうやって有効だと検証した？ | 独自のFoV（視野角）階層化ベンチマークを構築し、Perspective、Wide-FoV、Fisheye、Panoramaの各カテゴリで評価。既存手法（PanoDreamer, Matrix3D, SHARP等）と比較し、PSNR、SSIM、LPIPSの各指標で大幅な精度向上を確認した。 |
| 議論はある？ | フィードフォワードモデルの特性上、入力画像に全く映っていない領域に対する長期的な外挿（幻覚的な補完）には限界がある。今後は効率性と幾何学的一貫性を維持しつつ、より広範囲の外挿性能を高めることが課題。 |
| 次に読むべき論文は？ | [UniK3D [47]](https://arxiv.org/abs/2505.24053) (光線ベース表現の基礎), [SHARP [12]](https://arxiv.org/abs/2606.07514) (ベースとなった手法), [PanoDreamer [60]](https://arxiv.org/abs/2505.24053) |
| PDFリンク | https://arxiv.org/pdf/2606.07514v1 |
