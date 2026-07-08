---
title: "From RGB Generation to Dense Field Readout: Pixel-Space Dense Prediction with Text-to-Image Models"
date: 2026-07-08
arxiv_id: 2607.06553v1
url: http://arxiv.org/abs/2607.06553v1
---

# From RGB Generation to Dense Field Readout: Pixel-Space Dense Prediction with Text-to-Image Models

| 項目 | 内容 |
|---|---|
| どんなもの？ | 既存のテキスト生成画像モデル（DiT）の内部構造を再利用し、RGB生成ではなく「読み出し（Readout）」という手法で高精度な密予測（深度、セグメンテーション、法線推定など）を行うフレームワーク。VAEデコーダーによる画像再構成という冗長な工程を排除し、効率的なタスク遂行を実現している。 |
| 先行研究と比べてどこがすごい？ | 従来手法（画像生成・編集モデルの流用）はVAEを通した再構成が必要で計算コストが高かったが、本手法は不要な生成パスを削除することで、最大2.48倍の高速化とSOTA（あるいは同等）の精度を両立した。 |
| 技術や手法のキモはどこ？ | 凍結したDiTバックボーンに対してタスク特化のLoRAを適用し、中間層の空間トークンをそのままタスクごとの線形ヘッド（Token-local linear head）に入力する点。生成ではなく「空間的キャリア（spatial carrier）」として情報を読み出す設計に変換した。 |
| どうやって有効だと検証した？ | 6つの密予測タスク（深度、法線、マット抽出、セグメンテーション、姿勢推定、顕著性検知）に対し、12以上のベンチマークで評価を実施。特にKITTI深度、P3Mマット抽出などでSOTAを達成し、計算速度の優位性も実証した。 |
| 議論はある？ | 現在はFLUX-Kleinといった特定のバックボーンでの検証が中心である。今後は他の基盤モデルへの拡張や、より複雑なピクセル空間以外のターゲットへの適用が将来課題として挙げられている。 |
| 次に読むべき論文は？ | [10] Lotus: Diffusion-based visual foundation model for high-quality dense prediction, [42] What matters when repurposing diffusion models for general dense perception tasks? |
| PDFリンク | https://arxiv.org/pdf/2607.06553v1 |
