---
title: "Learning Length-Extrapolatable Recurrent Models"
date: 2026-09-09
arxiv_id: 2609.09157v1
url: http://arxiv.org/abs/2609.09157v1
---

# Learning Length-Extrapolatable Recurrent Models

| 項目 | 内容 |
|---|---|
| どんなもの？ | 学習時よりも大幅に長いシーケンスを扱う際、再帰型モデル（RNN等）が直面する性能低下を解決する手法。バックプロパゲーション（BPTT）過程での「状態のクレジット（寄与）」を適切に安定化させる手法「CST（Credit Stabilization through Time）」を提案している。 |
| 先行研究と比べてどこがすごい？ | 従来の勾配消失・爆発への対策とは異なり、順伝播の計算やアーキテクチャを変更せず、バックプロパゲーション中の「状態クレジット」のみを介入・調整する。これにより、学習済みモデルの推論限界を最大128倍まで延長しつつ、計算コストを抑えたスケーラブルな学習を実現している点。 |
| 技術や手法のキモはどこ？ | 勾配が過去へ伝播する際のノルムが変化する性質に着目し、各セグメント境界でクレジット信号をスカラー値で局所的に再スケーリング（増幅・減衰）することで、情報の伝播方向を変えずに信号の強度を維持・安定化させる点。 |
| どうやって有効だと検証した？ | FSA、MQAR、Meta-FSA等の合成タスクにて、訓練長の最大128倍のシーケンスで性能評価を実施。また、実際の言語モデル（Gated DeltaNet）に対しても、Books3やGovReport等のデータセットでNLL（負の対数尤度）の改善を確認し、キーとなるトークンの予測精度向上を実証した。 |
| 議論はある？ | クレジットのノルムを安定させるだけであり、失われた勾配の方向性を復元するわけではない。また、特定のタスクやモデル構成において性能向上が限定的である場合や、計算コストと精度のトレードオフが依然として存在することが課題として挙げられている。 |
| 次に読むべき論文は？ | [15] Mamba: Linear-time sequence modeling with selective state spaces, [46] Unbiasing truncated backpropagation through time, [56] Gated delta networks: Improving mamba2 with delta rule |
| PDFリンク | https://arxiv.org/pdf/2609.09157v1 |
