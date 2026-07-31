---
title: "ReToken: One Token to Improve Vision-Language Models for Visual Retrieval"
date: 2026-07-31
arxiv_id: 2607.28627v1
url: http://arxiv.org/abs/2607.28627v1
---

# ReToken: One Token to Improve Vision-Language Models for Visual Retrieval

| 項目 | 内容 |
|---|---|
| どんなもの？ | 長大な視覚コンテキスト（画像集や長時間動画）から、質問に関連する少数のフレームを効率的に選択・検索するための学習可能な埋め込みトークン「RETOKEN」を提案した。既存のVLMのアーキテクチャを維持しつつ、少数のパラメータを追加・学習させることで、ゼロショットで長時間動画の推論精度を大幅に向上させる手法。 |
| 先行研究と比べてどこがすごい？ | 既存のAttentionベースの検索手法がVLM内でうまく機能しない（関連性が低い）という問題を特定し、より精度の高い「Value空間」での検索を可能にした。たった1つのトークンを追加する軽量な設計ながら、Visual HaystacksやLVBenchなどの主要ベンチマークで高い性能を発揮し、単一のH100 GPUで訓練・推論が完結する。 |
| 技術や手法のキモはどこ？ | クエリに対する関連性を、従来のQuery-Keyペアの積ではなく、学習されたトークンと各フレームの「Valueベクトル（最終層）」とのコサイン類似度で計算する点。また、タスクに応じて適切に情報を選択できるよう、特定の検索損失関数を用いたクラスバランス付き二値交差エントロピーで学習する。 |
| どうやって有効だと検証した？ | Visual Haystacks（画像集）およびQAEgo4D、LVBench、Video-MME（動画）を用いて検証。特にVisual Haystacksにおいて、コンテキストサイズが増加しても精度低下を最小限に抑え、Qwen3VL-8BやInternVL3.5-8Bにおいて20%以上の相対的な改善を実現した。 |
| 議論はある？ | 現在はフレーム単位の検索に限定されているため、時間的構造を伴うクエリには課題が残る。また、推論時に2パスの処理が必要となり、メモリと応答時間にわずかなオーバーヘッドが生じる。今後はトークンレベルでの検索や、時間的変位を考慮した検索メカニズムが課題となる。 |
| 次に読むべき論文は？ | [13] Streaming video question-answering with in-context video kv-cache retrieval, [45] Visual haystacks: A vision-centric needle-in-a-haystack benchmark |
| PDFリンク | https://arxiv.org/pdf/2607.28627v1 |
