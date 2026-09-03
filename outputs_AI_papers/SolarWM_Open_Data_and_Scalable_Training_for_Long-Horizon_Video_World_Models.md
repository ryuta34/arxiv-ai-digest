---
title: "SolarWM: Open Data and Scalable Training for Long-Horizon Video World Models"
date: 2026-09-03
arxiv_id: 2609.02886v1
url: http://arxiv.org/abs/2609.02886v1
---

# SolarWM: Open Data and Scalable Training for Long-Horizon Video World Models

| 項目 | 内容 |
|---|---|
| どんなもの？ | インタラクティブな動画世界モデルを構築するための、オープンなデータ基盤とスケーラブルな学習フレームワーク「SolarWM」です。データ準備から長時間の推論までを一貫して扱うことができ、4つの異なるモデルファミリー（5B〜33B）を提供します。 |
| 先行研究と比べてどこがすごい？ | 異種混合データソース間の不整合を解消する「データエンジン」と、各バックボーンの特性を維持したままカメラ制御を統合する「アダプテーションフレームワーク」を両立しました。特に5秒の動画で学習するだけで、数分から数時間に及ぶ長時間ロールアウトを可能にする高い汎用性と再現性を実現しています。 |
| 技術や手法のキモはどこ？ | ①1.43M件のデータを正規化したデータエンジン、②カメラ制御をAttention層に直接統合する「fused-PRoPE」、③Bidirectional Training、AR初期化、DMD（Distribution Matching Distillation）を組み合わせた3段階の統一学習レシピです。 |
| どうやって有効だと検証した？ | 4つの異なる動画生成バックボーン（Wan2.2, LTX-2.5, MiniMax-H3）を対象に、OOD（学習外ドメイン）画像からの生成実験を行い、長時間（1時間スケール）の連続生成における視覚的整合性とカメラ追従性能を評価しました。 |
| 議論はある？ | 物理的なクリーンアップや加工プロセスを挟むことで、元のソースの品質を一部損なう可能性や、依然として特定のドメインに依存するバイアスの存在が考えられます。 |
| 次に読むべき論文は？ | [Causal Forcing](https://arxiv.org/abs/2602.02214)、[AnyFlow](https://arxiv.org/abs/2605.13724)、[DreamX-World](https://arxiv.org/abs/2606.16993) |
| PDFリンク | https://arxiv.org/pdf/2609.02886v1 |
