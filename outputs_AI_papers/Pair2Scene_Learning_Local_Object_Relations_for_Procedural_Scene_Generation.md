---
title: "Pair2Scene: Learning Local Object Relations for Procedural Scene Generation"
date: 2026-04-14
arxiv_id: 2604.11808v1
url: http://arxiv.org/abs/2604.11808v1
---

# Pair2Scene: Learning Local Object Relations for Procedural Scene Generation

| 項目 | 内容 |
|---|---|
| どんなもの？ | 複雑で高密度な3D室内シーンを、物体間の局所的な関係性（物理的サポート関係と機能的意味関係）に基づいて段階的に生成するフレームワーク「Pair2Scene」。シーン全体を一度にモデリングするのではなく、近傍物体との関係ルールを学習・推論することで、学習データの分布を超えた複雑でリアルな環境生成を可能にする。 |
| 先行研究と比べてどこがすごい？ | 従来手法（エンドツーエンドの学習やLLM/VLMガイド）が抱えていた、データ不足による生成能力の限界や、物体数増加に伴うモデルの複雑化、空間推論精度の低さを克服。局所的なルールベースの分解アプローチにより、学習データ以上の複雑なシーン生成においても高い物理的・意味的妥当性を維持できる点。 |
| 技術や手法のキモはどこ？ | 物体配置を「サポート関係（物理的重心）」と「機能的関係（意味的リンク）」に分解してモデル化し、これを学習するための「3D-Pairsデータセット（約14万件）」を構築したこと。さらに、Transformerベースの「Geometry-Aware Layout Predictor」による局所確率分布の予測と、物理シミュレーションを統合した「衝突回避型リジェクションサンプリング」を組み合わせた生成プロセス。 |
| どうやって有効だと検証した？ | 3D-Frontデータセットを用いた「fitting（学習分布再現）」と「beyond（分布外の複雑化）」の両設定で定量・定性評価を実施。既存手法（ATISS, DiffuScene, FactoredScenes, LayoutVLM等）と比較し、FID/KIDスコアおよび22名の被験者によるユーザースタディ（意味的整合性、物理的妥当性、複雑さ）で優位性を実証した。 |
| 議論はある？ | 空間的な関係性には強いが、物体個々の様式（スタイル）の整合性を保証する機能はない。また、複数のアンカーを必要とする複雑なケースや、吊り下げ物などの稀な関係性に対する対応には限界があり、今後の課題としている。 |
| 次に読むべき論文は？ | [ATISS](https://arxiv.org/abs/2108.07905), [DiffuScene](https://arxiv.org/abs/2403.11986), [FactoredScenes](https://arxiv.org/abs/2510.10292), [LayoutVLM](https://arxiv.org/abs/2503.04870) |
| PDFリンク | https://arxiv.org/pdf/2604.11808v1 |
