---
title: "Designer-RSI: Evolving Procedural Memory from User Traffic for Agentic Graphic Design"
date: 2026-09-21
arxiv_id: 2609.22086v1
url: http://arxiv.org/abs/2609.22086v1
---

# Designer-RSI: Evolving Procedural Memory from User Traffic for Agentic Graphic Design

| 項目 | 内容 |
|---|---|
| どんなもの？ | プロフェッショナルなグラフィックデザインを行うエージェントにおいて、ユーザーからの実トラフィックに基づき、外部の「手続き的メモリ（Procedural Memory）」を継続的に適応・改善させるフレームワーク「EVOLVE」を提案しています。モデルの重みを更新することなく、再利用可能なデザイン手順のライブラリ（スキルバンク）を適応させることで、複雑で多ステップな設計タスクの成功率と品質を向上させます。 |
| 先行研究と比べてどこがすごい？ | LLMのパラメータを更新せずに、失敗と成功の履歴に基づいた「 widening（未解決タスクへの新スキル作成）」と「deepening（既存スキルの修正）」という2つのメカニズムを結合し、保守的な「リプレイゲート」で regression（性能劣化）を確実に防ぎながら継続的に学習できる点です。 |
| 技術や手法のキモはどこ？ | 学習データや報酬ラベルが乏しい環境でも動作する「リプレイゲート」です。新しいスキルや修正案が既存の成功事例を損なわないかを、ペア比較テストで厳格に判定します。また、手続きを自然言語記述の形で保持し、実行時に適切な手順を選択・ロードする設計により、効率的なツール利用を実現しています。 |
| どうやって有効だと検証した？ | 1,406件のユーザーリクエストによる5ラウンドの進化ループを経て、Claude-Sonnet-4やOpus-4.6、Qwenなどの複数のバックボーンで評価。GenEval2などのT2Iベンチマークに加え、GraphicBench等のデザイン特化型ベンチマークにおいて、ベースラインを大幅に上回る成功率と生成品質を達成しました。 |
| 議論はある？ | 長い多ステップの構成において、手続き記述の忠実度が低下する「fidelity leak」の課題が挙げられています。また、本手法はあくまで自然言語によるガイドであり、非常に複雑な幾何学的精度を要するタスクでは、モデルの推論能力や検証メカニズムの限界に依存する点が将来課題とされています。 |
| 次に読むべき論文は？ | [MACLA](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/FKYO8341.pdf), [Skill-Pro](https://arxiv.org/abs/2602.01869), [SkillAudit](https://arxiv.org/abs/2606.14239) |
| PDFリンク | https://arxiv.org/pdf/2609.22086v1 |
