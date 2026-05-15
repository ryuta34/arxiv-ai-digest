---
title: "EntityBench: Towards Entity-Consistent Long-Range Multi-Shot Video Generation"
date: 2026-05-15
arxiv_id: 2605.15199v1
url: http://arxiv.org/abs/2605.15199v1
---

# EntityBench: Towards Entity-Consistent Long-Range Multi-Shot Video Generation

| 項目 | 内容 |
|---|---|
| どんなもの？ | マルチショット動画生成におけるキャラクター、オブジェクト、場所の長期的な整合性を評価するためのベンチマーク「EntityBench」と、これを改善するためのメモリ拡張生成システム「EntityMem」を提案した研究。 |
| 先行研究と比べてどこがすごい？ | 従来のベンチマークが単一ショットや限定的なエンティティの整合性に留まっていたのに対し、140エピソード・2,491ショットの大規模データセットで複数のエンティティを同時に追跡し、 intra-shot（単一ショット内）、prompt-following（プロンプト追従）、cross-shot（複数ショット間）の3本柱で網羅的に評価できる点。 |
| 技術や手法のキモはどこ？ | 生成前にLLMエージェントを用いて各エンティティの視覚的・テキスト的参照を生成・検証し、永続的なメモリバンクに保存しておく点。生成時にこのメモリバンクから参照情報を動的に取得・注入することで、一貫した視覚的アイデンティティを維持する。 |
| どうやって有効だと検証した？ | 既存の代表的な動画生成手法（HoloCine, CineTrans, StoryMem等）をEntityBench上で評価。提案手法EntityMemがキャラクターの忠実度（Cohen's d = +2.33）や存在感において他手法を凌駕し、特に長期的な連続性維持に有効であることを示した。 |
| 議論はある？ | オブジェクトの整合性においては、シーン依存のコンテキスト保持が難しく、StoryMem等にわずかに及ばない場合がある点。また、DINOv2による埋め込み類似度とLLMによるアイデンティティ判断の間に乖離が見られ、単なる画的な類似と人間が認識するアイデンティティ保持の区別の難しさが指摘されている。 |
| 次に読むべき論文は？ | [1] [HoloCine](https://arxiv.org/abs/2510.20822), [2] [StoryMem](https://arxiv.org/abs/2512.19539), [3] [VBench](https://arxiv.org/abs/2403.08473) |
| PDFリンク | https://arxiv.org/pdf/2605.15199v1 |
