---
title: "Persistent Visual Memory: Sustaining Perception for Deep Generation in LVLMs"
date: 2026-05-04
arxiv_id: 2605.00814v1
url: http://arxiv.org/abs/2605.00814v1
---

# Persistent Visual Memory: Sustaining Perception for Deep Generation in LVLMs

| 項目 | 内容 |
|---|---|
| どんなもの？ | 大規模視覚言語モデル（LVLM）の長時間生成時に発生する「視覚信号の希釈（Visual Signal Dilution）」問題を解決する、Persistent Visual Memory (PVM) というモジュールを提案する研究。推論中も視覚情報を動的かつ持続的に取得できるようにする。 |
| 先行研究と比べてどこがすごい？ | 既存の視覚注入手法（raw tokenの挿入等）が引き起こす「逐次的干渉」を避け、標準的なTransformerのアーキテクチャを維持しつつ、視覚情報へのアクセスを独立した並列経路に分離することで、文脈長が長くなっても精度の低下を大幅に抑制した点。 |
| 技術や手法のキモはどこ？ | TransformerのFFNと並列に「Looking Path（PVMブランチ）」を配置し、視覚エンコーダーから抽出された埋め込みに対して専用のクロスアテンションを行う点。また、独立した正規化により、増大するテキスト履歴による確率分布の希釈を構造的に回避した点。 |
| どうやって有効だと検証した？ | 8つのマルチモーダルベンチマーク（MMMU、MMBench、MathVerse等）で評価し、Qwen3-VL-8Bおよび4Bモデルにおいてベースラインを大きく上回る性能（8Bで+4.8%、4Bで+4.4%）を達成。また、LogitLensを用いた分析で予測収束の加速を確認した。 |
| 議論はある？ | 現在の理論的保証は「固定された局所クエリ」という仮定に基づいている点や、評価対象がQwen3-VLシリーズに限定されている点。今後はより広範なアーキテクチャへの適用や、長時間の動的ストリーミング動画理解への拡張が課題。 |
| 次に読むべき論文は？ | [1] DeepStack (Meng et al., 2024), [2] MemVR (Zou et al., 2024), [3] Qwen3-VL Technical Report (Bai et al., 2025) |
| PDFリンク | https://arxiv.org/pdf/2605.00814v1 |
