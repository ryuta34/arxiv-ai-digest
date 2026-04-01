---
title: "OmniRoam: World Wandering via Long-Horizon Panoramic Video Generation"
date: 2026-04-01
arxiv_id: 2603.30045v1
url: http://arxiv.org/abs/2603.30045v1
---

# OmniRoam: World Wandering via Long-Horizon Panoramic Video Generation

| 項目 | 内容 |
|---|---|
| どんなもの？ | ユーザー指定のカメラ軌道に沿って、一貫性のあるパノラマビデオを生成するフレームワーク「OmniRoam」。長時間のシーン探索を可能にするため、粗いプレビュー生成と高精細なリファインの2段階アプローチを採用している。 |
| 先行研究と比べてどこがすごい？ | 従来のパースペクティブビデオモデルで見られた長時間の撮影に伴う歪みや崩れを、パノラマ表現の持つ全体的な空間整合性によって克服した点。また、独自の「Loop Consistency」指標を提案し、長期的な空間的一貫性を定量評価できるようにした点。 |
| 技術や手法のキモはどこ？ | カメラの動きを「方向（flow）」と「尺度（scale）」に分解する制御手法と、グローバルな構造を先に生成してから詳細を強化する「Global-to-Local（プレビュー・リファイン）」設計。さらに、回転不変な座標系と3DGSを活用したトレーニングデータセットの構築。 |
| どうやって有効だと検証した？ | インターネット上の画像を入力とした定性的比較および、複数の指標（FAED, SSIM, LPIPS, PSNR）を用いた定量的比較を実施。特に閉ループ軌道を用いた長期的な空間整合性の検証を行い、既存手法（Matrix-3D等）に対する優位性を実証した。 |
| 議論はある？ | 計算コストの制約により、高解像度での一括生成は不可能であること。また、生成されるビデオの品質は学習データの多様性に依存し、未知の環境や極端なカメラ動作に対しては課題が残る可能性がある。 |
| 次に読むべき論文は？ | [Matrix-3D: Omnidirectional Explorable 3D World Generation](https://arxiv.org/abs/2508.08086), [CamPVG: Camera-Controlled Panoramic Video Generation with Epipolar-Aware Diffusion](https://arxiv.org/abs/2501.12185) |
| PDFリンク | https://arxiv.org/pdf/2603.30045v1 |
