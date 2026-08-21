---
title: "WithEveryone: Unified Planning and Identity Grounding for Group Image Generation"
date: 2026-08-21
arxiv_id: 2608.20336v1
url: http://arxiv.org/abs/2608.20336v1
---

# WithEveryone: Unified Planning and Identity Grounding for Group Image Generation

| 項目 | 内容 |
|---|---|
| どんなもの？ | 5〜10人の複数人を同時に生成するグループ画像生成モデル「WithEveryone」です。IDトークンによるアイデンティティ管理と、構造化されたレイアウト計画を単一モデル内で統合し、高品質かつID保持精度の高い集合写真生成を実現します。 |
| 先行研究と比べてどこがすごい？ | 従来手法（GPT-Image 2等）では困難だった多人数（5〜10人）生成における「IDの混同」や「コピー＆ペーストのアーティファクト」を劇的に低減しました。特に、レイアウトアノテーションに基づいた監視を行うことで、人数の増加に伴うアイデンティティ精度の低下を抑え、高い忠実度を達成しています。 |
| 技術や手法のキモはどこ？ | IDをトークン化してレイアウトと直接結びつける「ID–Layout binding」、生成前にアイデンティティ表現を予測させる「ID Representation Forcing」、およびレイアウトの注釈領域を利用してIDを直接監視する「Layout-Grounded ID Loss (LG-ID Loss)」を導入した点です。 |
| どうやって有効だと検証した？ | 5〜10人のIDを含む210個の実写グループ画像を用いた評価ベンチマークを独自に構築しました。GPT-Image 2やNano Banana等の最新モデルと比較し、Sim(Tgt)スコアの向上とコピー＆ペーストアーティファクトの低減、および高いIDカバー率を示しました。 |
| 議論はある？ | 生成モデル全般に言えることですが、個人の同意なく似た画像を生成するリスクがあるため、出典元明示（provenance signalling）や本人の同意取得が不可欠であると述べています。また、レイアウト評価の難しさや、評価ベンチマークの規模に関する限定性も言及しています。 |
| 次に読むべき論文は？ | [ATLAS (Liu et al., 2026)](https://arxiv.org/abs/2607.16409), [WithAnyone (Xu et al., 2025)](https://arxiv.org/abs/2510.14975), [Transfusion (Zhou et al., 2025)](https://openreview.net/forum?id=6446-6469) |
| PDFリンク | [https://arxiv.org/pdf/2608.20336v1](https://arxiv.org/pdf/2608.20336v1) |
