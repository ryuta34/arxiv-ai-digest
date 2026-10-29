---
title: "Honeycomb-Surfels: Compact Hexagonal Primitives for Efficient Scene Rendering and Reconstruction"
date: 2026-10-29
arxiv_id: 2610.37668v1
url: http://arxiv.org/abs/2610.37668v1
---

# Honeycomb-Surfels: Compact Hexagonal Primitives for Efficient Scene Rendering and Reconstruction

| 項目 | 内容 |
|---|---|
| どんなもの？ | 効率的な3Dシーンおよび2D画像の表現と再構築を目的とした、六角形のサーフェス要素「Hexels」を用いた手法です。従来のガウシアンを用いた手法よりもメモリ使用量と計算コストを抑えつつ、より高精度な視点合成と再構築を実現しました。 |
| 先行研究と比べてどこがすごい？ | 2DGS（2D Gaussian Splatting）などの手法と比較して、同等のモデルメモリでPSNRを4.53〜7.38dB向上させ、最大7倍のVRAM削減を達成しました。また、テクスチャマップやニューラルネットワークに依存せず、プリミティブ自体で効率的な表現を完結させています。 |
| 技術や手法のキモはどこ？ | 六角形のサポート領域を採用し、さらに各要素内で一次の空間色フィールド（第一階近似の色変化）を保持することで、少ないプリミティブ数で滑らかな色変化と境界を表現する点です。これにより、過剰なオーバードローを抑えつつ、構造的冗長性を排除しています。 |
| どうやって有効だと検証した？ | Mip-NeRF360、DTU、Tanks and Templesの計34シーンを用い、メモリ制約がある状況とプリミティブ数が制限された状況の両方で評価しました。また、2D画像の表現においてもImage-GSと比較し、PSNRと処理速度の両面で優位性を示しました。 |
| 議論はある？ | 現在のモデルは平面的な要素に限定されており、複雑なテクスチャの表現や、幾何学的な「水密性（watertightness）」の確保には課題が残ります。今後は、開発可能な形状（developable Hexels）への拡張を検討しています。 |
| 次に読むべき論文は？ | [14] 2D Gaussian Splatting for Geometrically Accurate Radiance Fields, [18] 3D Gaussian Splatting for Real-Time Radiance Field Rendering, [30] Nexels: Neurally-Textured Surfels for Real-time Novel View Synthesis |
| PDFリンク | https://arxiv.org/pdf/2610.37668v1 |
