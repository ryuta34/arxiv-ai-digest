---
title: "BAS: A Decision-Theoretic Approach to Evaluating Large Language Model Confidence"
date: 2026-04-06
arxiv_id: 2604.03216v1
url: http://arxiv.org/abs/2604.03216v1
---

# BAS: A Decision-Theoretic Approach to Evaluating Large Language Model Confidence

| 項目 | 内容 |
|---|---|
| どんなもの？ | 大規模言語モデル（LLM）が自身の出力に対する自信（確信度）をいかに適切に判断し、回答すべきか棄権すべきかを決定できるかを評価する新しい指標「Behavioral Alignment Score (BAS)」を提案した論文。LLMの過信による誤回答を厳しくペナルティ化し、意思決定の信頼性を測るための決定理論に基づくフレームワークである。 |
| 先行研究と比べてどこがすごい？ | 従来のECEやAURCといった指標は、過信による誤回答という重大なリスクを過小評価する傾向があった。BASは明示的な効用モデルに基づき、過信エラーに対して非対称かつ強力なペナルティを課すため、安全性が重視される実世界での意思決定において、より実用的な信頼性評価が可能となった。 |
| 技術や手法のキモはどこ？ | 回答するか棄権するかを選択する「selective prediction」の問題としてモデル化し、真の確率に対する自信の正しさを決定理論的に定義した点。特に、誤回答に対するペナルティが対数項（ln(1-s)）によって計算されるため、自信満々な誤回答（過信）を構造的に厳しく排除するように設計されている。 |
| どうやって有効だと検証した？ | AIME、MedQA、SimpleQAという多様なタスクを用い、12種類のモデルでBAS、ECE、AURCを比較検証した。さらに、top-k回答の提示や事後キャリブレーション（等張回帰）を行うことで、モデルの自信がいかに向上するかを実験的に示した。 |
| 議論はある？ | 評価はモデルの「自己申告」した確信度に依存するため、確信度を引き出すプロンプト手法によって結果が左右される。また、BASは一般的用途（一様分布）を基準にしているが、用途に応じたリスクプロファイルのカスタマイズが必要であると指摘している。 |
| 次に読むべき論文は？ | [Chow (2003)](https://ieeexplore.ieee.org/document/1055745)（最適認識誤り・棄権トレードオフの基礎）、[Geifman & El-Yaniv (2017)](https://proceedings.neurips.cc/paper/2017/hash/f33033f20d5718a29a4c017406a147d3-Abstract.html)（選択的分類に関する論文）、[Huang et al. (2025a)](https://aclanthology.org/2025.acl-long.xxx/)（棄権学習に関する論文） |
| PDFリンク | https://arxiv.org/pdf/2604.03216v1 |
