---
title: "Can 4D Foundation Models Remember?"
date: 2026-09-18
arxiv_id: 2609.20819v1
url: http://arxiv.org/abs/2609.20819v1
---

# Can 4D Foundation Models Remember?

| 項目 | 内容 |
|---|---|
| どんなもの？ | 4D基盤モデルの「視覚的記憶能力」を定量的に評価するための新しいベンチマーク「PERSISTBENCH」を提案した研究。物体が視野から外れた後も、モデルがその存在、動き、外見を正しく記憶・再現できているかを評価する。 |
| 先行研究と比べてどこがすごい？ | 従来の評価手法はレンダリングの忠実度（PSNR等）のみに焦点を当てていたが、本研究は現実世界の360度動画をオムニシエント（全知）な正解データとして活用し、物体中心の記憶能力を明確に切り出して評価できる点。 |
| 技術や手法のキモはどこ？ | 360度動画から「入力用（物体が途中で消える）」と「正解参照用（物体が見え続ける）」のペアを生成するデータ構築パイプラインと、物体存在（Object Permanence）、運動連続性（Motion Continuity）、外見保持（Appearance Preservation）を評価する3つの指標。 |
| どうやって有効だと検証した？ | 12種類の主要な4D再構築および動画生成モデルに対し、PERSISTBENCHを用いて評価。その結果、すべてのモデルが視野外では性能が大幅に低下することを明らかにし、モデルの記憶能力の欠如を定量的に示した。 |
| 議論はある？ | 現在のモデルは対象が連続的に見える動画での学習に偏っており、記憶のための監督信号が不足していると指摘。今後は閉塞（オクルージョン）を伴うデータの学習や、明示的な幾何学的制約を導入したアーキテクチャの開発が重要となる。 |
| 次に読むべき論文は？ | [16] WorldScore: A unified evaluation benchmark for world generation. (ICCV 2025) / [48] Out of sight, out of mind? evaluating state evolution in video world models. (arXiv 2026) |
| PDFリンク | https://arxiv.org/pdf/2609.20819v1 |
