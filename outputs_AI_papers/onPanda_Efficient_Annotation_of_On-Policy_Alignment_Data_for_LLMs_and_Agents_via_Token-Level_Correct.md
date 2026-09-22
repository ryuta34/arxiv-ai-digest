---
title: "onPanda: Efficient Annotation of On-Policy Alignment Data for LLMs and Agents via Token-Level Correction"
date: 2026-09-22
arxiv_id: 2609.24983v1
url: http://arxiv.org/abs/2609.24983v1
---

# onPanda: Efficient Annotation of On-Policy Alignment Data for LLMs and Agents via Token-Level Correction

| 項目 | 内容 |
|---|---|
| どんなもの？ | 大規模言語モデル（LLM）やエージェントのアライメントデータ作成を効率化する対話型ツール「onPanda」の提案。モデルの生成結果に対してトークン単位での修正（locate-correct-continue）を繰り返すことで、低コストかつ高精度なデータ作成を実現する。 |
| 先行研究と比べてどこがすごい？ | 従来の手動による全文編集やランキング方式と比較して、修正箇所のみを特定してモデルに再生成させるため、アライメント時間が51.5%削減され、かつモデル独自のサンプリング分布を保持した「on-policy」なデータを効率的に生成できる点。 |
| 技術や手法のキモはどこ？ | モデルの確率分布（logprobs）を可視化し、修正が必要なトークンを特定する機能、修正後に該当箇所からモデルに自動で再生成を行わせる仕組み、およびそれらの操作を自動記録してSFTデータや選好データとして保存するプロトコル。 |
| どうやって有効だと検証した？ | 21個の画像説明タスクを用いた制御実験において、既存プラットフォーム（POTATO, Argilla）と時間・品質（ペアワイズ勝率）・忠実度（PPL）を比較。また、NASA-TLXを用いたユーザースタディで作業負担の軽減を確認した。 |
| 議論はある？ | モデルが生成する内容が目標から大きく外れている場合の修正コスト増大や、評価がLLM-as-a-judgeに依存している点。また、下流タスクへの学習効果は今後の検証課題としている。 |
| 次に読むべき論文は？ | [ProcessBench](https://arxiv.org/abs/2501.00977) (Zheng et al., 2025) や [Let's verify step by step](https://arxiv.org/abs/2305.20050) (Lightman et al., 2024) |
| PDFリンク | https://arxiv.org/pdf/2609.24983v1 |
