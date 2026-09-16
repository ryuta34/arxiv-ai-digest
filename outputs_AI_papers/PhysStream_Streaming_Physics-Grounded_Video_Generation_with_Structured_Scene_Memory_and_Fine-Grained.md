---
title: "PhysStream: Streaming Physics-Grounded Video Generation with Structured Scene Memory and Fine-Grained Motion Control"
date: 2026-09-16
arxiv_id: 2609.17521v1
url: http://arxiv.org/abs/2609.17521v1
---

# PhysStream: Streaming Physics-Grounded Video Generation with Structured Scene Memory and Fine-Grained Motion Control

| 項目 | 内容 |
|---|---|
| どんなもの？ | 物理法則に基づいたマルチオブジェクトの挙動を、ユーザーによるスパースな速度制御（インタラクティブな指示）を通じて生成する autoregressive な画像から動画への変換モデル。卓上の剛体や変形物に対して、物理的に自然な衝突や挙動を生成することができる。 |
| 先行研究と比べてどこがすごい？ | 従来手法は生成開始前に全制御スケジュールが必要か、ピクセルレベルの密度が高い制御を必要としたが、本手法は生成中に随時介入が可能であり、かつ物理量（速度）で制御するため物理的整合性が高い。 |
| 技術や手法のキモはどこ？ | 過去の生成フレームからオンラインで推定される「構造化シーンメモリ（位置マップとオブジェクト追跡マップ）」を条件付けに用いる点と、bidirectionalな教師モデルから causal なautoregressiveモデルへ2段階で学習させる手法。 |
| どうやって有効だと検証した？ | 10万件の合成データセットを用いた物理指標（FVD, FVMD, Traj-ADE等）での定量的評価に加え、実世界の映像を用いたMLLM（GPT-4o）による評価および人間による比較研究を実施した。 |
| 議論はある？ | tumbling（回転・転倒）のような極めて複雑な動きには依然として課題がある。また、対象が剛体に限定されており、よりリッチな素材への対応にはデータセットの拡張が必要。リアルタイム生成については今後の課題としている。 |
| 次に読むべき論文は？ | [Causal Forcing](https://arxiv.org/abs/2602.02214)、[RealWonder](https://arxiv.org/abs/2603.05449)、[DragStream](https://arxiv.org/abs/2510.03550) |
| PDFリンク | https://arxiv.org/pdf/2609.17521v1 |
