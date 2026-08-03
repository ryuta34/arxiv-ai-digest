---
title: "Scaling Properties of Text Conditioning in Visual Generation"
date: 2026-08-03
arxiv_id: 2607.29679v1
url: http://arxiv.org/abs/2607.29679v1
---

# Scaling Properties of Text Conditioning in Visual Generation

| 項目 | 内容 |
|---|---|
| どんなもの？ | テキスト条件付けにおける「情報のスケーリング則」を提唱し、画像生成モデルの品質を向上させる「構造化プロンプト（SP）」と、それを推論するLLMプロンプターの訓練フレームワーク。プロンプトの長さではなく、構造化された情報量こそが拡散モデルの損失を低減させる要因であることを示した。 |
| 先行研究と比べてどこがすごい？ | 従来の「長い自然言語プロンプトが必ずしも品質向上に寄与しない」という問題を特定し、構造化プロンプトの導入により diffusion loss との定量的相関を明らかにした点。さらに、SFT、Cold-start、RFTを用いた訓練パイプラインにより、既存のオープンウェイトモデルを大幅に上回る生成精度を達成した。 |
| 技術や手法のキモはどこ？ | キャプションの情報をGPG（ホワイトボックス）とED（ブラックボックス）という指標で定量化し、モデルの性能を「Diffusability（情報を組織化する能力）」と「Promptability（ユーザー要求から構造化プロンプトを生成する能力）」の積として定式化したこと。 |
| どうやって有効だと検証した？ | 15種類の異なるキャプション構成を用いた大規模な拡散モデル訓練（BAGELバックボーン）により、情報のスケーリング則を実証。さらに、Qwen-Imageモデルを用いた end-to-end の評価（GenEval2, DPG-Bench, WISE等）で、従来のプロンプト拡張手法やClosed-sourceモデルを上回る性能を示した。 |
| 議論はある？ | 手動設計されたスキーマに依存している点や、構造化プロンプト導入によるプロンプターの推論コスト増加、および評価指標がモデルの出力（画像）とプロンプトの対に依存しているため、特定の評価モデルに依存する可能性が指摘されている。 |
| 次に読むべき論文は？ | [PixArt-Σ (Chen et al., 2024)](https://arxiv.org/abs/2403.05135) や [DALL-E 3 (Betker et al., 2023)](https://cdn.openai.com/papers/dall-e-3.pdf)、[Cosmos 3 (NVIDIA, 2026)](https://arxiv.org/abs/2606.02800) |
| PDFリンク | https://arxiv.org/pdf/2607.29679v1 |
