---
title: "CordisBench: Can Language Models Reason About Component Lifecycles in Dynamic Agent Harnesses?"
date: 2026-09-02
arxiv_id: 2609.01600v1
url: http://arxiv.org/abs/2609.01600v1
---

# CordisBench: Can Language Models Reason About Component Lifecycles in Dynamic Agent Harnesses?

| 項目 | 内容 |
|---|---|
| どんなもの？ | 言語モデルが、動的エージェントハーネス（実行環境）におけるコンポーネントの依存関係やライフサイクル、およびプラグイン変更による状態変化をどの程度推論できるかを測定する1,200問のベンチマーク「CordisBench」を提案した研究。 |
| 先行研究と比べてどこがすごい？ | 従来の論理推論ベンチマークと異なり、プラグインの追加・削除に伴う「依存関係の伝搬」や「クリーニング処理の順序依存性」という、エージェント環境特有の複雑なライフサイクル推論能力を体系的に測定できる点。 |
| 技術や手法のキモはどこ？ | 依存関係とクリーニング効果を形式化した「形式言語モデル」と、実際にCordisランタイム上で動作検証を行う「Cordis-native設定」を組み合わせ、相互作用の数を2から32までスケーリングして評価する設計。 |
| どうやって有効だと検証した？ | Gemini 3.7 Flash、GPT-5.6 Luna、DeepSeek V4 Flashの3モデルを対象に、localization（影響範囲特定）、schedule prediction（最終状態予測）等の各タスクで推論性能を評価し、推論コストやスケールによる性能低下を定量化した。 |
| 議論はある？ | 24〜32の相互作用数は現実的な設定というよりストレステストの側面が強い点や、エージェントが提供するツールやフィードバック等の他のメカニズムが推論難易度に与える影響を完全には網羅できていない点。 |
| 次に読むべき論文は？ | [Shi et al. (2026), "A programming paradigm for spatiotemporal composability"](https://arxiv.org/abs/2609.01600) (Cordisランタイムの基盤論文) |
| PDFリンク | https://arxiv.org/pdf/2609.01600v1 |
