---
title: "A Unifying Lens on Supervised Fine-Tuning Through Target Distribution Design"
date: 2026-06-10
arxiv_id: 2606.11189v1
url: http://arxiv.org/abs/2606.11189v1
---

# A Unifying Lens on Supervised Fine-Tuning Through Target Distribution Design

| 項目 | 内容 |
|---|---|
| どんなもの？ | 大規模言語モデルの教師ありファインチューニング（SFT）を、損失関数の最適化ではなく「ターゲット分布の設計」として再定義するフレームワーク。SFTにおけるラベルへの依存度と、代替トークンへの確率割り当てを明示的に制御する手法。 |
| 先行研究と比べてどこがすごい？ | 既存のSFT改善手法（トークン重み付けや蒸留など）を統一的な「Q-targetフレームワーク」で体系化し、ラベルの不確実性に応じて適応的に監督信号を調整することで、数学的・科学的推論タスクにおいて一貫して高い性能を達成した点。 |
| 技術や手法のキモはどこ？ | トークンごとの理想的なターゲット分布 $Q_t = \gamma_t\delta_{y_t} + (1 - \gamma_t)\tilde{\pi}_t$ を設計し、$\gamma_t$（モデルの確信度に基づく信頼スコア）と $\tilde{\pi}_t$（教師モデルの指導による残差分布）の2軸で監督信号を構成したこと。 |
| どうやって有効だと検証した？ | NuminaMath-CoT、OpenR1-15k、m23kなど複数のデータセットと、Qwen2.5/3、LLaMA-3.1/3.2を含む多様なモデルサイズを用いて、Average@16精度による比較実験を実施し、ベースラインを上回る性能を証明した。 |
| 議論はある？ | 提案手法はラベルの不確実性が高い場合に特に有効だが、ラベルが完全に信頼できるタスクにおいては標準的なSFTと差が縮まる可能性がある。また、教師モデルの選択や分布の設計におけるハイパーパラメータへの依存性が課題となり得る。 |
| 次に読むべき論文は？ | [Beyond log likelihood: Probability-based objectives for supervised fine-tuning across the model capability continuum (Li et al., 2026)](https://arxiv.org/abs/2606.11189v1) ※本論文の参考文献 [6] |
| PDFリンク | https://arxiv.org/pdf/2606.11189v1 |
