---
title: "Power Reinforcement Post-Training of Text-to-Image Models with Super-Linear Advantage Shaping"
date: 2026-05-12
arxiv_id: 2605.10937v1
url: http://arxiv.org/abs/2605.10937v1
---

# Power Reinforcement Post-Training of Text-to-Image Models with Super-Linear Advantage Shaping

| 項目 | 内容 |
|---|---|
| どんなもの？ | テキストから画像を生成するモデルの強化学習（RL）における「報酬ハッキング」を抑制する手法「Super-Linear Advantage Shaping (SLAS)」を提案する論文。従来のGRPO手法で生じていた報酬の正規化による誤校正の問題を特定し、よりロジックに忠実な生成を可能にする。 |
| 先行研究と比べてどこがすごい？ | 従来のDanceGRPOなどの手法で顕著だった報酬ハッキング（報酬スコアだけを高める不自然な生成）を低減し、SD1.4やFLUX.1といった異なるモデル規模で一貫して優れた性能向上と頑健性を示した点。特にGenEvalやUniGenBench++などのベンチマークで高いスコアを記録した。 |
| 技術や手法のキモはどこ？ | 情報幾何学の観点からFisher–Rao情報計量を拡張し、報酬の差分に応じた非線形な重み付け（$\tilde{A}_i = \text{sign}(\Delta r) \cdot |\Delta r|^{1+\gamma}$）を導入したこと。これにより、高い利得（Advantage）を持つサンプルに対しては更新を促し、ノイズ由来の低い利得を持つサンプルは更新を抑制する幾何構造を設計した点。 |
| どうやって有効だと検証した？ | SD1.4およびFLUX.1 Devモデルを用い、DanceGRPOをベースラインとしてGenEvalおよびUniGenBench++ベンチマークで評価。HPS-v2.1とCLIPScoreの学習ダイナミクスを分析し、提案手法が報酬ハッキングを防ぎつつ、セマンティックな一貫性や compositional（合成的）な生成能力が高いことを定量的・定性的に証明した。 |
| 議論はある？ | 現在の検証は公開されているHPD-v2データセットに限定されている点、また報酬関数の最適化方法にはさらなる改善の余地がある。強化学習用のプロンプト選択や、最適な報酬関数の設計については将来の課題としている。 |
| 次に読むべき論文は？ | [7] DanceGRPO: Unleashing GRPO on visual generation (arXiv:2505.07818), [20] DeepSeekMath: Pushing the limits of mathematical reasoning in open language models (arXiv:2402.03300) |
| PDFリンク | https://arxiv.org/pdf/2605.10937v1 |
