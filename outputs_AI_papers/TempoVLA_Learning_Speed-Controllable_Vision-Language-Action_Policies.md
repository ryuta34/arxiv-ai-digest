---
title: "TempoVLA: Learning Speed-Controllable Vision-Language-Action Policies"
date: 2026-06-07
arxiv_id: 2606.06491v1
url: http://arxiv.org/abs/2606.06491v1
---

# TempoVLA: Learning Speed-Controllable Vision-Language-Action Policies

| 項目 | 内容 |
|---|---|
| どんなもの？ | ロボット操作（マニピュレーション）において、明示的な速度条件入力（スカラー値$s$）を付与することで、推論時の実行速度をリアルタイムに制御可能にするVision-Language-Action (VLA) フレームワーク「TempoVLA」。訓練済みのVLAを再学習せずに速度制御を導入でき、さらにVLMによる動的な速度スケジューリングも実現した。 |
| 先行研究と比べてどこがすごい？ | 既存研究がモデル圧縮や強化学習等を用いて「特定の速度」にシフトさせるだけだったのに対し、本手法は一つのモデルで双方向（加速・減速）の明示的な速度制御を可能にした点。また、VLMと組み合わせることで、タスクの局面に応じてロボットが自律的に加減速を最適化できる。 |
| 技術や手法のキモはどこ？ | 1. 訓練データを任意の速度にオンラインで変換する「VSTA（Variable-Speed Trajectory Augmentation）」：連続するアクションをマージ（加速）または分割（減速）することで、動的な速度データの生成を行う。<br>2. 速度スカラー$s$をVLAの入力として注入する軽量な条件付け機構（Textual prefix等）。 |
| どうやって有効だと検証した？ | LIBEROベンチマーク（シミュレーション）およびFrankaアームを用いた実機環境で検証。幅広い速度範囲において指令速度通りの実行が実現可能であること、およびデフォルトの速度性能向上（データ拡張効果）と、VLMを用いた動的スケジューリングによるタスク成功率の改善（80%→96%）を確認した。 |
| 議論はある？ | 高速域では低レベルコントローラーの追従帯域による物理的な限界があり、それ以上の加速にはコントローラーとの協調チューニングが必要。また、元データの速度ばらつきを標準化する「デフォールト速度の正規化」の洗練が今後の課題。 |
| 次に読むべき論文は？ | [1] RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control (arXiv:2307.15818)<br>[2] OpenVLA: An Open-source Vision-Language-Action Model (arXiv:2406.09246)<br>[3] π0: A Vision-Language-Action Flow Model for General Robot Control (arXiv:2410.24164) |
| PDFリンク | https://arxiv.org/pdf/2606.06491v1 |
