---
title: "MemoryVLA++: Temporal Modeling via Memory and Imagination in Vision-Language-Action Models"
date: 2026-06-09
arxiv_id: 2606.09827v1
url: http://arxiv.org/abs/2606.09827v1
---

# MemoryVLA++: Temporal Modeling via Memory and Imagination in Vision-Language-Action Models

| 項目 | 内容 |
|---|---|
| どんなもの？ | ロボット操作のためのビジョン・言語・アクション（VLA）モデル「MemoryVLA++」を提案。過去の記憶を保持するエピソード記憶と、未来の状態を予測する世界モデルによる想像を統合し、長期的な推論が必要なタスクを効率的にこなすフルタイムスタンプモデリングフレームワーク。 |
| 先行研究と比べてどこがすごい？ | 従来のVLAは現在時点の観測のみに依存するため長期タスクに弱かった。本手法は過去の経験を冗長性を排除して圧縮保存する記憶バンクと、計算コストを抑えた潜在空間での未来予測（想像）を組み合わせ、高い効率と精度で長期・複雑なタスクを成功させる点。 |
| 技術や手法のキモはどこ？ | 「知覚・認知記憶バンク」により過去の決定に関連する文脈を検索・統合する点と、Stable Video Diffusionを操作タスク向けに調整し、潜在空間で部分的なデノイジングを行うことで未来を予測し、それを記憶でガイドしながら統合する点。 |
| どうやって有効だと検証した？ | Libero、SimplerEnv、Mikasa-Robo、Calvin、Libero-Plus等の5つのシミュレーションベンチマークおよび、3種類のロボットを用いた実機実験（一般操作、長期メモリ依存タスク、長期想像依存タスク）で検証。ベースラインに対して大幅な成功率向上を達成。 |
| 議論はある？ | ワールドモデルの予測における決定に無関係なノイズの抑制や、限られた計算リソースでの効率的な運用が課題。また、より強力なVLMバックボーン（Qwen2.5等）の活用によるさらなる性能向上の余地がある。 |
| 次に読むべき論文は？ | [1] OpenVLA [https://arxiv.org/abs/2406.03844] <br> [2] CogACT [https://arxiv.org/abs/2411.19650] <br> [3] MemoryVLA [https://arxiv.org/abs/2508.19236] |
| PDFリンク | https://arxiv.org/pdf/2606.09827v1 |
