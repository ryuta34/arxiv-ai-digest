---
title: "Multi-Agent AI System for Radiology Report Structuring and Quality Assurance with Independent Radiologist Evaluation"
date: 2026-08-19
arxiv_id: 2608.18072v1
url: http://arxiv.org/abs/2608.18072v1
---

# Multi-Agent AI System for Radiology Report Structuring and Quality Assurance with Independent Radiologist Evaluation

| 項目 | 内容 |
|---|---|
| どんなもの？ | 放射線科レポートの構造化と品質保証（QA）を自動化する、マルチエージェント型AIパイプライン。元の文章を改変せずに、解剖学的なセクションへの整理と、論理的矛盾やリスクの検出を同時に行う。 |
| 先行研究と比べてどこがすごい？ | 内容を要約・生成して元の情報を損なうリスクがある従来手法に対し、既存文を分類・配置する手法を採用し、情報の忠実性を担保した点。また、局所的なLLM環境で動作させ、セキュリティを確保している点。 |
| 技術や手法のキモはどこ？ | ルールベース（Regex）、軽量LLM（LLaMA-3）、推論LLM（DeepSeek-R1）を階層的に組み合わせた4エージェント構造。確定的な分類はルールで高速に行い、曖昧な文のみ推論モデルへ送る効率的なパイプライン。 |
| どうやって有効だと検証した？ | 638件のCTレポートを処理し、専門医2名による独立評価を実施。45件のサブセットを対象に、構造化の正確性、臨床的な情報の欠落・捏造の有無、QA機能の妥当性を評価した。 |
| 議論はある？ | 構造化により情報が重複して可読性が下がる場合があることや、評価対象が限定的であること。また、現状では偽陽性のフラグが一部存在しており、さらなるモデルの微調整が必要。 |
| 次に読むべき論文は？ | Hartsock I, et al. "Improving radiology report conciseness and structure via local large language models." [J Imaging Inform Med (2026)](https://doi.org/10.1007/s10278-025-01510-w) |
| PDFリンク | https://arxiv.org/pdf/2608.18072v1 |
