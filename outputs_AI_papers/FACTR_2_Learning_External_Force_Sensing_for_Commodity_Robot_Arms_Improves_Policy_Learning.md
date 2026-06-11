---
title: "FACTR 2: Learning External Force Sensing for Commodity Robot Arms Improves Policy Learning"
date: 2026-06-11
arxiv_id: 2606.12406v1
url: http://arxiv.org/abs/2606.12406v1
---

# FACTR 2: Learning External Force Sensing for Commodity Robot Arms Improves Policy Learning

| 項目 | 内容 |
|---|---|
| どんなもの？ | センサーレスで安価なロボットアームでも外部トルクを推定し、接触を伴う作業の精度を向上させる手法「FACTR 2」を提案した。この手法は、ニューラルネットワークによる外部トルク推定と、接触段階を重視した学習データのリサンプリング訓練から構成される。 |
| 先行研究と比べてどこがすごい？ | 専用の力覚センサーを必要とせず、わずか10分間の自由運動データと1分間の学習で、高価なトルクセンサーと同等の推定性能を実現した。また、接触前後の重要なフェーズを訓練データ上で強調することで、従来の学習手法を17%上回るタスク成功率を達成した。 |
| 技術や手法のキモはどこ？ | NEXT（Neural External Torque Estimation）による、時系列履歴を用いた逆動力学モデルでの高精度トルク推定と、FIRST（Force-Informed Re-Sampling Training）による、接触状態に基づいた訓練データの動的なアップサンプリング（重み付け）。 |
| どうやって有効だと検証した？ | Frankaアームを用いた外部トルク推定精度の定量評価、およびPiperやYAMといった安価なロボットアームを用いた力覚フィードバック・テレオペレーションと、5つの高難度な接触作業タスクでの成功率向上により検証した。 |
| 議論はある？ | 外部トルクの絶対的なスケール精度がモーターのトルク定数に依存する点や、モデルがロボットアームごとに特化しており、ハードウェアが変わるごとに再学習が必要であるという制限がある。 |
| 次に読むべき論文は？ | [6] J. J. Liu et al., "FACTR: Force-Attending Curriculum Training for Contact-Rich Policy Learning", RSS 2025. [45] M. Reuss et al., "Multimodal diffusion transformer", RSS 2024. |
| PDFリンク | https://arxiv.org/pdf/2606.12406v1 |
