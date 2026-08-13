---
title: "Redistribution-based Cost Inference Improves Sparse Safe Offline RL"
date: 2026-08-13
arxiv_id: 2608.12306v1
url: http://arxiv.org/abs/2608.12306v1
---

# Redistribution-based Cost Inference Improves Sparse Safe Offline RL

| 項目 | 内容 |
|---|---|
| どんなもの？ | 軌道レベルのまばらな安全停止フィードバック（バイナリ信号）のみを使用して、オフライン強化学習で安全なポリシーを訓練するための「Redistribution-based Cost Inference (RCI)」フレームワーク。リターン分解を用いて停止信号を各ステップのコストに変換し、既存の制約付きオフライン強化学習手法に適用可能にする。 |
| 先行研究と比べてどこがすごい？ | 従来手法が要求していたステップごとの詳細なコストラベルを不要とし、人手によるアノテーションコストを削減した点。理論的に制約付きマルコフ決定過程（CMDP）における最適なポリシーとラグランジュ乗数を保存することを証明しており、ラベルノイズに対しても頑健である。 |
| 技術や手法のキモはどこ？ | RUDDERなどのリターン分解手法を用いて、エピソード全体のコスト信号を時間軸に逆伝播させ、各状態・行動ペアに対する dense なコストを推定する点。さらに、報酬等価な補償項 $\delta_T$ を導入することで、モデルの予測精度に関わらず元の期待コストとの等価性を保証している。 |
| どうやって有効だと検証した？ | HighwayEnv（自律走行）とSafe-FetchReach（ロボットアーム）の2つのベンチマークにおいて、他のベースライン（SparseやHazard分類器）と比較。多様なデータセット構成やラベルノイズ条件下で、タスクパフォーマンスを維持しつつ、違反率を大幅に低減できることを示した。 |
| 議論はある？ | データセットが特定の傾向に偏っている場合の過度な保守性、モデルが統計的な相関を捉えるに留まり因果的な危険性を完全には識別できない点、単一の制約条件に限定されている点が挙げられる。将来的な課題として、不確実性を考慮した再分配や、より複雑なアーキテクチャの検討が示唆されている。 |
| 次に読むべき論文は？ | [RUDDER: Return Decomposition for Delayed Rewards](https://arxiv.org/abs/1806.07857), [Constrained Policy Optimization](https://arxiv.org/abs/1705.10528), [Off-Policy Deep Reinforcement Learning without Exploration (BCQ)](https://arxiv.org/abs/1812.02900) |
| PDFリンク | https://arxiv.org/pdf/2608.12306v1 |
