---
title: "Next Forcing: Causal World Modeling with Multi-Chunk Prediction"
date: 2026-06-10
arxiv_id: 2606.11187v1
url: http://arxiv.org/abs/2606.11187v1
---

# Next Forcing: Causal World Modeling with Multi-Chunk Prediction

| 項目 | 内容 |
|---|---|
| どんなもの？ | 自己回帰型ビデオ生成モデルにおいて、現在のチャンクだけでなく、未来の複数のチャンクを同時に予測するマルチチャンク予測（MCP）フレームワーク「Next Forcing」。訓練効率と推論速度を向上させ、ロボット制御における世界モデルの学習を加速させる手法。 |
| 先行研究と比べてどこがすごい？ | 従来手法の「近傍フレームの類似性」に依存した局所的な学習（myopic supervision）という欠陥を克服した点。高フレームレート環境において、ベースライン比で2.3倍の学習加速と、推論時の2倍の高速化を実現し、RoboTwinベンチマークでSOTAを達成した。 |
| 技術や手法のキモはどこ？ | メインモデルの複数の中間層から特徴を抽出する「Multi-Layer Feature Fusion」と、予測深度ごとにチェインを形成する「Causal Chain」構造。また、MCPモジュールに高いノイズレベルを強制することで、メインモデルの表現能力を強化し、長期間の動的進化を捉える学習を促す点。 |
| どうやって有効だと検証した？ | ロボット制御シミュレーション（RoboTwin）および物理法則理解ベンチマーク（PhyWorld）にて評価。50fpsの高フレームレート環境下での学習収束速度やタスク成功率、および一般的なビデオ事前学習データセットでのFVD（Fréchet Video Distance）削減率を測定し、定量的・定性的な優位性を確認した。 |
| 議論はある？ | MCPモジュールを追加することによる学習時の計算コスト増加が限界として挙げられている。今後は、さらに予測範囲を広げた際のドリフト現象への対応や、推論速度向上のためのさらなる効率化が課題。 |
| 次に読むべき論文は？ | [13] [Diffusion forcing: Next-token prediction meets full-sequence diffusion](https://arxiv.org/abs/2407.01466), [36] [Causal world modeling for robot control](https://arxiv.org/abs/2601.21998) |
| PDFリンク | https://arxiv.org/pdf/2606.11187v1 |
