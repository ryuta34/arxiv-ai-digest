---
title: "OmniGameArena: A Unified UE5 Benchmark for VLM Game Agents with Improvement Dynamics"
date: 2026-06-09
arxiv_id: 2606.09826v1
url: http://arxiv.org/abs/2606.09826v1
---

# OmniGameArena: A Unified UE5 Benchmark for VLM Game Agents with Improvement Dynamics

| 項目 | 内容 |
|---|---|
| どんなもの？ | Unreal Engine 5（UE5）環境で構築された12種類のゲームを用いる、VLM（Vision-Language Model）エージェント向けの新しいベンチマーク「OmniGameArena」と、その改善プロセスを可視化する手法「Improvement Dynamics Curve (IDC)」を提案。ソロ、対戦（PvP）、協力（Coop）の3つの異なる相互作用体制を単一の環境で評価可能にする。 |
| 先行研究と比べてどこがすごい？ | 既存ベンチマークが商用タイトルの流用による学習データ汚染のリスクを抱えていたのに対し、独自開発したゲームを用いることで高い新規性を確保した。また、単発のスコア計測だけでなく、反復的な自己改善の軌跡（Improvement Dynamics Curve）を計測し、保持されたスキルが未知のタスクバリエーションへ汎化するかまでを評価できる点。 |
| 技術や手法のキモはどこ？ | エージェントが自身の試行結果を読み取り、自律的に「スキルのプロンプト」を修正する反復的な自己改善ハーネス。プロンプトを「経験ノート」「検証済みスキル」「過去のパフォーマンス（曲線）」として蓄積・管理し、パフォーマンスが急落した際にはベストな状態へロールバックする仕組みを持つ。 |
| どうやって有効だと検証した？ | 12種類のゲームで商用VLM、オープンソースVLM、専門エージェントを評価し、コールドスタート時のリーダーボードを作成。さらに上位4エージェントに対し、10ラウンドの反復改善（IDC）を行い、その過程で得られたスキルが未知のバリエーションタスクでどれだけ汎化するかを分析。 |
| 議論はある？ | 計算リソースの制約からIDC実験は2環境（LastStand/SharedFloor）に限定されている。また、エージェントと改善を行うリフレクターが同一モデルであることの影響や、単一プロンプト形式の限界についても触れており、将来的な拡張が必要である。 |
| 次に読むべき論文は？ | [Reflexion (Shinn et al., 2023)](https://arxiv.org/abs/2303.11366) や [Voyager (Wang et al., 2023)](https://arxiv.org/abs/2305.16291)、[GameVerse (Zhang et al., 2026)](https://arxiv.org/abs/2603.06656) が先行研究として挙げられる。 |
| PDFリンク | https://arxiv.org/pdf/2606.09826v1 |
