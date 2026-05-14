---
title: "What is Learnable in Valiant's Theory of the Learnable?"
date: 2026-05-14
arxiv_id: 2605.13840v1
url: http://arxiv.org/abs/2605.13840v1
---

# What is Learnable in Valiant's Theory of the Learnable?

| 項目 | 内容 |
|---|---|
| どんなもの？ | 1984年のValiantの論文で提案された「正例のみ観測し、帰属クエリが可能な学習モデル」の学習可能性を解明した理論的研究。PAC学習と正例のみ学習（クエリなし）の間に位置する、新たな学習クラスの特性を明らかにしました。 |
| 先行研究と比べてどこがすごい？ | 従来の学習モデルでは未解決だった「3つの要素（正例のみ・片側誤差・帰属クエリ）」を組み合わせたモデルの学習可能性を、「適応型クエリ圧縮スキーム」という概念を用いて完全に特徴付けた点です。特に、ハーフスペースに対する初の学習アルゴリズムを提案しました。 |
| 技術や手法のキモはどこ？ | 「適応型クエリ圧縮スキーム（Adaptive-Query Compression Scheme）」の導入です。これは、学習者が受け取った正例に対して、帰属クエリを行うことでそのサンプルを「証明（認証）」し、版空間（version space）を絞り込む対話的な仕組みです。 |
| どうやって有効だと検証した？ | 帰属クエリを用いた新しい学習アルゴリズムを設計し、ハーフスペースの学習可能性を証明しました。また、VC次元を用いた下界の証明や、PAC学習との比較を通じた理論的な検証を行いました。 |
| 議論はある？ | 現在のアルゴリズムは必ずしも多項式時間ではない点が挙げられます。また、一般の無限ドメインに対する学習可能性の完全な特徴付けや、ハーフスペースの学習における最適なサンプル・クエリ複雑度の追求が今後の課題とされています。 |
| 次に読むべき論文は？ | [Val84a] L. G. Valiant, "A Theory of the Learnable" (1984) / [Nat87] B. K. Natarajan, "On Learning Boolean Functions" (1987) / [HKLM20] M. Hopkins et al., "Point Location and Active Learning" (2020) |
| PDFリンク | https://arxiv.org/pdf/2605.13840v1 |
