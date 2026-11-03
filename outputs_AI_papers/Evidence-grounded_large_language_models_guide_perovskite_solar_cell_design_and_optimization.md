---
title: "Evidence-grounded large language models guide perovskite solar cell design and optimization"
date: 2026-11-03
arxiv_id: 2611.00633v1
url: http://arxiv.org/abs/2611.00633v1
---

# Evidence-grounded large language models guide perovskite solar cell design and optimization

| 項目 | 内容 |
|---|---|
| どんなもの？ | ペロブスカイト太陽電池の研究において、科学的な推論能力を持つAI「OpenPerov」と、その推論能力を評価するベンチマーク「PSM-Bench」を構築した研究。専門家の知識を組み込んだ証拠レコードに基づき、実験の解釈や設計の最適化を支援する。 |
| 先行研究と比べてどこがすごい？ | 単なるQA学習ではなく、4,532件の論文から実験戦略、コントロール、観測結果、機械的解釈をリンクさせた証拠レコードを構築し学習させた点。これにより、他の大規模言語モデルと比較して圧倒的な科学的推論精度（Scientific Mastery 87.6）を達成した。 |
| 技術や手法のキモはどこ？ | 文献から抽出した科学的議論の構造（実験とメカニズムの論理的連鎖）を学習する「構造化証拠学習」と、既存の回答に対して関連文献を検索し、不整合や不足を修正する「証拠に基づく局所的修正（Evidence-linked local revision）」を組み合わせた点。 |
| どうやって有効だと検証した？ | 800問の専門家開発問題によるベンチマーク評価、独立した専門家による二重盲検評価、および未知の最新論文を用いた実証試験を実施。さらに、自己組織化単分子膜（SAM）の設計においてモデルが提案したK（カリウム）添加分子が、専門家が好んだNa添加分子を性能・安定性で上回ることを実証した。 |
| 議論はある？ | AIの回答精度は向上したが、依然として修正の程度（リライトの範囲）が設計上の課題であることや、訓練データに含まれない最新の研究に対する適用可能性の限界について言及されている。 |
| 次に読むべき論文は？ | [1] Boiko, D. A. et al. [Autonomous chemical research with large language models](https://doi.org/10.1038/s41586-023-06792-0)、[11] Wang, X.-D. et al. [Perovskite-R1](https://doi.org/10.1038/s43246-026-01099-9)、[15] Gao, D. et al. [Autonomous closed-loop framework for reproducible perovskite solar cells](https://doi.org/10.1038/s41586-026-10482-y) |
| PDFリンク | [https://arxiv.org/pdf/2611.00633v1](https://arxiv.org/pdf/2611.00633v1) |
