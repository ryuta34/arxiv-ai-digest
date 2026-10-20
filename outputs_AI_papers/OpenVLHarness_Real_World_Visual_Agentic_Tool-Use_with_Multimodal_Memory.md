---
title: "OpenVLHarness: Real World Visual Agentic Tool-Use with Multimodal Memory"
date: 2026-10-20
arxiv_id: 2610.26860v1
url: http://arxiv.org/abs/2610.26860v1
---

# OpenVLHarness: Real World Visual Agentic Tool-Use with Multimodal Memory

| 項目 | 内容 |
|---|---|
| どんなもの？ | 視覚的な推論タスクにおいて、MLLM（マルチモーダル大規模言語モデル）の推論能力を補完するための視覚エージェント用フレームワーク「OpenVLHarness」。ツール利用の統一インターフェースを提供する「Capability Layer」と、生成された視覚・構造化データを保持・再利用する「Persistent Multimodal Memory」を備える。 |
| 先行研究と比べてどこがすごい？ | 従来のツール利用エージェントが持つ「異種バックエンドの不整合」や「推論ステップ間でのデータ保持の脆弱性」を解決した点。また、モデルの重みを更新せず、失敗分析に基づくプロンプトやツール構成の自動最適化を実現した点。 |
| 技術や手法のキモはどこ？ | ツール出力を視覚的・構造的に解釈可能な形式に変換してモデルに提示する「Evidence Rendering」と、Pythonコーディングエージェントを介してメモリ上のartifacts（画像、マスク、データバインディング等）を直接操作・計算可能にした「Persistent Multimodal Memory」の連携。 |
| どうやって有効だと検証した？ | grounded perception、visual search、一般VQA、空間推論の4ドメイン、計22のベンチマークにおいて、8つの主要なオープンソースおよびプロプライエタリなモデル（Qwen、Kimi、GPT-6等）を使用して評価。ツールなしのベースラインと比較し、平均スコアを9.7〜12.6ポイント改善した。 |
| 議論はある？ | 高い推論努力（compute budget）をかけても、ツール利用なしでは性能向上には限界があることが示された。また、モデルが複雑なタスクで誤った対象を選択した場合、その後のパイプラインで自動的に修正できないケースがあることが失敗分析で明らかにされた。 |
| 次に読むべき論文は？ | [Visual Sketchpad (Hu et al., 2024)](https://arxiv.org/abs/2311.13934)、[OctoTools (Lu et al., 2025)](https://arxiv.org/abs/2502.11271)、[ViperGPT (Surís et al., 2023)](https://arxiv.org/abs/2303.14628) |
| PDFリンク | https://arxiv.org/pdf/2610.26860v1 |
