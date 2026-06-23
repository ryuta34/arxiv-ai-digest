---
title: "CoorDex: Coordinating Body and Hand Priors for Continuous Dexterous Humanoid Loco-Manipulation"
date: 2026-06-23
arxiv_id: 2606.23680v1
url: http://arxiv.org/abs/2606.23680v1
---

# CoorDex: Coordinating Body and Hand Priors for Continuous Dexterous Humanoid Loco-Manipulation

| 項目 | 内容 |
|---|---|
| どんなもの？ | 高自由度の人型ロボットにおいて、全身の移動と器用な手先操作を同時に行う「Loco-Manipulation（移動操作）」を実現する学習パイプライン。従来のストップ・アンド・ゴー方式を脱却し、歩行しながら物体を掴む・運ぶといった連続的な動作を可能にする。 |
| 先行研究と比べてどこがすごい？ | 従来手法は全身制御と手先制御を個別に扱うか、低自由度のグリッパーに限定されることが多かったが、本手法は全身（29DoF）と手先（20DoF）を協調的な潜在変数として統合することで、高次元かつ接触を伴う複雑なタスクを学習可能にした点。 |
| 技術や手法のキモはどこ？ | 全身と手先の動作をそれぞれ教師あり学習で潜在空間に事前定義（プリオ）し、それらを「協調トランク（Coordination Trunk）」を介して結合する点。潜在空間上で残差制御を行うことで、探索効率と動作の自然さを両立させている。 |
| どうやって有効だと検証した？ | Isaac Lab環境において「歩きながらのボトル把持」「冷蔵庫のドア開け」「歩行中の物体持ち替え」の3タスクを実施。従来手法（関節直接制御や単純な潜在変数結合）と比較し、高い成功率を達成したことを定量的・定性的に示した。 |
| 議論はある？ | 現在は教師あり学習によるプリビレッジ（特権的）な状態情報を前提としているため、視覚情報を用いた実世界への転送が未解決。また、長距離タスクにおける探索には段階的なカリキュラム学習（NoDemoRSI）が必要となる。 |
| 次に読むべき論文は？ | [11] [Universal humanoid motion representations](https://arxiv.org/abs/2403.01294)、[29] [ManipTrans](https://arxiv.org/abs/2503.21860)、[32] [Isaac Lab](https://arxiv.org/abs/2511.04831) |
| PDFリンク | https://arxiv.org/pdf/2606.23680v1 |
