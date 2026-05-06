---
title: "Safety and accuracy follow different scaling laws in clinical large language models"
date: 2026-05-06
arxiv_id: 2605.04039v1
url: http://arxiv.org/abs/2605.04039v1
---

# Safety and accuracy follow different scaling laws in clinical large language models

| 項目 | 内容 |
|---|---|
| どんなもの？ | 臨床現場におけるLLMの安全性を評価するためのフレームワーク「SaFE-Scale」と、専用ベンチマーク「RadSaFE-200」を提案する研究です。モデルの精度向上と安全性の向上が必ずしも比例しないこと（デカップリング）を明らかにし、エビデンス品質の重要性を指摘しています。 |
| 先行研究と比べてどこがすごい？ | 従来の「平均的な精度」のみを重視する評価指標を批判し、臨床的に重大な失敗（高リスク誤りや矛盾、過信）を個別に追跡する新しい評価軸を導入した点です。また、スケーリングが自動的に安全性を高めるわけではないことを、34個のLLMを用いた大規模実験で実証しました。 |
| 技術や手法のキモはどこ？ | Clinician-defined（臨床医による）clean evidence（正確な根拠）の付与が、RAGやモデルの拡大よりも圧倒的に安全性を向上させることを突き止めた点です。また、危険な過信を「誤答」「高リスクな選択」「高確信度」の組み合わせとして定義・測定しています。 |
| どうやって有効だと検証した？ | 34個のLLM、6つの展開条件（プロンプト、RAG、エージェントなど）、200問のRadSaFE-200を用いて全40,800通りの評価を実施しました。さらに自己整合性（self-consistency）やアンサンブル学習による推論時計算の増加が安全性を改善しないことも検証しています。 |
| 議論はある？ | テキストベースの多肢選択問題に限定されているため、実臨床の複雑なマルチモーダル処理を完全には網羅していません。また、安全性の定義（ラベル付け）に臨床医の主観が含まれる可能性があり、今後の研究ではより多角的なラベリングが求められます。 |
| 次に読むべき論文は？ | [1] Singhal et al. "Large language models encode clinical knowledge" (Nature 2023) / [2] Hager et al. "Evaluation and mitigation of the limitations of large language models in clinical decision-making" (Nature medicine 2024) / [12] Wind et al. "Multi-step retrieval and reasoning improves radiology question answering with large language models" (npj Digital Medicine 2025) |
| PDFリンク | https://arxiv.org/pdf/2605.04039v1 |
