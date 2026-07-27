---
title: "Explainable Reinforcement Learning for assisting Air Traffic Controllers"
date: 2026-07-27
arxiv_id: 2607.22525v1
url: http://arxiv.org/abs/2607.22525v1
---

# Explainable Reinforcement Learning for assisting Air Traffic Controllers

| 項目 | 内容 |
|---|---|
| どんなもの？ | 航空交通管制（ATC）におけるAIの信頼性向上を目指し、深層強化学習（DQN）を用いた自動航行システムに説明可能性（XAI）を組み込んだ研究。エージェントの意思決定過程を可視化する手法を提案している。 |
| 先行研究と比べてどこがすごい？ | ブラックボックス化しやすい深層強化学習モデルに対し、Saliency Map（顕著性マップ）を用いて入力特徴量ごとの重要度を時間経過に応じて提示する手法を導入した点。 |
| 技術や手法のキモはどこ？ | 飛行状態（位置、速度、目標距離、NFZ座標など）を入力としたDQNモデルに対し、最大Q値の入力状態に対する勾配を算出することで、エージェントが各フェーズで何を重視して意思決定したかを定量的かつ視覚的に明らかにしたこと。 |
| どうやって有効だと検証した？ | 2Dのグリッド環境（40×40マイル）における航空機の航行タスクをシミュレーション。飛行軌道の分析に加え、航行中の各フェーズ（初期、NFZ回避、最終アプローチ）におけるSaliency Mapの変化を追跡し、安全と効率のバランスが適切に調整されていることを実証した。 |
| 議論はある？ | 現在は単純化された環境でのテストにとどまっており、より複雑で現実的な航空シナリオへの拡張が課題。また、モデルの複雑さと解釈可能性のトレードオフ、既存レガシーシステムとの統合が挙げられている。 |
| 次に読むべき論文は？ | Heuillet et al., [Explainability in deep reinforcement learning](https://doi.org/10.1016/j.knosys.2020.106685) |
| PDFリンク | https://arxiv.org/pdf/2607.22525v1 |
