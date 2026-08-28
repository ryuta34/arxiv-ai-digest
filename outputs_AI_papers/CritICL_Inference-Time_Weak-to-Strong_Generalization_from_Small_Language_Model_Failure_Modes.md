---
title: "CritICL: Inference-Time Weak-to-Strong Generalization from Small Language Model Failure Modes"
date: 2026-08-28
arxiv_id: 2608.27455v1
url: http://arxiv.org/abs/2608.27455v1
---

# CritICL: Inference-Time Weak-to-Strong Generalization from Small Language Model Failure Modes

| 項目 | 内容 |
|---|---|
| どんなもの？ | 大規模言語モデル（LLM）の推論時において、より小規模なモデルが生成した誤答パターン（失敗モード）を構造化し、それをヒントとして活用することで、強力なモデルの推論性能を効率的に向上させるフレームワーク「CritICL」。 |
| 先行研究と比べてどこがすごい？ | 従来の手法（自己反省や多数決など）のように、推論時に何度も生成を繰り返す必要がないため、大幅な計算コストの削減と推論の効率化を実現した点。また、モデルファミリー間で失敗パターンの分布が安定しているという特性を突いた、効率的な誘導手法である点。 |
| 技術や手法のキモはどこ？ | 小規模モデルの誤答から作成した「CritBank（失敗・ critiqueのデータセット）」を用い、クエリに応じた失敗モードを特定して、その失敗を回避するための critique を in-context examples として提示する点。 |
| どうやって有効だと検証した？ | GSM8KやMATHなどの数学的推論ベンチマークに加え、AMC23やAIMEなどの競争レベルの難問、さらには化学や生物といった他ドメイン（GPQA）で評価し、標準的なFew-shotやテスト時スケーリング手法を上回る精度と低トークンコストを実証した。 |
| 議論はある？ | クロスファミリー（QwenからLlamaへなど）の転移は可能だが、同一ファミリー内での転移ほど強力ではない。また、失敗モードの分類やラベル付けにおける自動アノテーションの精度には限界があり、将来的に更なる洗練が必要である。 |
| 次に読むべき論文は？ | [Didolkar et al., 2024](https://arxiv.org/abs/2405.19783) (Metacognitive capabilities of LLMs: An exploration in mathematical problem solving) |
| PDFリンク | https://arxiv.org/pdf/2608.27455v1 |
