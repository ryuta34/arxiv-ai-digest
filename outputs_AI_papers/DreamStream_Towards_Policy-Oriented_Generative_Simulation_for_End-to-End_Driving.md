---
title: "DreamStream: Towards Policy-Oriented Generative Simulation for End-to-End Driving"
date: 2026-09-23
arxiv_id: 2609.26792v1
url: http://arxiv.org/abs/2609.26792v1
---

# DreamStream: Towards Policy-Oriented Generative Simulation for End-to-End Driving

| 項目 | 内容 |
|---|---|
| どんなもの？ | 自動運転のEnd-to-End（E2E）ポリシーを評価するための、政策指向の生成型クローズドループ・シミュレーター「DreamStream」。物理シミュレーターによる接地性と、大規模動画モデル蒸留による視覚的リアリズムを両立し、安全性や頑健性を診断するベンチマーク「Navhard-CL」を構築している。 |
| 先行研究と比べてどこがすごい？ | 従来のシミュレーターは視覚的なリアリズムと制御性の両立が困難であったが、本手法は交通レイアウトの幾何学的整合性を保ちつつ、多様な環境（天候・照明等）の生成を可能にした。また、既存のFIDやFVDでは評価できなかった「ポリシーの意思決定に必要な視覚情報」の整合性を測る新指標FDπを導入した。 |
| 技術や手法のキモはどこ？ | ①交通レイアウトをガイドとした動画生成モデルの3段階蒸留（TGD）。②訓練データ外の多様な環境条件を扱うためのDiverse-scene distillation。③ポリシーの意思決定に関連する特徴量の分布の一致を評価する新指標「FDπ」の設計。 |
| どうやって有効だと検証した？ | nuScenesやNAVSIM等の既存データセットで評価し、従来手法と比較してFDπ指標で1.6倍〜4.7倍の改善を達成した。さらにNavhard-CLを用い、これまで見過ごされていたポリシーの「スコアの不整合（scorer bias）」や「リカバリー軌道の生成能力不足」といった失敗モードを特定した。 |
| 議論はある？ | 実環境の走行テストやハードウェア・イン・ザ・ループ環境ではなく、あくまでシミュレーション上の評価である点。また、長時間の生成において自己回帰モデル特有のドリフト蓄積が生じる課題があり、今後の改善が必要である。 |
| 次に読むべき論文は？ | [18] NAVSIM: Data-driven non-reactive autonomous vehicle simulation and benchmarking (NeurIPS 2024), [41] DiffusionDrive: Truncated diffusion model for end-to-end autonomous driving (CVPR 2025) |
| PDFリンク | https://arxiv.org/pdf/2609.26792v1 |
