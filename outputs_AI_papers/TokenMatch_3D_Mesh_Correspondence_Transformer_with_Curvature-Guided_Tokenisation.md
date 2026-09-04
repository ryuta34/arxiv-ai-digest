---
title: "TokenMatch: 3D Mesh Correspondence Transformer with Curvature-Guided Tokenisation"
date: 2026-09-04
arxiv_id: 2609.04202v1
url: http://arxiv.org/abs/2609.04202v1
---

# TokenMatch: 3D Mesh Correspondence Transformer with Curvature-Guided Tokenisation

| 項目 | 内容 |
|---|---|
| どんなもの？ | 3Dメッシュの形状対応付け（コレスポンス）を高精度かつ高速に行うための、トランスフォーマーベースの統合的な学習モデル。部分的な形状や非等長変形を含む困難な条件下でも、教師あり学習のみで堅牢な対応付けを実現する。 |
| 先行研究と比べてどこがすごい？ | 既存手法が依存していたテンプレートやカテゴリ固有の前提を排除しつつ、部分対部分の学習のみで全形状への汎用性を達成した点。また、従来の最適化ベースの手法と比較して大幅に高速な推論（サブ秒単位）が可能である。 |
| 技術や手法のキモはどこ？ | 曲率に基づいた「曲率ガイド付きトークン化（Curvature-Guided Tokenisation）」と、重なり（オーバーラップ）を許容するパッチ生成手法。これにより、メッシュの不規則なサンプリングや局所的な幾何変化に対しても、幾何学的に一貫した特徴抽出が可能となった。 |
| どうやって有効だと検証した？ | CP2P, PSMAL, BeCoS等の主要な部分形状データセットに加え、FAUST, SCAPE等の全形状データセットを用いた網羅的な評価を実施。平均測地誤差（GE）およびIntersection-over-Union（IoU）指標において、既存の学習ベース手法を上回る性能を示した。 |
| 議論はある？ | 現在の実装は測地距離計算に依存しており、メッシュ解像度が非常に高い場合に計算コストが増大する可能性がある。また、非常にノイズの多い非構造的な形状に対する頑健性の更なる向上を将来の課題としている。 |
| 次に読むべき論文は？ | [3] Deep partial functional maps (DPFM), [72] Echomatch: Partial-to-partial shape matching via correspondence reflection, [38] Meshmae: Masked autoencoders for 3d mesh data analysis |
| PDFリンク | https://arxiv.org/pdf/2609.04202v1 |
