---
title: "Temporal Taskification in Streaming Continual Learning: A Source of Evaluation Instability"
date: 2026-04-24
arxiv_id: 2604.21930v1
url: http://arxiv.org/abs/2604.21930v1
---

# Temporal Taskification in Streaming Continual Learning: A Source of Evaluation Instability

| 項目 | 内容 |
|---|---|
| どんなもの？ | ストリーミング環境での継続学習（CL）において、データの「時間的なタスク分割（タスク化）」自体が評価結果を左右する構造的な変数であることを示した論文。時間的な分割方法の違いが、学習アルゴリズムの性能評価（予測誤差や忘却など）に本質的な影響を与えることを明らかにしている。 |
| 先行研究と比べてどこがすごい？ | 既存研究では、タスク分割は前提条件として固定されていたが、本研究はタスク分割こそがベンチマークの安定性を損なう評価変数であると特定した点。モデルの学習前に、タスク分割の頑健性を定量評価する枠組みを提案した点が新しい。 |
| 技術や手法のキモはどこ？ | タスク数に依存しない「可塑性（Plasticity）プロファイル」と「安定性（Stability）プロファイル」を定義し、タスク間の距離を測定する「プロファイル距離」を導入した。さらに、境界の微小な変更に対する感度を測る「境界プロファイル安定性（BPS）」を評価指標として提案したこと。 |
| どうやって有効だと検証した？ | ネットワークトラフィック予測データセット（CESNET-Timeseries24）を用い、9日間・30日間・44日間のタスク分割を比較。同一モデル・同一学習予算でも、分割方法を変えるだけで予測誤差や忘却スコアに大きな差が出ることを示し、BPSがタスク分割の脆弱性を事前に診断できることを実証した。 |
| 議論はある？ | 実証範囲がネットワークトラフィック予測に限定されていることや、評価に用いるCL手法が標準的なものに限られている点。また、現在はあくまで診断的なフレームワークであり、最適なタスク分割を自動選択する手法や、分割の変化に頑健なCL手法の提案までは至っていない。 |
| 次に読むべき論文は？ | [A continual learning survey: Defying forgetting in classification tasks (De Lange et al., 2021)](https://ieeexplore.ieee.org/document/9349272)、[The benchmark lottery (Dehghani et al., 2021)](https://arxiv.org/abs/2107.07002) |
| PDFリンク | https://arxiv.org/pdf/2604.21930v1 |
