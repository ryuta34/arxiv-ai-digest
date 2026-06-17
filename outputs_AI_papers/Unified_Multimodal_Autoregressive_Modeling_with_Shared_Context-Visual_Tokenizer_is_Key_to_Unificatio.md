---
title: "Unified Multimodal Autoregressive Modeling with Shared Context-Visual Tokenizer is Key to Unification"
date: 2026-06-17
arxiv_id: 2606.18249v1
url: http://arxiv.org/abs/2606.18249v1
---

# Unified Multimodal Autoregressive Modeling with Shared Context-Visual Tokenizer is Key to Unification

| 項目 | 内容 |
|---|---|
| どんなもの？ | ビジュアル理解と生成を単一の離散的ビジュアルトークナイザーで統合した、新しい自己回帰型マルチモーダルモデル「UniAR」。トークナイザーと生成器を共有することで、再エンコードなしに生成と理解をシームレスに行える枠組み。 |
| 先行研究と比べてどこがすごい？ | 従来手法が理解用と生成用で別々のトークナイザーを必要としたのに対し、UniARは単一のトークナイザーで表現空間を統合。また、並列ビット単位予測により生成速度を大幅に向上させつつ、軽量な構成でSOTAクラスの性能を実現した。 |
| 技術や手法のキモはどこ？ | 複数レイヤーの視覚特徴を融合する「マルチレベル特徴融合」と、明示的なコードブックを必要としない「Lookup-freeビット単位量子化（BSQ）」を採用。さらに、2x2の空間グリッドを並列に予測するメカニズムでシーケンス長を短縮している点。 |
| どうやって有効だと検証した？ | GenEval（画像生成）、OneIG-Bench/LongText-Bench（テキストレンダリング）、ImgEdit Bench（画像編集）、および複数のマルチモーダル理解ベンチマーク（OCRBench等）において、競合モデルを上回る性能を実証。 |
| 議論はある？ | 純粋なテキストデータの事前学習が不足しており、推論能力の向上に余地がある。また、強化学習による最適化が画像生成タスクに限定されており、今後は理解能力や特定領域（美学、テキストレンダリング等）の報酬モデル開発が課題。 |
| 次に読むべき論文は？ | [18] Infinity: Scaling bitwise autoregressive modeling for high-resolution image synthesis (CVPR 2025), [68] Nextflow: Unified sequential modeling activates multimodal understanding and generation |
| PDFリンク | https://arxiv.org/pdf/2606.18249v1 |
