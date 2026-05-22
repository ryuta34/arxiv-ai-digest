---
title: "Which Way Did It Move? Diagnosing and Overcoming Directional Motion Blindness in Video-LLMs"
date: 2026-05-22
arxiv_id: 2605.22823v1
url: http://arxiv.org/abs/2605.22823v1
---

# Which Way Did It Move? Diagnosing and Overcoming Directional Motion Blindness in Video-LLMs

| 項目 | 内容 |
|---|---|
| どんなもの？ | Video-LLMが「右」「左」といった基本的な動作方向の認識に失敗する現象（方向性動作盲目）を特定・診断し、それを解消する手法DeltaDirectを提案した論文。方向信号はモデル内部に存在するが、最終的な回答選択肢と結びつかない「方向結合ギャップ」というボトルネックを解明した。 |
| 先行研究と比べてどこがすごい？ | 従来のモデルが視覚的な色や物体の認識は高い一方で、動作方向にはランダムに近い精度しか出せない問題を初めて系統的に分析した点。また、推論時の計算コストを増やさず、学習時のみの補助タスクによって動作方向の理解を劇的に向上させた点。 |
| 技術や手法のキモはどこ？ | プロジェクターの出力に対し、隣接フレーム間の特徴量の差分（デルタ）から2D動作ベクトルを予測する補助損失（DeltaDirect）を導入したこと。これにより、特定の動作方向信号をモデル内部で強め、最終的な言語回答との「結合」を最適化したこと。 |
| どうやって有効だと検証した？ | 制御された合成動画データセットMODIRECTと、実動画ベンチマークMODIRECT-REALBENCHを用いて検証。 instruction tuning（指示チューニング）だけでは解決しなかったOOD（未知ドメイン）への汎化性能が、DeltaDirectによって大幅に向上（21.9ポイント向上）することを確認した。 |
| 議論はある？ | 提案手法は2D平面上の動作には有効だが、奥行き方向の動き、回転、加速度、非剛体変形などは対象外。また、学習に用いた合成データに依存しており、より複雑な現実世界の動的なシーケンスへの完全な適用には、追跡技術や擬似ラベルが必要となる可能性がある。 |
| 次に読むべき論文は？ | [LLaVA-Video](https://arxiv.org/abs/2501.13106) / [MotionBench](https://arxiv.org/abs/2504.14815) / [Map the flow](https://arxiv.org/abs/2602.04351) |
| PDFリンク | https://arxiv.org/pdf/2605.22823v1 |
