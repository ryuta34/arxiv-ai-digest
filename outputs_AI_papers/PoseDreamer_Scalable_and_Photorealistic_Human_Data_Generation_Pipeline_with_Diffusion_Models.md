---
title: "PoseDreamer: Scalable and Photorealistic Human Data Generation Pipeline with Diffusion Models"
date: 2026-03-31
arxiv_id: 2603.28763v1
url: http://arxiv.org/abs/2603.28763v1
---

# PoseDreamer: Scalable and Photorealistic Human Data Generation Pipeline with Diffusion Models

| 項目 | 内容 |
|---|---|
| どんなもの？ | 拡散モデル（Diffusion Models）を活用し、高精度な3Dメッシュアノテーションを伴う50万件以上の高品質な合成人間画像データセットを生成するパイプライン「PoseDreamer」。従来の手動アノテーションやレンダリングベースの手法に代わる、スケーラブルかつ写実的なデータ生成手法を提案している。 |
| 先行研究と比べてどこがすごい？ | 従来のレンダリング手法で見られた「合成っぽさ（ドメインギャップ）」を大幅に解消し、写実的な画像を生成できる点。また、大規模なレンダリングデータセットに匹敵または凌駕する性能を、より低コストかつ効率的に実現した点。 |
| 技術や手法のキモはどこ？ | 1. 3DメッシュをRGB画像へ変換する独自のカラーコーディング手法。2. Direct Preference Optimization (DPO) を用いた、3D制御と生成画像の整合性を高めるアライメント。3. 下流タスクの精度に基づく「カリキュラムベースのハードサンプルマイニング」と多段階フィルタリングによる高品質化。 |
| どうやって有効だと検証した？ | 複数のベンチマーク（AGORA, UBody, EgoBody, 3DPW, EHF）を用いたヒューマンメッシュ復元（HMR）モデルの評価。また、Inception ScoreとFIDによる画像品質の定量的評価や、消去実験（アブレーション研究）を行い、提案手法の各コンポーネントが寄与していることを示した。 |
| 議論はある？ | 生成画像には依然としてわずかな矛盾が生じる可能性があり、物理的に不可能な状況（浮遊など）が含まれることがある。また、基盤モデルの学習データに起因するバイアスが潜在的な課題として挙げられている。 |
| 次に読むべき論文は？ | [1] [Cai et al., "SMPLer-X: Scaling up expressive human pose and shape estimation" (NeurIPS 2024)](https://arxiv.org/abs/2309.12547) <br> [2] [Black et al., "BEDLAM: A synthetic dataset of bodies exhibiting detailed lifelike animated motion"](https://arxiv.org/abs/2305.07009) <br> [3] [Zhang et al., "EasyControl: Adding efficient and flexible control for diffusion transformer"](https://arxiv.org/abs/2503.07027) |
| PDFリンク | https://arxiv.org/pdf/2603.28763v1 |
