---
title: "Gamma-World: Generative Multi-Agent World Modeling Beyond Two Players"
date: 2026-05-28
arxiv_id: 2605.28816v1
url: http://arxiv.org/abs/2605.28816v1
---

# Gamma-World: Generative Multi-Agent World Modeling Beyond Two Players

| 項目 | 内容 |
|---|---|
| どんなもの？ | マルチプレイヤー環境でのインタラクティブな動画生成を可能にする、スケーラブルな生成マルチエージェント世界モデル。2人以上のプレイヤーが存在する環境において、アクションに応じた予測動画をリアルタイムで生成する。 |
| 先行研究と比べてどこがすごい？ | 従来手法（Solarisなど）が抱えていた、エージェント数の増加に伴う計算量の増大（二乗コスト）や、固定されたスロットによる順列対称性の欠如を解決。エージェント数が増えても計算コストが線形で、学習不要でスケーリング可能な点。 |
| 技術や手法のキモはどこ？ | エージェントを正規単体の頂点として符号化し、パラメータフリーかつ順列対称性を保持する「Simplex Rotary Agent Encoding」と、全対全の注意機構を避け、ハブトークン経由で情報を伝播させる「Sparse Hub Attention」。 |
| どうやって有効だと検証した？ | マルチプレイヤーのMinecraft環境（2人〜4人）および実ロボットの協調タスクで検証。FVDやFID等の評価指標において従来手法を上回る性能を示し、4人プレイヤー環境へのゼロショット転移の有効性も確認した。 |
| 議論はある？ | 現在はゲームやロボット制御に焦点が当たっており、より複雑で異質な環境での汎用性は今後の課題。また、大規模なエージェント群への対応や、3D幾何学的な厳密な物理拘束の欠如による長期間での不整合の蓄積が限界として挙げられる。 |
| 次に読むべき論文は？ | [Solaris: Building a multiplayer video world model in minecraft](https://arxiv.org/abs/2602.22208)、[Diffusion forcing: Next-token prediction meets full-sequence diffusion](https://arxiv.org/abs/2407.01414) |
| PDFリンク | https://arxiv.org/pdf/2605.28816v1 |
