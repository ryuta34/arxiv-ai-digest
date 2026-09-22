---
title: "VideoGen-Agent: Reinforcing Video Generation Agents"
date: 2026-09-22
arxiv_id: 2609.24997v1
url: http://arxiv.org/abs/2609.24997v1
---

# VideoGen-Agent: Reinforcing Video Generation Agents

| 項目 | 内容 |
|---|---|
| どんなもの？ | 外部ツール（検索、物理シミュレーション、物体検出など）を統合し、マルチステップの推論と検証を通じて複雑な動画生成を最適化するマルチモーダルエージェント。 |
| 先行研究と比べてどこがすごい？ | 個別のツール使用に特化した従来手法とは異なり、6つの異なるタスクカテゴリ（物理シミュレーション、アイデンティティ保持等）を単一のエージェントで横断的に解決可能。ベースとなる動画生成器自体をアップグレードするだけで、再学習なしに性能が大幅に向上する汎用性を備えている。 |
| 技術や手法のキモはどこ？ | 教師データによる教師あり微調整（SFT）と、GRPO（Group Relative Policy Optimization）を用いたマルチタスク強化学習の二段階学習。また、ツール使用の妥当性や生成品質を評価するハイブリッド報酬モデルと、タスク間の学習信号をバランスさせるタスクアドバンテージ正規化を導入した点。 |
| どうやって有効だと検証した？ | 600のプロンプトからなる新ベンチマーク「VABench」を構築し、既存の商用・オープンソースの動画生成モデルとの比較を実施。自動評価（Gemini 3.1 Pro）および人間の選好評価の両面で、ベースラインを大幅に上回る性能を実証した。 |
| 議論はある？ | 現在の生成ツール自体の品質や応答待ち時間、検証用フィードバックの網羅性に制限がある。また、より複雑なワークフローに対応するためには、より強力な動画理解モデルや、より迅速で高品質な生成ツールの導入が必要である。 |
| 次に読むべき論文は？ | [VISTA: A Test-Time Self-Improving Video Generation Agent](https://arxiv.org/abs/2606.07649), [Newton: Agentic planning for physically grounded video generation](https://arxiv.org/abs/2605.18396) |
| PDFリンク | https://arxiv.org/pdf/2609.24997v1 |
