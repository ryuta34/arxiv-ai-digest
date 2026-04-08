---
title: "HaloProbe: Bayesian Detection and Mitigation of Object Hallucinations in Vision-Language Models"
date: 2026-04-08
arxiv_id: 2604.06165v1
url: http://arxiv.org/abs/2604.06165v1
---

# HaloProbe: Bayesian Detection and Mitigation of Object Hallucinations in Vision-Language Models

| 項目 | 内容 |
|---|---|
| どんなもの？ | 視覚言語モデル（LVLM）における物体幻覚（hallucination）を検出し、モデルの内部構造を改変することなく緩和するベイズ的フレームワーク「HaloProbe」の提案。トークン位置や物体出現頻度といった外部特徴量と、内部の注意・推論信号を統合することで、モデルの信頼性を向上させる手法。 |
| 先行研究と比べてどこがすごい？ | 既存の介入型手法がモデルの内部パラメータを直接操作し、文章の流暢性や多様性を損なうリスクがあるのに対し、HaloProbeは非侵襲的（外部スコアとしての利用）であり、流暢性を保ちつつ高い検出・緩和精度を実現した点。 |
| 技術や手法のキモはどこ？ | トークン位置や物体繰り返しなどの「外部特徴」と、モデルの注意・ロジットなどの「内部特徴」をベイズの定理で因数分解して学習する点。また、学習時のデータ不均衡を解消する「クラス均衡化」と、誤ったショートカット学習を防ぐ「事後補正」により、頑健な推論を可能にしたこと。 |
| どうやって有効だと検証した？ | MS COCOデータセットを用いて、LLaVA-1.5、Shikra、MiniGPT-4などの代表的モデルで評価。CHAIRスコア等の指標を用い、従来の手法と比較して低い幻覚率を維持しつつF1スコアで優れた結果を示したほか、アブレーション分析で各コンポーネントの寄与を検証した。 |
| 議論はある？ | 外部特徴量が不可欠な要因である一方で、モデル内部の直接的な操作よりも計算コストがやや増大する可能性がある。また、今回は物体幻覚に焦点を当てており、属性の誤りや関係性の幻覚など、より複雑な現象への適用が今後の課題である。 |
| 次に読むべき論文は？ | [Rohrbach et al. (2018)](https://arxiv.org/abs/1809.02156) (幻覚の定義の基礎)、[Jiang et al. (2025)](https://arxiv.org/abs/2501.12753) (DIML手法)、[Huang et al. (2024)](https://arxiv.org/abs/2405.05256) (OPERA手法) |
| PDFリンク | https://arxiv.org/pdf/2604.06165v1 |
