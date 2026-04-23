---
title: "DeVI: Physics-based Dexterous Human-Object Interaction via Synthetic Video Imitation"
date: 2026-04-23
arxiv_id: 2604.20841v1
url: http://arxiv.org/abs/2604.20841v1
---

# DeVI: Physics-based Dexterous Human-Object Interaction via Synthetic Video Imitation

| 項目 | 内容 |
|---|---|
| どんなもの？ | 高価な3Dモーションキャプチャデータを使わず、テキスト条件付きの合成動画から物理ベースの器用な人-物インタラクション（HOI）を学習する手法「DeVI」を提案。動画生成モデルをモーションプランナーとして活用し、シミュレーション環境でのゼロショットの動作生成を可能にする。 |
| 先行研究と比べてどこがすごい？ | 3Dデモンストレーションデータの代わりに合成2D動画を用いることで、多様なオブジェクトや操作への拡張性を実現。また、従来の6Dポーズ推定に依存する手法よりも、2D軌跡を用いたハイブリッド報酬により、物理的な整合性と成功率を向上させている点。 |
| 技術や手法のキモはどこ？ | 合成動画から抽出した「3D人間の姿勢」と「2Dオブジェクトの軌跡」を組み合わせた「ハイブリッド模倣ターゲット」と、それに基づく「ハイブリッド追跡報酬」の導入。また、視覚的なHOIアライメントによる3D人間モデルと動画・物体の整合性確保。 |
| どうやって有効だと検証した？ | GRABデータセットを用いた定量的比較評価と、多様なオブジェクトや複数物体シーンにおける定性的評価を実施。既存の3Dデモ模倣手法と比較し、MPJPE（関節誤差）や成功率において優れた性能を示した。 |
| 議論はある？ | 動画生成モデル特有のパースペクティブ誤差（奥行き方向の不正確さ）や、自動接触推定におけるピクセル速度ベースの限界。特に精密な配置が必要な操作における誤差が課題として挙げられる。 |
| 次に読むべき論文は？ | [49] Wan: Open and advanced large-scale video generative models, [64] InterMimic: Towards universal whole-body control for physics-based human-object interactions |
| PDFリンク | https://arxiv.org/pdf/2604.20841v1 |
