---
title: "3D-Aware VLMs with Implicit and Explicit Geometries"
date: 2026-07-24
arxiv_id: 2607.21595v1
url: http://arxiv.org/abs/2607.21595v1
---

# 3D-Aware VLMs with Implicit and Explicit Geometries

| 項目 | 内容 |
|---|---|
| どんなもの？ | 2DのRGB動画から、暗黙的（Implicit）な空間的文脈と明示的（Explicit）な幾何学的構造の両方を学習し、VLMs（Vision-Language Models）の3D空間理解能力を向上させる統一フレームワーク「VLM-IE3D」。追加の3Dセンサー入力なしで、精緻な空間推論を実現する。 |
| 先行研究と比べてどこがすごい？ | 既存のRGB-only手法が「大まかな空間レイアウト（暗黙的表現）」のみに依存していたのに対し、本手法は深度マップ等から抽出した「詳細な幾何学的構造（明示的表現）」を組み合わせて補完した点。これにより、3D認識の解像度と定量的な推論精度が大幅に向上した。 |
| 技術や手法のキモはどこ？ | 高レベルな幾何学的優先情報を持つ「Implicit Geometry Tokens (IGTs)」と、詳細な構造情報を持つ「Explicit Geometry Tokens (EGTs)」を導入し、これらを「3D-aware adapter」を通じて2D視覚特徴と効果的に融合させる点。 |
| どうやって有効だと検証した？ | Scan2Cap（3Dキャプション生成）、ScanRefer（3D視覚接地）、3D動画検出、VSI-Bench（空間推論）の各ベンチマークで実験。既存のRGB-only手法を凌駕し、3Dデータ入力を必要とするモデルに匹敵する性能を実証した。 |
| 議論はある？ | 深度マップなどの明示的情報を生成するための基盤モデルに依存する点や、モデル全体の推論速度が軽量モデルと比較して僅かに低下（7 FPSから6 FPSへ）するトレードオフがある。 |
| 次に読むべき論文は？ | AnySplat [19] (本研究の基盤エンコーダ), Scan2Cap [10], Video-3D LLM [49], VG LLM [50] |
| PDFリンク | https://arxiv.org/pdf/2607.21595v1 |
