---
title: "CreativeInstruct: Scalably Teaching LLMs to Balance Quality, Creativity, and Diversity"
date: 2026-08-10
arxiv_id: 2608.07460v1
url: http://arxiv.org/abs/2608.07460v1
---

# CreativeInstruct: Scalably Teaching LLMs to Balance Quality, Creativity, and Diversity

| 項目 | 内容 |
|---|---|
| どんなもの？ | 大規模言語モデル（LLM）の指示追従能力を維持しつつ、出力の多様性と創造性を向上させるための新しい命令チューニング手法「CREATIVEINSTRUCT」を提案した。この手法は、生成時に創造性を高める特殊トークンを自律的に挿入することで、単一モデルで高品質かつ多様な生成を実現する。 |
| 先行研究と比べてどこがすごい？ | 従来手法（複数モデルの推論時ルーティング等）が抱えていた推論時の高い計算コストやメモリオーバーヘッドを解消した。また、物語の構造的差異を測定する新しい評価指標「LLM-GED」を導入し、語彙レベルを超えた物語生成の多様性を定量化した点。 |
| 技術や手法のキモはどこ？ | ベースモデル（高い多様性）とアラインメント済みモデル（高い指示追従性）の出力をルーティングする仕組みを利用し、ベースモデル由来の spans を「[StartCreativity]」「[EndCreativity]」という特殊トークンで囲ったデータを学習させる。これにより、モデル自身が生成中に創造性のスイッチを切り替えることを学習する。 |
| どうやって有効だと検証した？ | 5つのモデルサイズとファミリー（7B〜32B）に対し、Narrative Discourseデータセットを用いて多様性指標（Cos-D, Vendi, NLI, LLM-GED）と質（コヒーレンス、流暢さ等）を比較。さらに人間による評価と、強化学習（GRPO）を用いた数学推論課題への応用により、多様性がモデルの汎化性能を向上させることを実証した。 |
| 議論はある？ | 現在の手法では生成時に特殊トークンを注入する必要があり、その制御の限界や、より長大な物語における構造的一貫性の維持が課題。また、数学的推論においては有効性が示されたが、すべてのタスクにおいて常に最高性能を保証するわけではない。 |
| 次に読むべき論文は？ | [Wang et al. (2026): Optimizing diversity and quality through base-aligned model collaboration](https://arxiv.org/abs/2604.02319)、[Shao et al. (2024): Deepseekmath](https://arxiv.org/abs/2402.03300) |
| PDFリンク | https://arxiv.org/pdf/2608.07460v1 |
