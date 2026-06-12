---
title: "EvoArena: Tracking Memory Evolution for Robust LLM Agents in Dynamic Environments"
date: 2026-06-12
arxiv_id: 2606.13681v1
url: http://arxiv.org/abs/2606.13681v1
---

# EvoArena: Tracking Memory Evolution for Robust LLM Agents in Dynamic Environments

| 項目 | 内容 |
|---|---|
| どんなもの？ | 動的な環境下でLLMエージェントが継続的に適応・学習するためのベンチマーク「EvoArena」と、環境の変化を「パッチ」として記録し再利用するメモリパラダイム「EvoMem」を提案した論文。既存のベンチマークが想定する静的な環境とは異なり、ツールやコードベース、ユーザー設定が時間経過とともに進化する状況でのエージェントの頑健性を評価する。 |
| 先行研究と比べてどこがすごい？ | 従来のベンチマークが環境の静的なスナップショットを対象としていたのに対し、環境の進化を時系列のチェーンとして捉えることで、エージェントの「バージョン適応能力」と「過去の知識との整合性」を測定できる点。また、EvoMemにより、単なる最新状態の保持だけでなく、過去の変更理由や証拠をトレース可能にした。 |
| 技術や手法のキモはどこ？ | Gitのようなパッチベースのメモリ構造。エージェントのメモリ更新を「非加算的（既存知識の書き換えや修正）」なものとして検出し、変更前後の状態、変更理由、根拠となった文脈をパッチとして保存する点。推論時には最新のメモリに加えて、クエリに関連する過去のパッチを動的に取得して利用する。 |
| どうやって有効だと検証した？ | ターミナル操作（Terminal-Bench-Evo）、ソフトウェア開発（SWE-Chain-Evo）、対話による好み（PersonaMem-Evo）の3領域で構成されるEvoArenaを用いて評価。ベースラインのモデルと比較し、EvoMemを適用することでステップ精度およびチェーンレベルの精度が全体的に向上することを確認した。 |
| 議論はある？ | 現在の検証は3つの代表的な領域に限定されており、今後はロボティクスや科学的ワークフローなど、より広範な動的環境への拡張が必要。また、パッチベースのメモリは機密情報を含む可能性があるため、適切なアクセス制御やデータ最小化の仕組みが不可欠であると述べている。 |
| 次に読むべき論文は？ | [13] Terminal-bench: Benchmarking agents on hard, realistic tasks in command line interfaces, [24] A-mem: Agentic memory for LLM agents, [26] Memento-skills: Let agents design agents |
| PDFリンク | https://arxiv.org/pdf/2606.13681v1 |
