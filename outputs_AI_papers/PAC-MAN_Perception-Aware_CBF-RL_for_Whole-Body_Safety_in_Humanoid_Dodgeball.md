---
title: "PAC-MAN: Perception-Aware CBF-RL for Whole-Body Safety in Humanoid Dodgeball"
date: 2026-07-31
arxiv_id: 2607.28623v1
url: http://arxiv.org/abs/2607.28623v1
---

# PAC-MAN: Perception-Aware CBF-RL for Whole-Body Safety in Humanoid Dodgeball

| 項目 | 内容 |
|---|---|
| どんなもの？ | ヒューマノイドロボットが頭部カメラからの視覚情報のみを用いて、飛来するボールを全身で回避する「ドッジボール」タスクを実現するフレームワーク「PAC-MAN」の提案。強化学習に制御バリア関数（CBF）による安全性のガイダンスを組み合わせ、限られた視覚情報下でも高度な回避行動を可能にした。 |
| 先行研究と比べてどこがすごい？ | 従来は精緻な状態推定やオンラインでの計算負荷が高いCBFが必要だったが、本研究では学習時にCBFで安全性を内部化（学習）させることで、実行時には複雑なフィルタリングなしで高い回避成功率（95%）を実現した点。 |
| 技術や手法のキモはどこ？ | 学習時にのみ全関節やリンクを考慮した「Joint-CBF」と、軽量なリンク単位の報酬「Link-CBF」を用いて安全性を報酬関数に組み込み、ポリシー自体に安全な反射行動を学習させたこと。さらにAMP（Adversarial Motion Prior）で自然な身体運動を正則化した点。 |
| どうやって有効だと検証した？ | シミュレーション上で、情報の観測レベル（固定カメラ、アクティブジンバル、状態オラクル）と安全策モードを比較評価。その後、実機のUnitree G1に実装し、実環境下で20回の投球に対する回避成功率を測定した。 |
| 議論はある？ | 現在のシステムは固定カメラを使用しているため、追跡能力に限界がある。今後は、セグメンテーションによるトラッキングを用いたアクティブジンバル化や、静止状態だけでなく歩行中の回避タスクへの拡張が課題。 |
| 次に読むべき論文は？ | [11] L. Yang et al., “CBF-RL: Safety filtering reinforcement learning in training with control barrier functions,” ICRA 2026. ※PAC-MANの基盤となった手法。 |
| PDFリンク | https://arxiv.org/pdf/2607.28623v1 |
