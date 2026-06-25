---
title: "On-Policy Self-Distillation with Sampled Demonstrations Reduces Output Diversity"
date: 2026-06-25
arxiv_id: 2606.26091v1
url: http://arxiv.org/abs/2606.26091v1
---

# On-Policy Self-Distillation with Sampled Demonstrations Reduces Output Diversity

| 項目 | 内容 |
|---|---|
| どんなもの？ | 大規模言語モデル（LLM）の自己蒸留（SDSD）において、サンプリングされた実証データを用いることで生成された回答の多様性が著しく低下する現象を明らかにした研究。この多様性の低下が、モデルの学習と推論における「機能的・意味的な多様性の欠如」を招くことを理論的および実験的に示した。 |
| 先行研究と比べてどこがすごい？ | 従来の強化学習（RL）が報酬に対して報酬分布を広く維持するのに対し、自己蒸留は「ポイントワイズ条件付き相互情報量（PCMI）」によって確率分布を歪ませ、確率の高いモードに過度に集中してしまうことを理論的に解明した点。 |
| 技術や手法のキモはどこ？ | 自己蒸留の目的関数が、報酬による報酬ベースの勾配ではなく、教師モデルが実証データから受ける「支持の度合い（PCMI）」で最適化されるため、すでに確率が高い経路をさらに強化するという「成功体験の悪循環（Rich-get-richer）」を生むメカニズムを定式化した点。 |
| どうやって有効だと検証した？ | グラフパス探索タスクにおいて「意味的多様性」を定義して計測し、SDSDを用いたモデルが標準的なRL手法と比較して、分布外データ（OOD）に対する適応能力やパス探索の多様性で劣ることを示した。また、科学QAベンチマークでも同様の現象を確認した。 |
| 議論はある？ | SDSDの多様性低下は、KL正則化や外部からの多様なデモンストレーションを用いても完全には解決できない本質的な問題であると結論づけている。今後は、多様性を明示的に考慮した学習モニタリングの重要性を指摘している。 |
| 次に読むべき論文は？ | [Hübotter et al. (2026), "Reinforcement learning via self-distillation"](https://arxiv.org/abs/2601.20802) や [Zhao et al. (2026), "Self-distilled reasoner: On-policy self-distillation for large language models"](https://arxiv.org/abs/2601.18734) |
| PDFリンク | https://arxiv.org/pdf/2606.26091v1 |
