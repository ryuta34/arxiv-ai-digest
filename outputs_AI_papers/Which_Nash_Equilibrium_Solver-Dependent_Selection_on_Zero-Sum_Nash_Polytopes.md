---
title: "Which Nash Equilibrium? Solver-Dependent Selection on Zero-Sum Nash Polytopes"
date: 2026-06-29
arxiv_id: 2606.28308v1
url: http://arxiv.org/abs/2606.28308v1
---

# Which Nash Equilibrium? Solver-Dependent Selection on Zero-Sum Nash Polytopes

| 項目 | 内容 |
|---|---|
| どんなもの？ | 2人ゼロ和ゲームにおいて、ソルバーがNash均衡の集合の中から特定の均衡を「選択」するメカニズムを解明した研究。アルゴリズムの種類によって選択される均衡が異なり、それが幾何学的な構造に依存することを明らかにした。 |
| 先行研究と比べてどこがすごい？ | 従来は等価に扱われていたソルバー（CFR系と正規化ラストイテレート系）が、実際にはNash均衡集合内の異なるメンバーを選択していることを分析的に証明し、正規化手法が「最大エントロピーメンバー（I-projection）」を導出するという仮説を提示した点。 |
| 技術や手法のキモはどこ？ | 正規化されたラストイテレート手法（R-NaD等）において、動的な参照ポリシー（moving reference）を用いることで、制約付き最適化問題としてのNash均衡選択（エントロピー最大化）を実現している点。また、CFR系の境界ドリフトの原因が「正値直交射影（max(R,0)）」ではないことを実験的に反証した点。 |
| どうやって有効だと検証した？ | 解析的に解ける6つのゲームおよび180ゲームからなるランダムなゲーム集合を用い、ソルバーが選択する均衡の座標、エントロピー、および対戦相手に対するロバスト性を網羅的に計測することで検証した。 |
| 議論はある？ | 最大エントロピー均衡選択は「アンカー追従」的であり、初期の参照ポリシーに依存する。また、強固な理論的証明は今後の課題であり、現時点では強力な実験データに基づく「仮説（Conjecture 1）」として提示されている。 |
| 次に読むべき論文は？ | [Pérolat et al. (2021) "From Poincaré recurrence to convergence in imperfect-information games"](https://arxiv.org/abs/2102.04518)、[Sokota et al. (2023) "A unified approach to reinforcement learning, quantal response equilibria, and two-player zero-sum games"](https://arxiv.org/abs/2206.05825) |
| PDFリンク | https://arxiv.org/pdf/2606.28308v1 |
