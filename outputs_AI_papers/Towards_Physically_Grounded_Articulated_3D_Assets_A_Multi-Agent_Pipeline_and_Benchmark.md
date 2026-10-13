---
title: "Towards Physically Grounded Articulated 3D Assets: A Multi-Agent Pipeline and Benchmark"
date: 2026-10-13
arxiv_id: 2610.13947v1
url: http://arxiv.org/abs/2610.13947v1
---

# Towards Physically Grounded Articulated 3D Assets: A Multi-Agent Pipeline and Benchmark

| 項目 | 内容 |
|---|---|
| どんなもの？ | 物理的に正しく動作し、ロボットのシミュレーション環境で直接使用可能な関節付き3Dアセットを生成するためのマルチエージェント型パイプライン「ARTISAN」と、その性能を評価する包括的なベンチマーク。従来の生成手法が抱えていた物理的な不整合（衝突や不安定さ）を解決し、実用的な3D資産を作成する。 |
| 先行研究と比べてどこがすごい？ | 単一エージェントによる自己評価の限界（自己評価バイアス）を、設計・コーディング・レビューの3つの独立したエージェントによるパイプラインで解消した点。また、従来の手法とは異なり、物理シミュレーター（MuJoCo）からのフィードバックを直接生成プロセスに組み込むことで、極めて高い物理的妥当性（低衝突率・高安定性）を実現した点。 |
| 技術や手法のキモはどこ？ | 設計・コーディング・レビューの3エージェントによる分業体制に加え、物理エンジンを用いたフィードバックループを構築したこと。さらに、機械設計を模した標準コネクタの採用や、物理的に正しい質量の推論、衝突回避のための自動修正プログラムなど、シミュレーション準備済みアセット生成のための具体的ツール群を備えた点。 |
| どうやって有効だと検証した？ | 空間的忠実度、物理的妥当性（衝突・安定性・質量）、ロボット操作タスクへの適用可能性の4側面から評価。10種以上の代表的なモデルと比較し、ARTISANが空間的忠実度で競合しつつ、衝突率の大幅な削減と安定性の向上を実現したことを示した。また、ロボットアームの操作実験を通じ、生成アセットの機能的有用性を証明した。 |
| 議論はある？ | 現在の手法はAPIコストが比較的高く、生成時間が長くなる傾向がある。また、ロボットの動作において物理的に可能であっても、参照されたデモンストレーションの動作形式と生成された機構が一致しない「軌道転送の失敗」が課題として挙げられている。 |
| 次に読むべき論文は？ | [Articraft: An agentic system for scalable articulated 3d asset generation (Zhou et al., 2026)](https://arxiv.org/abs/2608.17975)、[RoboTwin 2.0: A scalable data generator and benchmark with strong domain randomization (Chen et al., 2026)](https://openreview.net/forum?id=itonej9GIV) |
| PDFリンク | https://arxiv.org/pdf/2610.13947v1 |
