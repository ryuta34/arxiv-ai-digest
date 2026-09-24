---
title: "Where Should I Join? Robot Group Joining via Language-Guided Goal Prediction"
date: 2026-09-24
arxiv_id: 2609.28467v1
url: http://arxiv.org/abs/2609.28467v1
---

# Where Should I Join? Robot Group Joining via Language-Guided Goal Prediction

| 項目 | 内容 |
|---|---|
| どんなもの？ | 自然言語指示に基づき、周辺の人間グループを特定し、社会的に適切な位置と向きで合流するロボットのための言語誘導型ゴール予測手法。グループの構成メンバーの特定と、その空間的・社会的な文脈に適した合流ポーズの予測を二段階で行う。 |
| 先行研究と比べてどこがすごい？ | 既存の社会ナビゲーションは目標地点が固定されていることが多いが、本手法は言語指示から動的にグループを特定し、かつ形成されているF-formation（社会的な配置）に適応した合流ポーズを確率的に予測できる点。大規模VLMベースラインよりも高速かつ高精度な合流を実現した。 |
| 技術や手法のキモはどこ？ | 再帰的なスペクトルクラスタリングで候補となる人間サブセットを構造的に生成し、ペアワイズランキングで言語指示に最適なグループを特定する点。また、グループの配置パターンを学習し、エネルギー・オリエンテーションマップを用いてマルチモーダルな合流ポーズ分布を出力する点。 |
| どうやって有効だと検証した？ | 15の会話、15の列、12の観客シーンからなる合計42のオフラインベンチマークで、精度、時間、ポーズ有効性を評価。さらに、Boston Dynamics Spotロボットを用いた実環境実験で、静的・動的なグループに対するリアルタイムな合流能力を検証。 |
| 議論はある？ | 現在はグループ特定のための仮説生成を距離ベースの親和性行列に依存しているため、候補に正しいグループが含まれない場合がある。また、環境を移動の制約としてのみ扱っており、環境自体がもたらす合流の可能性を完全には活用できていない点。 |
| 次に読むべき論文は？ | [1] Barua et al., "Enabling social robots to perceive and join socially interacting groups using f-formation: a comprehensive overview" (arXiv:2308.13840) [2] Shah et al., "LM-Nav: Robotic navigation with large pre-trained models of language, vision, and action" (arXiv:2207.04429) |
| PDFリンク | https://arxiv.org/pdf/2609.28467v1 |
