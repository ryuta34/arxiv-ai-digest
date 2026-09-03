---
title: "Graph Machine: Towards Better Pretraining via Edges"
date: 2026-09-03
arxiv_id: 2609.02881v1
url: http://arxiv.org/abs/2609.02881v1
---

# Graph Machine: Towards Better Pretraining via Edges

| 項目 | 内容 |
|---|---|
| どんなもの？ | $O(n)$サイズの状態を維持しつつ、動的でスパースなルーティングを用いて効率的に情報アクセスを行うグラフ機械（Graph Machine: GM）アーキテクチャ。Transformer層の大部分をGMスパース層に置き換えることで、精度を維持しながら計算効率を向上させている。 |
| 先行研究と比べてどこがすごい？ | 固定サイズ状態（RNN/SSM）や静的スパースルーティング（Sliding-window）と異なり、柔軟な動的アドレス指定（$\Theta(\log n)$ビット）により、モデルの複雑性を$O(n)$に保ちつつ効率的な検索を可能にした点。 |
| 技術や手法のキモはどこ？ | ポインター操作に似た「参照（Referral）」機構により、近傍ノードを再帰的に更新してエッジを生成する点。また、注意機構（Attention）と参照機構を、整数インデックスと浮動小数点重みによるグラフ構造を介して統合した点。 |
| どうやって有効だと検証した？ | Qwen3-0.6Bベースのモデルの75%の層をGMに置き換え、15.7Bトークンで事前学習を実施。KVヘッドあたりわずか2〜4個のトークン検索で、ベースラインと同等の精度を達成しつつ、学習計算コストを削減できることを示した。 |
| 議論はある？ | 現在のプロトタイプ実装では汎用的なカーネルを使用しているため、計算効率がQwen3より劣る場合がある。また、実験規模が限定的であり、長文脈へのスケーラビリティやダウンストリームタスクでの検証が今後の課題。 |
| 次に読むべき論文は？ | [1] Lintai Hou. "Graph machine: Exploring edge mechanisms as an inductive bias" (2026). [13] Gu and Dao, "Mamba: Linear-time sequence modeling with selective state spaces" (2024). [19] Yuan et al., "Native sparse attention" (2025). |
| PDFリンク | https://arxiv.org/pdf/2609.02881v1 |
