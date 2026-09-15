---
title: "The Router Within: Eliciting Native Skill Routing from a Frozen LLM"
date: 2026-09-15
arxiv_id: 2609.15982v1
url: http://arxiv.org/abs/2609.15982v1
---

# The Router Within: Eliciting Native Skill Routing from a Frozen LLM

| 項目 | 内容 |
|---|---|
| どんなもの？ | 大規模言語モデル（LLM）エージェントにおいて、文脈にスキル（指示やツールなど）を読み込ませず、LLM自身の内部状態を直接読み取ることで最適なスキルを選択・ルーティングする手法「Gavel」を提案した論文。 |
| 先行研究と比べてどこがすごい？ | 従来手法はスキル情報をプロンプトに含めるため文脈を圧迫したり、外部モデルによる検索で推論能力を十分に活かせなかった。GavelはフリーズされたLLMから直接ルーティング信号を抽出するため、文脈をクリーンに保ちつつ、モデル本来の推論能力でスキル選択が可能。 |
| 技術や手法のキモはどこ？ | 学習済みの2つの線形写像を用いた「Glance（全ライブラリの概観）」と、LLMの生成・識別的推論を併用する「Verdict（短縮候補の精査）」の二段構え。また、スキルバンクの情報をε-coverで圧縮し、計算コストを大幅に削減している点。 |
| どうやって有効だと検証した？ | 3つの既存スキル選択ベンチマークおよび、新規作成した実演シミュレーションベンチマーク「SkillTraj」で評価。最大16Bのパラメータを持つ外部モデルを組み合わせた従来手法を大きく上回る性能を達成した。 |
| 議論はある？ | 現在はスキルルーティングの判断ゲートを線形分類器で実装しているが、より高度なタイミング制御にはシーケンスモデルの導入が必要。また、現状はスキル選択に特化しているが、将来的にはツールやメモリ等のルーティングへの拡張も検討課題である。 |
| 次に読むべき論文は？ | [SkillRouter: Skill routing for LLM agents at scale](https://arxiv.org/abs/2603.22455), [Skill-use: Can LLMs actually use skills in agentic harnesses?](https://arxiv.org/abs/2608.04828) |
| PDFリンク | https://arxiv.org/pdf/2609.15982v1 |
