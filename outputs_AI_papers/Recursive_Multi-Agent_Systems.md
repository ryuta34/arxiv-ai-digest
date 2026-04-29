---
title: "Recursive Multi-Agent Systems"
date: 2026-04-29
arxiv_id: 2604.25917v1
url: http://arxiv.org/abs/2604.25917v1
---

# Recursive Multi-Agent Systems

| 項目 | 内容 |
|---|---|
| どんなもの？ | 複数のLLMエージェント間の協調を、テキストベースの対話ではなく、共通の潜在空間（Latent Space）における反復的な再帰計算として定式化したマルチエージェントシステム（MAS）フレームワーク。 |
| 先行研究と比べてどこがすごい？ | テキストベースの対話で発生するレイテンシや勾配消失の問題を克服し、平均8.3%の精度向上と最大2.4倍の推論速度向上、75.6%のトークン削減を達成した点。 |
| 技術や手法のキモはどこ？ | 軽量な「RecursiveLink」モジュールを用いて、エージェント間の隠れ状態（Latent Thoughts）を直接伝播・更新させることで、システム全体を単一の再帰的計算グラフとして最適化する点。 |
| どうやって有効だと検証した？ | 数学、科学、医療、検索、コード生成など9つのベンチマークにおいて、様々なエージェント構成（Sequential, Mixture, Distillation, Deliberation等）で評価を実施。 |
| 議論はある？ | 再帰回数が増えるにつれてさらなる性能向上は見込めるが、再帰的な学習に伴う計算コストの最適化や、より多様なアーキテクチャへの汎用性については今後の課題。 |
| 次に読むべき論文は？ | [LoopLM (Zhu et al., 2025)](https://arxiv.org/abs/2510.25741)、[Mixture-of-Agents (Wang et al., 2025b)](https://arxiv.org/abs/2506.21734)、[TextGrad (Yuksekgonul et al., 2025)](https://arxiv.org/abs/2504.02029) |
| PDFリンク | https://arxiv.org/pdf/2604.25917v1 |
