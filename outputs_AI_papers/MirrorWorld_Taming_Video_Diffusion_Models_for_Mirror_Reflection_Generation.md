---
title: "MirrorWorld: Taming Video Diffusion Models for Mirror Reflection Generation"
date: 2026-08-10
arxiv_id: 2608.07463v1
url: http://arxiv.org/abs/2608.07463v1
---

# MirrorWorld: Taming Video Diffusion Models for Mirror Reflection Generation

| 項目 | 内容 |
|---|---|
| どんなもの？ | 動画内のミラー反射生成において、周囲のシーンと矛盾のない一貫した鏡像を生成するための新しいフレームワーク「MirrorWorld」を提案している。シーン内容の整合性を保ちながら、幾何学的に正しい鏡像を動画として生成する手法である。 |
| 先行研究と比べてどこがすごい？ | 従来の静止画ベース手法や一般的な動画インペインティング手法では困難だった、シーン全体の文脈と鏡像の空間的な整合性（何が映るべきか、どう配置されるべきか）を、提案する2つのコンポーネントにより高精度に制御できる点。 |
| 技術や手法のキモはどこ？ | 学習済みモデルから関係情報を抽出する「Semantic Relation Distillation (SRD)」で「何を映すべきか」を特定し、時系列コンテキストを活用した「Geometric Transformation Alignment (GTA)」で「どう配置すべきか」の空間的変換を学習する点。 |
| どうやって有効だと検証した？ | 既存の動画ミラーデータセット4つを統合したベンチマークを構築し、PSNR、SSIM、LPIPS、FVDを用いて評価。既存の画像ベース手法や動画インペインティング手法と比較し、全指標で優れた結果を示した。 |
| 議論はある？ | カメラの視野外にある対象が鏡に映る場合、現在のフレーム内の可視情報だけでは正確な鏡像生成が困難であるという限界がある。今後は、より複雑な反射の幾何学モデル化が課題となる。 |
| 次に読むべき論文は？ | [VideoPainter (Bian et al. 2025)](https://arxiv.org/abs/2501.00103) および [MirrorFusion (Dhiman et al. 2025)](https://arxiv.org/abs/2501.11239) |
| PDFリンク | https://arxiv.org/pdf/2608.07463v1 |
