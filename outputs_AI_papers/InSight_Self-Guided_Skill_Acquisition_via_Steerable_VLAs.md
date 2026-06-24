---
title: "InSight: Self-Guided Skill Acquisition via Steerable VLAs"
date: 2026-06-24
arxiv_id: 2606.24884v1
url: http://arxiv.org/abs/2606.24884v1
---

# InSight: Self-Guided Skill Acquisition via Steerable VLAs

| 項目 | 内容 |
|---|---|
| どんなもの？ | 視覚言語行動（VLA）モデルを「プリミティブ（基本動作）」単位で制御可能（Steerable）にし、新しいタスクに必要な動作をVLMの誘導で自律的に獲得するフレームワーク「INSIGHT」です。これにより、人間による追加のデモンストレーションなしで、ロボットが継続的にスキルを拡張・学習できます。 |
| 先行研究と比べてどこがすごい？ | 従来のVLAは学習データ内のスキルに能力が限定されていましたが、INSIGHTは未知のタスクに対して不足しているプリミティブを特定し、自律的にデータを収集・学習することで、ゼロからスキルを構築できる点です。推論だけでなく、ポリシー自体を更新するため、継続的なスキル獲得が可能です。 |
| 技術や手法のキモはどこ？ | (1)人間のデモンストレーションを自動でプリミティブに分解するセグメンテーション、(2)VLMが不足するプリミティブを特定して計画するプランナー、(3)VLM誘導による自律的なデータ収集と成功判定、(4)獲得したプリミティブをVLAに統合する再学習ループの組み合わせです。 |
| どうやって有効だと検証した？ | シミュレーション（LIBERO環境でのブロックフリップや引き出し閉め）と実機（UFactory xArmを用いたボトル開封、注ぎ、長期間のタスク構成など）で評価。その結果、ゼロから新しい動作を獲得し、最大96%の成功率を達成しつつ、元々のスキルも保持できることを示しました。 |
| 議論はある？ | 現在はプリミティブが単一軸の動きに限定されているため、より複雑な軌道の学習には適していない点が課題です。また、自律的な試行には手動のリセットが必要であり、今後はシミュレーションやワールドモデルを用いた安全な自律試行への拡張が検討されています。 |
| 次に読むべき論文は？ | [1] [OpenVLA: An Open-Source Vision-Language-Action Model](http://arxiv.org/abs/2406.09246), [14] [CaP-X: A Framework for Benchmarking and Improving Coding Agents for Robot Manipulation](http://arxiv.org/abs/2603.22435), [15] [π0.7: a steerable generalist robotic foundation model with emergent capabilities](https://arxiv.org/abs/2604.15483) |
| PDFリンク | https://arxiv.org/pdf/2606.24884v1 |
