---
title: "Never Look Back: Understanding Persistence in 3D Object Memory from Egocentric Videos"
date: 2026-10-09
arxiv_id: 2610.10538v1
url: http://arxiv.org/abs/2610.10538v1
---

# Never Look Back: Understanding Persistence in 3D Object Memory from Egocentric Videos

| 項目 | 内容 |
|---|---|
| どんなもの？ | エゴセントリック動画（一人称視点動画）から、時間的・空間的に持続する3Dオブジェクトのメモリを構築する手法「LEDGER」を提案した。複雑な動画から物体の位置、履歴、文脈情報を抽出・保存し、動画を再生することなく、後から行われる空間的な質問に対して正確に回答可能にした。 |
| 先行研究と比べてどこがすごい？ | 従来のメモリ手法では困難だった「物体との接触の有無に関わらない全物体の保持」「明示的な移動履歴の管理」「動画の再再生が不要なテキスト形式での効率的なクエリ回答」を可能にした点。また、HD-EPICベンチマークにおいて従来手法を大幅に上回る精度（29.7%→42.6%）を達成した。 |
| 技術や手法のキモはどこ？ | オブジェクトを「rest segments（休息セグメント）」として時系列的にクラスタリングし、物体が移動したという確実な証拠がある場合のみ記録を更新するpersistence rule（持続性ルール）を導入した点。これにより、 localization noise（位置推定ノイズ）による偽の移動検知を抑制している。 |
| どうやって有効だと検証した？ | HD-EPIC（3D知覚と物体動作）、Ego4D VQ3D（物体位置特定）、UCS-Bench（空間推論）という主要なエゴセントリック動画ベンチマークを用いて評価した。また、メモリを構成する各要素（持続性、文脈記述、三角測量など）が精度に与える影響を詳細なアブレーション研究で検証した。 |
| 議論はある？ | 非常に高密度な物体が含まれる動画では計算コストや精度の維持に課題がある。また、現在の手法はオフライン構築に限定されており、実時間でのストリーミング処理や因果的なオンラインメモリ化は今後の課題である。 |
| 次に読むべき論文は？ | [17] Ego4d: Around the world in 3,000 hours of egocentric video, [35] HD-EPIC: A highly-detailed egocentric video dataset, [49] Keep it in mind: User-centric continual spatial intelligence reasoning in egocentric video streams |
| PDFリンク | https://arxiv.org/pdf/2610.10538v1 |
