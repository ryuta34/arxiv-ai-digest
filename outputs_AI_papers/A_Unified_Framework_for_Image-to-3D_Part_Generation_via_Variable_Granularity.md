---
title: "A Unified Framework for Image-to-3D Part Generation via Variable Granularity"
date: 2026-10-23
arxiv_id: 2610.31671v1
url: http://arxiv.org/abs/2610.31671v1
---

# A Unified Framework for Image-to-3D Part Generation via Variable Granularity

| 項目 | 内容 |
|---|---|
| どんなもの？ | 画像から3Dパーツを生成するための統一フレームワーク「FlexPart」。スパースな点やバウンディングボックス、密なマスクといった異なる粒度の幾何学的条件（プロンプト）を単一モデルで柔軟に処理し、高品質な3Dパーツを生成できる。 |
| 先行研究と比べてどこがすごい？ | 従来手法は特定の入力粒度（マスクのみ等）に特化していたが、本作は単一モデルで多様なプロンプトを統合処理できる。また、強力な事前知識を持つ入力を利用した幾何学的ガイダンスにより、スパースな入力でも高品質な生成を可能にした。 |
| 技術や手法のキモはどこ？ | Gated AdaLNによる多様な入力の柔軟な統合と、学習時に微分可能な最適輸送（Partial Optimal Transport）を用いて、密な空間的知識をスパースな表現へと転移させる「非対称幾何学的ガイダンス」にある。 |
| どうやって有効だと検証した？ | PartVerseXLやPartObjaverse-Tinyデータセットを用いて評価。Chamfer Distance（CD）やIoU等の指標で他手法（TripoSG、OmniPart等）を上回る精度を達成し、かつ多様な入力形式に対する堅牢性を定量的・定性的に検証した。 |
| 議論はある？ | 単一視点の画像条件に依存するため、隠蔽（オクルージョン）された領域の復元や、複雑な遮蔽下での空間推論に限界がある点を課題として挙げている。 |
| 次に読むべき論文は？ | [PartCrafter](https://arxiv.org/abs/2501.12202)や[OmniPart](https://arxiv.org/abs/2501.12202)、[TripoSG](https://arxiv.org/abs/2501.12202)など、パーツベースの3D生成に関する近年の研究。 |
| PDFリンク | https://arxiv.org/pdf/2610.31671v1 |
