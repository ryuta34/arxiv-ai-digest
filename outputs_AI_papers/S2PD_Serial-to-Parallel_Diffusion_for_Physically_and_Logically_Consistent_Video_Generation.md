---
title: "S2PD: Serial-to-Parallel Diffusion for Physically and Logically Consistent Video Generation"
date: 2026-10-07
arxiv_id: 2610.06847v1
url: http://arxiv.org/abs/2610.06847v1
---

# S2PD: Serial-to-Parallel Diffusion for Physically and Logically Consistent Video Generation

| 項目 | 内容 |
|---|---|
| どんなもの？ | 物理法則や論理的整合性が求められるビデオ生成において、高いノイズレベルで自己回帰的に構造を決定し、低いノイズレベルで並列的に精緻化を行う「Serial-to-Parallel Diffusion (S2PD)」を提案した論文。 |
| 先行研究と比べてどこがすごい？ | 従来の完全並列的な拡散モデルが苦手としていた、長い因果関係や複雑なルール（ゲームや物理シミュレーション）の維持を大幅に改善した。さらに、純粋な自己回帰モデルよりも高速なサンプリングを実現した点。 |
| 技術や手法のキモはどこ？ | ノイズレベルτを境に、高いノイズ領域ではブロック単位の自己回帰的な生成（シリアル）を行い、低いノイズ領域では全ビデオトークンを一度に扱う並列生成へと切り替える2段階のサンプリング手法。 |
| どうやって有効だと検証した？ | Conwayのライフゲーム、チェス、物理シミュレーション（衝突球、ダブルペンデュラム等）、実映像（ルービックキューブ）など広範なデータセットを用い、ルール違反数や力学誤差、CD-FVD等の指標で既存のBidirectional手法と比較検証した。 |
| 議論はある？ | サンプリング効率は向上したが、依然として計算コストと品質のトレードオフが存在する。また、複雑な実映像データセットでは、既存手法と比較して必ずしも常に最良の結果が得られるわけではなく、データセットの多様性による影響が示唆されている。 |
| 次に読むべき論文は？ | [The Serial Scaling Hypothesis](https://arxiv.org/abs/2507.12549)、[Diffusion forcing: Next-token prediction meets full-sequence diffusion](https://arxiv.org/abs/2407.01392) |
| PDFリンク | https://arxiv.org/pdf/2610.06847v1 |
