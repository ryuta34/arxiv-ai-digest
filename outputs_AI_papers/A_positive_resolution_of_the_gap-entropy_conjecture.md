---
title: "A positive resolution of the gap-entropy conjecture"
date: 2026-09-10
arxiv_id: 2609.10529v1
url: http://arxiv.org/abs/2609.10529v1
---

# A positive resolution of the gap-entropy conjecture

| 項目 | 内容 |
|---|---|
| どんなもの？ | 固定信頼度のもとでの最良腕識別（Best-arm identification）において、以前提案された「ギャップ・エントロピー予想（Gap-Entropy Conjecture）」を肯定的に解決した論文。各腕のギャップの分布に応じてサンプリングコストがどのように決まるかを理論的に解明し、インスタンスごとに最適な計算量の上界と下界を示した。 |
| 先行研究と比べてどこがすごい？ | 従来手法には残っていた余分な多対数因子（polylogarithmic factor）を取り除き、あらゆる1-サブガウス分布の報酬に対してインスタンスごとに最適な（instance-optimal）性能を達成する単一のアルゴリズムを構築した点。また、先行研究で課されていたアルゴリズムの制限や特定のインスタンス構造（ギャップのべき乗など）への依存を排除した。 |
| 技術や手法のキモはどこ？ | 腕をギャップの大きさに基づいて幾何学的な「シェル（殻）」に分割し、そのエントロピーに基づいて予算配分を行う手法。各ステップでMedianおよびFractionテストを用いてアクティブな腕集合を効率的に削減し、未知のギャップ構造をデータから発見して予算を適応させる「適応的サンプリング手法」を構築したこと。 |
| どうやって有効だと検証した？ | 理論的な解析により、最良腕識別問題における期待サンプルコストが $H(\log(1/\delta) + \text{Ent}(I))$ のオーダーであることを、下界の証明（標準的な変更測度論法を拡張）と上界の構成（適応的な消去アルゴリズム）の両面から示した。 |
| 議論はある？ | 提示されたアルゴリズムはインスタンスに適応可能だが、その適応コストとして $g^{-2} \log \log(e^e/g)$ という項が必要であり、これは2腕の場合でも不可避であることが議論されている。 |
| 次に読むべき論文は？ | [1] Chen and Li (2015) [On the optimal sample complexity for best arm identification], [2] Chen and Li (2016) [Open problem: Best arm identification], [3] Chen, Li and Qiao (2017) [Towards instance optimal bounds for best arm identification] |
| PDFリンク | https://arxiv.org/pdf/2609.10529v1 |
