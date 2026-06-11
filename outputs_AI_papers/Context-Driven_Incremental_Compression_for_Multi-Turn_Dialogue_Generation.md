---
title: "Context-Driven Incremental Compression for Multi-Turn Dialogue Generation"
date: 2026-06-11
arxiv_id: 2606.12411v1
url: http://arxiv.org/abs/2606.12411v1
---

# Context-Driven Incremental Compression for Multi-Turn Dialogue Generation

| 項目 | 内容 |
|---|---|
| どんなもの？ | 長期にわたるマルチターン対話において、対話履歴をインタラクティブなコンテキストスレッドとして効率的に圧縮・更新するフレームワーク「C-DIC」を提案した。対話履歴全体を保持するコストを抑えつつ、長期間の対話でも高い一貫性と正確性を維持することを目指している。 |
| 先行研究と比べてどこがすごい？ | 従来の手法（単純な切り捨てや静的な要約）では情報の損失や文脈の断絶が発生し、静的なlatent圧縮では連続的な更新（Revision）ができないという課題があった。C-DICは、Retrieve→Revise→Write-backのループを通じて情報を動的に更新可能にし、数百ターンにわたる対話でも安定した推論と高い長距離整合性を実現した点。 |
| 技術や手法のキモはどこ？ | 会話を「インターリーブされた文脈スレッド」と捉え、圧縮状態を固定的な要約ではなく「更新可能なメモリ」として扱う点。また、勾配を使用しないメモリ更新ルールと、 retrieval-awareなTruncated BPTTを用いて、全履歴を再エンコードせずに学習と推論を行えるようにした点。 |
| どうやって有効だと検証した？ | Multi-Session Chat (MSC) および REALTALK データセットを用い、パープレキシティ（PPL）、BLEU、ROUGEなどの指標で評価。さらに、長距離依存性を検証するための診断用タスク（MSC-QA）や、長期間対話での推論レイテンシ測定を行い、他手法と比較して高い精度と効率性を実証した。 |
| 議論はある？ | メモリのスロット数が対話の進展に伴い増加する可能性がある点や、学習済み圧縮モデルの初期値に依存する点。また、 latentメモリが機密情報を含む場合があり、単純な削除が困難であるため、適切なプライバシー対策が必要であると述べている。 |
| 次に読むべき論文は？ | [In-context autoencoder for context compression in a large language model](https://arxiv.org/abs/2307.06945), [Llms get lost in multi-turn conversation](https://arxiv.org/abs/2505.06120), [MemGPT: Towards LLMs as Operating Systems](https://arxiv.org/abs/2310.08560) |
| PDFリンク | https://arxiv.org/pdf/2606.12411v1 |
