---
title: "EgoForce: Forearm-Guided Camera-Space 3D Hand Pose from a Monocular Egocentric Camera"
date: 2026-05-13
arxiv_id: 2605.12498v1
url: http://arxiv.org/abs/2605.12498v1
---

# EgoForce: Forearm-Guided Camera-Space 3D Hand Pose from a Monocular Egocentric Camera

| 項目 | 内容 |
|---|---|
| どんなもの？ | 単眼エゴセントリック（一人称視点）カメラから、前腕の情報を活用して高精度なカメラ空間での3D手・腕の姿勢と形状を復元するフレームワーク。多様なカメラモデル（魚眼、歪みあり等）に単一のネットワークで対応する。 |
| 先行研究と比べてどこがすごい？ | 従来手法は単眼カメラ特有の奥行きとスケールの曖昧さや、広角レンズの歪みに弱かった。本手法はカメラモデルに依存しないレイ空間（Ray Space）での解法と前腕の幾何学的制約を用いることで、カメラ空間での位置推定誤差を最大28%削減した。 |
| 技術や手法のキモはどこ？ | ①前腕を考慮した統一的なTransformerアーキテクチャ（HALO）、②カメラの歪みやクロップ情報を明示的にエンコードするCrop Intrinsics Token (CIT)、③ピクセル座標ではなく、較正済みカメラモデルに基づくレイ（光線）上の制約として解く「レイ空間ソルバー」。 |
| どうやって有効だと検証した？ | ARCTIC、HOT3D、H2Oなど複数の主要な一人称視点ベンチマークで評価。既存のカメラ空間推定手法（MobRecon, HandOccNet, HandDGP等）と比較し、articulation（姿勢）とcamera-space（絶対位置）の両面で最高精度を達成した。 |
| 議論はある？ | 手首から先と前腕のメタ的なスケール調整には課題が残る。また、極端な遮蔽や高速な動きには限界があり、より大局的な人体モデリングとの統合が将来課題。 |
| 次に読むべき論文は？ | [UmeTrack](https://arxiv.org/abs/2209.08381), [HaMeR](https://arxiv.org/abs/2312.06682), [HandDGP](https://arxiv.org/abs/2403.11894) |
| PDFリンク | https://arxiv.org/pdf/2605.12498v1 |
