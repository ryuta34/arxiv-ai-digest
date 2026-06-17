---
title: "Visual Verification Enables Inference-time Steering and Autonomous Policy Improvement"
date: 2026-06-17
arxiv_id: 2606.18247v1
url: http://arxiv.org/abs/2606.18247v1
---

# Visual Verification Enables Inference-time Steering and Autonomous Policy Improvement

| 項目 | 内容 |
|---|---|
| どんなもの？ | ロボットの推論時に複数の行動案を生成し、視覚的な検証器（Visual Verifier）を用いて最適な行動を選択・実行するフレームワーク「VERITAS」。検証を通過した成功データを蓄積し、事後のオフライン強化学習に利用することで、人間の介入なしにロボットが自律的に改善し続けるサイクルを実現した。 |
| 先行研究と比べてどこがすごい？ | 大規模な人間による教師データ収集を必要とせず、推論時の計算能力を活用することで、ベースポリシーを即座に改善（ステアリング）し、かつ長期的にも自律的な改善が可能である点。また、タスク固有の学習済み検証器を使わず、汎用的なVLMを用いた幾何学的アプローチにより、未知のタスクにも柔軟に対応できる。 |
| 技術や手法のキモはどこ？ | 推論時に「確率的生成器（ポリシー）」と「勾配フリーな視覚検証器（VLMベース）」を組み合わせる点。VLMが生成した空間上の目標軌道と、ロボットの実際のアクション候補の幾何学的整合性をチェックすることで、コストを抑えつつ高精度なフィルタリングを実現している。 |
| どうやって有効だと検証した？ | シミュレーション環境（SIMPLER）および実環境（DROIDプラットフォーム）にて、複数のベースポリシーに対して評価を実施。推論時のステアリングにより成功率がシミュレーションで12.6%、実環境で35%向上したほか、自動生成データでのファインチューニングが人間による教示データに匹敵する効率性を持つことを示した。 |
| 議論はある？ | 現在は静的な視覚的トレースに依存しているため、急激に状況が変化する動的な環境での適用が課題。また、推論時の繰り返しサンプリングによる計算コストがかかる点や、ベースポリシーが持つ探索範囲（事前分布）の質が性能の上限を決定してしまう点が挙げられている。 |
| 次に読むべき論文は？ | [5] Physical Intelligence. π0: A vision-language-action flow model for general robot control (2024), [22] DROID: A large-scale in-the-wild robot manipulation dataset (RSS 2024), [38] Steering your generalists: Improving robotic foundation models via value guidance (CoRL 2024) |
| PDFリンク | https://arxiv.org/pdf/2606.18247v1 |
