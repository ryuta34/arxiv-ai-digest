---
title: "CSF: Contextual Safety Filtering for Motion Generators"
date: 2026-10-10
arxiv_id: 2610.12467v1
url: http://arxiv.org/abs/2610.12467v1
---

# CSF: Contextual Safety Filtering for Motion Generators

| 項目 | 内容 |
|---|---|
| どんなもの？ | 言語指示に基づくモーション生成モデルに対し、学習不要で適用可能なセマンティック安全フィルター「CSF (Contextual Safety Filtering)」を提案。動的なシーンコンテキストに基づき、安全でない動作をリアルタイムで検出し、安全な動作へと誘導することでロボットの安全な動作生成を実現する手法。 |
| 先行研究と比べてどこがすごい？ | 既存手法と異なり、生成モデルの再学習や追加の安全性モデルの訓練を一切必要としない。また、単なるプロンプトのチェックや幾何学的制約だけでなく、言語的な意味と視覚的なシーン情報を組み合わせて、同じ動作でも状況に応じて安全か否かを動的に判断できる。 |
| 技術や手法のキモはどこ？ | 生成モデル自体が出力する「安全な参照軌道」と「危険な参照軌道」の差分からセマンティックな境界（アフィン・マージン）を定義し、CBF-QP（制御バリア関数を用いた二次計画問題）で最小限の介入で安全な軌道に修正する点。また、実行時にシーンが変化しても追従する動的なシールド機能を持つ点。 |
| どうやって有効だと検証した？ | 4種類の既存のプレトレイン済み生成モデル（Kimodo-G1, ECHO, MotionHiFlow, ARDY）に適用し、2,688のテストケースで検証。実機Unitree G1ロボットにおいても、人との対面や物とのインタラクションを含む多様なシナリオで、安全でない動作を適切に遮断・誘導できることを実証した。 |
| 議論はある？ | 現在は「ポーズ」の修正に焦点を当てており、ロボットの根本的な移動（Locomotion）や経路の変更には対応できていない。また、より複雑で進化し続けるインタラクションに対応するため、リアルタイムでの安全な継続動作の生成能力向上が将来の課題である。 |
| 次に読むべき論文は？ | [8] A. D. Ames et al., "Control barrier functions: Theory and applications" (CBFの基礎), [4] K. Zhao et al., "Autoregressive diffusion with hybrid representation for interactive human motion generation" (ARDYモデルの詳細) |
| PDFリンク | https://arxiv.org/pdf/2610.12467v1 |
