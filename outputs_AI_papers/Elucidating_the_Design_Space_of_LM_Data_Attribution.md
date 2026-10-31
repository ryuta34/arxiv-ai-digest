---
title: "Elucidating the Design Space of LM Data Attribution"
date: 2026-10-31
arxiv_id: 2610.40655v1
url: http://arxiv.org/abs/2610.40655v1
---

# Elucidating the Design Space of LM Data Attribution

| 項目 | 内容 |
|---|---|
| どんなもの？ | 言語モデル（LM）のデータアトリビューション（どの学習データがモデルの予測に貢献したかを特定する技術）における評価方法の設計空間を解明し、既存手法の性能低下原因を特定した研究。合成データを用いたベンチマーク「CATT」を提案し、損失関数の変更とトークン選択によりアトリビューション精度を大幅に向上させた。 |
| 先行研究と比べてどこがすごい？ | 既存の評価指標は複数のデータセット特性が同時に変化するため要因の切り分けが困難だったが、本研究はデータ冗長性やノイズとなるトークンを個別に制御することで、性能低下の根本原因である「希釈現象（Dilution Phenomenon）」を診断・特定した点。 |
| 技術や手法のキモはどこ？ | 学習時の損失関数を標準的なクロスエントロピーから「負の対数オッズ（Negative Log-odds）」に変更し、さらに文書全体を平均化するのではなく、重要度の高い「Top-kトークン」のスコアのみを抽出・集約する手法。 |
| どうやって有効だと検証した？ | 合成知識を用いたベンチマーク「CATT」で、文書の冗長性やノイズ（lexical distractors）を操作して実験。さらに、既存の [FTRACE-TREX](https://arxiv.org/abs/2210.02401) ベンチマークにおいても、提案手法が対向事実の再学習による精度低下を従来比最大4.9倍で予測可能であることを示した。 |
| 議論はある？ | Top-k集約には新たなハイパーパラメータ（k）が必要であり、実環境のように正解ラベルが存在しない場合には動的なしきい値決定が課題となる。また、単一のトークン予測に焦点を当てており、複雑な推論を伴うマルチステップの予測には未対応である。 |
| 次に読むべき論文は？ | [Towards tracing knowledge in language models back to the training data](https://arxiv.org/abs/2210.02401)、[Trak: Attributing model behavior at scale](https://arxiv.org/abs/2303.14186)、[Studying large language model generalization with influence functions](https://arxiv.org/abs/2308.03296) |
| PDFリンク | https://arxiv.org/pdf/2610.40655v1 |
