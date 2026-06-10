---
title: "AnyMod-LLVE: Low-Light Video Enhancement with Modality-Agnostic Inference"
date: 2026-06-10
arxiv_id: 2606.11186v1
url: http://arxiv.org/abs/2606.11186v1
---

# AnyMod-LLVE: Low-Light Video Enhancement with Modality-Agnostic Inference

| 項目 | 内容 |
|---|---|
| どんなもの？ | 低照度ビデオ強調（LLVE）において、補助モダリティ（イベントストリームや赤外線画像）が利用可能な場合は活用し、利用不可能な場合でも高品質な結果を得られるモダリティ非依存型の学習フレームワーク「AMNet」を提案した研究。 |
| 先行研究と比べてどこがすごい？ | 従来のマルチモーダルLLVE手法は推論時に補助モダリティの入力を必須としていたが、本手法はRGB入力のみでも補助モダリティの情報を暗黙的に生成することで、デバイスの制限やデータの欠損に左右されない堅牢な推論を実現した。 |
| 技術や手法のキモはどこ？ | 空間的・周波数的なゲーティング機構を備えた「Spatial-Spectral Dual-Gated (S2DG) Translator」により、低照度RGBから補助モダリティに相当する暗黙的な特徴を抽出し、補助モダリティの欠損を補完する点。 |
| どうやって有効だと検証した？ | DID、SDSD、SDEといった公開されている実データセットを用いて、RGBのみの場合および補助モダリティがある場合の双方で評価を実施。既存の最先端手法と比較し、RGB単体性能でも高い精度を達成し、欠損時にも性能低下を最小限に抑えられることを示した。 |
| 議論はある？ | 生成された補助モダリティの品質向上には、より多様なデータでの大規模な事前学習が必要となる。また、推論時の計算コストと生成モダリティの精度とのトレードオフや、極端な低照度下での情報の限界が課題として残る。 |
| 次に読むべき論文は？ | [Cai et al., 2023, Retinexformer](https://arxiv.org/abs/2303.16706)や[Chen et al., 2025a, EvLight++](https://arxiv.org/abs/2405.15660)など。 |
| PDFリンク | https://arxiv.org/pdf/2606.11186v1 |
