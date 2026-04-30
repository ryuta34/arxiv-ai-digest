---
title: "Select to Think: Unlocking SLM Potential with Local Sufficiency"
date: 2026-04-30
arxiv_id: 2604.26940v1
url: http://arxiv.org/abs/2604.26940v1
---

# Select to Think: Unlocking SLM Potential with Local Sufficiency

| 項目 | 内容 |
|---|---|
| どんなもの？ | 大規模言語モデル（LLM）の推論能力を、計算コストの高い生成ではなく、小規模言語モデル（SLM）の候補選択タスクとして蒸留することで、低レイテンシかつ高性能な推論を実現する枠組み「SELECT TO THINK (S2T)」およびその自律型モデル「S2T-LOCAL」を提案した論文。 |
| 先行研究と比べてどこがすごい？ | 従来の生成ベースの協調推論（LLMの呼び出しを伴う）や標準的な蒸留（容量のギャップによる性能限界）に対し、本手法はSLM自身の推論候補の中からLLMが好むトークンを選択する「ローカル充足性」を活用する。これにより、外部推論コストを排除しつつ、SLMの推論性能を大幅に向上させ、8パス自己整合性に匹敵する精度を実現した点。 |
| 技術や手法のキモはどこ？ | 推論過程における「ローカル充足性（LLMが選ぶトークンがSLMのトップK候補に含まれている現象）」を特定し、LLMのガイダンスを生成から離散的な候補選択に再定義した点。さらに、 reserved tokens（予約トークン）のロジットを「内なる批判者（inner critic）」として機能させ、SLM内部で自律的な再ランキングを可能にしたこと。 |
| どうやって有効だと検証した？ | GSM8K, MATH, HumanEval, MMLU-Proなどの数学・推論ベンチマークで検証。1.5BのSLMが32BのLLMの選択を95%の確率で捕らえ、貪欲復号と比較して平均24.1%の性能向上を達成した。また、追加の計算コストをほぼゼロに抑えつつ、モデル規模を問わず強力な転移学習性能を示すことを確認した。 |
| 議論はある？ | 本手法はSLMの潜在的な候補生成能力に依存しており、候補集合の外に正解が存在する場合には性能が制限される。また、トリガー機構に依存した介入を行うため、誤ったタイミングでの介入が推論を阻害する可能性があり、トリガーの閾値設定やロバスト性のさらなる改善が将来課題として挙げられる。 |
| 次に読むべき論文は？ | [Zip-rc: Zero-overhead inference-time prediction of reward and cost for adaptive and interpretable generation](https://arxiv.org/abs/2512.01457), [Critical tokens matter: Token-level contrastive estimation enhances llm’s reasoning capability](https://arxiv.org/abs/2411.19943), [Relayllm: Efficient reasoning via collaborative decoding](https://arxiv.org/abs/2601.05167) |
| PDFリンク | https://arxiv.org/pdf/2604.26940v1 |
