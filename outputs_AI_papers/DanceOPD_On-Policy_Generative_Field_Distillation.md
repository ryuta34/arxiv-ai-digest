---
title: "DanceOPD: On-Policy Generative Field Distillation"
date: 2026-06-26
arxiv_id: 2606.27377v1
url: http://arxiv.org/abs/2606.27377v1
---

# DanceOPD: On-Policy Generative Field Distillation

| 項目 | 内容 |
|---|---|
| どんなもの？ | 複数の生成能力（テキストからの画像生成、局所的・広域的な画像編集など）を単一モデルに統合するための、オンポリシー生成フィールド蒸留フレームワーク「DanceOPD」。凍結された複数の専門家モデルを「速度フィールド」として扱い、学生モデルに効率的に学習させる手法。 |
| 先行研究と比べてどこがすごい？ | 従来の手法（データ混合やパラメータマージ）で見られた能力間の干渉を抑制し、ターゲット能力を強化しつつベースの生成品質を維持できる点。また、計算コストを抑えながら、複数の生成能力を高品質に合成できる。 |
| 技術や手法のキモはどこ？ | 1. 複数のフィールドをサンプルごとに厳密に振り分ける「ハードルーティング」、2. 学生モデルのロールアウト軌道上の状態を活用する「オンポリシー・クエリ」、3. 相関を避けるための「低ノイズ領域での単一クエリ」の3点。 |
| どうやって有効だと検証した？ | Z-ImageおよびSD3.5-Mを用い、T2Iと編集能力の合成、リアルリズム（品質）フィールドの吸収、CFG（分類器フリーガイダンス）の内部化などのタスクで評価。GEditBenchやGenEval等の指標で既存の蒸留手法を上回る性能を実証した。 |
| 議論はある？ | 現在の実装は事前に定義された機能バケットに基づくルーティングに依存している。タスク境界が曖昧な場合や、複数の能力が複雑に絡むプロンプトへの対応には、動的なベリファイアや報酬モデルによるルーティングの拡張が今後の課題。 |
| 次に読むべき論文は？ | [1] [On-policy distillation of language models: Learning from self-generated mistakes](https://arxiv.org/abs/2404.09549), [24] [Flow-OPD: On-policy distillation for flow matching models](https://arxiv.org/abs/2605.08063), [53] [DiffusionOPD: A unified perspective of on-policy distillation in diffusion models](https://arxiv.org/abs/2605.15055) |
| PDFリンク | https://arxiv.org/pdf/2606.27377v1 |
