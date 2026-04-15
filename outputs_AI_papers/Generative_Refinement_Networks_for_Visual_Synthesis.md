---
title: "Generative Refinement Networks for Visual Synthesis"
date: 2026-04-15
arxiv_id: 2604.13030v1
url: http://arxiv.org/abs/2604.13030v1
---

# Generative Refinement Networks for Visual Synthesis

| 項目 | 内容 |
|---|---|
| どんなもの？ | 従来の拡散モデルや自己回帰モデルの課題を解決する、新しいビジュアル生成パラダイム「Generative Refinement Networks (GRN)」を提案。離散トークン化における損失と、生成時の誤差蓄積という問題を同時に解決した。 |
| 先行研究と比べてどこがすごい？ | 理論上ほぼ損失のないHierarchical Binary Quantization (HBQ)により離散トークンの品質を連続表現と同等に向上させた。また、グローバルなリファインメント機構により、逐次的な誤り訂正と適応的な計算リソース配分を実現し、ImageNet等のベンチマークでSOTAを達成した。 |
| 技術や手法のキモはどこ？ | ①HBQによる near-lossless な離散化、②ランダムなトークンマップから開始し、リファインメントを繰り返すことで高品質な出力を生成する自己回帰リファインメント機構、③エントロピーに基づき生成ステップ数や計算量を適応的に配分する戦略。 |
| どうやって有効だと検証した？ | ImageNet 256x256の画像生成タスクでFID 1.81を達成し、他の拡散モデルや自己回帰モデルを上回る性能を示した。さらに、高解像度のText-to-ImageおよびText-to-Videoタスクへもスケーリングし、既存手法より優れた品質を実現した。 |
| 議論はある？ | 計算リソースの制限により、先行する大規模生成モデルほどのモデル規模までスケーリングできていない。また、動画生成においては人間が関わるシーンでは性能が良いものの、複雑なシーンでは詳細なディテールが不足し、歪みが生じることがある。 |
| 次に読むべき論文は？ | [VAR: Visual Autoregressive Modeling](https://arxiv.org/abs/2404.02905)、[Transfusion](https://arxiv.org/abs/2408.11039)、[MaskGIT](https://arxiv.org/abs/2202.04200) |
| PDFリンク | https://arxiv.org/pdf/2604.13030v1 |
