---
title: "SenseNova-U1: Unifying Multimodal Understanding and Generation with NEO-unify Architecture"
date: 2026-05-13
arxiv_id: 2605.12500v1
url: http://arxiv.org/abs/2605.12500v1
---

# SenseNova-U1: Unifying Multimodal Understanding and Generation with NEO-unify Architecture

| 項目 | 内容 |
|---|---|
| どんなもの？ | 視覚理解と生成を統合し、事前に学習された視覚エンコーダー（VE）やVAEを用いずに、ピクセルとテキストの生の入力から直接学習を行う、真にネイティブな統合マルチモーダルモデル「SenseNova-U1」を提案した研究です。 |
| 先行研究と比べてどこがすごい？ | 従来のモデルが抱えていた、理解と生成の分離によるアーキテクチャの断片化や中間表現への依存という制約を解消しました。NEO-unifyアーキテクチャを採用し、理解と生成を単一の根源的なプロセスの相補的な側面として扱うことで、両タスクでトップレベルの性能を両立させています。 |
| 技術や手法のキモはどこ？ | （1）VEやVAEを排除した「ほぼ無損失な視覚インターフェース」、（2）言語の自己回帰クロスエントロピーと視覚のピクセル空間フローマッチングを統合した「エンドツーエンドのモデリング」、（3）理解と生成を効率的に共存させる「ネイティブ混合エキスパート（MoT）アーキテクチャ」です。 |
| どうやって有効だと検証した？ | 多岐にわたるマルチモーダル理解（MMMU、MathVista、OCRBench等）および生成・編集ベンチマーク（GenEval、DPG-Bench、ImgEdit等）において、既存のオープンソースモデルを凌駕する性能を示すことで有効性を検証しました。 |
| 議論はある？ | 最終的なMLPヘッドがピクセルパッチを独立して処理することに起因するグリッド状のアーティファクトが発生する可能性があり、将来的にPixelShuffleモジュール等による改善が示唆されています。 |
| 次に読むべき論文は？ | [112] [SenseNova. Neo-unify: Building native multimodal unified models end to end](https://huggingface.co/blog/sensenova/neo-unify)、[30] [From pixels to words–towards native vision-language primitives at scale](https://arxiv.org/abs/2510.14979) |
| PDFリンク | https://arxiv.org/pdf/2605.12500v1 |
