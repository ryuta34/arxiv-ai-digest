---
title: "MintAct: A Unified Visual Agent for Digital Environments"
date: 2026-09-21
arxiv_id: 2609.22083v1
url: http://arxiv.org/abs/2609.22083v1
---

# MintAct: A Unified Visual Agent for Digital Environments

| 項目 | 内容 |
|---|---|
| どんなもの？ | モバイル、デスクトップ、Web、ツール利用という複数のデジタル環境における操作を、単一の軽量なモデル（2B/4B/8B）で統合的に実現する視覚言語エージェント「MintAct」。環境構築、データ生成、学習レシピを統合することで、各ドメイン特化型モデルと同等以上の性能を達成している。 |
| 先行研究と比べてどこがすごい？ | 個別のドメイン（UI操作、ナビゲーション、ツール利用）ごとにモデルが断片化されていた課題に対し、単一モデルでこれら全てを汎用的に扱える点。また、非同期RL（強化学習）フレームワークにより、異種環境が混在する中でも安定した学習と高いスループットを実現した点。 |
| 技術や手法のキモはどこ？ | ①GUI操作におけるドメイン共通の「共通観測・接地空間」の設定。②ドメイン固有のプロンプトを用いた「プロンプト条件付きアクションセット」。③非同期RLによる効率的な学習と、計算資源を最適化する「クォータベースのデータ混合制御」の導入。 |
| どうやって有効だと検証した？ | OSWorld、AndroidWorld、Weblica、MM-ToolSandBox等の主要ベンチマークで評価。MintAct-8BがOSWorld-Verifiedで48.9、Online-Mind2Webで39.1、AndroidWorldで67.0という最高水準のスコアを記録し、ドメイン統合による性能劣化がないことを証明した。 |
| 議論はある？ | 現在は「環境操作」と「動的なツール利用」が分離しており、状況に応じた自動的な切り替えが課題。また、長期的な対話履歴の蓄積によるコンテキスト長とメモリ消費の増大が将来的なスケールアップの制約となる。 |
| 次に読むべき論文は？ | [OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments](https://arxiv.org/abs/2404.07972), [AsyncWebRL: Efficient Multi-step RL for Visual Web Agents](https://arxiv.org/abs/2606.05597), [MM-ToolSandBox: A Unified Framework for Evaluating Visual Tool-Calling Agents](https://arxiv.org/abs/2607.11818) |
| PDFリンク | https://arxiv.org/pdf/2609.22083v1 |
