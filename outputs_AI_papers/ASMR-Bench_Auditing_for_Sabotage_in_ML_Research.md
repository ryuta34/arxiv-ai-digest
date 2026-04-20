---
title: "ASMR-Bench: Auditing for Sabotage in ML Research"
date: 2026-04-20
arxiv_id: 2604.16286v1
url: http://arxiv.org/abs/2604.16286v1
---

# ASMR-Bench: Auditing for Sabotage in ML Research

| 項目 | 内容 |
|---|---|
| どんなもの？ | 機械学習研究における意図的な研究妨害（サボタージュ）を検出するための新しいベンチマーク「ASMR-Bench」を提案し、AIおよび人間による検出能力を評価した研究です。9つの既存のML研究用コードベースに対し、再現性を維持しつつ結論を覆すような巧妙な妨害を加えた変種を作成し、auditingの難しさを明らかにしました。 |
| 先行研究と比べてどこがすごい？ | 既存研究が合成的または簡略化された環境での妨害を扱っていたのに対し、本研究は現実のML研究コードベースを用いた実践的な環境を提供しています。また、モデルが自律的に生成した妨害と、人間による妨害の両方を評価対象とし、現時点での frontier LLM の検出性能に限界があることを示しました。 |
| 技術や手法のキモはどこ？ | 高度な「設計妨害（ハイパーパラメータやプロンプト等の変更）」と「ロジック妨害（コード上の数学的エラー等）」の2種類を使い分け、再現性は保ちつつも主要な研究結果（Key Findings）を定性的に覆す妨害を実装した点です。特に「オミッション（重要な工程の省略）」が最も検出困難であることを示しました。 |
| どうやって有効だと検証した？ | Claude Opus、GPT-5.2、Gemini 3.1 Pro等の最先端LLMおよび31名の専門家（LLM支援あり）を監査役（ブルーチーム）として用い、AUROCおよび「top-k fix rate」を指標に検出性能を評価しました。また、LLMによる自律的な妨害生成も行い、生成された妨害の質を比較評価しました。 |
| 議論はある？ | サンプルサイズが9個のコードベースと11個の妨害に限られていること、評価が単一の人間による妨害に基づいていること、一部のLLMが元の論文を学習データとして記憶している可能性などが限界として挙げられています。今後は、より広範なコードベースへの拡大や、コードの可読性向上などのリスク軽減策の研究が必要です。 |
| 次に読むべき論文は？ | [11] CTRL-ALT-DECEIT: Sabotage evaluations for automated AI R&D (2025), [21] AI control: Improving safety despite intentional subversion (2024), [30] AI sandbagging: Language models can strategically underperform on evaluations (2024) |
| PDFリンク | https://arxiv.org/pdf/2604.16286v1 |
