---
title: "RAD-2: Scaling Reinforcement Learning in a Generator-Discriminator Framework"
date: 2026-04-17
arxiv_id: 2604.15308v1
url: http://arxiv.org/abs/2604.15308v1
---

# RAD-2: Scaling Reinforcement Learning in a Generator-Discriminator Framework

| 項目 | 内容 |
|---|---|
| どんなもの？ | 自動運転のモーションプランニングに向けた、拡散モデルベースのジェネレータと強化学習（RL）ベースのディスクリミネータを組み合わせた新しいフレームワーク「RAD-2」。高次元な軌道生成と効率的な報酬フィードバックを分離することで、閉ループ環境での安定した学習を実現している。 |
| 先行研究と比べてどこがすごい？ | 従来の拡散モデルを用いたプランナーの課題であった「強化学習の不安定さ」や「報酬割り当ての困難さ」を、高次元の軌道から低次元のスコアを予測するディスクリミネータへの分離により解決。また、BEV-Warpという高速なシミュレーション環境により大規模な強化学習を可能にした点。 |
| 技術や手法のキモはどこ？ | ①高次元軌道ではなく低次元スコアをRLで最適化する分離設計、②時間的一貫性を持たせたサンプリングと「TC-GRPO」による安定したポリシー勾配、③BEV特徴空間での空間ワーピングを用いた「BEV-Warp」による高効率な閉ループ学習。 |
| どうやって有効だと検証した？ | BEV-Warp環境および3D Gaussian Splattingを用いたフォトリアルなシミュレーション環境で評価。従来の拡散モデルベースの手法と比較し、衝突率を56%低減し、安全性と走行効率の両面で優れた性能を実証した。 |
| 議論はある？ | 現在のBEV-WarpはBEV表現に特化しているため、生画像ベースや他の潜在表現アーキテクチャへの汎用性に制限がある。今後は、より柔軟な「生成世界モデル（Generative World Models）」との統合により、さらに複雑な環境への適応を目指す。 |
| 次に読むべき論文は？ | [RAD: Training an end-to-end driving policy via large-scale 3dgs-based reinforcement learning](https://arxiv.org/abs/2502.13144), [GenAD: Generative end-to-end autonomous driving](https://arxiv.org/abs/2405.00693) |
| PDFリンク | https://arxiv.org/pdf/2604.15308v1 |
