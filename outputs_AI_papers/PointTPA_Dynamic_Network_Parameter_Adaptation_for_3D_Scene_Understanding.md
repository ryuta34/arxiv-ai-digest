---
title: "PointTPA: Dynamic Network Parameter Adaptation for 3D Scene Understanding"
date: 2026-04-07
arxiv_id: 2604.04933v1
url: http://arxiv.org/abs/2604.04933v1
---

# PointTPA: Dynamic Network Parameter Adaptation for 3D Scene Understanding

| 項目 | 内容 |
|---|---|
| どんなもの？ | 3Dシーン理解のための、テスト時パラメータ適応（TPA）フレームワーク「PointTPA」。事前学習済みのモデルを凍結したまま、シーンごとの入力に応じて動的にネットワークパラメータを適応させることで、高い精度と計算効率を両立する。 |
| 先行研究と比べてどこがすごい？ | 従来のPEFT手法が静的なパラメータ変換に留まっていたのに対し、入力のシーンに応じた動的な重み生成を実現した。PTv3などのバックボーンに対して、わずか2%未満のパラメータ追加でSOTA（当時）を達成し、計算効率も向上させている。 |
| 技術や手法のキモはどこ？ | 入力ポイントクラウドを空間的に整理する「Serialization-based Neighborhood Grouping (SNG)」と、その局所的特徴に基づき動的な重みを生成する「Dynamic Parameter Projector (DPP)」の組み合わせ。 |
| どうやって有効だと検証した？ | ScanNet、ScanNet++、S3DISなどの主要な3Dシーン理解ベンチマークを使用。フルファインチューニングや既存のPEFT手法（IDPT, DAPT, PointGST等）と比較し、mIoU等の精度向上と、推論時間・パラメータ数の効率性を実証した。 |
| 議論はある？ | 動的パラメータの過度な導入は最適化を困難にする可能性があるため、挿入位置や構成の最適化が重要である点。また、より複雑なシーンにおけるさらなる頑健性の向上が将来課題。 |
| 次に読むべき論文は？ | [Point Transformer V3 (PTv3)](https://arxiv.org/abs/2407.15867), [PointGST](https://arxiv.org/abs/2403.11244), [DAPT](https://arxiv.org/abs/2403.11181) |
| PDFリンク | https://arxiv.org/pdf/2604.04933v1 |
