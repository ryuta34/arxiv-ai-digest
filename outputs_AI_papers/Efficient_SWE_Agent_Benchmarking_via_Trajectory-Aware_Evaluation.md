---
title: "Efficient SWE Agent Benchmarking via Trajectory-Aware Evaluation"
date: 2026-09-02
arxiv_id: 2609.01603v1
url: http://arxiv.org/abs/2609.01603v1
---

# Efficient SWE Agent Benchmarking via Trajectory-Aware Evaluation

| 項目 | 内容 |
|---|---|
| どんなもの？ | ソフトウェアエンジニアリング（SWE）エージェントの性能評価を、少数のタスク実行のみで低コストかつ高精度に行うための「PTA-IRT」という枠組み。従来のIRT（項目応答理論）では無視されていた「エージェントの試行錯誤プロセス（軌跡）」を評価に組み込んだ手法。 |
| 先行研究と比べてどこがすごい？ | 従来のIRTベースの評価手法が「成功・失敗」のみを信号としていたのに対し、本手法は実行過程を「特権情報」として活用することで、低予算（Calibration budget）下でも非常に高いランキング再現性とスコア推定精度を実現した点。 |
| 技術や手法のキモはどこ？ | 実行ログを構造化した「プロセスサマリー」を抽出し、LUPI（Learning Using Privileged Information）を用いて、教師・生徒モデル間で軌跡に基づく知識を蒸留する点。また、Fisher情報量に基づき、難易度を考慮したタスク選択を行う点。 |
| どうやって有効だと検証した？ | SWE-bench（Lite, Verified, Full, Pro）の4つのベンチマークを用いて、10%以下の低予算設定で既存手法（Deep-IRT, PSN-IRT, AutoJudger等）と比較。MAE、Kendallのτ、Spearmanのρで最高性能を示した。 |
| 議論はある？ | 実行ログが完全に欠落している場合や、プロセスの質が極端に低い場合には効果が制限される。また、本手法はトレーニング段階で過去のエージェントデータ（軌跡）を必要とする。 |
| 次に読むべき論文は？ | [1] Swe-agent (2024), [3] Deep item response theory (2021), [6] Lost in benchmarks? (2026), [45] AutoJudger (2026) |
| PDFリンク | https://arxiv.org/pdf/2609.01603v1 |
