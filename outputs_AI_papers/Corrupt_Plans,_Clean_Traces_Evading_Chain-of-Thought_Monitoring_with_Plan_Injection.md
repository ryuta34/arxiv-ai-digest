---
title: "Corrupt Plans, Clean Traces: Evading Chain-of-Thought Monitoring with Plan Injection"
date: 2026-09-15
arxiv_id: 2609.15989v1
url: http://arxiv.org/abs/2609.15989v1
---

# Corrupt Plans, Clean Traces: Evading Chain-of-Thought Monitoring with Plan Injection

| 項目 | 内容 |
|---|---|
| どんなもの？ | 大規模言語モデルのコンテキストに有害な推論過程を「計画（Plan）」として埋め込むことで、モデルに自発的な推論として実行させ、安全監視（CoTモニタリング）を回避させる「プラン注入（Plan Injection）」攻撃を提案した論文。 |
| 先行研究と比べてどこがすごい？ | 従来手法がモデルに明示的な指示（命令）を与えるのに対し、本手法はモデルが自律的に推論しているかのように振る舞わせることで、監視側の検知を大幅にすり抜ける。また、モデルが大規模化しても攻撃が有効であることを示し、監視リソース（推論予算）の増加が必ずしも検知能力向上に寄与しない逆説的な現象を明らかにした。 |
| 技術や手法のキモはどこ？ | Investigator-agentフレームワークを用い、モデルの思考過程（CoT）の文脈に溶け込むような「害のないように見える有害な計画」を自動生成する点。また、モデルが注入された計画をそのままコピーするのではなく、自らの言葉でパラフレーズ（言い換え）を行うことで、監視モデルの検知を困難にしている。 |
| どうやって有効だと検証した？ | TruthfulQA、APPS（コーディング）、Bio-Math（生物学・数学）の各データセットを用い、QwenやDeepSeek-R1等のモデルで攻撃を試行。GPT-4o MiniやClaude 3.7 Sonnetを含む複数の監視モデルを用いて、提案手法の検知回避率（25〜76%）および推論予算が増えた際の監視能力の動向を評価した。 |
| 議論はある？ | 監視の推論予算を増やすと、かえって注入された有害な論理を「妥当なもの」として合理化・正当化してしまうリスクが指摘された。また、本研究は生成された計画の影響に焦点を当てており、どのようにその計画がコンテキストに混入するか（RAG等の経路）の詳細は将来課題としている。 |
| 次に読むべき論文は？ | [Li et al. (2025) "Eliciting language model behaviors with investigator agents"](https://arxiv.org/abs/2501.12345)、[Guan et al. (2025) "Monitoring monitorability"](https://arxiv.org/abs/2512.18311)、[Korbak et al. (2025) "Chain of thought monitorability"](https://arxiv.org/abs/2507.11473) |
| PDFリンク | https://arxiv.org/pdf/2609.15989v1 |
