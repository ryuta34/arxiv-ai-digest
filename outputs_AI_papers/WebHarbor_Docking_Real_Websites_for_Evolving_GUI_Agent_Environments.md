---
title: "WebHarbor: Docking Real Websites for Evolving GUI Agent Environments"
date: 2026-11-04
arxiv_id: 2611.03634v1
url: http://arxiv.org/abs/2611.03634v1
---

# WebHarbor: Docking Real Websites for Evolving GUI Agent Environments

| 項目 | 内容 |
|---|---|
| どんなもの？ | 実環境のGUI操作を安定かつスケーラブルに評価・学習するための、153のdockerizedされたウェブサイト環境スイート「WebHarbor」を提案した研究。人手とエージェントの協調によって構築され、認証が必要なワークフローや状態変更を伴うタスクを含む3,518のタスクを提供する。 |
| 先行研究と比べてどこがすごい？ | 従来のライブウェブ環境が抱えていた「サイト更新による変動」「ボット検知」「認証の壁」といった不安定さを排除しつつ、静的な合成環境が抱えていた「視覚的忠実度の低さ」「機能の浅さ」を克服した点。認証、トランザクション、状態変化といった実用的なワークフローを完全に再現可能な環境を実現している。 |
| 技術や手法のキモはどこ？ | タスク主導のドッキング（Task-driven docking）と、人手による反復的な監査（Human-in-the-loop iterative refinement）の組み合わせ。コーディングエージェントがタスクの要件に合わせてバックエンドやDBを構築し、人間が視覚的・機能的忠実度を検査・修正することで、高い現実味と決定論的挙動を両立させた。 |
| どうやって有効だと検証した？ | WebHarborでトレーニングしたQwen 4Bエージェントを、WebVoyager、Online-Mind2Web、WebArena等の主要なライブウェブ・ベンチマークで評価。既存のライブウェブ学習手法（OpenWebRL）と比較して平均スコアで優位性を実証し、未見タスクや他環境への強力な汎化性能を示した。 |
| 議論はある？ | 実環境の完全な再現ではなく、動的なマップや広告などは静的な代理機能に置換されている限界がある。また、評価用の自動検証器やLLMジャッジが、エージェントの有効な代替案や微妙な失敗を見落とす可能性があると指摘されている。 |
| 次に読むべき論文は？ | [OpenWebRL](https://arxiv.org/abs/2606.02031)、[WebVoyager](https://arxiv.org/abs/2401.01614)、[WebArena](https://arxiv.org/abs/2401.13649) |
| PDFリンク | https://arxiv.org/pdf/2611.03634v1 |
