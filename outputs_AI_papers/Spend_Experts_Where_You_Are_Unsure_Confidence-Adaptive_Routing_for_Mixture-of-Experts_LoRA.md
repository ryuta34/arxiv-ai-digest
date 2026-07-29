---
title: "Spend Experts Where You Are Unsure: Confidence-Adaptive Routing for Mixture-of-Experts LoRA"
date: 2026-07-29
arxiv_id: 2607.26052v1
url: http://arxiv.org/abs/2607.26052v1
---

# Spend Experts Where You Are Unsure: Confidence-Adaptive Routing for Mixture-of-Experts LoRA

| 項目 | 内容 |
|---|---|
| どんなもの？ | Mixture-of-Experts (MoE) LoRAにおいて、トークンごとの不確実性に応じてアクティブにするエキスパート数を適応的に変更する手法「CARE」を提案。推論時に計算コストを抑えつつ、モデルの精度と不確実性の推定能力を向上させる手法。 |
| 先行研究と比べてどこがすごい？ | 従来の固定されたtop-kルーティングと異なり、モデルが自身の予測に自信があるか（集中度）とエキスパート間の意見の相違（不確実性）を読み取ることで、計算リソースを難易度の高いトークンへ動的に再配分できる点。追加パラメータや追加の推論パスを一切必要としない。 |
| 技術や手法のキモはどこ？ | ルーターのソフトマックス出力分布から「累積質量（confidence）」と「エキスパート間の出力分散（disagreement）」を算出し、これを統合した信号に基づいてnucleus samplingのようにエキスパートを動的に選択する点。さらに計算予算を一定に保つための「予算サーモスタット」機構を備える。 |
| どうやって有効だと検証した？ | LLaMA-3.1-8BおよびQwen2.5-7Bを用い、コモンセンス推論、数学、コード、知識などのベンチマークで評価。固定kのベースラインと比較して、同等の計算量で精度を向上させ、同等の精度をより少ない平均エキスパート数（12%削減）で達成した。また、OOD（分布外）検知性能の向上も確認。 |
| 議論はある？ | ルーターが未学習または崩壊している場合は機能が低下することや、動的なkの決定が本番環境での静的バッチ処理を複雑にする可能性がある点を指摘。また、本手法は現在の分類タスク中心の評価にとどまっており、生成タスクへの拡張は今後の課題としている。 |
| 次に読むべき論文は？ | [LoRA: Low-rank adaptation of large language models](https://arxiv.org/abs/2106.09685), [Outrageously large neural networks: The sparsely-gated mixture-of-experts layer](https://arxiv.org/abs/1701.06538), [MixLoRA: Enhancing large language models fine-tuning with LoRA-based mixture of experts](https://arxiv.org/abs/2404.15159) |
| PDFリンク | https://arxiv.org/pdf/2607.26052v1 |
