---
title: "EVA-Bench: A New End-to-end Framework for Evaluating Voice Agents"
date: 2026-05-14
arxiv_id: 2605.13841v1
url: http://arxiv.org/abs/2605.13841v1
---

# EVA-Bench: A New End-to-end Framework for Evaluating Voice Agents

| 項目 | 内容 |
|---|---|
| どんなもの？ | 音声対話エージェントを評価するためのエンドツーエンドのフレームワーク「EVA-Bench」を提案。実運用環境を模したボット対ボットの対話生成と、音声特有の失敗モードを捕捉する評価指標を統合的に提供する。 |
| 先行研究と比べてどこがすごい？ | 従来手法が個別のコンポーネント（STTやTTSなど）の評価に限定されていたのに対し、完全なマルチターン対話を通じた end-to-end の評価を可能にした点。また、自動シミュレーション検証と、精度の「EVA-A」、対話体験の「EVA-X」という複合指標により、アーキテクチャを問わない直接比較を実現した。 |
| 技術や手法のキモはどこ？ | バリデーションゲートを設けた自動ボット対ボット対話シミュレーションと、実運用における堅牢性を測るためのアクセントやノイズを含む摂動スイート。また、単一試行（pass@1）だけでなく、複数試行の整合性を測るpass@kおよびpass^kを用いた信頼性評価。 |
| どうやって有効だと検証した？ | 3つのエンタープライズ領域（CSM, HRSD, ITSM）で合計213のシナリオを作成し、計12のシステムを評価。清潔なベースライン環境および摂動条件下での性能劣化を測定し、各モデルの精度と対話体験のトレードオフを分析した。 |
| 議論はある？ | 評価に使用するLLMジャッジのスタイリスティックなバイアスや、シミュレーターと実ユーザーの乖離（Sim2Real gap）の可能性。また、API利用コストの高さや、現時点では英語のみの対応である点。 |
| 次に読むべき論文は？ | [14] VoiceAgentBench: Are voice assistants ready for agentic tasks? (https://arxiv.org/abs/2510.07978), [28] τ-voice: Benchmarking full-duplex voice agents on real-world domains (https://arxiv.org/abs/2603.13686) |
| PDFリンク | [https://arxiv.org/pdf/2605.13841v1](https://arxiv.org/pdf/2605.13841v1) |
