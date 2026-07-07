---
title: "From Fixed to Free Cameras: Calibration-Free View-Robust Vision-Language-Action Model"
date: 2026-07-07
arxiv_id: 2607.05396v1
url: http://arxiv.org/abs/2607.05396v1
---

# From Fixed to Free Cameras: Calibration-Free View-Robust Vision-Language-Action Model

| 項目 | 内容 |
|---|---|
| どんなもの？ | 実環境でのロボット導入において、カメラの配置変更やズレに対して頑健な視覚言語行動（VLA）モデル「CamVLA」を提案している。カメラの位置情報を外部から与えることなく、RGB画像からカメラとロボットの幾何学的関係を自己推定することで、キャリブレーション不要な操作を実現した。 |
| 先行研究と比べてどこがすごい？ | 従来のVLAモデルはカメラ位置の既知情報を前提とするため配置変更に脆かったが、本手法は深層学習による幾何学的な自己定位能力により、カメラの再配置やドリフトに対して事前のキャリブレーションなしで汎用的な適応を可能にした点。 |
| 技術や手法のキモはどこ？ | VLAモデルを「カメラ視点の動作生成」と「カメラ視点の幾何学的接地（Hand-Eye行列の回帰）」の2つのヘッドに切り分けることで、視覚入力と動作空間の空間的整合性を保ったまま、カメラの外部パラメータの変動を独立して扱う「デカップリング設計」にある。 |
| どうやって有効だと検証した？ | RLBenchを用いたシミュレーション環境と、Franka Research 3を用いた実ロボット環境の両方で検証。多様な未学習視点に対して、従来のVLAモデル（$\pi_0$やGR00T N1.7）と比較し、大幅な成功率の向上を達成した。 |
| 議論はある？ | 現在は第三者視点カメラに特化しており、手先カメラのドリフトには未対応。また、極端な視点変化や高精度が求められる作業では、領域外の視覚特徴によって性能が低下する可能性があり、今後の課題としている。 |
| 次に読むべき論文は？ | [5] [K. Black et al., "$\pi_0$: A vision-language-action flow model for general robot control"](https://arxiv.org/abs/2404.19733) <br> [8] [T. Zhang et al., "Grounding actions in camera space"](https://arxiv.org/abs/2601.03159) |
| PDFリンク | https://arxiv.org/pdf/2607.05396v1 |
