---
title: "Surprises in Proper Positive-Only Learning"
date: 2026-06-29
arxiv_id: 2606.28309v1
url: http://arxiv.org/abs/2606.28309v1
---

# Surprises in Proper Positive-Only Learning

| 項目 | 内容 |
|---|---|
| どんなもの？ | 陽性サンプルのみ（positive-only）から概念クラスを学習する「陽性のみ学習（positive-only learning）」において、学習器が概念クラス自身に属する仮説を出力する「適切な学習（proper learning）」の実現可能性を理論的に解明した研究。 |
| 先行研究と比べてどこがすごい？ | 長年未解決であった「適切な学習」の学習可能性を特徴付ける必要十分条件（VC次元の有限性に加え、新たに導入した「一様外部分離可能性（uniform exterior separability）」）を初めて提示した点。 |
| 技術や手法のキモはどこ？ | 陽性サンプルによって強制される仮説の共通部分（閉包）が概念クラスから外れる場合でも、ランダム化を用いることで、クラスの範囲内に留まりつつ外側を適切に制御する手法を確立したこと。 |
| どうやって有効だと検証した？ | 提案した組合せ論的条件を用いた理論的証明により、Nataraajanの予想（偽陽性ゼロを課さない場合でも、本質的に同じ条件が必要であるという推測）を反証し、標準的なPAC学習との決定的な差（適切な/不適切な学習の分離やランダム化の必要性）を証明した。 |
| 議論はある？ | 現在の理論的な学習可能性の特定にとどまっており、効率的なアルゴリズムの構築や、より詳細なランダムビットの計算量などの統計的最適性の追求が今後の課題である。 |
| 次に読むべき論文は？ | [Nat87] B. Natarajan, "On learning boolean functions" (本研究で反証された予想の基点), [MY16] S. Moran and A. Yehudayoff, "Sample Compression Schemes for VC Classes" (本研究で証明の鍵となった道具立て). |
| PDFリンク | [https://arxiv.org/pdf/2606.28309v1](https://arxiv.org/pdf/2606.28309v1) |
