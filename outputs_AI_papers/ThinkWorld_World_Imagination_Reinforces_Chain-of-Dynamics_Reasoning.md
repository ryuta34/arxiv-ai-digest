---
title: "ThinkWorld: World Imagination Reinforces Chain-of-Dynamics Reasoning"
date: 2026-10-29
arxiv_id: 2610.37666v1
url: http://arxiv.org/abs/2610.37666v1
---

# ThinkWorld: World Imagination Reinforces Chain-of-Dynamics Reasoning

| 項目 | 内容 |
|---|---|
| どんなもの？ | ロボットの動作推論を「Chain-of-Dynamics (CoD)」として定式化し、世界モデルによる未来予測を活用して強化学習を行うことで、人間とロボット双方のデータから汎用的な動作能力を学習するVLA（Vision-Language-Action）フレームワーク。 |
| 先行研究と比べてどこがすごい？ | 動作ラベルのない大量の人間ビデオデータを直接的な学習信号として活用できる点と、 embodiment（身体性）を超えた共通の動作言語（CoD）を構築することで、ロボット実機でのゼロショットおよび数ショットの汎化性能を大幅に向上させた点。 |
| 技術や手法のキモはどこ？ | アクションを離散的な「Chain-of-Dynamics」トークンとして表現し、モデルが予測した未来状態と実際の未来の観測結果が一致するかを報酬とする「World Imagination」による強化学習を導入したこと。 |
| どうやって有効だと検証した？ | 実機ロボットを用いたカラーマッチング、カップ掛け、物体仕分けタスクでの評価、およびLIBERO/LIBERO-PROベンチマークを用いたシミュレーション環境での広範な汎化性能評価により、既存手法を上回る成功率を実証。 |
| 議論はある？ | 実験は単一の乱数シードに基づいており、評価指標の変動幅についてはさらなる検証が必要。また、将来的な予測精度や計算負荷に関するさらなる最適化の余地がある。 |
| 次に読むべき論文は？ | [1] MolmoAct2 (Fang et al., 2026), [2] LIBERO-PRO (Zhou et al., 2025), [3] VLA-JEPA (Sun et al., 2026) |
| PDFリンク | https://arxiv.org/pdf/2610.37666v1 |
