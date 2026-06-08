---
title: "MemDreamer: Decoupling Perception and Reasoning for Long Video Understanding via Hierarchical Graph Memory and Agentic Retrieval Mechanism"
date: 2026-06-08
arxiv_id: 2606.07512v1
url: http://arxiv.org/abs/2606.07512v1
---

# MemDreamer: Decoupling Perception and Reasoning for Long Video Understanding via Hierarchical Graph Memory and Agentic Retrieval Mechanism

| 項目 | 内容 |
|---|---|
| どんなもの？ | 長時間の動画理解における、知覚と推論を分離する新しいフレームワーク「MEMDREAMER」の提案。動画を階層的なグラフメモリとして構造化し、エージェントによるツール利用を通じた能動的な探索を行うことで、長文脈の計算負荷と注意散漫の問題を解決する。 |
| 先行研究と比べてどこがすごい？ | 従来の手法が長時間の動画をフラットなトークン列として扱うのに対し、本手法は階層的グラフメモリとエージェント推論を組み合わせることで、フルコンテキスト入力の約2%のトークン数でSOTA精度を達成。さらに、エージェントの推論能力と動画理解性能の間に正の相関があることを初めて解明した点。 |
| 技術や手法のキモはどこ？ | ストリーミング動画から「ビデオルート」「スーパーイベント」「マクロイベント」の3階層で構成されるグラフメモリを構築する点。および、Observation-Reason-Actionループに基づき、ナビゲーション、検索、グラフ探索ツールを使い分けて情報を能動的に抽出するエージェント機構。 |
| どうやって有効だと検証した？ | LVBench、LongVideoBench、Video-MME、EgoSchemaという4つの主要な長時間動画理解ベンチマークで評価。エンドツーエンドのモデルと比較して最大12.5ポイントの精度向上を実証し、さらにエージェント推論能力と動画理解性能の統計的な正の相関をAIME2025ベンチマークを用いて確認した。 |
| 議論はある？ | 長時間の動画処理における計算コストの低減や、推論プロセスの透明性向上に成功している一方、グラフメモリ構築時のセグメンテーションや構造化の精度が最終的な推論結果を左右する点。今後はより複雑な動的シナリオへの適用と、メモリ構築のさらなる効率化が課題。 |
| 次に読むべき論文は？ | [VideoAgent (Wang et al., 2024b)](https://arxiv.org/abs/2403.11976), [VideoARM (Yin et al., 2025)](https://arxiv.org/abs/2512.12360), [MemGPT (Packer et al., 2023)](https://arxiv.org/abs/2310.08560) |
| PDFリンク | https://arxiv.org/pdf/2606.07512v1 |
