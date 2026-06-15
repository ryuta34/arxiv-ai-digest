---
title: "RepFusion: Leveraging Multimodal Priors for Denoising in Representation Space"
date: 2026-06-15
arxiv_id: 2606.14700v1
url: http://arxiv.org/abs/2606.14700v1
---

# RepFusion: Leveraging Multimodal Priors for Denoising in Representation Space

| 項目 | 内容 |
|---|---|
| どんなもの？ | 大規模言語モデル（LLM）を単なるテキストエンコーダーとしてではなく、ノイズを含んだ視覚表現を直接処理する「ノイズ表現エンコーダー」として活用するテキスト・画像生成モデル（RepFusion）。従来のVAEベースから、より意味的に構造化された表現オートエンコーダー（RAE）の潜在空間上で拡散モデルを構築することで、生成性能を向上させた。 |
| 先行研究と比べてどこがすごい？ | テキストエンコーダーを「静的」な入力として扱う従来手法に対し、RepFusionはノイズを含む視覚表現を入力に含めることで、拡散プロセスの各ステップでLLMの事前知識を動的に活用できる。これにより、パラメータ数や計算予算が同等なベースラインに対して大幅な性能向上を達成した。 |
| 技術や手法のキモはどこ？ | 1. 拡散モデルの潜在空間をRAE（表現オートエンコーダー）に移行。 2. 凍結した事前学習済みマルチモーダルLLMに対し、MLPプロジェクターを介してノイズを含む視覚表現を注入し、生成の条件付けとして利用する手法。 3. 推論時にLLMを動的に再計算することで、入力依存の条件信号を生成するスケーリング戦略。 |
| どうやって有効だと検証した？ | GenEval、GenEval++、GenEval2、DPG-Benchといった主要なベンチマークを用いて、既存のTextEmbedやTransfusionベースラインと比較評価。また、マルチモーダル知覚事前学習の有無や、LLMの微調整に関するアブレーション研究を実施し、性能向上要因を解明した。 |
| 議論はある？ | RAEデコーダーを使用すると画像がぼやけやすく、それがVLMベースの評価指標に悪影響を与える可能性がある点。また、性能向上は主にデノイザー（DiT）の拡大に依存する側面があり、LLM側のスケーリングよりもDiT側のスケーリングの方が推論効率が良いことが示唆されている。 |
| 次に読むべき論文は？ | [Diffusion transformers with representation autoencoders (Zheng et al., 2026)](https://arxiv.org/abs/2606.14700v1)（本論文のベースとなるRAEの研究） |
| PDFリンク | https://arxiv.org/pdf/2606.14700v1 |
