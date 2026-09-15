---
title: "Stellar Colosseum: A Many-Agent Harness for Long-Horizon Research in Mathematics and Theoretical Computer Science"
date: 2026-09-15
arxiv_id: 2609.15983v1
url: http://arxiv.org/abs/2609.15983v1
---

# Stellar Colosseum: A Many-Agent Harness for Long-Horizon Research in Mathematics and Theoretical Computer Science

| 項目 | 内容 |
|---|---|
| どんなもの？ | 数学および理論計算機科学における、長期間にわたる複雑な研究や証明を自動化するための多目的エージェント・ハーネス「STELLAR COLOSSEUM」である。戦略探索から証明の分解、並列解決、全体検証までをパイプライン化し、再帰的な改善を可能にする。 |
| 先行研究と比べてどこがすごい？ | 従来の単純な推論やモデルの単発的な投票方式と異なり、研究の進捗を構造化して管理する点や、反論（クリティーク）を提案とセットで保持する「ツリー構造集約」により、失敗から学習して効率的に難問を解決できる点が優れている。 |
| 技術や手法のキモはどこ？ | ①ステージごとの「読み込みゲート（Readiness Gate）」による戦略評価、②依存関係を考慮した証明の分解、③反証（falsification）を伴うランダムサンプリングによるツリー構造集約、④失敗や反論を「共有研究知識」として蓄積・活用する仕組み。 |
| どうやって有効だと検証した？ | TCS-Bench（FOCS/STOC/SODA由来の証明課題）において、モデル単体と比較して高い正解率（71.0%）を達成。また、Codeforcesの競技プログラミング課題222問中218問を解くなど、理論と実践の両面で有効性を実証した。 |
| 議論はある？ | 実行環境（コードプローブ）による修正の因果関係の分離や、研究軌跡の自動評価におけるクレジット割り当ての難しさが課題。また、現在の構成は静的なパラメータに依存しており、今後は動的な推論計算量の配分が重要となる。 |
| 次に読むべき論文は？ | [56] Woodruff et al. "Accelerating scientific research with Gemini"、[61] Zhang et al. "LeanMarathon"、[58] Wu et al. "Inference scaling laws" |
| PDFリンク | https://arxiv.org/pdf/2609.15983v1 |
