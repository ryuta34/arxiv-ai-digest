---
title: "ActionParty: Multi-Subject Action Binding in Generative Video Games"
date: 2026-04-03
arxiv_id: 2604.02330v1
url: http://arxiv.org/abs/2604.02330v1
---

# ActionParty: Multi-Subject Action Binding in Generative Video Games

| 項目 | 内容 |
|---|---|
| どんなもの？ | 複数のエージェント（主体）が登場する環境において、各主体に対して個別の行動を正確に割り当て（アクション・バインディング）、制御可能な動画生成を行うマルチエージェント・ワールドモデル。 |
| 先行研究と比べてどこがすごい？ | 既存の動画生成モデルは複数主体の同時制御が困難という課題があったが、本手法は最大7体の主体を同時に制御可能にし、アクション追従精度やアイデンティティの一貫性を大幅に向上させた。 |
| 技術や手法のキモはどこ？ | 主体の状態を保持する「subject state tokens（主体状態トークン）」を導入し、アテンションマスクで行動と主体の対応を強制した点。また、3D RoPE biasingを用いて、主体の空間位置と状態トークンを明示的に紐付けた点。 |
| どうやって有効だと検証した？ | Melting Potベンチマーク（46種類の2Dゲーム）を用い、行動追従精度（MA）、主体保存性（SP）、検出率（DR）などの指標で評価。ゼロショットI2Vやテキストベースのベースラインに対して優位性を確認。 |
| 議論はある？ | 現時点では完全なリアルタイム生成には至っていない点、主体の消失がインタラクションを妨げる場合がある点、および2D環境に特化しており3D環境への適用が将来課題である点。 |
| 次に読むべき論文は？ | [Genie: Generative interactive environments](https://arxiv.org/abs/2402.15391)、[Diffusion models are real-time game engines](https://arxiv.org/abs/2501.12781) |
| PDFリンク | https://arxiv.org/pdf/2604.02330v1 |
