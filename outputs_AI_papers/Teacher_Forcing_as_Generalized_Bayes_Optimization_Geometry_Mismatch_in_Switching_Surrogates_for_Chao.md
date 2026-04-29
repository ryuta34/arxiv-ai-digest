---
title: "Teacher Forcing as Generalized Bayes: Optimization Geometry Mismatch in Switching Surrogates for Chaotic Dynamics"
date: 2026-04-29
arxiv_id: 2604.25904v1
url: http://arxiv.org/abs/2604.25904v1
---

# Teacher Forcing as Generalized Bayes: Optimization Geometry Mismatch in Switching Surrogates for Chaotic Dynamics

| 項目 | 内容 |
|---|---|
| どんなもの？ | カオス力学系の代理モデル学習において用いられる教師強制（Teacher Forcing）が、統計的にはどのような最適化幾何学を誘導し、それが本来のモデルの尤度幾何学とどのように不一致を起こすかを解析した研究。本研究は、この「幾何学的不一致」がモデルの長期的なダイナミクス再現に与える悪影響を明らかにしている。 |
| 先行研究と比べてどこがすごい？ | 教師強制を「一般化ベイズ更新」の枠組みで解釈し、Louisの公式を用いて「スイッチング（切り替え）の曖昧さ」による曲率の欠損を定量化した点。また、最適化の曲率（幾何学）と長期的な dynamical Quantities of Interest (QoIs) との間に明確な不整合（Trade-off）が存在することを示した点。 |
| 技術や手法のキモはどこ？ | AL-RNNの構造を確率的なスイッチングSSM（PAL-RNN）へと拡張し、潜在的なスイッチング経路の曖昧さを考慮した「観測情報量（Observed Information）」と、教師強制による「局所的な曲率」を比較した点。この曲率のギャップ（gQ）を計算することで、教師強制がどの程度過剰に確信的（尖った）な幾何学を誘導しているかを可視化した。 |
| どうやって有効だと検証した？ | Lorenz-63カオス系を用いたシミュレーション実験を実施。確率的なスイッチングAR(1)トイモデルで理論の妥当性を確認した後、ITFで事前学習したモデルに対し、windowed evidenceを最大化する微調整（Particle-SAEM）を行い、それが逆に不変測度などの長期的指標（QoIs）を毀損させることを示した。 |
| 議論はある？ | 教師強制は短期的予測の安定化には寄与するが、その最適化曲率は長期的ダイナミクスの目標とは整合しない場合がある。また、windowed evidenceの改善が必ずしも長期的な力学系の再現性向上に繋がるとは限らず、目的に応じた幾何学設計（QoI-aware学習）が必要であると論じている。 |
| 次に読むべき論文は？ | [Mikhaeil et al. (2022) On the difficulty of learning chaotic dynamics with rnns](https://arxiv.org/abs/2205.14371) / [Hess et al. (2023) Generalized teacher forcing for learning chaotic dynamics](https://arxiv.org/abs/2306.04406) |
| PDFリンク | https://arxiv.org/pdf/2604.25904v1 |
