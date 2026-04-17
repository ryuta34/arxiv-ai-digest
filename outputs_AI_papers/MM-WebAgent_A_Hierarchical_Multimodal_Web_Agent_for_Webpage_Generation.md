---
title: "MM-WebAgent: A Hierarchical Multimodal Web Agent for Webpage Generation"
date: 2026-04-17
arxiv_id: 2604.15309v1
url: http://arxiv.org/abs/2604.15309v1
---

# MM-WebAgent: A Hierarchical Multimodal Web Agent for Webpage Generation

| 項目 | 内容 |
|---|---|
| どんなもの？ | マルチモーダルなウェブページ生成を最適化するための、階層的なエージェントフレームワーク「MM-WebAgent」。単なるコード生成にとどまらず、画像や動画、チャートなどのマルチモーダル要素を、グローバルなレイアウト計画と連携させながら生成・統合する。 |
| 先行研究と比べてどこがすごい？ | 既存手法は要素を個別に生成するため、スタイルの不一致や配置のミスが多発していた。MM-WebAgentは、設計プロセス全体を「計画」と「洗練」の反復として捉え、階層的なプランニングと自己反省機構を導入することで、一貫性と視覚的整合性を大幅に向上させた点。 |
| 技術や手法のキモはどこ？ | 全体レイアウトと各要素の役割を定義する「階層的計画」と、要素レベル、コンテキストレベル、グローバルレベルの3段階で生成物を繰り返し修正・最適化する「階層的自己反省メカニズム」。 |
| どうやって有効だと検証した？ | マルチモーダルなウェブページ生成に特化したベンチマーク「MM-WebGEN-Bench」を構築し、既存のコード生成手法やエージェントベースのベースラインと比較。また、専門家によるユーザー評価を行い、生成されたページの質が高いことを証明した。 |
| 議論はある？ | 外部のAIGCツールへの依存により、ツールの制限（安定性やバイアスなど）の影響を受けやすい。また、現在は学習ベースではなく訓練不要のオーケストレーション手法であるため、今後は強化学習による計画やツール使用の最適化が将来課題となる。 |
| 次に読むべき論文は？ | [Webmmu: A benchmark for multimodal multilingual website understanding and code generation](https://arxiv.org/abs/2506.13663)、[Designcoder: Hierarchy-aware and self-correcting ui code generation with large language models](https://arxiv.org/abs/2506.13663) |
| PDFリンク | https://arxiv.org/pdf/2604.15309v1 |
