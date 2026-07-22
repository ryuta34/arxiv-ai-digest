---
title: "ExpertVerse: A General-Purpose Benchmark for Expert-Level Reasoning in Knowledge-Intensive Visual Synthesis"
date: 2026-07-22
arxiv_id: 2607.19341v1
url: http://arxiv.org/abs/2607.19341v1
---

# ExpertVerse: A General-Purpose Benchmark for Expert-Level Reasoning in Knowledge-Intensive Visual Synthesis

| 項目 | 内容 |
|---|---|
| どんなもの？ | 知識集約的な視覚合成タスクにおけるモデルの推論能力を評価するためのベンチマーク「ExpertVerse」と、それに基づき学習された推論エンジン「KnowThinker」を提案した論文。9つの認知能力と8つの専門分野を網羅し、高精度な推論と命令追従を可能にする。 |
| 先行研究と比べてどこがすごい？ | 既存のベンチマークが主に単純な常識推論や単一タスクに限定されていたのに対し、58のサブカテゴリからなる広範なタスク構成と、思考プロセス（CoT）を伴う体系的な評価を導入した点。また、オープンソースモデルとしてSOTAを大幅に更新した点。 |
| 技術や手法のキモはどこ？ | 推論エンジンと視覚生成エンジンを分離する「Thinker-centric」な学習パラダイムの採用と、マルチタスク学習における報酬の不整合や勾配衝突を解決する強化学習アルゴリズム「BPPO（Bootstrapped Pareto Policy Optimization）」を提案した点。 |
| どうやって有効だと検証した？ | ExpertVerseベンチマークに加え、RISEBench、KRISBench、UniREditBench、WiseEdit等の既存ベンチマークを用いた広範な評価を実施。KnowThinkerがプロプライエタリなモデル（NanoBanana-Pro等）に匹敵する性能を達成することを示した。 |
| 議論はある？ | 現在のモデルの限界は、主に凍結された視覚エディタの制限によるものであり、純粋な計画不足ではない可能性を示唆している。また、知識集約的なタスクにおけるHallucination（幻覚）の抑制が依然として重要課題である。 |
| 次に読むべき論文は？ | [RISEBench (Zhao et al. 2026)](https://arxiv.org/abs/2607.19341v1), [KRISBench (Wu et al. 2026)](https://arxiv.org/abs/2607.19341v1), [UniREditBench (Han et al. 2025)](https://arxiv.org/abs/2607.19341v1) ※いずれも論文内引用文献 |
| PDFリンク | https://arxiv.org/pdf/2607.19341v1 |
