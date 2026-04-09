---
title: "Measurement of Generative AI Workload Power Profiles for Whole-Facility Data Center Infrastructure Planning"
date: 2026-04-09
arxiv_id: 2604.07345v1
url: http://arxiv.org/abs/2604.07345v1
---

# Measurement of Generative AI Workload Power Profiles for Whole-Facility Data Center Infrastructure Planning

| 項目 | 内容 |
|---|---|
| どんなもの？ | 生成AIワークロード（学習・ファインチューニング・推論）の高分解能な電力消費プロファイルを測定し、それを基にデータセンター全体の施設レベルのエネルギー需要をシミュレーションする手法を提案した研究。本研究では、測定データセットを公開するとともに、インフラ計画や負荷予測に活用可能な「DIPLOEE」モデルを開発した。 |
| 先行研究と比べてどこがすごい？ | 既存のデータセンターエネルギーモデルは proprietory（非公開）なデータに依存したり、解像度が不十分であったりしたが、本研究はNVIDIA H100 GPUを用いた0.1秒単位の高分解能な実測値に基づいている点。また、標準的なベンチマーク（MLCommons, vLLM）を採用し、再現性と透明性を確保した点。 |
| 技術や手法のキモはどこ？ | ノードレベルの消費電力プロファイルを、離散イベントシミュレーション（SimPyを用いた「DIPLOEE」）を通じて、施設全体の運用データやユーザー行動パターンと組み合わせ、大規模なデータセンターの電力需要推移へスケーリングするボトムアップ型のモデリング手法。 |
| どうやって有効だと検証した？ | 10MWのコロケーションデータセンターおよび1MWの推論データセンターの2つのケーススタディを実施。1年間の運用を1分単位のタイムステップでシミュレーションし、稼働率の変動や要求トラフィックが施設全体の電力消費プロファイル（ピーク・平均電力、PAR等）に与える影響を定量的に分析した。 |
| 議論はある？ | 特定のハードウェアや限られたアルゴリズム設定での測定である点。また、冷却装置等の補助負荷や、実環境の多様な運用プロファイルを完全には網羅できていない点。今後は熱・電気インフラモデルとの統合や、より広範なモデル、プラットフォームへの拡張が必要。 |
| 次に読むべき論文は？ | [1] Shehabi et al. (2024), "2024 United States Data Center Energy Usage Report" (doi:10.71468/P1WC7Q)<br>[13] Latif et al. (2024), "Empirical measurements of ai training power demand on a gpu-accelerated node" (arXiv:2412.08602)<br>[14] Patel et al. (2024), "Characterizing power management opportunities for llms in the cloud" (doi:10.1145/3620666.3651329) |
| PDFリンク | https://arxiv.org/pdf/2604.07345v1 |
