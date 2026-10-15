---
title: "Hierarchical Residual Policy Learning for Real-World Mobile Manipulation with Sparse Human Guidance"
date: 2026-10-15
arxiv_id: 2610.20607v1
url: http://arxiv.org/abs/2610.20607v1
---

# Hierarchical Residual Policy Learning for Real-World Mobile Manipulation with Sparse Human Guidance

| 項目 | 内容 |
|---|---|
| どんなもの？ | 実世界のモバイルマニピュレーション（MoMa）において、事前学習済みポリシーを効率的に微調整するためのフレームワーク「HiRe-MoMa」の提案。複雑なロボットシステムの階層構造を活用し、少量の人的介入と強化学習を組み合わせることで、短時間での適応を可能にする。 |
| 先行研究と比べてどこがすごい？ | モバイルベースとマニピュレーター間の結合による勾配干渉問題を解決し、アーキテクチャに依存しない汎用的な微調整を実現した点。特に、25〜40分という短時間のオンライン学習で性能を大幅に向上させ、実機でのサンプル効率と安定性を両立した。 |
| 技術や手法のキモはどこ？ | 1. **Hierarchical Decoupling**: モバイルベースとアームを独立したresidualポリシーに分割し、単方向条件付けで物理的階層を模倣。2. **Expert-Guided Value Alignment**: 少量の人的介入をポリシーの模倣ではなく、評価関数（Critic）の価値地形を専門家の好みに合わせるための補助損失として利用する点。 |
| どうやって有効だと検証した？ | TIAGo++プラットフォームを用い、「Place Only」「Sweep Litter」「Pick Place」の3つのタスクで実験。Diffusion PolicyとACTの2つの異なるベースポリシーに対して、成功率の向上とエピソード長の短縮を確認し、各コンポーネントの有効性をアブレーションスタディで実証した。 |
| 議論はある？ | 現在は空間的な階層のみを考慮しており、時間的な階層性は未解決。また、人的介入による学習バイアスや、特定のハードウェア制限に依存する部分がある。今後はマルチモーダルセンサーの統合や、より深い階層構造への拡張が課題。 |
| 次に読むべき論文は？ | [Luo et al., "Precise and dexterous robotic manipulation via human-in-the-loop reinforcement learning" (2025)](https://arxiv.org/abs/2505.02271) および [Jiang et al., "TRANSIC: Sim-to-real policy transfer by learning from online correction" (2025)](https://arxiv.org/abs/2403.04859) |
| PDFリンク | https://arxiv.org/pdf/2610.20607v1 |
