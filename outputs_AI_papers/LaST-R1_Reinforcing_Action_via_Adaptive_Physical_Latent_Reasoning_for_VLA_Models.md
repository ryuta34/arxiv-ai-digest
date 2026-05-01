---
title: "LaST-R1: Reinforcing Action via Adaptive Physical Latent Reasoning for VLA Models"
date: 2026-05-01
arxiv_id: 2604.28192v1
url: http://arxiv.org/abs/2604.28192v1
---

# LaST-R1: Reinforcing Action via Adaptive Physical Latent Reasoning for VLA Models

| 項目 | 内容 |
|---|---|
| どんなもの？ | ロボット操作（VLA）モデルにおいて、行動実行前に物理的な状況をLatent（潜在）空間で推論する「Latent Chain-of-Thought (CoT)」と、強化学習（RL）を組み合わせた新しいフレームワーク「LaST-R1」を提案した。行動だけでなく推論プロセス自体を環境からの報酬で最適化することで、高い成功率と適応的なロボット操作を実現する。 |
| 先行研究と比べてどこがすごい？ | 従来のRLベースのVLAモデルが単純な行動空間の最適化に留まっていたのに対し、本作は推論プロセスと行動生成を同時に最適化する。また、タスクの難易度に応じて推論の深さを変える「適応的Latent CoT」を導入し、計算効率と実行精度の両立を可能にした。LIBEROベンチマークで99.8%の成功率を達成した。 |
| 技術や手法のキモはどこ？ | 推論プロセスを潜在変数として扱い、強化学習によって報酬を推論と行動の両方にフィードバックさせる「Latent-to-Action Policy Optimization (LAPO)」手法。また、Vision-Languageモデルの出力をDINOv3で構造化・潜在空間化して事前に準備し、推論の計算コストを抑えつつ物理的一貫性を高めている点。 |
| どうやって有効だと検証した？ | LIBEROの4つのタスクスイート（Spatial, Object, Goal, Long）でのシミュレーション実験に加え、実機のFranka Research 3を用いた複雑な操作タスク（袋のジッパー開け、皿拭き、ボトルキャップ開け等）で検証。さらに、未知の物体や背景、照明変化に対するゼロショットの汎化性能も評価した。 |
| 議論はある？ | 高い汎化性能を示す一方で、未知の極端な分布外（OOD）データ遭遇時の予測不能な物理挙動のリスクには言及されている。将来課題として、これらのリスクを低減するための安全ガードレールの導入や、より厳格なハードウェアレベルの操作境界の設定を挙げている。 |
| 次に読むべき論文は？ | [SimpleVLA-RL (arXiv:2509.09674)](https://arxiv.org/abs/2509.09674)、[VLA-RL (arXiv:2505.18719)](https://arxiv.org/abs/2505.18719)、[π0.5 (arXiv:2504.16054)](https://arxiv.org/abs/2504.16054) |
| PDFリンク | https://arxiv.org/pdf/2604.28192v1 |
