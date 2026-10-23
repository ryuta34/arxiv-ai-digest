---
title: "Direct Pass@$k$ Optimization for Thought Pruning: Balancing Quality and Diversity in Test-Time Reasoning"
date: 2026-10-23
arxiv_id: 2610.31667v1
url: http://arxiv.org/abs/2610.31667v1
---

# Direct Pass@$k$ Optimization for Thought Pruning: Balancing Quality and Diversity in Test-Time Reasoning

| 項目 | 内容 |
|---|---|
| どんなもの？ | 推論モデルが生成する多数の候補解決策（ロールアウト）を、完了前に一部だけ選択して推論コストを削減するテスト時の剪定手法「PKTP」の提案。品質（正解しやすさ）と多様性（正解への到達ルートの分散）を直接バランスさせることで、推論の精度と効率を両立する。 |
| 先行研究と比べてどこがすごい？ | 既存手法は「品質のみ（線形プローブ）」や「多様性のみ（RepExp）」に偏りがちであったが、本手法はpass@k（少なくとも一つが正解する確率）を直接最大化する目的関数を導入した点。これにより、トレードオフを明示的に最適化でき、特に中程度の剪定数で既存手法を上回る精度を実現した。 |
| 技術や手法のキモはどこ？ | ロールアウトの成否を潜在ガウスモデルでモデル化し、その成否が互いに相関すること（類似したロールアウトは成否も連動する）を考慮した点。この目的関数は複雑だが、サブモジュラ性を持つ二次近似（closed-form）を導出したことで、高速な貪欲法による選択が可能となった。 |
| どうやって有効だと検証した？ | 8つのオープンウェイト推論モデルと、AIME、HMMT、Omni-MATHなどの複数の数学・論理推論ベンチマークを使用して検証。ランダム剪定と比較して、幅広いモデルとベンチマークで高いpass@kの向上を達成した。 |
| 議論はある？ | 剪定時に使用する表現（EMAによる隠れ状態のプーリング）の品質が推論の成否判定の限界になる可能性がある。より正確に正解を予測できる表現の獲得が今後の課題である。 |
| 次に読むべき論文は？ | [39] Tuyls et al., "Representation-based exploration for language models: From test-time to post-training" (RepExpの出典) / [54] Zhang et al., "Reasoning models know when they’re right: Probing hidden states for self-verification" |
| PDFリンク | [https://arxiv.org/pdf/2610.31667v1](https://arxiv.org/pdf/2610.31667v1) |
