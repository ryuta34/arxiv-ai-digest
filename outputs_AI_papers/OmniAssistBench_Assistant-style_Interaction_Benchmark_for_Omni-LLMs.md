---
title: "OmniAssistBench: Assistant-style Interaction Benchmark for Omni-LLMs"
date: 2026-08-24
arxiv_id: 2608.21360v1
url: http://arxiv.org/abs/2608.21360v1
---

# OmniAssistBench: Assistant-style Interaction Benchmark for Omni-LLMs

| 項目 | 内容 |
|---|---|
| どんなもの？ | 実世界のビデオアシスタントとしてのOmni-LLMの能力を評価するための、インタラクティブなベンチマーク「OmniAssistBench」を提案した。ユーザーの行動がモデルの応答によって変化する動的な対話シナリオをシミュレートする。 |
| 先行研究と比べてどこがすごい？ | 従来の静的なビデオ評価ベンチマークとは異なり、モデルの応答がその後の対話やビデオコンテンツに影響を与える「双方向の対話」を評価できる。また、1000時間以上の専門家による手作業で構築され、マルチターン対話の評価に特化している。 |
| 技術や手法のキモはどこ？ | インターネット動画を逆解析してユーザーゴールと固定の対話パスを導き出し、モデルが特定のルートを辿るよう設計したデータ構築手法。また、ビデオへの音声音声埋め込みや、手作業でのビデオトリミングによるマルチターン対話のシミュレーション。 |
| どうやって有効だと検証した？ | Gemini-3-ProやQwen3-Omni-Instructを含む主要なモデルを対象に、Basic/Advancedの2階層のタスク群および3つのリアルワールドケースで評価。GPT-5等を用いたLLMベースの自動評価システムを構築してスコア化。 |
| 議論はある？ | 現在のモデルは、視覚的プロンプト（ジェスチャー）への対応、長期間の文脈保持、応答タイミングの制御に課題がある。また、モデルのコンテキストウィンドウの制限や、複雑なマルチタスク管理における推論精度の低下が指摘されている。 |
| 次に読むべき論文は？ | [Qwen3-Omni: Scaling up, toward native omni-modal AGI](https://arxiv.org/abs/2509.17765), [VITA-1.5: Towards GPT-4o level real-time vision and speech interaction](https://arxiv.org/abs/2411.03628), [StreamingBench](https://arxiv.org/abs/2411.03628) |
| PDFリンク | https://arxiv.org/pdf/2608.21360v1 |
