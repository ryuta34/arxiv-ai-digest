---
title: "Good Agentic Friends Do Not Just Give Verbal Advice: They Can Update Your Weights"
date: 2026-05-14
arxiv_id: 2605.13839v1
url: http://arxiv.org/abs/2605.13839v1
---

# Good Agentic Friends Do Not Just Give Verbal Advice: They Can Update Your Weights

| 項目 | 内容 |
|---|---|
| どんなもの？ | マルチエージェントLLMシステムの通信において、自然言語のメッセージ交換に代わり、送信側エージェントの隠れ状態から受信側モデルへ「一時的な重み摂動（LoRA）」を直接注入する手法「TFLOW」を提案。これにより、KVキャッシュの肥大化や推論コストの増大を抑制しつつ、効率的な共同作業を実現する。 |
| 先行研究と比べてどこがすごい？ | 自然言語や潜在表現（embedding）の送信ではなく、重み空間での通信を行うことで、受信側のコンテキストを汚染せずにインスタンスレベルの適応が可能。既存のテキストベースのマルチエージェント手法と比較し、処理トークン数を最大83.27%削減し、推論時間を最大4.6倍高速化しながら、同等の精度を達成した。 |
| 技術や手法のキモはどこ？ | 学習可能な「パラメータジェネレータ」が、各送信エージェントの隠れ状態を入力として、受信側の特定の線形層に対してクエリ依存の低ランク（LoRA）摂動を生成・注入する点。摂動は推論時のみ適用され、生成後に破棄されるため、ベースモデルを永続的に変更しない。 |
| どうやって有効だと検証した？ | GSM8K、MATH、MMLU、HumanEval+、MBPP+の5つのベンチマークで、単一モデルおよび従来のテキストベース・マルチエージェント（TextMAS）と比較。精度向上とトークン消費量・推論速度の観点から効率性を検証し、アブレーションスタディでインスタンス依存の適応の重要性を示した。 |
| 議論はある？ | 自然言語によるメッセージ交換ではないため、エージェント間の貢献度や推論プロセスの人間による解釈性が低い点。また、HumanEval+のような複雑なコード生成タスクでは、テキストによる詳細な中間推論トレースが生成長を補う利点があるため、TFLOWの簡潔な適応では補いきれない性能差が生じることが示唆された。 |
| 次に読むべき論文は？ | [17] Hu et al., "LoRA: Low-rank adaptation of large language models." (ICLR 2022) <br> [24] Wang et al., "Mixture-of-agents enhances large language model capabilities." (ICLR 2025) <br> [38] Wang et al., "LoRA-Flow: Dynamic LoRA fusion for large language models in generative tasks." (ACL 2024) |
| PDFリンク | https://arxiv.org/pdf/2605.13839v1 |
