---
title: "When LLMs Stop Following Steps: A Diagnostic Study of Procedural Execution in Language Models"
date: 2026-05-04
arxiv_id: 2605.00817v1
url: http://arxiv.org/abs/2605.00817v1
---

# When LLMs Stop Following Steps: A Diagnostic Study of Procedural Execution in Language Models

| 項目 | 内容 |
|---|---|
| どんなもの？ | 大規模言語モデル（LLM）が、プロンプトで指示された多段階の算術手順を忠実に実行できるかを検証する診断用ベンチマーク。単純な算術計算であっても、手順の長さや依存関係が複雑になると、LLMの推論能力が著しく低下することを明らかにしている。 |
| 先行研究と比べてどこがすごい？ | 最終的な回答の正誤だけで評価するのではなく、モデルが生成プロセスでどのように手順を踏んでいるかを詳細に分析した点。特に「手順のスキップ」や「早期回答」といった生成レベルの失敗モードを可視化した。 |
| 技術や手法のキモはどこ？ | 手順の長さ（5〜95ステップ）と、中間結果を参照する必要がある「ルックバック依存性（直前の変数から過去数ステップ前の変数への参照）」を制御して難易度を段階的に高めたベンチマーク設計。 |
| どうやって有効だと検証した？ | 14モデル、55種類のデータセット、合計55,000例を用い、正解率だけでなく、回答位置やステップの遂行状況（過少実行・過剰実行・正確な実行）を指標として評価した。 |
| 議論はある？ | 現在は算術演算のみを対象としているため、より広範なタスクへの一般化や、LLMが「推論しているように見せかけている（パターンマッチング）」だけなのかを解明する点が今後の課題。 |
| 次に読むべき論文は？ | [Shojaee et al. (2025a) The illusion of thinking](https://arxiv.org/abs/2506.06941)、[Varela et al. (2025) Rethinking the illusion of thinking](https://arxiv.org/abs/2502.15631) |
| PDFリンク | https://arxiv.org/pdf/2605.00817v1 |
