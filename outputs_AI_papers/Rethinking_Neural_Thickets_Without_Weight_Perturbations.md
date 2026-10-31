---
title: "Rethinking Neural Thickets Without Weight Perturbations"
date: 2026-10-31
arxiv_id: 2610.40649v1
url: http://arxiv.org/abs/2610.40649v1
---

# Rethinking Neural Thickets Without Weight Perturbations

| 項目 | 内容 |
|---|---|
| どんなもの？ | 大規模言語モデルの重みをランダムに摂動させることで精度が向上する現象（Neural Thickets）に対し、重みの摂動自体は不要であることを示した論文。代わりに、モデルを凍結したまま出力ロジットにランダムなバイアスを加えて選択・投票を行う手法「Logit PSV」を提案した。 |
| 先行研究と比べてどこがすごい？ | 重み空間を直接操作するのではなく、出力空間のみを操作することで、計算コストを抑えつつ同等以上の精度向上を実現した。また、Neural Thicketsの本質が「専門家の探索」ではなく「出力の多様化・検証・アンサンブル」であることを理論的・実験的に解明した。 |
| 技術や手法のキモはどこ？ | モデルを完全に凍結し、推論時に出力ロジットへ固定のガウスバイアス（Perturb）を加え、検証セットで性能の良いものを選抜（Select）し、最後に多数決（Vote）を行うPerturb-Select-Vote (PSV) フレームワークの導入。 |
| どうやって有効だと検証した？ | 言語モデル（OLMo, Qwen2.5）を用いた数学・推論タスク、および視覚モデル（DINOv3）を用いたドメインシフト下での画像分類タスクで、フルウェイトの摂動と比較・検証した。 |
| 議論はある？ | 言語実験は7Bパラメータまでの検証であること、PSVには評価用のラベル付き検証セットが必要であること、また推論時にK回（アンサンブル分）のモデル評価が必要でコストが増加する点が課題。 |
| 次に読むべき論文は？ | [Neural thickets: Diverse task experts are dense around pretrained weights](https://arxiv.org/abs/2610.40649) (本研究の直接の比較対象) |
| PDFリンク | https://arxiv.org/pdf/2610.40649v1 |
