---
title: "VidForensics-M1: Meta-Detection Reinforcement Learning with Verifiable Temporal Grounding for AI-Generated Video Forensics"
date: 2026-08-12
arxiv_id: 2608.11201v1
url: http://arxiv.org/abs/2608.11201v1
---

# VidForensics-M1: Meta-Detection Reinforcement Learning with Verifiable Temporal Grounding for AI-Generated Video Forensics

| 項目 | 内容 |
|---|---|
| どんなもの？ | AI生成動画の検出において、「メタ検出」という概念を導入し、ラベルの正しさと証拠（時間的根拠）の妥当性を統合的に最適化する新しい強化学習フレームワーク「VidForensics-M1」を提案した。 |
| 先行研究と比べてどこがすごい？ | テキストベースの根拠（モデル生成）は幻覚やバイアスに弱いが、提案手法は制御可能なデータ生成プロセスから得られる客観的かつ検証可能な「時間的根拠（temporal grounding）」を用いることで、より堅牢で汎用性の高い検出を実現した点。 |
| 技術や手法のキモはどこ？ | （1）境界フレームを用いた自動的なペアデータ構築、（2）証拠の質に応じてラベル正解サンプル内の報酬を再分配する「証拠誘導型報酬再分配（EGRR）」アルゴリズム。 |
| どうやって有効だと検証した？ | ViF-BenchおよびGenBuster-Benchを用い、従来のラベルレベルの強化学習と比較。精度、再現率、F1スコアにおいて大幅な向上を確認し、特に未知のデータセットやWild環境での汎用性の高さを示した。 |
| 議論はある？ | 現在は時間的な操作に基づいているが、より複雑な物理違反や空間的なアーティファクトの検出には、さらなる高度な証拠定義やアノテーションの手法が必要となる可能性がある。 |
| 次に読むべき論文は？ | [16] VidGuard-R1: AI-generated video detection and explanation via reasoning MLLMs and RL ([arXiv:2510.02282](https://arxiv.org/abs/2510.02282)) |
| PDFリンク | https://arxiv.org/pdf/2608.11201v1 |
