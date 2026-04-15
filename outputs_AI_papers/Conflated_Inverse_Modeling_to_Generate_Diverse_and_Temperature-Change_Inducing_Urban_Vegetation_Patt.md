---
title: "Conflated Inverse Modeling to Generate Diverse and Temperature-Change Inducing Urban Vegetation Patterns"
date: 2026-04-15
arxiv_id: 2604.13028v1
url: http://arxiv.org/abs/2604.13028v1
---

# Conflated Inverse Modeling to Generate Diverse and Temperature-Change Inducing Urban Vegetation Patterns

| 項目 | 内容 |
|---|---|
| どんなもの？ | 都市の熱環境改善を目的とし、建物の高さや温度データに基づいて、目標とする温度変化を実現する多様な植生パターン（NDVI）を生成する逆問題モデル。 |
| 先行研究と比べてどこがすごい？ | 従来の決定論的な手法では単一の平均的な解しか得られなかったのに対し、拡散モデルを用いて、データが少ない環境下でも温度目標を満たす多様かつ物理的に妥当な植生配置を生成できる点。 |
| 技術や手法のキモはどこ？ | 学習済みの順モデル（予測器）と拡散モデルによる逆モデルを組み合わせた「コンフレート（統合）型」アプローチ。粗い温度情報で条件付けを行い、地域平均レベルの物理制約を導入することで、多様性を維持しつつ目標温度を実現した点。 |
| どうやって有効だと検証した？ | 米国20都市のLandsat 8データを用い、提案手法がベースライン（U-Net等）と比較して温度制御誤差（CtrlErr）を37%低減し、多様性を3.4倍向上させることを定量的・定性的に示した。 |
| 議論はある？ | 植生配置の現実的な制約（既存インフラや土地利用規則）がモデルに組み込まれていない点や、衛星プラットフォーム間の解像度と熱データのトレードオフが課題として挙げられている。 |
| 次に読むべき論文は？ | [15] Tero Karras et al., "Elucidating the design space of diffusion-based generative models" (https://arxiv.org/abs/2206.00364) |
| PDFリンク | https://arxiv.org/pdf/2604.13028v1 |
