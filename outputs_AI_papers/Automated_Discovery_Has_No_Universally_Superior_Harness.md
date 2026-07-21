---
title: "Automated Discovery Has No Universally Superior Harness"
date: 2026-07-21
arxiv_id: 2607.18235v1
url: http://arxiv.org/abs/2607.18235v1
---

# Automated Discovery Has No Universally Superior Harness

| 項目 | 内容 |
|---|---|
| どんなもの？ | LLMを用いた自律的なアルゴリズム探索システムにおいて、特定の探索プロセス（ハーネス）のレシピが万能ではなく、モデルや課題に応じて適切に調整すべき「ハイパーパラメータ」であると示した研究。探索の初期段階におけるパフォーマンスが最終結果を予測することを利用し、有望な探索プロセスを優先してリソースを配分する適応型手法を提案した。 |
| 先行研究と比べてどこがすごい？ | 従来はOpenEvolveやTTT-Discoverなどの複雑な探索手法が単一のレシピとして評価されていたが、本研究はこれらを分解し、大規模な統計的分析（310万件以上のロールアウト）を通じて、特定の構成が万能ではないことを実証した点。また、探索の途中で有望な構成のみに計算リソースを集中させる「適応型ハーネスアンサンブル」を導入し、効率を向上させた点。 |
| 技術や手法のキモはどこ？ | 探索システムを archive、parent selection、exploration、budget allocation などのコンポーネントに分解した点。また、探索初期の評価スコアが最終性能と強く相関することを見出し、部分的な実行結果に基づいて低性能な探索を枝刈り（pruning）し、計算リソースを再配分する手法（Successive HalvingやHyperbandの考え方を応用）を実装した点。 |
| どうやって有効だと検証した？ | 3Bから120BパラメータのLLMを用いて、3つの数学的探索課題（Circle Packing, Heilbronn triangle, Second autocorrelation inequality）に対し、計30種類の異なるハーネス構成で検証。ブートストラップ統計を用いて、単純なSequential Best-of-Nベースラインに対する有意な改善を厳密に評価し、適応的配分アルゴリズムの有効性を確認した。 |
| 議論はある？ | 提案手法は平均的な性能を向上させるが、個別のタスクにおいてどのモデルにどのハーネスが最適かを完全自動で特定するまでは至っていない。また、探索の枝刈りやリソース再配分の閾値設定はヒューリスティックに依存しており、より汎用的な最適化手法の検討が残されている。 |
| 次に読むべき論文は？ | [AdaEvolve: Adaptive llm driven zeroth-order optimization](https://arxiv.org/abs/2602.20133), [Agentic harness engineering](https://arxiv.org/abs/2604.25850), [Compute allocation in evolutionary search](https://arxiv.org/abs/2605.29268) |
| PDFリンク | https://arxiv.org/pdf/2607.18235v1 |
