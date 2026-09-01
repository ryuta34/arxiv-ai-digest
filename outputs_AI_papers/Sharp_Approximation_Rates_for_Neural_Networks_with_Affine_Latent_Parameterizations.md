---
title: "Sharp Approximation Rates for Neural Networks with Affine Latent Parameterizations"
date: 2026-09-01
arxiv_id: 2608.31157v1
url: http://arxiv.org/abs/2608.31157v1
---

# Sharp Approximation Rates for Neural Networks with Affine Latent Parameterizations

| 項目 | 内容 |
|---|---|
| どんなもの？ | ニューラルネットワークのパラメータを低次元の潜在表現から生成する手法（アフィン潜在パラメータ化）において、潜在次元数$M$とネットワークの総パラメータ数$P$という2つのリソース制約の下での近似誤差の評価を行った研究。|
| 先行研究と比べてどこがすごい？ | 従来手法が単一のパラメータ数で複雑さを評価していたのに対し、潜在次元数とネットワークのデコーダ予算を明確に区別し、両者を用いた sharp なミニマックス近似率を解明した点。$M \le P$および$M \ge P$の各レジームにおける最適なスケーリング則を確立した。 |
| 技術や手法のキモはどこ？ | アフィン生成器 $A(\xi) = A\xi + a$ を共有し、ターゲットごとに潜在ベクトル $\xi$ のみを変更する枠組みを採用。この条件下で、近似誤差が $[P \cdot \min\{M, P\}]^{-\alpha/d}$ というオーダーで収束することを理論的に証明した点。特に$M$を固定しても$P$の増加に伴い誤差が algebraic に減少することを示した。 |
| どうやって有効だと検証した？ | $\alpha$-Hölder関数クラスに対する近似理論の観点から、完全連結ReLUネットワークを用いた構成的な上限評価と、疑似次元（pseudo-dimension）およびバンプパッキングを用いた下限評価の両面から数理的に検証した。 |
| 議論はある？ | 本研究の理論は「完全な実数演算」を前提としており、有限ビット精度や数値的安定性、あるいは勾配降下法による最適化の動態については直接扱っていない。また、アフィン生成器以外の非線形生成器については別途理論が必要であるとしている。 |
| 次に読むべき論文は？ | [Shen et al., 2022b (Intrinsic parameters)](https://arxiv.org/abs/2207.02717)、[Yarotsky, 2018 (Deep ReLU networks)](https://proceedings.mlr.press/v75/yarotsky18a.html)、[Zhang et al., 2023 (Parameter sharing)](https://proceedings.mlr.press/v202/zhang23ad.html) |
| PDFリンク | https://arxiv.org/pdf/2608.31157v1 |
