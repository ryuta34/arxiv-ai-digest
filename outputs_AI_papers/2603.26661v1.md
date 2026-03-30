---
title: "GaussianGPT: Towards Autoregressive 3D Gaussian Scene Generation"
date: 2026-03-30
arxiv_id: 2603.26661v1
url: http://arxiv.org/abs/2603.26661v1
---

# GaussianGPT: Towards Autoregressive 3D Gaussian Scene Generation

| 項目 | 内容 |
|---|---|
| どんなもの？ | 3D Gaussian Splattingを用いた室内シーン生成・補完・編集を行うための、完全自己回帰型のトランスフォーマーモデル「GaussianGPT」。3Dシーンを離散的なトークン列として扱い、次トークン予測によって段階的な空間生成を実現する。 |
| 先行研究と比べてどこがすごい？ | 従来の拡散モデルやフローマッチングによるホリスティック（全体的）な生成手法に対し、自己回帰的な順次生成を行うことで、シーンの増分生成、部分的な補完、および固定訓練サイズを超えた無限の空間アウトペインティングが自然かつ柔軟に可能になった点。 |
| 技術や手法のキモはどこ？ | Sparse 3D CNNを用いた特徴グリッドの圧縮・ベクトル量子化による「シーンのトークン化」と、3Dの空間関係を維持するための「3D Rotary Positional Embedding (RoPE)」を導入した点。位置トークンと特徴トークンを交互に予測することで、空間構造と見栄えのモデリングを分離している。 |
| どうやって有効だと検証した？ | PhotoShapeデータセットを用いた椅子（オブジェクト）の生成評価（FID, KID, COV, MMD指標）に加え、3D-FRONTおよびASEデータセットを用いた室内シーンの生成・補完・アウトペインティングの質的評価を実施。従来手法と比較して、幾何学的な整合性と多様性の両立を示した。 |
| 議論はある？ | 現在のオートエンコーダーの再構成能力が実世界データでは限界となる点や、局所的な制約内での生成に限られている点がある。将来課題として、実世界データにおける不確実性の明示的なモデリングや、より広域な長期生成の安定化が挙げられている。 |
| 次に読むべき論文は？ | [L3DG: Latent 3D Gaussian Diffusion](https://arxiv.org/abs/2410.13530)、[SceneScript: Reconstructing Scenes With An Autoregressive Structured Language Model](https://arxiv.org/abs/2403.13064)、[Point Transformer V3](https://arxiv.org/abs/2312.10035) |
| PDFリンク | https://arxiv.org/pdf/2603.26661v1 |
