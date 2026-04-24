---
title: "Evaluation of Automatic Speech Recognition Using Generative Large Language Models"
date: 2026-04-24
arxiv_id: 2604.21928v1
url: http://arxiv.org/abs/2604.21928v1
---

# Evaluation of Automatic Speech Recognition Using Generative Large Language Models

| 項目 | 内容 |
|---|---|
| どんなもの？ | 自動音声認識（ASR）システムの性能評価において、生成AI（LLM）の活用可能性を検討した研究。従来のWER（単語誤り率）に代わり、LLMの深い文脈理解を用いた評価指標の有用性を提示している。 |
| 先行研究と比べてどこがすごい？ | WERや従来の埋め込みベースの指標（BERT等）が持つ「意味的ニュアンスや人間の直感との乖離」という課題を、最新のデコーダベースLLMを用いて克服した点。特に人間の評価者との高い合意率（92〜94%）を達成している。 |
| 技術や手法のキモはどこ？ | (1) LLMが2つの候補から正しい方を判断する「LLM as a judge」手法、(2) LLMの隠れ層からの埋め込みベクトルにpooling操作を施すことによる意味類似度評価、(3) 誤り内容の定性的な自動分類。 |
| どうやって有効だと検証した？ | フランス語のASR評価用データセット「HATS」を使用。LLMによる仮説選択の合意率をWERや従来の指標と比較し、あわせてLLMの埋め込みを用いた類似度スコアと人間による評価との相関を検証した。 |
| 議論はある？ | LLMのモデルサイズと埋め込み性能の相関が必ずしも強くないことや、次世代のトークン予測に特化した学習が埋め込みの質に与える影響、特定のタスク（分類等）向けにファインチューニングされたモデルの優位性が課題として挙げられる。 |
| 次に読むべき論文は？ | [HATS dataset (Bañeras-Roux et al., 2023)](https://aclanthology.org/2023.tsd-1.15/)、[SemDist (Kim et al., 2021)](https://ieeexplore.ieee.org/document/9541584)、[BERTScore (Zhang et al., 2019)](https://openreview.net/forum?id=SkeHuCVFDr) |
| PDFリンク | https://arxiv.org/pdf/2604.21928v1 |
