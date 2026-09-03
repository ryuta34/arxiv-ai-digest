---
title: "GRADSOLVE: fast exact gradients for ODE ensembles on GPUs"
date: 2026-09-03
arxiv_id: 2609.02876v1
url: http://arxiv.org/abs/2609.02876v1
---

# GRADSOLVE: fast exact gradients for ODE ensembles on GPUs

| 項目 | 内容 |
|---|---|
| どんなもの？ | GPU上でODE（常微分方程式）アンサンブルの順方向ソルブと逆方向微分を高速に行うためのJAXライブラリ「gradsolve」。個別の軌道に対する適応的な計算手順を一度記録し、その手順に従った固定ステップの再現（リプレイ）を効率的に微分することで、高速かつ正確な勾配計算を実現する。 |
| 先行研究と比べてどこがすごい？ | 従来のGPU向け高速ソルバー（DiffEqGPU.jlなど）は微分に非対応か順方向のみで、微分可能なソルバー（Diffraxなど）は計算が遅いというトレードオフを解消した。Diffrax等のcheckpointingを用いた手法に対し、記録された固定ステップの計算を微分することで、5.6〜14.1倍の勾配計算速度を実現した。 |
| 技術や手法のキモはどこ？ | 適応的なステップ選択を含む最初の実行を記録し、そのステップ順序を「固定データ」として再利用（リプレイ）する手法。これにより、逆方向微分時にステップ選択の分岐やエラー制御の計算を排除でき、単一の固定長ループとしてGPU上で極めて効率的に計算できる。 |
| どうやって有効だと検証した？ | Lorenz系、Van der Pol系、Robertson系など計6つのベンチマーク問題を用い、Diffrax、torchode、torchdiffeqといった主要な微分可能ODEソルバーと、計算精度を合わせた状態で実行時間を比較。また、完全なパラメータ最適化プロセス（フィッティング）における収束時間の短縮も検証した。 |
| 議論はある？ | 状態次元が増加するとメモリやレジスタ制約の影響を受ける（d > 64で汎用パスへフォールバック）。また、非常に高い精度を要求される stiff（硬い）問題では、高次手法を持つベースラインが有利になる場合があり、適応的制御の再導入が課題となる。 |
| 次に読むべき論文は？ | [19] Kidger, P. (2021). Diffrax: numerical differential equation solvers in JAX. https://github.com/patrick-kidger/diffrax<br>[33] Rackauckas, C., & Nie, Q. (2017). DifferentialEquations.jl. https://github.com/SciML/DifferentialEquations.jl<br>[50] Utkarsh, U., et al. (2024). Automated translation and accelerated solving of differential equations on multiple GPU platforms. https://doi.org/10.1016/j.cma.2023.116591 |
| PDFリンク | https://arxiv.org/pdf/2609.02876v1 |
