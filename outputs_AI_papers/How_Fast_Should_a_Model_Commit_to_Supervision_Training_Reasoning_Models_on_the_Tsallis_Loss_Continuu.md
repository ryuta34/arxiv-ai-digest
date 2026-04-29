---
title: "How Fast Should a Model Commit to Supervision? Training Reasoning Models on the Tsallis Loss Continuum"
date: 2026-04-29
arxiv_id: 2604.25907v1
url: http://arxiv.org/abs/2604.25907v1
---

# How Fast Should a Model Commit to Supervision? Training Reasoning Models on the Tsallis Loss Continuum

| 項目 | 内容 |
|---|---|
| どんなもの？ | 推論モデルの強化学習（RLVR）における「コールドスタート問題（初期成功率が低いと学習が停滞する問題）」を解消するための、Tsallis q-logarithmに基づいた損失関数ファミリー $J_Q$ を提案する論文。学習率とは独立したサンプルごとの勾配増幅メカニズムにより、学習初期の探索とノイズ耐性のトレードオフを制御する。 |
| 先行研究と比べてどこがすごい？ | 従来のRLVRが抱える $\Omega(1/p_0)$ という遅い脱出速度に対し、$\Theta(\log(1/p_0))$ の脱出速度を実現した点。また、学習の安定性を高める「勾配増幅（GARL）」と「後方確率減衰（PAFT）」という二つの補完的な勾配推定器を導出し、RLとSFTの連続的な補間を実現した。 |
| 技術や手法のキモはどこ？ | $P_\theta^{-q}$ という勾配増幅因子による、インスタンスごとのコミットメント（重要度）調整。これにより、RLVRの exploitation（利用）と最大尤度推定（密度推定）という二極を単一のパラメータ $q$ で繋ぎ、学習初期は高い勾配で高速に学習を進め、学習が安定した段階で $q$ を調整してノイズの記憶を抑制できる点。 |
| どうやって有効だと検証した？ | FinQA、HotPotQA、MuSiQueの3つの推論ベンチマークを用い、Qwen 3 0.6Bモデルで評価。特にHotPotQAでは、従来のGRPOと比較してmaj@16において+14.4ポイントの改善を達成し、コールドスタート状況下でもプロンプトなしで高いパフォーマンスを示した。 |
| 議論はある？ | 勾配増幅の副作用として、一部のデータセット（HotPotQA等）で学習途中の精度急落（collapse）が観測される。これに対し、PAFTを用いることで安定した学習が可能であることを示したが、なぜGARLで急落が起きるかという根本的なメカニズムの解明は将来課題としている。 |
| 次に読むべき論文は？ | [DeepSeek-AI, 2025 (DeepSeek-R1)](https://arxiv.org/abs/2501.12948)、[Zhou et al., 2026 (VeriFree)](https://openreview.net/forum?id=nnwvwge40d)、[Burda et al., 2015 (IWAE)](https://api.semanticscholar.org/CorpusID:11383178) |
| PDFリンク | [https://arxiv.org/pdf/2604.25907v1](https://arxiv.org/pdf/2604.25907v1) |
