---
title: "HandX: Scaling Bimanual Motion and Interaction Generation"
date: 2026-03-31
arxiv_id: 2603.28766v1
url: http://arxiv.org/abs/2603.28766v1
---

# HandX: Scaling Bimanual Motion and Interaction Generation

| 項目 | 内容 |
|---|---|
| どんなもの？ | 高精度な両手協調動作と指の動きを生成するための、大規模なデータセット「HandX」と、それを用いた生成フレームワーク。テキストから細粒度な両手動作を生成し、拡散モデルおよび自己回帰モデルによるベンチマークを確立した。 |
| 先行研究と比べてどこがすごい？ | 既存データセットが抱えていた「手の動きの細かさの欠如」や「両手協調・接触の記述不足」を解決した点。54.2時間分もの高品質な動作データと、LLMによる自動生成された細粒度なテキスト記述を組み合わせた点が大きな強み。 |
| 技術や手法のキモはどこ？ | 運動理解と自然言語生成を分離した「2段階アノテーション手法」を採用し、運動のキネマティックな特徴からLLMを介して豊かなテキスト記述を生成した点。また、拡散モデルによるマスク付き部分ノイズ除去により、インペインティングや軌道制御など多機能な生成を実現した点。 |
| どうやって有効だと検証した？ | 拡散モデルと自己回帰モデルの双方でモデル容量やデータセット規模を変化させるスケーリング則を検証。R-Precisionや接触精度（Cprec）などの指標を用い、データ量とモデルサイズの拡大が生成品質の向上に寄与することを確認し、ユーザー調査でも有効性を立証した。 |
| 議論はある？ | データセット規模には依然として限界があり、現実世界のあらゆる状況を網羅しているわけではない点。また、既存データセットの再利用に伴う軽微なジッターや運動の不整合が完全には排除できていない点が今後の課題。 |
| 次に読むべき論文は？ | [14] ARCTIC: A dataset for dexterous bimanual hand-object manipulation, [19] GigaHands: A massive annotated dataset of bimanual hand activities, [53] CLUTCH: Contextualized language model for unlocking text-conditioned hand motion modelling in the wild |
| PDFリンク | https://arxiv.org/pdf/2603.28766v1 |
