---
title: "Reroute, Don't Remove: Recoverable Visual Token Routing for Vision-Language Models"
date: 2026-06-11
arxiv_id: 2606.12412v1
url: http://arxiv.org/abs/2606.12412v1
---

# Reroute, Don't Remove: Recoverable Visual Token Routing for Vision-Language Models

| 項目 | 内容 |
|---|---|
| どんなもの？ | 視覚言語モデル（VLM）において、デコーダーの視覚トークン削減を「不可逆的な剪定」ではなく、「再利用可能なルーティング」として再定義する手法「Reroute」を提案した。訓練不要のプラグインとして、従来の削減手法と計算コストを維持しつつ、後続の層で必要なトークンを復帰させることで精度を向上させる。 |
| 先行研究と比べてどこがすごい？ | 従来の「rank-and-remove（スコア順に選んで捨てる）」パラダイムは、初期層で重要でないと判断されたトークンが深層で重要になるケースに対処できず、 groundingの崩壊を招いていた。Rerouteは学習不要かつ追加パラメーターなしでこの irrecoverability（不可逆性）を解決し、 aggressiveな削減環境下でも grounding精度を大幅に改善した。 |
| 技術や手法のキモはどこ？ | 各ステージで「選択されたトークン」のみにAttn+FFNを適用し、「延期されたトークン」は削除せずにバイパス（残差接続）させることで、次ステージの候補プールに再エントリーさせる仕組み。既存手法のランキングルールをそのまま流用するため、計算コスト（FLOPsやKVキャッシュ）を増大させない。 |
| どうやって有効だと検証した？ | LLaVA-1.5、Qwen2.5-VL、Qwen3.5-9B-Hybrid等の複数のバックボーンと、FastVやPDrop等の主要な削減手法に対して適用。RefCOCO-seriesでのgrounding精度向上と、VQAにおける汎用的な視覚推論能力が維持されることを広範なベンチマークで確認した。 |
| 議論はある？ | スコアリング手法の性能に依存するため、ランキングが著しく悪い場合は改善が限定的になる。効率的な実装にはGather/ScatterカーネルとKVキャッシュの最適化が不可欠である点、およびハイブリッドモデル（Qwen3.5など）における線形アテンションとの相互作用については将来的な詳細解析が必要。 |
| 次に読むべき論文は？ | [12] Chen et al., "An image is worth 1/2 tokens after layer 2", ECCV 2024 / [71] Xing et al., "Pyramiddrop: Accelerating your large vision-language models via pyramid visual redundancy reduction" / [56] Raposo et al., "Mixture-of-depths: Dynamically allocating compute in transformer-based language models" |
| PDFリンク | https://arxiv.org/pdf/2606.12412v1 |
