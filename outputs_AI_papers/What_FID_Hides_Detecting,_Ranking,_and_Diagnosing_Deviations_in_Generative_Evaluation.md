---
title: "What FID Hides: Detecting, Ranking, and Diagnosing Deviations in Generative Evaluation"
date: 2026-08-27
arxiv_id: 2608.24881v1
url: http://arxiv.org/abs/2608.24881v1
---

# What FID Hides: Detecting, Ranking, and Diagnosing Deviations in Generative Evaluation

| 項目 | 内容 |
|---|---|
| どんなもの？ | 生成モデルの評価指標であるFIDやKIDの限界（モーメントのみの評価や方向性の欠如）を克服する、新しい評価診断手法「ZID（Z-resolved Integrated Diagnostic）」を提案する論文。モデルのランク付け、統計的な検定、および分布の歪みが「過小分散か過大分散か」を診断する機能を提供する。 |
| 先行研究と比べてどこがすごい？ | FID/KIDなどの従来のスカラ値指標が抱える「分布の違いを見落とす（matched-moment blind spot）」という脆弱性を指摘し、単なるスカラ値ではなく、順位付け・統計的検定・符号付きの分散診断という3つの出力を組み合わせることで、より詳細な評価が可能になった点。 |
| 技術や手法のキモはどこ？ | グラフベースの順位統計（RISE）とカーネルベースの検定（GPK）を組み合わせた6つの「アーム」を構築し、それらをFlat-Simes法で集約することで、特定の異常に対して感度を高く保ちつつ全体的な検出力を高めたこと。また、分散のズレを符号付きで特定する診断ロジックを導入した点。 |
| どうやって有効だと検証した？ | 制御された変換を加えたCIFAR-10データセットを用いた広範なシミュレーションと、BigGAN, DDPM, DiT-XL/2, SiT-XL/2などの主要な生成モデルを用いた実データ評価を実施。FIDで逆転や無反応が起きるケースでも、ZIDが安定して分布の乖離を捉えられることを示した。 |
| 議論はある？ | 計算コストやアルゴリズムの複雑性がFIDより高い可能性がある。また、診断指標の「Ambiguous（判定不能）」なケースの扱いなど、指標の解釈性に関する境界条件について言及がある。 |
| 次に読むべき論文は？ | [Heusel et al. (2017) GANs trained by a two time-scale update rule](https://arxiv.org/abs/1706.08500)、[Bińkowski et al. (2018) Demystifying MMD GANs](https://arxiv.org/abs/1801.01401)、[Song and Chen (2024) Generalized kernel two-sample tests](https://arxiv.org/abs/2205.10905) |
| PDFリンク | https://arxiv.org/pdf/2608.24881v1 |
