---
title: "Weak-to-Strong Generalization via Direct On-Policy Distillation"
date: 2026-07-07
arxiv_id: 2607.05394v1
url: http://arxiv.org/abs/2607.05394v1
---

# Weak-to-Strong Generalization via Direct On-Policy Distillation

| 項目 | 内容 |
|---|---|
| どんなもの？ | 強化学習(RL)を用いて学習した小規模モデルの「強化学習によるポリシーの改善分」のみを抽出し、より強力なモデルへ効率的に蒸留する弱から強への汎化フレームワーク「Direct-OPD」を提案する。 |
| 先行研究と比べてどこがすごい？ | 従来の教師モデルの最終ポリシーを模倣する手法（OPD）と異なり、教師モデルの「RLによる改善の方向性」のみを転移するため、学生モデルが自身の能力を超えた教師モデルの制限に縛られず、効率的かつ確実に性能向上できる点。 |
| 技術や手法のキモはどこ？ | 教師モデルのRL前後におけるポリシーの対数比（$\log \pi_T - \log \pi_{T_{\text{ref}}}$）を、学生モデルが生成する状態に対する「denseな暗黙的報酬」として利用する点。また、KL係数を学習中に適応的に制御する手法を導入している。 |
| どうやって有効だと検証した？ | Qwen3-1.7B/4BやR1-Distill-7B等のモデルに対し、AIME 2024/2025データセットを用いて検証。Direct-OPDは同等の計算予算で直接RLを行うよりも高い精度を達成し、教師モデルより元々高性能な学生に対しても改善が見られた。 |
| 議論はある？ | 教師モデルと学生モデルのペアに依存して最適なKL強度が異なる点、また教師モデルの改善信号が学生モデルが訪れる状態で意味をなさない場合には失敗する可能性があるという条件付きの信号であることが限界として挙げられる。 |
| 次に読むべき論文は？ | [1] DeepSeek-R1 (Nature 2025), [5] Rethinking on-policy distillation (arXiv:2604.13016), [97] Weak-to-strong preference optimization (arXiv:2410.18640) |
| PDFリンク | https://arxiv.org/pdf/2607.05394v1 |
