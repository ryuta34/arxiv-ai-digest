---
title: "ProxyPose: 6-DoF Pose Tracking via Video-to-Video Translation"
date: 2026-07-08
arxiv_id: 2607.06555v1
url: http://arxiv.org/abs/2607.06555v1
---

# ProxyPose: 6-DoF Pose Tracking via Video-to-Video Translation

| 項目 | 内容 |
|---|---|
| どんなもの？ | 6自由度（6-DoF）の物体・表面姿勢トラッキングを「動画から動画への変換」問題として再定義する新しい手法「ProxyPose」です。特別な3Dモデルや深度情報、セグメンテーションなしで、単眼動画と最初の1フレームの点指定のみから高精度な姿勢推定を実現します。 |
| 先行研究と比べてどこがすごい？ | 3Dモデルや深度センサ、物体マスク、事前のセグメンテーションといった追加の入力情報が不要です。テクスチャレスな物体、透明・反射素材、非剛体表面に対しても頑健に追跡できるため、従来手法が苦手としていた動的かつ自由な環境でのトラッキングが可能です。 |
| 技術や手法のキモはどこ？ | 動画拡散モデルを微調整し、指定したピクセル点における局所的な動きを「カラーポリヘドロン（立方体）」の動きとして合成（プロキシ動画生成）する点です。既知の形状と色の立方体に変換することで、従来型の幾何学的解法（PnP）で姿勢を簡単に算出可能にしました。 |
| どうやって有効だと検証した？ | HO3DやYCBInEOATといった動的姿勢推定のベンチマークデータセットで、既存の最先端手法（FoundationPoseやCoTracker等）と精度を比較しました。また、反射・透明物体の追跡や、顔トラッキング、カメラ姿勢推定といった実世界の複雑な動画でも定性評価を行っています。 |
| 議論はある？ | 現在の課題として、動画モデルの生成長によるフレーム数の制限や、超高速移動時のVAEブラー（ボケ）による精度低下が挙げられます。また、流体のような定義が難しい表面での追跡ドリフトや、推論に要する計算時間（数分）も今後の改善点です。 |
| 次に読むべき論文は？ | [Wan: Open and advanced large-scale video generative models](https://arxiv.org/abs/2503.20314)（基盤モデル）、[CoTracker: It is better to track together](https://arxiv.org/abs/2403.05121)（点追跡）、[FoundationPose: Unified 6D pose estimation and tracking of novel objects](https://arxiv.org/abs/2401.03429)（姿勢推定） |
| PDFリンク | https://arxiv.org/pdf/2607.06555v1 |
