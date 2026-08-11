---
title: "Learning How the World Evolves: Extrapolative Video World Models via Latent Dynamics Reasoning"
date: 2026-08-11
arxiv_id: 2608.09926v1
url: http://arxiv.org/abs/2608.09926v1
---

# Learning How the World Evolves: Extrapolative Video World Models via Latent Dynamics Reasoning

| 項目 | 内容 |
|---|---|
| どんなもの？ | 物理法則に基づいた動的な推論を行うことで、学習分布外の未知のシナリオに対しても高い汎化性能を持つ動画世界モデル（LDR）。従来のピクセルベースの拡散モデルとは異なり、明示的な運動学の統合を導入することで、正確な物理挙動の予測を可能にした。 |
| 先行研究と比べてどこがすごい？ | 従来の動画生成モデルはピクセルを模倣するだけで物理的な正確性に欠けるが、LDRは学習分布外（OOD）での誤差を既存手法比で20倍以上小さく抑えることに成功。さらに、パラメータ数で26倍の削減、推論速度で143倍の高速化を実現した。 |
| 技術や手法のキモはどこ？ | 入力フレームを動的に無関係な情報を含まない構造化された潜在変数（SL）にエンコードし、物理的な運動方程式（3階以上の高次微分を残差として学習）に基づいた数値積分で未来の潜在状態をロールアウトする手法。 |
| どうやって有効だと検証した？ | PhyWorldシミュレータ上で5つの物理タスク（等速運動、放物運動、衝突、跳ね返り、接近）を設定。学習分布外の速度、サイズ、スケール率を用いたOODテストを行い、GT（正解）と比較することで位置精度と半径精度を評価。 |
| 議論はある？ | 動的推論がコンテンツに対して独立（agnostic）であり、色の変化のような視覚的ダイナミクスを扱えない可能性がある点。また、現在のモデルは単純なオブジェクトに特化しており、より複雑な実世界のシーンへの拡張が今後の課題。 |
| 次に読むべき論文は？ | [Kang et al. 2025 (PhyWorld)](https://arxiv.org/abs/2501.03575), [Xu et al. 2021 (How Neural Networks Extrapolate)](https://arxiv.org/abs/2009.11848), [Jakab et al. 2018 (Unsupervised Learning of Object Landmarks)](https://arxiv.org/abs/1806.07564) |
| PDFリンク | https://arxiv.org/pdf/2608.09926v1 |
