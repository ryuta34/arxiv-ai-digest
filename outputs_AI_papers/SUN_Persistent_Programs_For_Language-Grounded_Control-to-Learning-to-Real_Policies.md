---
title: "SUN: Persistent Programs For Language-Grounded Control-to-Learning-to-Real Policies"
date: 2026-09-01
arxiv_id: 2608.31167v1
url: http://arxiv.org/abs/2608.31167v1
---

# SUN: Persistent Programs For Language-Grounded Control-to-Learning-to-Real Policies

| 項目 | 内容 |
|---|---|
| どんなもの？ | 言語指示に基づき、幾何学的・接触関係を定義した実行可能プログラム「SUN Program」を生成・実行するロボット学習フレームワーク「Kuafu」。モデルベース制御（MPC）でスクリーニングされたタスク構造を、ポリシー学習とデータ生成まで一貫して保持し、長期的な操作タスクを効率的かつ堅牢に実行する。 |
| 先行研究と比べてどこがすごい？ | 従来の報酬設計の手間や、学習後の挙動が制御時に検証されたタスク構造から逸脱する「セマンティック・ドリフト」を解消。9つのタスクにおいてベースラインを大幅に上回る成功率（82.03%）を達成し、かつ計算コストを大幅に削減（Eureka比3.91倍の効率）した点。 |
| 技術や手法のキモはどこ？ | LLMを用いて自然言語から「SUN Program（型付き実行可能アーティファクト）」を構築し、MPCによる閉ループシミュレーションで検証済みタスク構造を確定させる点。これを報酬関数、遷移条件、診断ロジックにコンパイルし、ステージ条件付き行動クローニングおよび残差強化学習に適用することで、制御と学習の橋渡しをシームレスに行う。 |
| どうやって有効だと検証した？ | Isaac Labにおける9つの多段階操作タスク（積み木、引き出し開け、挿入など）を用いて実験。手法の信頼性（形成と修理の成功率）、データ効率、およびFrankaやKinovaロボットを用いた実機へのゼロショット・シム・トゥ・リアル転移の成否を測定・評価した。 |
| 議論はある？ | 現在の手法では変形物体や流体には対応できず、新しい演算子の定義が必要。また、状態モニターの単調進行制約により物理的な回帰（再試行の失敗）からの復帰が困難な点や、Q95評価がMPCベースの相対的な指標である点が挙げられる。 |
| 次に読むべき論文は？ | [8] W. Huang et al., "ReKep: Spatio-temporal reasoning of relational keypoint constraints for robotic manipulation", CoRL 2025. / [2] Y. J. Ma et al., "Eureka: Human-level reward design via coding large language models", ICLR 2024. |
| PDFリンク | https://arxiv.org/pdf/2608.31167v1 |
