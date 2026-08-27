---
title: "Do Robotic World Models Really Follow Actions? Diagnosing and Aligning Action-Conditioned Generation for Policy Learning"
date: 2026-08-27
arxiv_id: 2608.24885v1
url: http://arxiv.org/abs/2608.24885v1
---

# Do Robotic World Models Really Follow Actions? Diagnosing and Aligning Action-Conditioned Generation for Policy Learning

| 項目 | 内容 |
|---|---|
| どんなもの？ | ロボットの行動予測モデル（AC-WM）が、指示された行動に忠実に従っているかを診断・改善・検証するためのフレームワーク。従来の「専門家デモのみの評価」に潜むオフ専門家行動への不適合を明らかにし、より信頼性の高いシミュレータとして機能させるための手法。 |
| 先行研究と比べてどこがすごい？ | 専門家デモだけでなく、摂動やポリシーロールアウトを含む広範な「オフ専門家」行動クエリを用いた評価手法（WorldEcho）を導入した点。また、視覚的整合性とSE(3)軌跡整合性を組み合わせた厳格な評価プロトコルにより、モデルの行動追従能力を詳細に診断できる点。 |
| 技術や手法のキモはどこ？ | 学習データを拡張する「分布の拡大」、モデル中間層をロボットダイナミクスに結びつける「Action-Forcing Expert (AFE)」、介入前後の変化を ground-truth と整合させる「Intervention-Effect (IE) Supervision」の3軸でモデルを強化するWorldSync手法。 |
| どうやって有効だと検証した？ | RoboTwinベンチマーク上の50タスクおよび実ロボット（カップ積みタスク）を用いて、WorldSync適用モデルが従来手法よりも低い「整合性エラー」と高い「視覚的パス率」を達成し、実際のポリシー改善において高い成功率を実現することを実証。 |
| 議論はある？ | ワールドモデルの評価範囲は大幅に拡大したが、依然として多様な環境や長期的な相互作用の網羅には課題が残る。また、視覚的整合性と行動追従性のバランスを調整する際、アーキテクチャごとに性能の伸びが異なる点。 |
| 次に読むべき論文は？ | [MiraBench](https://arxiv.org/abs/2605.29360), [WorldArena](https://arxiv.org/abs/2602.08971), [RoboTwin 2.0](https://arxiv.org/abs/2607.01060) |
| PDFリンク | https://arxiv.org/pdf/2608.24885v1 |
