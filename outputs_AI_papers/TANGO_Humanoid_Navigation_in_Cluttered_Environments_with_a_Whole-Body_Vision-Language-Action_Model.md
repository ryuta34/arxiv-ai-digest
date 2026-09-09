---
title: "TANGO: Humanoid Navigation in Cluttered Environments with a Whole-Body Vision-Language-Action Model"
date: 2026-09-09
arxiv_id: 2609.09158v1
url: http://arxiv.org/abs/2609.09158v1
---

# TANGO: Humanoid Navigation in Cluttered Environments with a Whole-Body Vision-Language-Action Model

| 項目 | 内容 |
|---|---|
| どんなもの？ | 複雑な室内環境での歩行や障害物回避を伴うナビゲーションを、人間のような全身動作（Whole-Body）で行うためのヒューマノイド向け視覚言語行動（VLA）フレームワーク「TANGO」。言語指示とRGB画像を入力とし、直接29自由度の関節空間アクションを出力することで、ナビゲーションと全身制御を統合的に実現する。 |
| 先行研究と比べてどこがすごい？ | 従来手法が2Dナビゲーションや高レベルコマンドによるデカップリング設計であるのに対し、TANGOは衝突回避や全身の幾何学的な適応を考慮したエンドツーエンドの全身運動生成が可能。シミュレーションで学習したモデルを、追加学習なし（Zero-shot）で実機ヒューマノイド（Unitree G1）に適用し、複雑な障害物環境を突破できる点に優位性がある。 |
| 技術や手法のキモはどこ？ | 「Plan-Edit-Track (PET)」という自動データ生成パイプラインにより、衝突のない高品質な全身動作データを大規模に構築した点。また、Qwen2.5VL-7Bをベースとした視覚言語モデル（System-2）と、リアルタイムのチャンキングを用いたフローマッチングベースの行動エキスパート（System-1）を組み合わせ、低遅延かつ高精度な実時間制御を実現した。 |
| どうやって有効だと検証した？ | シミュレーション環境「VLNVerse」および拡張された3D障害物環境にて、既存のVLNや全身制御のベースラインとSR（成功率）、SPL（経路効率）、CR（衝突率）を比較。さらに、実機ヒューマノイドを用いて、ロングホライゾンなナビゲーションや段差の跨ぎ越し、障害物の潜り抜けなどのタスクにおけるゼロショット転移性能を定量・定性的に検証した。 |
| 議論はある？ | 動作の微調整において低レベルコントローラの性能に依存していることや、RGB画像のみの入力であるため、視覚的に曖昧な環境や低照度環境下での認識精度に課題がある。今後はDepthカメラやLiDARの統合による環境理解の強化が期待される。 |
| 次に読むべき論文は？ | [12] "Collision-free humanoid traversal in cluttered indoor scenes" (arXiv:2601.16035) や [2] "Sonic: Supersizing motion tracking for natural humanoid whole-body control" (arXiv:2511.07820) |
| PDFリンク | https://arxiv.org/pdf/2609.09158v1 |
