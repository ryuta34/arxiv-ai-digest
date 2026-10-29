---
title: "Heads of Security: Learned Attention Gates Improve Prompt Injection Robustness"
date: 2026-10-29
arxiv_id: 2610.37657v1
url: http://arxiv.org/abs/2610.37657v1
---

# Heads of Security: Learned Attention Gates Improve Prompt Injection Robustness

| 項目 | 内容 |
|---|---|
| どんなもの？ | 大規模言語モデルにおけるプロンプトインジェクション攻撃を防ぐための、学習可能な「アテンションゲート（Heads of Security: HoS）」を導入する手法。モデルのアーキテクチャに直接介入し、信頼できるプロンプトと信頼できない外部データ間の命令分離を強制することで、堅牢性とモデル本来の有用性を両立させる。 |
| 先行研究と比べてどこがすごい？ | 従来のファインチューニングベースの手法（SecAlign等）やアーキテクチャによる分離手法（ASIDE等）と比較し、適応的な攻撃（RL-HammerやClaudiniなど）に対する高い堅牢性を実現しつつ、few-shotやマルチターン環境での有用性の低下を劇的に抑制した点。また、調整が必要なパラメータが極めて少ない（数万単位）ため、効率的である。 |
| 技術や手法のキモはどこ？ | アテンションメカニズムにおける各ヘッドに対し、クエリとキーのチャネル（信頼できる/できない/テンプレート）に基づいてアテンションの重みを再分配する「ゲート」を導入したこと。これにより、モデルの既存の推論能力を損なうことなく、特定の入力ソースからの命令追従を動的に抑制できる。 |
| どうやって有効だと検証した？ | Llama-3.3-70BやGPT-OSS-20Bを用い、AgentDojo、AgentDyn、LLMail-Injectなどのエージェント向けベンチマークで評価。また、RL-Hammer等の強固な適応的攻撃を用いたレッドチーミングを行い、攻撃成功率（ASR）の低減と、タスク遂行能力（有用性）の維持を多角的に比較検証した。 |
| 議論はある？ | HoSはトラスト境界（何が信頼できるか）の定義には依存するため、エンドツーエンドの万能な解決策ではない。また、線形アテンション等のアーキテクチャには直接適用できないことや、攻撃者が新しい手法に適応する可能性については今後も注視が必要である。 |
| 次に読むべき論文は？ | [ASIDE: Architectural separation of instructions and data in language models](https://arxiv.org/abs/2602.03117)、[Meta-SecAlign: A secure foundation LLM against prompt injection attacks](https://arxiv.org/abs/2507.02735)、[Prompt injection as role confusion](https://openreview.net/forum?id=Lm3DQDyIsI) |
| PDFリンク | https://arxiv.org/pdf/2610.37657v1 |
