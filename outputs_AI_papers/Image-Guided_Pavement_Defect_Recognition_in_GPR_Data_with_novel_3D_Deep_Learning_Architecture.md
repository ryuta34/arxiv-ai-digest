---
title: "Image-Guided Pavement Defect Recognition in GPR Data with novel 3D Deep Learning Architecture"
date: 2026-08-20
arxiv_id: 2608.19177v1
url: http://arxiv.org/abs/2608.19177v1
---

# Image-Guided Pavement Defect Recognition in GPR Data with novel 3D Deep Learning Architecture

| 項目 | 内容 |
|---|---|
| どんなもの？ | 道路の表面画像（RGB）を用いて、自動的に3次元GPR（地中レーダー）データにラベルを付与する手法と、それを用いた新しい3次元深層学習モデル。大規模なGPRデータセットの構築と、路面下欠陥（パッチや亀裂）の自動検出を目指した研究。 |
| 先行研究と比べてどこがすごい？ | 従来、GPRデータの手動アノテーションは専門知識が必要でコストが高かったが、本手法はコスト効率の良いデータ準備パイプラインにより大規模アノテーションを可能にした。また、3D GPRの特性（深さ・空間情報）を直接処理する専用のCNNアーキテクチャを提案した点。 |
| 技術や手法のキモはどこ？ | RGB画像とGPRデータを共登録し、表面の欠陥位置から対応する地下セグメントへラベルを転送する仕組み。モデルには、残差接続、混合カーネル畳み込み、および深さとチャネルの両方に対するAttention機構（Squeeze-and-excitation等）を統合した点。 |
| どうやって有効だと検証した？ | 英国のA14高速道路の舗装路面で収集した実データセットを用い、既存の2D転用モデル（ResNet-18等）および標準的な3D-CNNと比較検証。アブレーションスタディにより各構成要素（Attention機構等）の有効性を確認。 |
| 議論はある？ | RGBによるアノテーションはあくまで「プロキシ（代理）ラベル」であり、物理的な地下欠陥と常に一致するとは限らない。また、ノイズの多い実環境データであるため、現時点ではスタンドアロンの判断システムではなく、検査を支援するスクリーニングツールとして位置付けるべきとしている。 |
| 次に読むべき論文は？ | [Brilakis et al. (2019)](https://www.repository.cam.ac.uk/handle/1810/318329), [d’Avigneau et al. (2025)](https://doi.org/10.1016/j.aei.2025.103036), [Pan et al. (2024)](https://doi.org/10.1016/j.autcon.2024.105654) |
| PDFリンク | https://arxiv.org/pdf/2608.19177v1 |
