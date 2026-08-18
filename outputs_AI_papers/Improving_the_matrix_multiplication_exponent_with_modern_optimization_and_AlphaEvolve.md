---
title: "Improving the matrix multiplication exponent with modern optimization and AlphaEvolve"
date: 2026-08-18
arxiv_id: 2608.16884v1
url: http://arxiv.org/abs/2608.16884v1
---

# Improving the matrix multiplication exponent with modern optimization and AlphaEvolve

| 項目 | 内容 |
|---|---|
| どんなもの？ | 行列積の計算量（指数 $\omega$）の理論的な上界を改善する研究。最新の最適化手法とAlphaEvolveを組み合わせることで、従来の$\omega < 2.371339$から$\omega < 2.371177$へと記録を更新した。 |
| 先行研究と比べてどこがすごい？ | 従来手法（Alman et al., 2025）では計算負荷から難しかった再帰レベル $\ell^* = 4$（約700万パラメータ）の最適化を実現した点。勾配ベースの最適化とAIによるコード最適化を統合し、効率的な並列計算を可能にした。 |
| 技術や手法のキモはどこ？ | JaxによるGPU並列化、非凸最適化のための微分可能な目的関数の設計、およびSinkhorn-Knoppアルゴリズムを用いた最大エントロピー分布の効率的な計算。さらにAlphaEvolveによる最適化アルゴリズム自体の自動修正。 |
| どうやって有効だと検証した？ | 浮動小数点演算の結果を rational arithmetic（有理数演算）による厳密な計算に置き換え、最大エントロピーの証明書を作成することで、数値誤差のない厳密な上界であることを数学的に検証した。 |
| 議論はある？ | さらなる改善には単なる最適化の枠組みを超えた、数学的な新しい着想が必要であるとしている。 |
| 次に読むべき論文は？ | [Alman et al. (2025) "More Asymmetry Yields Faster Matrix Multiplication"](https://epubs.siam.org/doi/abs/10.1137/1.9781611978322.63) |
| PDFリンク | https://arxiv.org/pdf/2608.16884v1 |
