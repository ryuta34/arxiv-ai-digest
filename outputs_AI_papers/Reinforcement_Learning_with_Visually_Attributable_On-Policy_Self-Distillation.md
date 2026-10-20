---
title: "Reinforcement Learning with Visually Attributable On-Policy Self-Distillation"
date: 2026-10-20
arxiv_id: 2610.26856v1
url: http://arxiv.org/abs/2610.26856v1
---

# Reinforcement Learning with Visually Attributable On-Policy Self-Distillation

| 項目 | 内容 |
|---|---|
| どんなもの？ | マルチモーダル推論において、教師モデルの視覚的証拠に基づかない不適切な修正（汚染）を排除し、視覚的に根拠のある修正のみを蒸留する「Visual-Attribution Gating (VAG)」を提案した。既存のRLVR（検証可能報酬付き強化学習）を拡張し、タスクレベルの報酬とトークンレベルの視覚的一貫性を両立させる学習パラダイム。 |
| 先行研究と比べてどこがすごい？ | 従来のオンポリシー自己蒸留（OPSD）では、モデルの「思い込み」や「言語的偏見」が混入し、誤った修正を強化してしまう「特権的修正の汚染」という課題があった。本手法は、視覚的な証拠がある場合のみ修正を許可するゲーティング機構を導入することで、これを解決し、複数の視覚推論ベンチマークでSOTAを達成した。 |
| 技術や手法のキモはどこ？ | 教師モデルに対し、証拠を含む「中心クロップ画像」と、証拠を隠した「ランダムマスク画像」の2つのビューを入力し、その出力差（視覚的コントラスト）を算出する点。このコントラストと教師の修正方向が一致する場合のみ修正を適応する「Visual-Attribution Gate (VAG)」により、汚染された情報をフィルタリングする。 |
| どうやって有効だと検証した？ | V* Bench、ZoomBench、HR-Benchなど6つの視覚推論ベンチマークで、GRPOやOPSD、既存のVision-OPD等のベースラインと比較検証を実施。さらに、Holdoutタスクにおいても汎化性能の低下がないことを示し、特に細かい視覚的証拠が必要なタスクで大幅な精度向上を確認した。 |
| 議論はある？ | 実験において、ハイパーパラメータτ（温度）やη（重み付け）の設定が性能に直結することを示している。また、視覚的な証拠が広範囲に及ぶ場合など、特定の条件下での制約については今後のさらなる検討が必要とされる。 |
| 次に読むべき論文は？ | [Vision-OPD: Learning to see fine details for multimodal LLMs via on-policy self-distillation](https://arxiv.org/abs/2605.18740), [Opd-v: Visual on-policy self-distillation with modality balance](https://arxiv.org/abs/2608.05131) |
| PDFリンク | https://arxiv.org/pdf/2610.26856v1 |
