---
title: "Introspective Coupling: Self-Explanation Training Tracks Behavioral Change Despite Fixed Supervision"
date: 2026-07-01
arxiv_id: 2606.32038v1
url: http://arxiv.org/abs/2606.32038v1
---

# Introspective Coupling: Self-Explanation Training Tracks Behavioral Change Despite Fixed Supervision

| 項目 | 内容 |
|---|---|
| どんなもの？ | 言語モデルの出力に対する「自己説明」を訓練する際、モデルが訓練用ラベルを模倣するだけでなく、モデル自身の現在の動作を忠実に反映した内省的説明を行えるようになる現象（introspective coupling）を明らかにした研究。固定された過去のデータセットで訓練しても、モデルが自身の動作ドリフトを捉えて説明を適応させる能力を持つことを示した。 |
| 先行研究と比べてどこがすごい？ | 従来はモデルの出力を説明させるために、その都度最新の動作データでラベルを更新する必要があると考えられていたが、本手法では固定された静的なラベルからでも、訓練中にモデルの動作を適切に正則化することで、自己の動作を追従可能な自己説明能力が獲得できることを実証した点。 |
| 技術や手法のキモはどこ？ | KLダイバージェンスを用いた「動作の正則化」を説明訓練と併用すること。これにより、モデルが説明ターゲット（過去の動作）から乖離しすぎず、かつ訓練中に変化するモデル自身の現在の挙動と整合性を保つための「内省的結合」が生じる。また、この説明能力は異なるモデル間で得られたラベルに対しても汎用可能である点。 |
| どうやって有効だと検証した？ | Sycophancy（追従）や拒絶行動に関する3つのデータセット（Hint-MMLU, AITA, Refusal）を用い、説明の正解率（EM）を評価。さらに、訓練中に発生する動作の変化に対して説明も適切に追従しているかを確認し、機械的な解釈性解析（Activation Patching）を通じて動作と説明の回路が共有されていることを証明した。 |
| 議論はある？ | 訓練データにおける動作の多様性が不足していると、説明訓練の信号自体が崩壊する可能性があること。また、内省的結合の出現メカニズムに関する理論的な説明は一部不完全であり、なぜ高い学習率でこのギャップが広がるのかなど、複数の要因が絡み合っている点などが今後の課題。 |
| 次に読むべき論文は？ | [Looking inward: Language models can learn about themselves by introspection (Binder et al., 2025)](https://openreview.net/forum?id=eb5pkwIB5i)、[Training language models to explain their own computations (Li et al., 2025a)](https://arxiv.org/abs/2511.08579) |
| PDFリンク | https://arxiv.org/pdf/2606.32038v1 |
