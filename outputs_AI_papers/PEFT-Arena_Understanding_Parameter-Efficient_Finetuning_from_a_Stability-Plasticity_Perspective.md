---
title: "PEFT-Arena: Understanding Parameter-Efficient Finetuning from a Stability-Plasticity Perspective"
date: 2026-05-28
arxiv_id: 2605.28819v1
url: http://arxiv.org/abs/2605.28819v1
---

# PEFT-Arena: Understanding Parameter-Efficient Finetuning from a Stability-Plasticity Perspective

| 項目 | 内容 |
|---|---|
| どんなもの？ | パラメータ効率の良い微調整（PEFT）における「安定性と可塑性のジレンマ（適応能力と汎用的な知識保持の両立）」を評価するための新しいベンチマーク「PEFT-Arena」を提案した研究。モデルの微調整が内部の重みや活性化の幾何構造に与える影響を分析し、過学習（オーバーシュート）を診断・改善する手法を提示している。 |
| 先行研究と比べてどこがすごい？ | 従来のPEFT評価がターゲットタスクの性能向上のみを重視していたのに対し、汎用的な能力の保持（抵抗力）を同時に測定する評価軸を導入した点。また、内部幾何学的な視点から、なぜ特定のPEFT手法が汎用性能を保持できるのかを解明し、事後的な性能回復手法（パスワイズ・リワインディング）を提案した点。 |
| 技術や手法のキモはどこ？ | 重み空間でのスペクトル分析と、活性化空間での表現の幾何学的な歪み（Procrustes residual等）を測定することで、モデル内部の劣化を定量化した点。また、線形補間ではなく各手法の自然な更新経路（OFTならCayley経路など）に基づいた補間を行い、最適化の「行き過ぎ（オーバーシュート）」を診断するアプローチ。 |
| どうやって有効だと検証した？ | Qwen2.5-7BとLlama3.2-3Bを用いた数学・医療タスクへの微調整実験を実施。多数のPEFTベースライン（LoRA, PiSSA, OFT等）を、ターゲットタスク精度と汎用能力保持のパレートフロンティア上で比較。さらに、提案手法によるリワインディングが、汎用能力の劣化を抑えつつターゲットタスクの精度を維持できることを示した。 |
| 議論はある？ | 現在の分析は実証的な診断に基づくものであり、忘却の完全な因果理論を構築したわけではないこと。また、評価対象が主に英語のベンチマークに限られている点や、重み更新を陽に扱わないプロンプトチューニング等の手法への適用には拡張が必要であること。 |
| 次に読むべき論文は？ | [LoRA: Low-rank adaptation of large language models](https://arxiv.org/abs/2106.09685), [Orthogonal finetuning made scalable](https://arxiv.org/abs/2501.05559), [The stability-plasticity dilemma: Investigating the continuum from catastrophic forgetting to age-limited learning effects](https://doi.org/10.3389/fpsyg.2013.00504) |
| PDFリンク | https://arxiv.org/pdf/2605.28819v1 |
