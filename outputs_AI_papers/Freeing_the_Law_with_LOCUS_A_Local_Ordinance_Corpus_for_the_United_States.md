---
title: "Freeing the Law with LOCUS: A Local Ordinance Corpus for the United States"
date: 2026-06-18
arxiv_id: 2606.19334v1
url: http://arxiv.org/abs/2606.19334v1
---

# Freeing the Law with LOCUS: A Local Ordinance Corpus for the United States

| 項目 | 内容 |
|---|---|
| どんなもの？ | 米国全土の地方自治体（市・郡）の条例を収集・正規化した大規模データセット「LOCUS」およびその解析基盤です。9,239の自治体から収集したPDFをOCRでデジタル化し、法規制の分類や4つの規範的次元（不透明さ、裁量度、パターナリズム、重要性）でスコアリングを行っています。 |
| 先行研究と比べてどこがすごい？ | 従来、断片化して公開されていた米国の地方条例を全国規模で機械可読な形式に統一した初の試みです。既存のLegalBench等が契約書や裁判記録に偏っていたのに対し、市民生活に直結する地方条例の網羅的な分析を可能にしました。 |
| 技術や手法のキモはどこ？ | ブラウザ自動化による収集パイプライン、VLM（LightOnOCR-2-1B）を用いた高精度OCR、ModernBERTを用いた条例の機能・トピック分類、およびLLM（GPT-5.4-nano）のペア比較結果をTrueSkillでランク付けし、それを回帰学習させることで各条例の規範的スコアを導出した点です。 |
| どうやって有効だと検証した？ | 10,000件の条例サンプルに対し、LLM-as-a-Judgeを用いた20万件のペア比較でTrueSkillスコアを算出し、それを教師データとしてBERTモデルを訓練しました。モデルの予測値とTrueSkill値のピアソン相関係数が0.82〜0.94に達することで有効性を評価しています。 |
| 議論はある？ | 現在の設計は「最も長いコード」を選択する簡略化を行っており、法的な優先関係（どの法律が支配的か）を完全に解決するものではない点。また、地方条例の構造は地域や歴史的背景に依存し、単純な全国的な調和が困難であるという制約が議論されています。 |
| 次に読むべき論文は？ | [LegalBench (Guha et al., 2023)](https://arxiv.org/abs/2308.11462), [Pile of Law (Henderson et al., 2022)](https://arxiv.org/abs/2207.00220), [CaseHOLD (Zheng et al., 2021)](https://arxiv.org/abs/2104.08671) |
| PDFリンク | https://arxiv.org/pdf/2606.19334v1 |
