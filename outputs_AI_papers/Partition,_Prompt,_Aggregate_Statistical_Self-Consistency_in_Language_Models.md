---
title: "Partition, Prompt, Aggregate: Statistical Self-Consistency in Language Models"
date: 2026-07-17
arxiv_id: 2607.15277v1
url: http://arxiv.org/abs/2607.15277v1
---

# Partition, Prompt, Aggregate: Statistical Self-Consistency in Language Models

| 項目 | 内容 |
|---|---|
| どんなもの？ | 言語モデル（LLM）の推論結果が確率分布として整合的であるか（統計的自己整合性）を評価するためのフレームワーク。二分決定木を用いて母集団を細分化し、全確率の法則に基づき、サブグループの集約値がモデルの直接的な予測値と一致するかを検証している。 |
| 先行研究と比べてどこがすごい？ | 外部の正解データ（Ground Truth）を必要としない「参照不要」な自己整合性評価指標を提案した点。また、直接的な集約推定よりも、細分化したサブグループからの再構成の方が高精度になるという「マクロの誤謬（macro fallacy）」という現象を実証的に示した点。 |
| 技術や手法のキモはどこ？ | 二分決定木による母集団の再帰的分割と、そこから得られる条件付き確率を全確率の法則で再構築する「分割・プロンプト・集約」プロトコル。さらに、制約の提示順序による不整合を評価する「順序整合性（Order consistency）」を導入した点。 |
| どうやって有効だと検証した？ | 米国国勢調査（ACS）データを用いた所得予測、World Values Survey（WVS）を用いた世論調査、およびテニスや架空の戦闘をテーマにした合成予測タスクで検証。最先端モデル（Frontier models）でも、これらの整合性基準を十分に満たしていないことを示した。 |
| 議論はある？ | 現在の指標はモデルの内部的な整合性を測る「必要条件」であり、整合的であっても必ずしも事実に即した精度（Alignment）が保証されるわけではない点。また、極端に細かい分割はモデルの予測をかえって不安定にさせるトレードオフが存在する。 |
| 次に読むべき論文は？ | [Santurkar et al. (2023)](https://proceedings.mlr.press/v202/santurkar23a.html), [Meister et al. (2024)](https://arxiv.org/abs/2411.05403), [Durmus et al. (2024)](https://arxiv.org/abs/2406.20094) |
| PDFリンク | https://arxiv.org/pdf/2607.15277v1 |
