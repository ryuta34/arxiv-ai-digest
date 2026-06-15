---
title: "Instruct-Particulate: Scaling Feed-Forward 3D Object Articulation with Kinematic Control"
date: 2026-06-15
arxiv_id: 2606.14699v1
url: http://arxiv.org/abs/2606.14699v1
---

# Instruct-Particulate: Scaling Feed-Forward 3D Object Articulation with Kinematic Control

| 項目 | 内容 |
|---|---|
| どんなもの？ | 任意の静止3Dメッシュに対し、テキストや点による動的なプロンプト（指示）を与えることで、その部品構成と関節運動パラメータを予測するフィードフォワード型モデル。 |
| 先行研究と比べてどこがすごい？ | 従来のモデルが小規模なデータセットに依存していたのに対し、VLM（視覚言語モデル）を用いて15万件以上の多様な3Dオブジェクトを自動擬似ラベル付けし、学習データの規模と多様性を飛躍的に向上させた点。 |
| 技術や手法のキモはどこ？ | キネマティック（運動学的）な指示を条件として与える新しいモデル構造と、VLMを活用した大規模な自動データ生成パイプラインにより、汎用的な「指示可能な（Instructable）」 articulation推論を実現したこと。 |
| どうやって有効だと検証した？ | 「Lightwheel」データセットを用い、画像のみ、メッシュ入力、メッシュ＋キネマティック条件の3つの設定で既存手法と比較し、精度の高さ（Part Matchや幾何学的指標）を実証した。 |
| 議論はある？ | AI生成メッシュ特有のアーティファクトによるセグメンテーション精度の低下や、出力されたアセットが物理シミュレーションに直接使用するための物理的特性を欠いている点が限界として挙げられる。 |
| 次に読むべき論文は？ | [Particulate: Feed-forward 3d object articulation](https://arxiv.org/abs/2606.14699v1)（本論文のベース）、[Articraft: An agentic system for scalable articulated 3d asset generation](https://arxiv.org/abs/2605.15187) |
| PDFリンク | https://arxiv.org/pdf/2606.14699v1 |
