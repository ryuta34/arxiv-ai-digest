---
title: "One Token per Highly Selective Frame: Towards Extreme Compression for Long Video Understanding"
date: 2026-04-16
arxiv_id: 2604.14149v1
url: http://arxiv.org/abs/2604.14149v1
---

# One Token per Highly Selective Frame: Towards Extreme Compression for Long Video Understanding

| 項目 | 内容 |
|---|---|
| どんなもの？ | 長時間の動画理解を効率化するためのExtreme Video Token Compressionモデル「XComp」です。フレーム単位で1トークンまで極限に圧縮し、さらに質問に関連するフレームを適切に選択することで、長時間動画の理解精度と計算効率を向上させます。 |
| 先行研究と比べてどこがすごい？ | 従来のヒューリスティックな圧縮手法と異なり、LLM層を教師ありで学習させることで、情報の損失を最小限に抑えつつ大幅な圧縮（one-token-per-frame）を実現しました。データ効率が高く、わずか2.5%の学習データで既存モデル（VideoChat-Flash）の精度を向上させています。 |
| 技術や手法のキモはどこ？ | 学習可能な「LP-Comp（各LLM層で段階的にトークンを圧縮）」と、推論時に質問内容に基づいて関連性の高いフレームを選択する「QC-Comp（セグメント化した局所アテンションを利用したフレーム選択）」の組み合わせです。 |
| どうやって有効だと検証した？ | LongVideoBench, MLVU, VideoMME等の長時間動画理解ベンチマークで性能を評価し、ベースラインモデルを上回る精度を達成しました。また、推論の遅延と計算量を大幅に削減したこと、多様なモデルへの適用可能性も実証しました。 |
| 議論はある？ | 計算予算の制約により統計的な実験回数（シード数）は限られています。また、本手法は特定のベースモデルを前提としており、より大規模なVLMへの適応や、フレーム選択とトークン圧縮の共同最適化が今後の課題です。 |
| 次に読むべき論文は？ | [VideoChat-Flash [35]](https://arxiv.org/abs/2501.00574)、[LLaVA-Next-Video [78]](https://arxiv.org/abs/2410.02713)、[LongViTA [55]](https://arxiv.org/abs/2502.05177) |
| PDFリンク | https://arxiv.org/pdf/2604.14149v1 |
