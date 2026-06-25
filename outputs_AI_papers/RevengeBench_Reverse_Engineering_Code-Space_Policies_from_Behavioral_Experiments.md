---
title: "RevengeBench: Reverse Engineering Code-Space Policies from Behavioral Experiments"
date: 2026-06-25
arxiv_id: 2606.26094v1
url: http://arxiv.org/abs/2606.26094v1
---

# RevengeBench: Reverse Engineering Code-Space Policies from Behavioral Experiments

| 項目 | 内容 |
|---|---|
| どんなもの？ | 大規模言語モデル（LLM）が、ゲーム環境における他エージェントの行動ログから、その内部的な意思決定プログラムを逆工学的に再現できるかを測定する新しいベンチマーク「REVENGEBENCH」を提案した研究です。 |
| 先行研究と比べてどこがすごい？ | 従来のプログラム合成や行動理解研究と異なり、環境への介入が「相手の行動を誘発する対戦相手プログラムの作成」という制約付きの実験操作に限定されており、より現実的な科学的推論に近い環境でモデルの能力を評価できる点です。 |
| 技術や手法のキモはどこ？ | コードをエージェントの意思決定ロジックの表現として扱い、対戦相手の行動を観察・分析しながら、独自作成した対戦相手（プローブ）で環境を能動的に操作し、繰り返しコードを修正して再現精度を高める「閉ループ型逆工学パイプライン」を導入した点です。 |
| どうやって有効だと検証した？ | 5つのゲーム環境、合計75のターゲットポリシーに対し、12種類の最新LLMを用いて再現実験を実施しました。さらに、再現したコードを用いて対戦での勝率が向上するか（戦略的な価値があるか）を検証しました。 |
| 議論はある？ | 再現プログラムの忠実度は環境依存で、特に複雑なゲームでは高い分散が生じることが課題です。また、行動ログの再現は、必ずしも元のターゲットと同一のプログラムを導出する唯一解ではなく、機能的に等価なクラスの一つを抽出しているに過ぎない可能性が指摘されています。 |
| 次に読むべき論文は？ | [Jha et al., 2026: Modeling others’ minds as code](https://openreview.net/forum?id=vHXo7xIer6), [Bachrach et al., 2025: Combining code generating large language models and self-play to iteratively refine strategies in games](https://arxiv.org/abs/2508.10999) |
| PDFリンク | https://arxiv.org/pdf/2606.26094v1 |
