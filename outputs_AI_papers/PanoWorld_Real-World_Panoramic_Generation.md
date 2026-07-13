---
title: "PanoWorld: Real-World Panoramic Generation"
date: 2026-07-13
arxiv_id: 2607.09661v1
url: http://arxiv.org/abs/2607.09661v1
---

# PanoWorld: Real-World Panoramic Generation

| 項目 | 内容 |
|---|---|
| どんなもの？ | 高忠実度かつ制御可能なパノラマ動画生成のためのフレームワーク「PanoWorld」。回転不変性と翻訳の分離を利用し、複雑なカメラ軌道に追従しながら、長時間の視覚的一貫性と幾何学的整合性を維持する。 |
| 先行研究と比べてどこがすごい？ | 従来のパノラマモデルが抱えていた視点シフト時のメモリ不整合を解決し、明示的な3D再構成なしで高精度な軌道制御と長時間のシーン持続性を両立した点。また、実世界とシミュレーションを統合した大規模ベンチマーク「World360」を構築した。 |
| 技術や手法のキモはどこ？ | パノラマの回転不変性を利用して回転と翻訳を分離し、Dense Panoramic Ray-Conditioning (DPRC) により幾何学的に正しいモーションをモデル化。さらに、Geometry-aware Memory Augmentation (GMA) を用いて、過去のフレームを幾何学的に整合性の取れた空間として保持・参照する点。 |
| どうやって有効だと検証した？ | 構築したデータセット「World360」を用い、FID等の分布忠実度指標や、PSNRによる軌道制御精度の評価を実施。ViPEを用いたカメラポーズ再構成による精量的評価も行い、既存手法（Matrix-3D, OmniRoam等）を大幅に上回る性能を実証した。 |
| 議論はある？ | 入力画像をそのまま初期フレームとして複製する手法が、初期と生成フレーム間の分布乖離を招き、長時間経過で品質が徐々に劣化する可能性がある。今後は境界の洗練モジュールや動的なメモリ管理による改善が検討課題。 |
| 次に読むべき論文は？ | [OmniRoam: World wandering via long-horizon panoramic video generation](https://arxiv.org/abs/2603.30045) |
| PDFリンク | https://arxiv.org/pdf/2607.09661v1 |
