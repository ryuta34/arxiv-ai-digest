---
title: "HANDOFF: Humanoid Agentic Task-Space Whole-Body Control via Distilled Complementary Teachers"
date: 2026-06-07
arxiv_id: 2606.06493v1
url: http://arxiv.org/abs/2606.06493v1
---

# HANDOFF: Humanoid Agentic Task-Space Whole-Body Control via Distilled Complementary Teachers

| 項目 | 内容 |
|---|---|
| どんなもの？ | 人型ロボットのための、汎用性が高くモジュール化されたタスク空間全身コントローラー「HANDOFF」の提案。言語指示を用いたエージェント型プランナーと組み合わせることで、複雑な全身操作タスクをデータセットの収集やモデルの微調整なしに実行可能にした。 |
| 先行研究と比べてどこがすごい？ | 従来の全身コントローラーが要求していた「密な関節運動軌道」の代わりに、プランナーから直接扱える「コンパクトな10次元のタスク空間コマンド（ベース速度、高さ、手首ターゲット）」を採用した点。これにより、高レベルのプランナーやVLMと容易に統合可能となった。 |
| 技術や手法のキモはどこ？ | 3つの専門教師モデル（全身追従、移動、転倒回復）を、コンテキスト条件付きの混合専門家（MoE）アーキテクチャを通じて単一の学生モデルへ蒸留した点。状況に応じて各専門家の能力を適応的に切り替える蒸留スキームが核心。 |
| どうやって有効だと検証した？ | Unitree G1ロボットを用いて、シミュレーションおよび実機環境で検証。速度追従性の精度評価に加え、ロボットが安定して操作可能な「頑健な操作ワークスペース」の体積を定量化し、既存のSOTA手法と比較して優れた性能を達成した。 |
| 議論はある？ | 現在は手首の3次元位置ターゲットのみを扱っており、完全な6自由度の把持姿勢には将来的に対応が必要。また、固定カメラによる前方視野の制限や、より多様な環境・接触条件への対応が今後の課題。 |
| 次に読むべき論文は？ | [16] HOMIE: Humanoid Loco-Manipulation with Isomorphic Exoskeleton Cockpit, [23] HOVER: Versatile neural whole-body controller for humanoid robots, [40] Being-0: A humanoid robotic agent with vision-language models and modular skills |
| PDFリンク | https://arxiv.org/pdf/2606.06493v1 |
