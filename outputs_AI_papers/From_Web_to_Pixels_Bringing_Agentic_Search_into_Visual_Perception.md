---
title: "From Web to Pixels: Bringing Agentic Search into Visual Perception"
date: 2026-05-13
arxiv_id: 2605.12497v1
url: http://arxiv.org/abs/2605.12497v1
---

# From Web to Pixels: Bringing Agentic Search into Visual Perception

| 項目 | 内容 |
|---|---|
| どんなもの？ | 画像内の対象が外部知識に依存して特定される「Perception Deep Research」という新しい課題設定と、それに対応するベンチマーク「WebEyes」を提案した論文。また、エージェントがWeb検索と推論を行い、対象を視覚情報に紐付けるワークフロー「Pixel-Searcher」を開発している。 |
| 先行研究と比べてどこがすごい？ | 従来の視覚接地（Grounding）や知識ベースVQAが単一の画像やモデル内部知識のみを前提としていたのに対し、本研究は最新のイベントや外部事実を能動的に検索して接地を行う、より実践的で困難なオープンワールド環境を実現した点。 |
| 技術や手法のキモはどこ？ | クエリをサブゴールに分解する「クエリプランニング」、検索・推論・解の特定を繰り返す「Search-Reasonループ」、および解決したターゲット情報を視覚的な候補領域に紐付ける「インスタンスバインディング」と「証拠検証」を組み合わせたエージェント設計。 |
| どうやって有効だと検証した？ | WebEyesベンチマーク上で、Search-based Grounding、Segmentation、VQAの3タスクにおいて、Pixel-Searcherが既存のオープンソースモデル（Qwen3-VL-8B等）の性能を一貫して向上させることを実証した。 |
| 議論はある？ | 失敗の主な要因はマスクの精細化ではなく、証拠の取得、IDの解決、および視覚的なインスタンス紐付けにあると分析。特に多義的な対象や類似物がある環境での検索の難しさが依然として残る課題である。 |
| 次に読むべき論文は？ | [13] MMSearch: Benchmarking the potential of large models as multi-modal search engines, [19] WebWatcher: Breaking new frontier of vision-language deep research agent, [34] Seg-research: Segmentation with interleaved reasoning and external search |
| PDFリンク | https://arxiv.org/pdf/2605.12497v1 |
