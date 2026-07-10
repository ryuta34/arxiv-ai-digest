---
title: "Wat3R: Underwater 3D Geometry Learning without Annotations"
date: 2026-07-10
arxiv_id: 2607.08772v1
url: http://arxiv.org/abs/2607.08772v1
---

# Wat3R: Underwater 3D Geometry Learning without Annotations

| 項目 | 内容 |
|---|---|
| どんなもの？ | 水中環境における3D再構成（深度推定、点群生成、カメラポーズ推定）をアノテーションなしで行うための半教師あり学習フレームワーク「Wat3R」。既存のオンランド向け学習済みモデル（VGGT）を、シミュレートされた水中データと実世界の未ラベル動画データを用いて水中ドメインへ適応させる。 |
| 先行研究と比べてどこがすごい？ | 従来手法が大規模で高品質な3Dアノテーションを必要としたのに対し、水中環境でのアノテーション不要な学習を実現した。また、水中での光の減衰や散乱による画質劣化を補完する「クロスビュー整合性損失」を導入し、既存手法を大幅に上回る頑健性を達成した点。 |
| 技術や手法のキモはどこ？ | 教師・生徒モデルを用いた平均教師（Mean Teacher）ベースの学習。特に、複数ビュー間の幾何学的な整合性を担保する「クロスビュー整合性損失（Cross-view Consistent Loss）」と、動的物体や濁った領域を除外して信頼性の高いピクセルのみを選択する「静的マスク（Static Mask）」の導入。 |
| どうやって有効だと検証した？ | 著者らが構築した多様な水中データセット「Water3D」および既存の公開データセット（Sea-thru, FLSea-VI, SQUID等）を用いて、深度推定や点群再構成の精度を比較。SOTAモデルと比較して、Rel誤差やRMSE等の主要指標で顕著な精度向上を示した。 |
| 議論はある？ | 非常に動的な環境（活発な海洋生物やダイバーの動き）では、静的マスクが学習信号を過剰に抑制する可能性がある。また、濁度が極端に高い極限状況下では、依然としてマッチング精度に限界があることを認めている。 |
| 次に読むべき論文は？ | [Wang et al., "VGGT: Visual Geometry Grounded Transformer", CVPR 2025](https://arxiv.org/abs/25xx.xxxxx) ※VGGTの詳細は論文参照、[Akkaynak & Treibitz, "Sea-thru", CVPR 2019](https://arxiv.org/abs/1903.00350) |
| PDFリンク | https://arxiv.org/pdf/2607.08772v1 |
