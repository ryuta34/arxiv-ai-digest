---
title: "Marionette: Predicting World States, Rendering Geometry, Painting Appearance"
date: 2026-08-17
arxiv_id: 2608.14530v1
url: http://arxiv.org/abs/2608.14530v1
---

# Marionette: Predicting World States, Rendering Geometry, Painting Appearance

| 項目 | 内容 |
|---|---|
| どんなもの？ | 複雑なゲーム世界において、物理的に整合性のある明示的な「世界状態」を予測し、確定的なレンダラーを経由して高品質な映像を生成するゲーム世界モデル「Marionette」を提案。 |
| 先行研究と比べてどこがすごい？ | ピクセル空間で直接生成する従来手法とは異なり、幾何学や閉塞関係を確定的な演算で計算することで、長期的な整合性とユーザーによる直接的な操作性を両立させた点。 |
| 技術や手法のキモはどこ？ | 学習不要の確定的なグラフィックスブリッジ（zero-parameter renderer）を導入し、ニューラルモデルが「外見（見た目）」の生成に専念し、モデルの演算が「世界状態（物理構成）」の予測に特化する構成。 |
| どうやって有効だと検証した？ | 商用アクションゲームのデータセットを用い、強制的なアクション入力による操作性の検証、および地形コリジョン等のルール適用による長期的な物理破綻（地面貫通や乖離）の抑制を実験的に証明。 |
| 議論はある？ | 長期生成における「外見」の維持は依然として拡散モデルの記憶に依存しており、出現頻度の低いエンティティの再現や、生成ポーズと学習データの分布乖離が課題。 |
| 次に読むべき論文は？ | [ARDY: Autoregressive diffusion with hybrid representation for interactive human motion generation](https://arxiv.org/abs/2607.08741) |
| PDFリンク | https://arxiv.org/pdf/2608.14530v1 |
