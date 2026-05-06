---
title: "Large Language Models are Universal Reasoners for Visual Generation"
date: 2026-05-06
arxiv_id: 2605.04040v1
url: http://arxiv.org/abs/2605.04040v1
---

# Large Language Models are Universal Reasoners for Visual Generation

| 項目 | 内容 |
|---|---|
| どんなもの？ | 大規模言語モデル（LLM）の「推論能力」を活用し、テキストから画像を生成する際の手順を最適化するフレームワーク「UniReasoner」。生成前の「視覚的なドラフト作成」と「自己評価による修正指示」をパイプラインに組み込むことで、複雑なプロンプトに対する忠実度を大幅に向上させる。 |
| 先行研究と比べてどこがすごい？ | 従来のモデルが単一のテキスト埋め込みに依存しがちであったのに対し、本手法はLLMの推論能力を用いて、生成プロセス中に「具体的な計画」と「誤りの修正指示」を動的に生成する。拡散モデルのアーキテクチャを変更することなく、推論と生成のギャップ（理解はできるが生成時に失敗する問題）を解消した点。 |
| 技術や手法のキモはどこ？ | 「Draft-Evaluate-Diffuse」パイプラインの採用。まずSigLIP 2に基づく離散トークンで粗い視覚ドラフトを作成し、次にLLM自身がそのドラフトを評価して「どこを修正すべきか」をテキストで言語化する。このドラフトと評価結果の双方を条件として拡散モデルを駆動させることで、高精度な生成を実現する。 |
| どうやって有効だと検証した？ | GenEvalおよびDPG-Benchといった指標を用い、ベースとなるSANA拡散モデルの構造を固定した状態で比較実験を実施。特に計数（Counting）、位置関係（Position）、属性結合（Attr. Binding）といった複雑な制約条件において大幅な性能向上が確認された。 |
| 議論はある？ | 現在の手法は拡散モデル自体の推論（デノイジング）を条件付けによって制御するものであり、アーキテクチャの変更は不要だが、ドラフト作成と自己評価のために推論ステップが増えることが示唆される。また、さらに高度な物理的・論理的整合性を求める場合の限界については今後の課題。 |
| 次に読むべき論文は？ | [SANA: Efficient High-Resolution Text-to-Image Synthesis with Linear Diffusion Transformers](https://arxiv.org/abs/2501.17811) や [BAGEL: Emerging Properties in Unified Multimodal Pretraining](https://arxiv.org/abs/2505.14683) |
| PDFリンク | https://arxiv.org/pdf/2605.04040v1 |
