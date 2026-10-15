---
title: "VITAL: From Visual Motion to Precise Action"
date: 2026-10-15
arxiv_id: 2610.20604v1
url: http://arxiv.org/abs/2610.20604v1
---

# VITAL: From Visual Motion to Precise Action

| 項目 | 内容 |
|---|---|
| どんなもの？ | 自動運転の行動予測において、視覚的な動き（モーションスキャフォールド）と、それによって補完しきれないセンチメートル単位の精密な誤差（メトリックレジデュアル）を分離して学習・予測するアクション・トークナイザー「VITAL」を提案している。 |
| 先行研究と比べてどこがすごい？ | 従来のワールドアクションモデルでは、視覚予測と行動生成の表現が独立しがちで、精密な制御に必要な詳細が失われていた。VITALは、粗い軌道骨組みと精密な残差を分離することで、単一の推論ステップで高精度な軌道生成と効率的な強化学習ベースの事後改善を両立している。 |
| 技術や手法のキモはどこ？ | 視覚的な動きを主たるターゲットとし、残差を正規化された学習スケールで扱うトークナイザー構成。フローマッチングを用いてこれらを統合予測する点と、推論時に追加のデノイジングや候補探索を必要とせず、固定されたベースポリシに対する拘束付きの局所的修正を行う残差RLを組み合わせた点。 |
| どうやって有効だと検証した？ | NAVSIM v1/v2 navtestおよびnavhardベンチマークを使用。PDMS（Planning Driving Metric Score）やEPDMSを用いて、単一の推論ステップで既存手法を上回る性能（NAVSIM v1で90.8 PDMS）を達成し、かつ推論速度が大幅に向上することを確認した。 |
| 議論はある？ | 局所的な残差修正は、高レベルなルート選択の誤りや、大きな視覚予測誤差を修正することはできない。また、ベンチマーク上の平均性能は優れているものの、未知の環境や特殊な状況下での安全性が保証されるわけではなく、さらなる検証が必要である。 |
| 次に読むべき論文は？ | [SimWAM](https://arxiv.org/abs/2608.07468) (SimWAM: A Simple World Action Model for End-to-End Autonomous Driving), [DiffusionDrive](https://arxiv.org/abs/2411.15139) (DiffusionDrive: Truncated Diffusion Model for End-to-End Autonomous Driving) |
| PDFリンク | https://arxiv.org/pdf/2610.20604v1 |
