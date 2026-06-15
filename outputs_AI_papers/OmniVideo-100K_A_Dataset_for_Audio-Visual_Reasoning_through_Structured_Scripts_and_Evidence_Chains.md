---
title: "OmniVideo-100K: A Dataset for Audio-Visual Reasoning through Structured Scripts and Evidence Chains"
date: 2026-06-15
arxiv_id: 2606.14702v1
url: http://arxiv.org/abs/2606.14702v1
---

# OmniVideo-100K: A Dataset for Audio-Visual Reasoning through Structured Scripts and Evidence Chains

| 項目 | 内容 |
|---|---|
| どんなもの？ | 映像の音声と視覚情報を統合し、論理的な推論を可能にするための自動データ生成パイプラインと、それを用いて構築された大規模なオーディオビジュアル推論データセット「OmniVideo-100K」を提案している。 |
| 先行研究と比べてどこがすごい？ | 従来の「動画→キャプション→QA」という分断されたパイプラインによる、音声・視覚情報の乖離やエンティティの一貫性の欠如、長期的な時間推論の弱さを克服した点。構造化されたスクリプトを介して、複雑なクロスモーダルな依存関係を維持しつつ高品質なQAペアを生成できる。 |
| 技術や手法のキモはどこ？ | 主な技術は(1)エンティティリストをグローバルな事前知識として用いて一貫性を保つ「Entity-Anchored Video Scripting」と、(2)スクリプトから多セグメントにまたがる重要な手がかりを抽出し、それに基づいて推論QAを生成する「Clue-Guided QA Generation」の二段階アプローチ。 |
| どうやって有効だと検証した？ | 「OmniVideo-100K」でVITA-1.5やQwen-OmniなどのMLLMをファインチューニングし、検証用テストセット「OmniVideo-Test」や既存ベンチマーク(Daily-Omni等)で評価。従来手法に対し最大20.59%の性能向上を確認したほか、アブレーションスタディで各コンポーネントの寄与を証明した。 |
| 議論はある？ | 現在の非言語音（サウンド）に関するスクリプト化において、汎用的な分類にとどまっており、より複雑な音響現象については専門的な音声モデルとの統合が将来の課題である。 |
| 次に読むべき論文は？ | [Video-MME](https://arxiv.org/abs/2501.01957)、[OmniVideoBench](https://arxiv.org/abs/2510.10689)、[Daily-Omni](https://arxiv.org/abs/2505.17862) |
| PDFリンク | https://arxiv.org/pdf/2606.14702v1 |
