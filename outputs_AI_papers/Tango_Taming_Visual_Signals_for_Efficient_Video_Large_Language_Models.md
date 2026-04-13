---
title: "Tango: Taming Visual Signals for Efficient Video Large Language Models"
date: 2026-04-13
arxiv_id: 2604.09547v1
url: http://arxiv.org/abs/2604.09547v1
---

# Tango: Taming Visual Signals for Efficient Video Large Language Models

| 項目 | 内容 |
|---|---|
| どんなもの？ | ビデオ大規模言語モデル（Video LLM）における効率的な推論を実現するための、トレーニング不要なトークン剪定（pruning）手法「Tango」です。重要トークンの選択と、類似度に基づくトークン統合の両面からボトルネックを解消する新しいフレームワークを提案しています。 |
| 先行研究と比べてどこがすごい？ | 従来のTop-k選択が注意分布のマルチモーダル性やロングテール分布を捉えきれない点、および単純なクラスタリングが空間的に断片化したノイズを含む表現を生む点を克服しました。結果として、LLaVA-OV-7Bにおいて10%のトークン保持率で98.9%の性能を維持しつつ、1.88倍の推論高速化を実現しています。 |
| 技術や手法のキモはどこ？ | 1. 密度ピーククラスタリングを用いた「多様性重視」のトークン選択による広範な意味的領域のカバー、2. 時空間的な位置情報をトークン類似度計算に組み込む「ST-RoPE（Spatio-temporal Rotary Position Embedding）」により、幾何学的構造を保持しつつ近接トークンを統合する仕組みです。 |
| どうやって有効だと検証した？ | Video-MME、MVBench、LongVideoBench、MLVUという4つの主要なビデオ理解ベンチマークを使用し、複数のVideo LLM（LLaVA-OneVision-7B, LLaVA-Video-7B, Qwen2.5-VL-7B）に対して広範な比較実験を行いました。また、剪定による各コンポーネントの有効性を検証するアブレーションスタディも実施しました。 |
| 議論はある？ | 複雑なオープンワールドのシーンや、群衆、抽象的なアートのような複雑なセマンティクスを含むデータの圧縮は依然として大きな課題です。また、アテンションシンク（注意の溜まり場）の影響を軽減するためのヒューリスティックなマスキング手法については、さらなる改善の余地があるとしています。 |
| 次に読むべき論文は？ | [1] [FastV](https://arxiv.org/abs/2403.00762), [5] [FastVID](https://arxiv.org/abs/2405.14324), [9] [HoliTom](https://arxiv.org/abs/2405.14324) |
| PDFリンク | https://arxiv.org/pdf/2604.09547v1 |
