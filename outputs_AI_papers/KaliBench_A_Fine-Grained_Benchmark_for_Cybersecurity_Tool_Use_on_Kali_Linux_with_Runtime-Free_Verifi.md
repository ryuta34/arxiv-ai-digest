---
title: "KaliBench: A Fine-Grained Benchmark for Cybersecurity Tool Use on Kali Linux with Runtime-Free Verifiable Rewards"
date: 2026-10-03
arxiv_id: 2610.02206v1
url: http://arxiv.org/abs/2610.02206v1
---

# KaliBench: A Fine-Grained Benchmark for Cybersecurity Tool Use on Kali Linux with Runtime-Free Verifiable Rewards

| 項目 | 内容 |
|---|---|
| どんなもの？ | サイバーセキュリティ業務における自然言語からKali Linuxのコマンドラインツールへの変換を評価するための、精緻で検証可能な新しいベンチマーク「KaliBench」の提案。8,504件のクエリ・コマンドペアを通じて、LLMのツール使用能力をコマンド構造レベルで測定する。 |
| 先行研究と比べてどこがすごい？ | 既存のツール使用ベンチマークがスキーマ定義（API等）を前提としていたのに対し、コマンドライン特有の非構造的な環境で、正確かつ実行可能なコマンド生成能力を直接評価できる点が画期的。また、サンドボックス実行や人間による精査を組み合わせた高精度なデータ検証パイプラインを構築している。 |
| 技術や手法のキモはどこ？ | 公式のドキュメントに基づくデータ生成と、LLMによる検証、サンドボックス実行、人間による修正を組み合わせた多段階の検証パイプライン。さらに、実行を伴わずに推論段階で報酬を計算可能な「ランタイム不要の検証可能報酬（Runtime-free verifiable rewards）」を導入し、強化学習によるモデル改善を効率化した。 |
| どうやって有効だと検証した？ | 24種類の汎用およびセキュリティ特化LLMを対象に、制約の強さが異なる3つのモード（非制約、制約あり、ヒント付き）で評価を実施。SFTおよびGRPO（強化学習）を用いた8Bモデルの微調整が、大規模モデルに匹敵する性能向上を実現することを実証した。 |
| 議論はある？ | 実世界の手動ドキュメントは更新や不整合が生じるため、完全な決定論的評価は困難である点。また、現在の評価は単一ターンのコマンド生成に焦点を当てており、マルチステップの攻撃チェーンや環境適応型の手順は対象外であること。 |
| 次に読むべき論文は？ | [17] API-Bank: A Comprehensive Benchmark for Tool-Augmented LLMs [https://aclanthology.org/2023.emnlp-main.267/](https://aclanthology.org/2023.emnlp-main.267/), [28] The Berkeley Function Calling Leaderboard (BFCL) [https://arxiv.org/abs/2406.11904](https://arxiv.org/abs/2406.11904) |
| PDFリンク | https://arxiv.org/pdf/2610.02206v1 |
