---
title: "Coding Agents with an Obstacle-Aware Harness for Safe Robot Manipulation"
date: 2026-09-18
arxiv_id: 2609.20822v1
url: http://arxiv.org/abs/2609.20822v1
---

# Coding Agents with an Obstacle-Aware Harness for Safe Robot Manipulation

| 項目 | 内容 |
|---|---|
| どんなもの？ | 言語モデルを用いたロボット操作エージェントにおいて、安全制約（障害物への衝突回避）を考慮した「SAFEHARNESS」というフレームワークを提案。タスク遂行と安全性の両立を目指し、経路計画と接触実行の2段階で障害物を意識した制約を適用する。 |
| 先行研究と比べてどこがすごい？ | 従来手法は後付けのフィルタリング（障壁関数）に頼っていたため、タスク成功率とのトレードオフが発生していた。本手法は意思決定の段階で安全性を組み込むため、タスク成功率を維持しつつ衝突回避率を大幅に向上させ、従来のSOTAを上回る性能を達成した。 |
| 技術や手法のキモはどこ？ | タスクを接触イベントで「フェーズ」に分割し、①経路計画時に障害物を境界ボックスとして接地し、検証と再計画を行う「障害物認識ルートプランニング」、②接触時に障害物との空間関係に基づいて最適な接触位置と向きを選択する「障害物認識コンタクト実行」の2つのハネスを導入した点。 |
| どうやって有効だと検証した？ | 障害物を含むSafeLIBEROベンチマークを用い、GPT-5.5およびGPT-6をバックボーンとしたエージェントで実験。従来手法（AEGIS等）と比較し、タスク成功率（TSR）と衝突回避率（CAR）の両面で優れた結果を示し、モデルのスケールアップだけでなく手法自体の有効性を実証した。 |
| 議論はある？ | 現在は単一の障害物のみを扱う設定であることや、シミュレーション環境での評価が中心である点が挙げられる。また、安全な経路を検証・確保する工程により、タスク実行時間が長くなる傾向がある。今後はより複雑な環境への適用や、リアルタイム性が課題となる。 |
| 次に読むべき論文は？ | [Harness VLA: Steering frozen vlas into reliable manipulation primitives via memory-guided agents](https://arxiv.org/abs/2607.08448)、[Libero: Benchmarking knowledge transfer for lifelong robot learning](https://arxiv.org/abs/2307.15818) |
| PDFリンク | https://arxiv.org/pdf/2609.20822v1 |
