---
title: "LKValues: Aligning Large Language Models with Sri Lankan Societal Values"
date: 2026-07-23
arxiv_id: 2607.20410v1
url: http://arxiv.org/abs/2607.20410v1
---

# LKValues: Aligning Large Language Models with Sri Lankan Societal Values

| 項目 | 内容 |
|---|---|
| どんなもの？ | スリランカの文化的・社会的価値観を学習・評価するための包括的なリソーススイート「LKValues」の提案。言語モデルを現地の文脈に合わせて調整するための調査駆動型パイプラインと、シンハラ語・英語のバイリンガル評価ベンチマークを構築した。 |
| 先行研究と比べてどこがすごい？ | 既存の多言語ベンチマークが主に西洋の価値観や広範な文化比較に焦点を当てていたのに対し、本研究はスリランカの現地調査（205名）に基づき、同国特有の社会的価値観（40項目）を定義・ operationalizeした点。また、現地ニュースに基づいた150kの学習データと1,000件の評価用ベンチマークを統合した初の試みである。 |
| 技術や手法のキモはどこ？ | 国際的な価値観フレームワークとLLMによる抽出を組み合わせた調査手法、および現地ニュース記事をフィルタリング・翻訳して構築した「LKvaluesIT」によるファインチューニング。LLMをループ内に組み込み、人間のアノテーターが検証を行うことで、文化的妥当性とラベルの信頼性を担保した点。 |
| どうやって有効だと検証した？ | Qwen3.5-4B-Base等のモデルをファインチューニングし、ベンチマーク「LKvaluesBench」を用いて、シンハラ語・英語での推論精度、無効な回答率、および言語間の格差を評価。プロンプトのフレーミングやモデル規模ごとの性能変化を詳細に分析した。 |
| 議論はある？ | サンプルサイズ（n=205）によるサブグループの偏りと代表性の限界、およびタスクの転移（LoRA適応がモデルファミリー間で均一に機能しない点）。また、現在は主にシンハラ語と英語を対象としており、タミル語を含む完全な三言語対応への拡張が将来の課題。 |
| 次に読むべき論文は？ | [CultureLLM: Incorporating cultural differences into large language models](https://arxiv.org/abs/2402.13605) / [Kornat: Llm alignment benchmark for korean social values and common knowledge](https://arxiv.org/abs/2402.13605) |
| PDFリンク | https://arxiv.org/pdf/2607.20410v1 |
