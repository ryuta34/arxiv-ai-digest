---
title: "Masked Visual Actions for Unified World Modeling"
date: 2026-07-22
arxiv_id: 2607.19343v1
url: http://arxiv.org/abs/2607.19343v1
---

# Masked Visual Actions for Unified World Modeling

| 項目 | 内容 |
|---|---|
| どんなもの？ | ロボットの動作を「ピクセル空間上の部分的に隠された軌道（Masked Visual Actions）」として表現し、事前学習済みの動画生成モデルを条件付きでファインチューニングすることで、汎用的なロボット世界モデルを実現する手法です。単一のチェックポイントで、ロボットの動作をシミュレートする順モデルと、目標から動作を逆算する逆モデルの両方を統合的に扱います。 |
| 先行研究と比べてどこがすごい？ | 従来のロボット用世界モデルが特定のロボットの物理パラメータや低次元の行動ベクトルに依存していたのに対し、本手法は視覚ベースのマスキングを用いることで、ロボットの形態（エボディメント）に依存せず、未知のロボットに対してもゼロショットで汎化できる点です。 |
| 技術や手法のキモはどこ？ | 動画内のロボットや対象物を「アクティブ（能動的）」と「パッシブ（受動的）」な実体として捉え、それらを部分的にマスキングして入力することで、同じ動画生成モデルを順・逆の両方向の推論にスイッチングして利用する点です。 |
| どうやって有効だと検証した？ | DROIDおよびRobocasaのデータセットを用い、ポリシー評価、モデルベース計画、逆動力学モデルによる動作抽出の3つのタスクで評価しました。また、BEHAVIOR-1K等の未知のロボット形態に対する汎化性能を定量的および定性的に検証しました。 |
| 議論はある？ | 因果関係ではなく相関関係を学習している点や、推論速度がベースとなる動画生成モデルの能力に制限される点が挙げられます。また、強力な生成モデルゆえに、不適切なロボット動作や安全上の懸念がある点も課題として認識されています。 |
| 次に読むべき論文は？ | [13] Wan-move: Motion-controllable video generation via latent trajectory guidance, [25] Ctrl-world: A controllable generative world model for robot manipulation, [63] Wan: Open and advanced large-scale video generative models |
| PDFリンク | https://arxiv.org/pdf/2607.19343v1 |
