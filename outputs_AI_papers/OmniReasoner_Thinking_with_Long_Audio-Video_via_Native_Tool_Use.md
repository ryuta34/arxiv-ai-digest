---
title: "OmniReasoner: Thinking with Long Audio-Video via Native Tool Use"
date: 2026-07-22
arxiv_id: 2607.19339v1
url: http://arxiv.org/abs/2607.19339v1
---

# OmniReasoner: Thinking with Long Audio-Video via Native Tool Use

| 項目 | 内容 |
|---|---|
| どんなもの？ | 長時間の動画・音声データを効率的に推論するための、ツール利用型ポストトレーニングフレームワーク「OmniReasoner」の提案。モデルは低解像度の全体プレビューを見て、必要に応じて高解像度な詳細部分（ズームイン）を呼び出すことで、効率的な推論と正確な時間的特定を両立する。 |
| 先行研究と比べてどこがすごい？ | 従来手法は一定のサンプリングレートで動画を処理しがちで、長時間の動画では重要な手がかりを見落としやすかった。OmniReasonerは、モデル自身が「いつ、どこを見るか」というツール利用戦略を学習することで、計算コストを抑えつつ長尺動画の細部まで正確に把握できる。 |
| 技術や手法のキモはどこ？ | 全体プレビューと詳細なローカルクリップという異なる粒度の間でも、時間軸を一致させる「TimeAnchor」メカニズムの導入と、FFmpegを用いた「Temporal Augmented Data Engine」によるツール利用能力の自動学習データ生成にある。 |
| どうやって有効だと検証した？ | OmniVideoBenchやLVOmniBenchなど、複数の音声・映像推論ベンチマークで検証。長尺動画になればなるほど（5-10分、10-30分と）ベースラインモデルに対する精度向上幅が拡大することを確認した。 |
| 議論はある？ | 現在は「ズームイン」という単一のツールに限定されており、ウェブ検索やコード実行など他のツールとの連携は未検証。また、ベースモデルのコンテキストウィンドウの制限や、マルチターン推論を行うための大規模なエージェント用RLインフラが未成熟であることが課題。 |
| 次に読むべき論文は？ | [Omni-r1: Reinforcement learning for omnimodal reasoning via two-system collaboration](https://arxiv.org/abs/2505.20256)、[Longvt: Incentivizing "thinking with long videos" via native tool calling](https://arxiv.org/abs/2511.20785) |
| PDFリンク | https://arxiv.org/pdf/2607.19339v1 |
