---
title: "SenseNova-U1.5: Towards Native Unified Visual Intelligence"
date: 2026-09-11
arxiv_id: 2609.11929v1
url: http://arxiv.org/abs/2609.11929v1
---

# SenseNova-U1.5: Towards Native Unified Visual Intelligence

| 項目 | 内容 |
|---|---|
| どんなもの？ | 8BパラメータのMixture-of-Transformers(MoT)アーキテクチャを採用した、エンコーダー・VAE不要のネイティブ統合型マルチモーダルモデル。視覚的理解・推論・生成を単一のエンドツーエンドフレームワークで実現している。 |
| 先行研究と比べてどこがすごい？ | 従来のパッチ単位の独立した生成ではなく、空間的に結合された再構成を行うことで、解像度4Kまでの高精細かつ空間的に一貫した生成を可能にした。また、各生成タスクに特化した専門家モデルをRLで学習させ、それをオンポリシー蒸留で統合する戦略により、マルチタスク性能を最大化した点。 |
| 技術や手法のキモはどこ？ | ①ピクセルレベルでの空間的に結合した再構成を行う空間デコーダー、②解像度に適応したノイズスケール埋め込み、③美学・テキスト・インフォグラフィックス・編集の4つの専門家モデルによる「専門化（Specialize）→統合（Unify）」の学習戦略。 |
| どうやって有効だと検証した？ | 視覚理解（MMMU、MathVista等）、画像生成（Qwen-Image-Bench等）、画像編集（ImgEdit等）、インターリーブ生成（OpenING）など、多岐にわたる包括的なベンチマークで、従来の手法を凌駕する性能を実証した。 |
| 議論はある？ | 複雑な構造や関係性を伴う推論生成において、プロプライエタリなモデル（GPT-4o等）との間には依然として性能ギャップが存在する。また、より深い言語的・文脈的理解に向けた改善の余地がある。 |
| 次に読むべき論文は？ | [SenseNova-U1 [29]](https://arxiv.org/abs/2605.12500)、[NEO-unify [101]](https://huggingface.co/blog/sensenova/neo-unify)、[MOPD [85]](https://arxiv.org/abs/2606.30406) |
| PDFリンク | [https://arxiv.org/pdf/2609.11929v1](https://arxiv.org/pdf/2609.11929v1) |
