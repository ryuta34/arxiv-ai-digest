---
title: "Principia: Relational Physics Tests for Video Models"
date: 2026-09-04
arxiv_id: 2609.04200v1
url: http://arxiv.org/abs/2609.04200v1
---

# Principia: Relational Physics Tests for Video Models

| 項目 | 内容 |
|---|---|
| どんなもの？ | 動画生成モデルおよびVision-Languageモデル（VLM）の物理推論能力を評価する新しいベンチマーク「Principia」を提案した論文。実際の物理実験に基づくペアの物体を用いた相対的な関係性の整合性を測定することで、モデルの物理的理解度を評価する。 |
| 先行研究と比べてどこがすごい？ | フレームレートやカメラキャリブレーション等の曖昧な指標に依存せず、物体間の相対的な動きという「物理的な不変量」を用いて、校正不要（Unit-Free）かつ定量的・多角的に物理推論を評価できる点。 |
| 技術や手法のキモはどこ？ | Newton力学に基づく8つの現象（重力、衝突、摩擦、回転慣性など）に対し、ペアとなる物体の動きが満たすべき不変関係を定義し、画像空間での測定値から連続的な「整合性スコア」を算出する手法。 |
| どうやって有効だと検証した？ | 500以上の実写映像データと、Isaac Simを用いた制御可能な合成テストベッドを構築。6つの主要な動画生成モデルと4つのVLMを評価し、VBench等で高スコアを出すモデルでも物理整合性では著しく低い性能を示すことを明らかにした。 |
| 議論はある？ | モデル規模の拡大が必ずしも物理的な整合性の向上に直結しないことや、現在の動画生成技術が視覚的なリアリズムは高くても物理法則の構造的な理解が欠けている点が指摘されている。今後はアーキテクチャや訓練手法の見直しが必要である。 |
| 次に読むべき論文は？ | [Thozhiyoor et al., "Objects in generated videos are slower than they appear..."](https://arxiv.org/abs/2512.02016)、[Huang et al., "VBench: Comprehensive benchmark suite for video generative models"](https://arxiv.org/abs/2403.11173) |
| PDFリンク | https://arxiv.org/pdf/2609.04200v1 |
