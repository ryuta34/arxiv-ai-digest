---
title: "Can Language Models Play the Wikipedia Game?"
date: 2026-10-13
arxiv_id: 2610.13948v1
url: http://arxiv.org/abs/2610.13948v1
---

# Can Language Models Play the Wikipedia Game?

| 項目 | 内容 |
|---|---|
| どんなもの？ | 大規模言語モデル（LLM）と文章埋め込みモデルの能力を、Wikipediaのリンクを辿って目的の記事に到達する「Wikipediaゲーム」を用いて評価した研究。複数の言語と学術論文データセット（OpenAlex）を対象に、人間との比較も含めた網羅的な検証を行っている。 |
| 先行研究と比べてどこがすごい？ | APIによる限定的な評価や小規模なグラフデータを用いた従来研究に対し、大規模で独自のグラフデータセットを構築した点、またLLMと埋め込みモデル、人間、TF-IDFという多様な手法を、言語やドメインを横断して一貫したベンチマークで比較した点。 |
| 技術や手法のキモはどこ？ | Wikipediaのハイパーリンク構造を巨大な有向グラフとしてモデル化し、各ノードの要約やタイトルを用いて、現在の記事から目的の記事へ近づくための次の一手を判断させる情報検索タスクとして定式化したこと。 |
| どうやって有効だと検証した？ | 5つの言語のWikipediaと5つの学術分野のOpenAlexデータセットを使用し、計10,000ゲームの試行を実施。成功率と到達効率（ステップ数）を指標に、モデルサイズや推論（Reasoning）プロンプトの効果を定量的に分析した。 |
| 議論はある？ | 言語モデルの成功率は人間と匹敵するが、効率面では依然として人間に劣ること。また、モデルの性能は言語やトピックによって変動し、特定の知識を「知っている」こととそれを「ゲームに応用できる」ことの間にギャップが存在することが示唆されている。 |
| 次に読むべき論文は？ | [49] West, R., Leskovec, J.: Automatic Versus Human Navigation in Information Networks. [54] Ziomek, J., et al.: LLM-WikiRace Benchmark: How Far Can LLMs Plan over Real-World Knowledge Graphs? |
| PDFリンク | https://arxiv.org/pdf/2610.13948v1 |
