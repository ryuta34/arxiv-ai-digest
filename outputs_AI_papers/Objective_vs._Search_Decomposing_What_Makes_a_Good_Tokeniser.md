---
title: "Objective vs. Search: Decomposing What Makes a Good Tokeniser"
date: 2026-09-17
arxiv_id: 2609.19145v1
url: http://arxiv.org/abs/2609.19145v1
---

# Objective vs. Search: Decomposing What Makes a Good Tokeniser

| 項目 | 内容 |
|---|---|
| どんなもの？ | 言語モデルのトークナイザーにおける「最適化目的（圧縮 vs. 対数尤度）」と「探索手法（ボトムアップ vs. トップダウン）」という2つの独立した設計軸を分離・解明した研究。既存のトークナイザーの設計を体系化し、新たな手法を導入することでトークナイザーの設計指針を提示した。 |
| 先行研究と比べてどこがすごい？ | 従来混同されていた「目的」と「探索」を分離し、2×2のデザイン空間を完全に網羅した点。特に、ボトムアップ型探索が目的関数に関わらずビット単価（BPB）においてトップダウン型より一貫して優れていることを突き止めた。 |
| 技術や手法のキモはどこ？ | BPE（ボトムアップ・圧縮）とUnigramLM（トップダウン・尤度）に加え、対となるBottomUpLL（ボトムアップ・尤度）とTopDownComp（トップダウン・圧縮）を新たに構築・実装し、各手法を同条件で厳密に比較した点。 |
| どうやって有効だと検証した？ | 英語および多言語コーパスを用い、モデルサイズを100Mから1Bまで変化させて言語モデルを訓練し、BPBによる性能評価とBLiMPによる文法性の評価を行った。さらに、語彙の重なりやトークン分布の解析を実施した。 |
| 議論はある？ | 最大1Bパラメータまでの検証であり、より大規模なモデルや長大な学習 horizon における変化は未確認。また、多言語における特定の語族への適応や、近似的計算（局所置換）の妥当性についても今後の課題としている。 |
| 次に読むべき論文は？ | [Schmidt et al. (2024) "Tokenization is more than compression"](https://arxiv.org/abs/2411.08671) や [Whittington et al. (2025) "Tokenisation is NP-complete"](https://arxiv.org/abs/2502.16480) |
| PDFリンク | https://arxiv.org/pdf/2609.19145v1 |
