---
title: "BRDFusion: Physics Meets Generation for Urban Scene Inverse Rendering"
date: 2026-06-16
arxiv_id: 2606.17049v1
url: http://arxiv.org/abs/2606.17049v1
---

# BRDFusion: Physics Meets Generation for Urban Scene Inverse Rendering

| 項目 | 内容 |
|---|---|
| どんなもの？ | 都市シーンの動的な動画から、高品質な3D形状・素材・HDR照明を分離抽出する物理ベースの逆レンダリング手法。物理シミュレーションの制御性と生成AIモデルのフォトリアリズムを融合させたフレームワーク。 |
| 先行研究と比べてどこがすごい？ | 物理ベースの手法に特有のノイズやアーティファクトを、生成AIを用いたデノイザーで解消するハイブリッド構成を実現。これにより、高品質な動画生成と、照明や物体挿入に対する精緻な制御を両立している点。 |
| 技術や手法のキモはどこ？ | 3D Gaussian Splattingを用いたシーン表現に対し、物理ベースのレンダリング（PBR）パスと、生成モデル（SDEdit）による精緻化パスを段階的に適用する最適化パイプライン。また、生成モデルをトレーニング時にも組み込み、幾何学的および素材的に一貫した出力を得ている。 |
| どうやって有効だと検証した？ | Waymo Open Datasetなどの実データおよび合成データを用いて、既存手法（UrbanIR, InvRGB+L, Gen3C+DR）との比較実験を実施。PSNRやSSIM等の指標での定量的評価に加え、 relighting（再照明）や物体挿入の視覚的品質を比較評価した。 |
| 議論はある？ | 夜間シーケンスにおける emissive（発光）素材の明示的なモデリングが未対応であり、未観測領域における「floaters（浮遊物）」や物理的な不整合が残るケースがある点を限界として挙げている。 |
| 次に読むべき論文は？ | [45] Liang et al., "DiffusionRenderer: Neural inverse and forward rendering with video diffusion models." (CVPR 2025) および [40] Kerbl et al., "3d gaussian splatting for real-time radiance field rendering." (ACM Trans. Graph. 2023) |
| PDFリンク | https://arxiv.org/pdf/2606.17049v1 |
