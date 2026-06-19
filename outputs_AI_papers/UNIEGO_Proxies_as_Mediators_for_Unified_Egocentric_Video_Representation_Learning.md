---
title: "UNIEGO: Proxies as Mediators for Unified Egocentric Video Representation Learning"
date: 2026-06-19
arxiv_id: 2606.20559v1
url: http://arxiv.org/abs/2606.20559v1
---

# UNIEGO: Proxies as Mediators for Unified Egocentric Video Representation Learning

| 項目 | 内容 |
|---|---|
| どんなもの？ | 視点（エゴ/エキソ）、モダリティ（RGB/深度/スケルトン）、基盤モデルといった異種混合の教師情報を統合し、推論時にはエゴ中心の動画のみで高精度な理解を可能にする統一的なエゴ中心動画表現学習フレームワーク「UNIEGO」を提案。 |
| 先行研究と比べてどこがすごい？ | 異種教師間の「表現ギャップ」と「競合する勾配」という課題を、中間的なプロキシモデルと選択的蒸留（SPD）により解決し、既存の多教師蒸留ベースラインを大幅に上回る性能を達成した点。 |
| 技術や手法のキモはどこ？ | (1) 異種教師の知識を同種のプロキシモデルに変換する「Proxy Learning」、(2) 信頼できるプロキシのみを選択的に蒸留する「Selective Proxy Distillation (SPD)」、(3) 損失空間の平坦な領域へモデルを導く「Proxy Merging Initialization」。 |
| どうやって有効だと検証した？ | EgoExo-Fitness、Assembly101、EgoExo4Dという3つのベンチマークを用い、アクション認識、ビデオ検索、アクションセグメンテーションの3タスクでSOTAを達成。また、複数のバックボーンでの汎用性も確認。 |
| 議論はある？ | 現在は「小損失」というヒューリスティックな基準でプロキシを選択しているが、より動的で学習状態や入力に依存した適応的な選択メカニズムの構築が今後の課題である。 |
| 次に読むべき論文は？ | [EgoExo4D (Grauman et al., 2024)](https://arxiv.org/pdf/2405.02528)や、マルチ教師蒸留の先行例として[AM-RADIO (Ranzinger et al., 2024)](https://arxiv.org/pdf/2312.06649)が挙げられる。 |
| PDFリンク | https://arxiv.org/pdf/2606.20559v1 |
