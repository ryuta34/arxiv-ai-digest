---
title: "CoinRAG: Contextualized Information Nugget KV Cache Reuse for Long-Context RAG"
date: 2026-08-10
arxiv_id: 2608.07458v1
url: http://arxiv.org/abs/2608.07458v1
---

# CoinRAG: Contextualized Information Nugget KV Cache Reuse for Long-Context RAG

| 項目 | 内容 |
|---|---|
| どんなもの？ | RAG（検索拡張生成）における推論コストと遅延を削減するための、情報ナゲット（重要文節）ベースのKVキャッシュ再利用フレームワーク。あらかじめ抽出した細粒度なテキストナゲットをオフラインでキャッシュし、推論時にクエリに関連するものを動的に組み合わせて利用する手法。 |
| 先行研究と比べてどこがすごい？ | 従来のチャンク単位のKVキャッシュ再利用に比べ、よりコンパクトで高密度な情報ナゲットを利用することで、推論時のプレフィル遅延を大幅に削減しつつ、精度を向上（平均5.3%のF1改善）させた点。 |
| 技術や手法のキモはどこ？ | テキストチャンクから重要情報を「ナゲット」としてオフライン抽出し、それに対応するKVキャッシュを切り出して再利用する点。さらに、異なるチャンク由来のキャッシュを連結する際の「位置アラインメント（Position Alignment）」と、ナゲット特化型のファインチューニングで精度を担保している点。 |
| どうやって有効だと検証した？ | LongBenchのマルチホップQAデータセット（HotpotQA, 2WikiMQA, MuSiQue）を用い、P99のTTFT（Time-to-First-Token）100ms以下の制約下で、Standard RAGやCacheBlend、TurboRAG等のベースラインと比較評価を行った。 |
| 議論はある？ | オフラインでの事前処理にコストがかかること、モデルアーキテクチャの変更に伴い再エンコードが必要になる点、および検索が失敗した場合はモデルの推論品質が低下するリスクがあることを認めている。 |
| 次に読むべき論文は？ | [TurboRAG (Lu et al., 2025)](https://arxiv.org/abs/2502.16002), [CacheBlend (Yao et al., 2025)](https://arxiv.org/abs/2502.16002), [KVLink (Yang et al., 2025)](https://arxiv.org/abs/2502.16002) |
| PDFリンク | https://arxiv.org/pdf/2608.07458v1 |
