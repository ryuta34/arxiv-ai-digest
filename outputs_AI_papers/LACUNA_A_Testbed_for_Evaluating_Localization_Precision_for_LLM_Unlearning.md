---
title: "LACUNA: A Testbed for Evaluating Localization Precision for LLM Unlearning"
date: 2026-07-04
arxiv_id: 2607.02513v1
url: http://arxiv.org/abs/2607.02513v1
---

# LACUNA: A Testbed for Evaluating Localization Precision for LLM Unlearning

| 項目 | 内容 |
|---|---|
| どんなもの？ | 大規模言語モデル（LLM）のアンラーニング（学習データの削除）において、モデル内部のパラメータレベルで知識が正しく削除されたかを評価するための初のテストベッド「LACUNA」を提案した論文。 |
| 先行研究と比べてどこがすごい？ | 既存研究が出力レベルの挙動のみを評価していたのに対し、LACUNAは特定の個人情報（PII）をモデルの特定の重みに意図的に埋め込むことで、知識の格納場所に対する「削除の正確性」を直接評価できる点を画期的とした。 |
| 技術や手法のキモはどこ？ | マスク付き継続的事前学習を用いて、特定の知識をモデル内の指定された重み領域（マスク）に隔離して注入する点。これにより、グラウンドトゥルース（削除対象の真の場所）を確定させた状態でアンラーニング手法の評価を可能にした。 |
| どうやって有効だと検証した？ | 1Bおよび7BのOLMoモデルを用いて、代表的なアンラーニング手法（SimNPO, AlphaEdit, MemFlex等）をベンチマークした。その結果、従来手法は出力レベルの性能は高くても、重みレベルでは極めて不正確であり、削除を回避する再学習攻撃に脆弱であることを示した。 |
| 議論はある？ | モデルの知識のすべてが必ずしも「局所的」に格納されているわけではないという現実的な制約を認めている。また、一部のデータは極めて削除困難（stubborn）であることも示唆されており、今後の研究課題とされた。 |
| 次に読むべき論文は？ | [Maini et al., 2024 (TOFU)](https://openreview.net/forum?id=B41hNBoWLo), [Fan et al., 2025 (SimNPO)](https://openreview.net/forum?id=JbvSQm5h1l), [Dorna et al., 2025 (OpenUnlearning)](https://openreview.net/forum?id=undefined) |
| PDFリンク | https://arxiv.org/pdf/2607.02513v1 |
