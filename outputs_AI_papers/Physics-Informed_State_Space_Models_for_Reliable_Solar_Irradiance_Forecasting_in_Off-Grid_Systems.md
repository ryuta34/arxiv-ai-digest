---
title: "Physics-Informed State Space Models for Reliable Solar Irradiance Forecasting in Off-Grid Systems"
date: 2026-04-14
arxiv_id: 2604.11807v1
url: http://arxiv.org/abs/2604.11807v1
---

# Physics-Informed State Space Models for Reliable Solar Irradiance Forecasting in Off-Grid Systems

| 項目 | 内容 |
|---|---|
| どんなもの？ | オフグリッド環境の太陽光発電灌漑システム向けに、物理法則に基づいた軽量な「物理情報付き状態空間モデル（PISSM）」を提案。エッジマイコンでの稼働を想定し、計算コストを抑えつつ高い予測精度と物理的な整合性を両立させた時系列予測フレームワーク。 |
| 先行研究と比べてどこがすごい？ | 従来のディープラーニングモデル（RNNやTransformer）が抱える計算負荷の高さや「夜間に発電を予測する」といった物理的矛盾を解消。4万未満という極めて少ないパラメータ数で、従来モデルと比較して圧倒的な軽量化と、98.7%という高い予測精度（R²）を実現した点。 |
| 技術や手法のキモはどこ？ | Hankel行列を用いた動的状態埋め込みによるノイズ除去、線形状態空間モデル（SSM）による効率的な時系列モデリング、および太陽天頂角と透明度指数を用いた「物理情報付きゲーティング機構」により、物理的な制約をハードに組み込んだ点。 |
| どうやって有効だと検証した？ | スーダンのオムドゥルマン地域における5年間のNASA POWERデータを用いたストレステストを実施。トレーニング期間から大きく離れた年次データに対しても、一貫した予測性能を維持できることをRMSEおよび決定係数（R²）で検証した。 |
| 議論はある？ | 現在は単一地点の予測に特化している。今後はマルチステップ予測への拡張、近隣観測所との空間相関の活用、および実環境でのシフトに適応するためのオンライン学習（継続学習）の実装が課題。 |
| 次に読むべき論文は？ | [Gu et al. (2021) "Efficiently Modeling Long Sequences with Structured State Spaces"](https://arxiv.org/abs/2111.00396) |
| PDFリンク | https://arxiv.org/pdf/2604.11807v1 |
