---
title: "EngramEdit: Decoupled Knowledge Updates in LLMs through Conditional Memory"
date: 2026-10-09
arxiv_id: 2610.10533v1
url: http://arxiv.org/abs/2610.10533v1
---

# EngramEdit: Decoupled Knowledge Updates in LLMs through Conditional Memory

| 項目 | 内容 |
|---|---|
| どんなもの？ | 大規模言語モデル（LLM）の条件付きメモリ（Conditional Memory）アーキテクチャにおいて、Transformer本体を固定したまま、n-gram埋め込みを編集することで事実知識を効率的に更新する手法「EngramEdit」を提案しています。知識の編集と維持を両立させ、学習済みモデルの知識更新を可能にする技術です。 |
| 先行研究と比べてどこがすごい？ | 従来手法に比べ、事実知識の更新成功率（Efficacy）と汎化性能（Generalization）が著しく高く、マルチホップ推論においても約3倍の精度向上を達成しました。また、知識更新を繰り返しても、他の知識や汎用能力を保持できる点が優れています。 |
| 技術や手法のキモはどこ？ | 事実を複数の表現に変換してn-gramの網羅性を高め、それらを単一の更新対象として最適化する点です。さらに、頻繁に再利用される埋め込みほど更新コストを高く設定する「再利用ベースの正則化（Reuse-based Regularization）」を導入し、無関係な知識への副作用を抑制しています。 |
| どうやって有効だと検証した？ | CounterFactやZsRE、MQuAKEなどのベンチマークを用い、最大5,000回に及ぶ逐次的な知識編集実験を行いました。また、アブレーション研究により、各提案コンポーネント（共同更新、正則化、生成表現）の有効性を詳細に検証しています。 |
| 議論はある？ | 知識の共有が激しい場合（同じn-gramが複数の事実で共有されている場合）、競合する更新ターゲットが学習を困難にすることが示唆されています。また、MRPCタスクのような文の意味的同値性の判定においては、表現が敏感に反応し性能が低下する傾向があります。 |
| 次に読むべき論文は？ | [3] Xin Cheng et al. "Conditional memory via scalable lookup" (2026), [9] Kevin Meng et al. "Locating and editing factual associations in GPT" (2022), [12] Kevin Meng et al. "Mass-editing memory in a transformer" (2023) |
| PDFリンク | https://arxiv.org/pdf/2610.10533v1 |
