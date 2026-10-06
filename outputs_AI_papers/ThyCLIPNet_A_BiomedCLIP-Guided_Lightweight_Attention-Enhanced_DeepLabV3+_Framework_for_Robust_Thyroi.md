---
title: "ThyCLIPNet: A BiomedCLIP-Guided Lightweight Attention-Enhanced DeepLabV3+ Framework for Robust Thyroid Nodule Segmentation"
date: 2026-10-06
arxiv_id: 2610.04743v1
url: http://arxiv.org/abs/2610.04743v1
---

# ThyCLIPNet: A BiomedCLIP-Guided Lightweight Attention-Enhanced DeepLabV3+ Framework for Robust Thyroid Nodule Segmentation

| 項目 | 内容 |
|---|---|
| どんなもの？ | 甲状腺超音波画像セグメンテーションのための、軽量かつ高性能なセマンティック誘導型ハイブリッドエンコーダ・デコーダフレームワーク「ThyCLIPNet」。事前に学習されたBiomedCLIPの視覚エンコーダを活用し、追加のテキストプロンプトなしで高精度なセグメンテーションを実現する。 |
| 先行研究と比べてどこがすごい？ | 従来のCLIPを用いた手法がテキストプロンプトや複雑なマルチモーダル処理を必要とするのに対し、本手法は視覚エンコーダのみを固定利用するため計算コストが低い。また、軽量なMobileNetV2をベースにしつつ、提案するBGFモジュール等により、SOTA手法を上回る精度と境界推論能力を軽量な構成で達成している。 |
| 技術や手法のキモはどこ？ | BiomedCLIPから得られるグローバルな意味情報を、テキスト入力なしでデコーダに注入する「BiomedCLIP-guided Gated Fusion (BGF)」モジュール。加えて、MobileNetV2エンコーダにECA（Efficient Channel Attention）を統合し、ボトルネック部にASPPとカスタムCBAMを組み合わせることで、低計算量で多スケールのコンテキストを抽出している点。 |
| どうやって有効だと検証した？ | 4つの公開甲状腺超音波データセット（TG3K, TN3K, DDTI, PKTN）を用いて定量・定性評価を実施。DICE係数、IoU、HD95などの指標でSOTAモデルと比較し、競合手法と同等以上の精度を維持しながら、モデルのパラメータ数やFLOPs、推論速度において優れた効率性を実証した。 |
| 議論はある？ | 現在は静止画ベースで固定の融合重みを使用しており、動的な状況や多様な臨床ドメインへの柔軟な適応に課題がある。また、現在評価に使用しているデータセットに放射線レポートが含まれていないため、外部のテキスト情報の活用については今後の発展途上である。 |
| 次に読むべき論文は？ | [54] CLIP-TNseg: A multi-modal hybrid framework for thyroid nodule segmentation in ultrasound images, [57] Segment anything, [65] Encoder-decoder with atrous separable convolution for semantic image segmentation |
| PDFリンク | https://arxiv.org/pdf/2610.04743v1 |
