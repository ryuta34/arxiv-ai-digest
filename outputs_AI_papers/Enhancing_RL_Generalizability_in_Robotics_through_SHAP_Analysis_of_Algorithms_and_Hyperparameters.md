---
title: "Enhancing RL Generalizability in Robotics through SHAP Analysis of Algorithms and Hyperparameters"
date: 2026-05-05
arxiv_id: 2605.02867v1
url: http://arxiv.org/abs/2605.02867v1
---

# Enhancing RL Generalizability in Robotics through SHAP Analysis of Algorithms and Hyperparameters

| 項目 | 内容 |
|---|---|
| どんなもの？ | 強化学習（RL）モデルのロボット環境間における汎化性能を向上させるため、SHAP（Shapley Additive exPlanations）を用いてアルゴリズムやハイパーパラメータが汎化性能に与える影響を定量化する説明可能なAIフレームワーク。 |
| 先行研究と比べてどこがすごい？ | 従来の手法では汎化性能への寄与がブラックボックス化されていたが、本研究はShapley値を用いて汎化誤差に対する各構成要素の貢献度を理論的・定量的に分解し、最適なハイパーパラメータを選択する体系的なガイドラインを提供した点。 |
| 技術や手法のキモはどこ？ | 汎化性能の理論的なバウンド（理論1）とShapley値による分解（理論2）を接続し、汎化誤差の最小化をSHAPによる感度分析を通じて実現する点。サンプリングされた構成のモデル群からSHAP explainerを構築し、影響パターンを可視化・最適化する点。 |
| どうやって有効だと検証した？ | MuJoCoとPyBulletの物理エンジン間における双方向のSim2Sim転移実験（4つの標準的なロボットタスク）を実施。予測された「最適」および「最悪」の構成と、実際の汎化性能を比較し、理論的な正当性とフレームワークの実用的な有効性を確認した。 |
| 議論はある？ | 現在の検証はシミュレーション環境間の転移に限定されている。また、ハイパーパラメータの組み合わせは探索的であり、より複雑な環境や高次元タスクへの拡張は今後の課題である。 |
| 次に読むべき論文は？ | [Raffin et al., Stable-Baselines3: Reliable reinforcement learning implementations (2021)](https://jmlr.org/papers/v22/20-1364.html)、[Beechey et al., Explaining reinforcement learning with shapley values (2023)](https://proceedings.mlr.press/v202/beechey23a.html) |
| PDFリンク | https://arxiv.org/pdf/2605.02867v1 |
