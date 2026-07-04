---
title: "WorldDirector: Building Controllable World Simulators with Persistent Dynamic Memory"
date: 2026-07-04
arxiv_id: 2607.02517v1
url: http://arxiv.org/abs/2607.02517v1
---

# WorldDirector: Building Controllable World Simulators with Persistent Dynamic Memory

| 項目 | 内容 |
|---|---|
| どんなもの？ | 長時間の動画生成において、動的なオブジェクトの永続性と視点の自由な探索を実現する世界シミュレータ「WorldDirector」。LLMによる高度なプランニングと、独自の条件付けメカニズムにより、オブジェクトが画面外に出た後も物理的論理と外観を保持して再登場させることを可能にした。 |
| 先行研究と比べてどこがすごい？ | 従来のモデルがカメラ視点に依存してオブジェクトの動きを推論していたのに対し、モーションプランニングと視覚生成を明示的に分離した点。これにより、長時間の隠蔽後でもオブジェクトのアイデンティティや挙動の整合性を高精度に維持できる。 |
| 技術や手法のキモはどこ？ | LLMを用いて3D軌道とカメラパスを計画し、それを「2Dバウンディングボックス条件」として生成に投影する点。さらに、過去のRGB特徴を視覚的アンカーとして注入する「Appearance Binding」と、生成品質を安定させる「Temporal Drop Mechanism」を導入したこと。 |
| どうやって有効だと検証した？ | 100種類の未学習シーンを含むテストデータセットで評価し、PSNR、SSIM、LPIPS、およびVBenchを用いた「対象」と「背景」の整合性指標でSOTAを達成。特に、動的オブジェクトの再登場における一貫性を測るDSC（Dynamic Subject Consistency）で高い性能を示した。 |
| 議論はある？ | 合成データを用いた学習によるドメインギャップが生じることがあり、時折、不自然な動きや顔のぼやけが発生する。将来的な課題として、実データを取り入れることで視覚的リアリズムをさらに向上させる必要がある。 |
| 次に読むべき論文は？ | [LingBot-World-Base [38]](https://arxiv.org/abs/2601.20540)、[HyDRA [12]](https://arxiv.org/abs/2603.25716)、[GLIGEN [30]](https://arxiv.org/abs/2301.07093) |
| PDFリンク | https://arxiv.org/pdf/2607.02517v1 |
