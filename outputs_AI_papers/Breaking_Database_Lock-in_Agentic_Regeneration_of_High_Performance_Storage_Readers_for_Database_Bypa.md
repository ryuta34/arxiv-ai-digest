---
title: "Breaking Database Lock-in: Agentic Regeneration of High Performance Storage Readers for Database Bypass"
date: 2026-07-09
arxiv_id: 2607.07696v1
url: http://arxiv.org/abs/2607.07696v1
---

# Breaking Database Lock-in: Agentic Regeneration of High Performance Storage Readers for Database Bypass

| 項目 | 内容 |
|---|---|
| どんなもの？ | データベースの内部ストレージファイルを直接読み取り、Apache Arrow形式のバッファに変換することで、JDBC/ODBCといった遅いワイヤプロトコルを経由せずに分析エンジンへデータを渡す手法「Jailbreak」を提案する研究。LLMを活用して、対象データベースの複雑なファイルフォーマットを解析する高性能なカスタムリーダーを自動合成する。 |
| 先行研究と比べてどこがすごい？ | 従来はデータベースのエンジン（JDBC等）を通す必要があり、データ変換やシリアライゼーションがボトルネックとなっていた。本手法はデータベースの内部構造をLLMで自動解析してバイパスするため、最大27倍の高速化を実現しつつ、煩雑な手動のパーサー開発工数を劇的に削減した点。 |
| 技術や手法のキモはどこ？ | LLMを活用した4つのエージェント（Dataset Generator, Architect, Coder, QA Tester）による自動合成パイプライン。ドキュメントやソースコードをLLMに ingestion させてカスタムリーダーを生成し、実行エラーが出た場合はフィードバックループを通じて修正を繰り返す点。 |
| どうやって有効だと検証した？ | PostgreSQLとMySQLを対象に、TPC-Hベンチマークデータを用いて検証を実施。DuckDB、DataFusion、PyArrow、Sparkなど6つの分析エンジンを組み合わせ、従来の手法（JDBC/ODBC経由）と性能を比較し、ETL処理において大幅な速度向上を確認した。 |
| 議論はある？ | 今後は生成されるリーダーの収束性やリトライ回数の評価、より広範なデータベースバージョンやスキーマへの対応が必要。また、現在はSQLiteやMongoDBなどへの拡張を将来課題として挙げている。 |
| 次に読むべき論文は？ | [10] GenDB: The Next Generation of Query Processing–Synthesized, Not Engineered (arXiv:2603.02081), [15] Bespoke OLAP: Synthesizing Workload-Specific One-size-fits-one Database Engines (arXiv:2603.02001) |
| PDFリンク | https://arxiv.org/pdf/2607.07696v1 |
