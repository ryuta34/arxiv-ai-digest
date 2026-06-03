---
title: "Imaginative Perception Tokens Enhance Spatial Reasoning in Multimodal Language Models"
date: 2026-06-03
arxiv_id: 2606.03988v1
url: http://arxiv.org/abs/2606.03988v1
---

# Imaginative Perception Tokens Enhance Spatial Reasoning in Multimodal Language Models

| 項目 | 内容 |
|---|---|
| どんなもの？ | 空間推論が必要な課題に対して、モデルが未観測の視点や統合された空間マップを「想像（生成）」するための「Imaginative Perception Tokens (IPT)」を導入し、空間推論能力を向上させる手法。視覚言語モデル（VLM）において、言語的な思考（CoT）よりも視覚的な中間表現を用いる方が空間情報の処理に適していることを示した。 |
| 先行研究と比べてどこがすごい？ | 従来の中間表現は既存の入力情報の再構成に留まるものが多かったが、本手法は入力から推論される「未観測の空間」を視覚的に生成させる点で優れている。また、空間処理において言語によるCoTがノイズを生み性能を低下させることがあるのに対し、IPTは直接的な視覚的モダリティで推論を補助することで、高い汎化性能と精度を達成した。 |
| 技術や手法のキモはどこ？ | Unified VLM（BAGEL）を用い、空間推論の過程で「未観測の視点や鳥瞰図」を生成するタスクを学習させる点。推論時には、この生成された中間イメージ（IPT）を再度モデルのコンテキストに入力として与えることで、複雑な空間的制約を考慮した回答を導き出す仕組み。 |
| どうやって有効だと検証した？ | 視点変更、経路追跡、多視点カウントという3つの空間推論タスクを定義し、約20K規模のデータセットを構築。AI2-THORや実環境データを用いた実験で、IPTの導入により回答精度が向上すること、および推論時に画像生成を省略（Answer-only）しても内部的な空間表現が強化され精度を維持できることを示した。 |
| 議論はある？ | 生成された中間画像の品質がダウンストリームの精度に直結しており、現状の生成能力ではピクセル単位の正確な再現が困難な場合がある。また、画像生成コストや、高解像度化に伴う過学習の可能性などの課題が挙げられる。 |
| 次に読むべき論文は？ | [12] Emerging properties in unified multimodal pretraining (BAGEL), [15] ThinkMorph: Emergent properties in multimodal interleaved chain-of-thought reasoning, [40] Machine mental imagery: Empower multimodal reasoning with latent visual tokens |
| PDFリンク | https://arxiv.org/pdf/2606.03988v1 |
