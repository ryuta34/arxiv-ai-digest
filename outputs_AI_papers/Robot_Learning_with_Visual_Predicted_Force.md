---
title: "Robot Learning with Visual Predicted Force"
date: 2026-10-06
arxiv_id: 2610.04741v1
url: http://arxiv.org/abs/2610.04741v1
---

# Robot Learning with Visual Predicted Force

| 項目 | 内容 |
|---|---|
| どんなもの？ | 接触を伴う複雑なマニピュレーションタスクにおいて、力覚センサや触覚センサを用いず、視覚情報のみからグリッパーの変形を捉えて力を予測・制御する手法。カメラ映像からグリッパーの変形を推定し、目標の力に近い動作を推論時に動的に選択することで、接触作業の成功率を大幅に向上させた。 |
| 先行研究と比べてどこがすごい？ | 高価なF/Tセンサや摩耗しやすい触覚センサを不要とし、3Dプリントした安価なFin Rayグリッパーと汎用カメラのみで構成可能。デプロイ時にハードウェアの変更や再キャリブレーションが不要で、視覚情報のみで安定した力加減が必要な作業（ベリーの摘み取りやプラグ挿入等）を実現した点。 |
| 技術や手法のキモはどこ？ | ①SAM2でグリッパーをセグメンテーションし、Sobelフィルタで変形を強調する視覚的力推定器の開発。②推定された力で教師データにラベル付けを行うこと。③推論時にポリシーから複数の「動作と推定力」のペアをサンプリングし、タスクに応じた目標力に最も近いものを選択する「Action-Force Proposal Policy」の採用。 |
| どうやって有効だと検証した？ | 4つの接触リッチなタスク（ベリーの摘み取り、空き缶の把持、プレートの再配向、プラグ挿入）で評価。ベースラインの「単一サンプル推論」と比較し、全てのタスクで成功率が向上した（例：ベリー摘み取りで0%→73.3%、プラグ挿入で26.7%→73.3%）。 |
| 議論はある？ | タスクごとに適した目標力を人間が設定する必要がある点、正常な把持力（法線方向）のみを推定し摩擦力やトルクを扱えない点。また、オンラインでの視覚的な力フィードバックを行っていないため、急激な接触変化への適応に限界がある。 |
| 次に読むべき論文は？ | [1] [Calandra et al., "More than a feeling: Learning to grasp and regrasp using vision and touch"](https://arxiv.org/abs/1710.03848) <br> [42] [Choi et al., "In-the-wild compliant manipulation with UMI-FT"](https://arxiv.org/abs/2601.09988) <br> [54] [Chi et al., "Diffusion policy: Visuomotor policy learning via action diffusion"](https://arxiv.org/abs/2303.04137) |
| PDFリンク | https://arxiv.org/pdf/2610.04741v1 |
