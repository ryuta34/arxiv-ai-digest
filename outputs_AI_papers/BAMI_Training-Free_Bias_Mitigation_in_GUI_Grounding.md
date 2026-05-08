---
title: "BAMI: Training-Free Bias Mitigation in GUI Grounding"
date: 2026-05-08
arxiv_id: 2605.06664v1
url: http://arxiv.org/abs/2605.06664v1
---

# BAMI: Training-Free Bias Mitigation in GUI Grounding

| 項目 | 内容 |
|---|---|
| どんなもの？ | GUIエージェントにおけるクリックやドラッグ等の要素特定（GUI Grounding）を、学習不要かつ推論時の工夫のみで高精度化する手法「BAMI」を提案した論文。既存モデルが抱える精度・曖昧性のバイアスを、マルチステップの構造的推論で解消する。 |
| 先行研究と比べてどこがすごい？ | 再学習や微調整を一切必要とせず、既存のGUIモデルに直接適用可能な点。Masked Prediction Distribution (MPD) を用いた誤差分析により、故障原因を「精度バイアス」と「曖昧性バイアス」と明示的に切り分けた点が新しい。 |
| 技術や手法のキモはどこ？ | 「Coarse-to-Fine Focus」（階層的クロッピングによる局所解像度の向上）と「Candidate Selection」（複数候補の生成とGUIの優先ルールに基づく外部モデルでの選択）を組み合わせた点。 |
| どうやって有効だと検証した？ | ScreenSpot-Pro等の難関ベンチマークで検証。TianXi-Action-7Bモデルに適用し、正解率を51.9%から57.8%へ向上させるなど、各種モデルのバックボーンで一貫した精度向上を示した。 |
| 議論はある？ | 言語モデルの推論回数が増えるため計算コストは増加する。また、提示された手法はInductive Biasの解消には有効だが、モデル自体の知識不足に起因するエラー（Knowledge Gap）の完全な解決には至っていない。 |
| 次に読むべき論文は？ | [ScreenSpot-Pro](https://arxiv.org/abs/2504.07981)、[UI-TARS](https://arxiv.org/abs/2501.12326)、[Mind2Web](https://arxiv.org/abs/2306.00958) |
| PDFリンク | https://arxiv.org/pdf/2605.06664v1 |
