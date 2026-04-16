---
title: "From $P(y|x)$ to $P(y)$: Investigating Reinforcement Learning in Pre-train Space"
date: 2026-04-16
arxiv_id: 2604.14142v1
url: http://arxiv.org/abs/2604.14142v1
---

# From $P(y|x)$ to $P(y)$: Investigating Reinforcement Learning in Pre-train Space

| 項目 | 内容 |
|---|---|
| どんなもの？ | 大規模言語モデル（LLM）の推論能力を強化するため、従来の条件付き分布 $P(y|x)$ の最適化に代わり、事前学習空間（Pre-train Space）での周辺分布 $P(y)$ を直接最適化する手法「PreRL」を提案する論文。さらに、これを標準的なRLと組み合わせた「Dual Space RL (DSRL)」により、モデルの推論能力を大幅に向上させる枠組みを構築した。 |
| 先行研究と比べてどこがすごい？ | 従来のRLVRはモデルの既存の出力分布に強く依存するという限界があったが、PreRLは報酬駆動のオンライン更新を事前学習空間に導入することで、より広範な探索能力を維持しつつ、推論経路の枝刈りを効率的に行う。結果として、より少ないステップ数で高い性能と優れた一般化能力を実現した。 |
| 技術や手法のキモはどこ？ | $log P(y)$ と $log P(y|x)$ の勾配が強く整合することを利用し、事前学習空間で「負のサンプルを用いた強化学習（NSR: Negative Sample Reinforcement）」を行うことで、誤った推論経路を迅速に排除し、モデルの自律的な推論能力（遷移・反映思考）を活性化させる点。 |
| どうやって有効だと検証した？ | MATH、AMC23、AIME24/25、OlympiadBenchなどの数学推論ベンチマーク、およびGPQA、MMLU-Pro、HumanEval等のOODデータセットで評価。Qwen3-4B/8Bをベースに、既存のRL手法（GRPO等）と比較し、精度の向上、学習効率の高さ、Pass@Kにおけるスケーラビリティを実証した。 |
| 議論はある？ | NSR-PreRLは推論能力を大幅に向上させる一方、過度に行うと応答が長くなりすぎるという副作用がある。そのため、事前学習空間の枝刈りから、後続の細粒度な強化学習へと切り替える「Policy Reincarnation（ポリシー転生）」という戦略の設計が重要である。 |
| 次に読むべき論文は？ | [DeepSeek-R1 (Guo et al., 2025a)](https://arxiv.org/abs/2501.12948)、[GRPO (Shao et al., 2024)](https://arxiv.org/abs/2402.03300)、[Reincarnating reinforcement learning (Agarwal et al., 2022)](https://arxiv.org/abs/2206.01626) |
| PDFリンク | https://arxiv.org/pdf/2604.14142v1 |
