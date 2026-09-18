---
title: "Workspace Models: Lightweight Robotic Memory via Saliency-Driven Supervision"
date: 2026-09-18
arxiv_id: 2609.20820v1
url: http://arxiv.org/abs/2609.20820v1
---

# Workspace Models: Lightweight Robotic Memory via Saliency-Driven Supervision

| 項目 | 内容 |
|---|---|
| どんなもの？ | ロボットが複雑な作業を遂行するために必要な長期記憶を、推論時の計算負荷を抑えつつ効率的に生成する「Workspace Model」を提案した論文。事前学習済みモデルの推論能力を学習時に活用し、軽量な潜在表現「ワークスペース・トークン」へ蒸留することで、実行時の低レイテンシと高いタスク成功率を両立した。 |
| 先行研究と比べてどこがすごい？ | 従来手法（Keyframe法など）は実行時にVLMへ問い合わせるため計算コストとレイテンシが高く、また入力の不連続性が原因で制御エラーを招いていた。本手法は学習時にVLMによる教師信号（Saliency-driven supervision）を使い、モデル自体に記憶能力を埋め込むため、デプロイ時にVLMの推論を一切必要とせず、かつ制御の滑らかさとタスク遂行能力が向上した点。 |
| 技術や手法のキモはどこ？ | 学習時にVLMを用いて各時刻のタスク関連イベントを特定し、関連するパッチを特定して抽出する「Saliency-driven supervision」。さらに、抽出した情報をデコーダで復元させる「集合再構成損失（Set-reconstruction loss）」を用いることで、ロボットのポリシーが効率的な「ワークスペース・トークン」を学習できる設計。 |
| どうやって有効だと検証した？ | ManiSkill3を用いた3つのシミュレーション環境（CubeDrop、DrawerRecall、BalanceBar）と、実機のFranka FR3ロボット（HalfAndHalf）で検証。ベースライン（VanillaDP, HistoryDP, Keyframe）と比較し、平均成功率91.5%と他手法を大きく上回る性能を実証した。 |
| 議論はある？ | 現在は完全自己回帰型トランスフォーマーを使用しているため、系列長が長くなると計算コストが二次的に増大する課題がある。今後は回帰的な構造やブロック対角アテンションの採用による効率化や、報酬を用いた強化学習によるグラウンディングの強化が期待される。 |
| 次に読むべき論文は？ | [Diffusion policy (Chi et al., 2023)](https://arxiv.org/abs/2303.04137)、[Bpp: Long-context robot imitation learning by focusing on key history frames (Mark et al., 2026)](https://arxiv.org/abs/2602.15010)、[Molmopoint: Better pointing for vlms with grounding tokens (Clark et al., 2026)](https://arxiv.org/abs/2603.28069) |
| PDFリンク | https://arxiv.org/pdf/2609.20820v1 |
