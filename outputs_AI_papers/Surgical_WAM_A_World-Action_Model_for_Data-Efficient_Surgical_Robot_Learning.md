---
title: "Surgical WAM: A World-Action Model for Data-Efficient Surgical Robot Learning"
date: 2026-08-12
arxiv_id: 2608.11204v1
url: http://arxiv.org/abs/2608.11204v1
---

# Surgical WAM: A World-Action Model for Data-Efficient Surgical Robot Learning

| 項目 | 内容 |
|---|---|
| どんなもの？ | 外科手術ロボットの操作学習において、少量の行動ラベル付きデータと大量の行動ラベルなし動画を活用する世界モデル「Surgical WAM」を提案した。手術動画で事前学習した表現を、閉ループの制御ポリシーに転用することで、データ効率の高いロボット学習を実現する。 |
| 先行研究と比べてどこがすごい？ | 従来手法が動画生成や評価に留まっていたのに対し、世界モデルの表現を直接ロボットの閉ループ制御（行動生成）に転用した点。一般ドメインのVLAモデルよりも手術タスクにおける精密動作で高い性能を示し、行動ラベルの収集コストというボトルネックを大幅に軽減する。 |
| 技術や手法のキモはどこ？ | 動画生成による「世界モデル」と「行動生成」を同一の拡散モデルアーキテクチャで統合し、動画から学習した視覚ダイナミクスを制御ポリシーに引き継ぐ二段階学習プロセス（事前学習＋ファインチューニング）。 |
| どうやって有効だと検証した？ | SurRoLシミュレーションベンチマークを用いた4つの手術タスク（Needle Pick, Peg Transfer等）における成功率で評価。さらに、実機のJIGSAWSデータセットを用いて、シミュレーション外の現実環境でも有効であることを確認。 |
| 議論はある？ | 長期間の fine-tuning により、限られた行動ラベル付きデータに対して過学習し、事前学習による視覚ダイナミクスの利点が損なわれる場合があること。また、実行 horizonte（再計画までのステップ数）の設定が性能に影響を与えること。 |
| 次に読むべき論文は？ | [Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning](https://arxiv.org/abs/2601.16163) (本手法の基盤)、[SurgSora: Object-Aware Diffusion Model for Controllable Surgical Video Generation](https://arxiv.org/abs/2506.02555) |
| PDFリンク | https://arxiv.org/pdf/2608.11204v1 |
