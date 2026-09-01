---
title: "GeBDA: Building Damage Assessment as Text-Based Sequence Prediction"
date: 2026-09-01
arxiv_id: 2608.28567v1
url: http://arxiv.org/abs/2608.28567v1
---

# GeBDA: Building Damage Assessment as Text-Based Sequence Prediction

| 項目 | 内容 |
|---|---|
| どんなもの？ | 汎用Vision-Language Model (VLM) であるGemmaをベースに、建物被害評価（BDA）を単一の自己回帰的なテキスト生成タスクとして解く手法「GeBDA」を提案した。画像対から建物の位置と被害状況を直接出力するエンドツーエンドの枠組みを実現している。 |
| 先行研究と比べてどこがすごい？ | 従来のGeoVLMが外部の検出器やセグメンテーションモジュールに頼っていたのに対し、本手法は追加コンポーネントなしで、単一パスの自己回帰デコードのみで建物の局所化と被害評価を同時に行える点。 |
| 技術や手法のキモはどこ？ | 建物ポリゴンをバウンディングボックス化し、その座標と被害クラスを文字列としてシリアライズしてトークン化する設計。Gemmaの事前学習済みモデルの数値表現能力を活かし、座標予測をテキスト生成として定式化した点。 |
| どうやって有効だと検証した？ | xBDおよびBRIGHTデータセットを用い、匈牙利算法（Hungarian algorithm）によるマッチングを介してF1スコアを算出。また、予測をラスター化して従来のピクセルベース手法と比較し、Oracle基準に近い精度であることを示した。 |
| 議論はある？ | 高密度な場面で小さなボックスがループしたり、不均質なタイルで予測が特定のクラスに偏る課題がある。また、プレーンテキスト形式の座標エンコーディングはトークン効率が悪く、SARデータの処理にはVision Encoderの追加調整が必要。 |
| 次に読むべき論文は？ | [Pix2seq](https://doi.org/10.48550/arXiv.2109.10852), [PaliGemma 2](https://doi.org/10.48550/arXiv.2412.03555), [Detect anything via next point prediction](https://doi.org/10.48550/arXiv.2510.12798) |
| PDFリンク | https://arxiv.org/pdf/2608.28567v1 |
