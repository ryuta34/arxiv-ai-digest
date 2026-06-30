---
title: "One-Step Gradient Delay is Not a Barrier for Large-Scale Asynchronous Pipeline Parallel LLM Pretraining"
date: 2026-06-30
arxiv_id: 2606.30634v1
url: http://arxiv.org/abs/2606.30634v1
---

# One-Step Gradient Delay is Not a Barrier for Large-Scale Asynchronous Pipeline Parallel LLM Pretraining

| 項目 | 内容 |
|---|---|
| どんなもの？ | 非同期パイプライン並列学習における勾配の遅延問題（ストーレネス）が、必ずしも大規模言語モデル（LLM）の学習性能を低下させる致命的な障壁ではないことを示した研究。適切なオプティマイザの選択と、勾配遅延を補正する手法を組み合わせることで、同期学習と遜色ない精度を実現した。 |
| 先行研究と比べてどこがすごい？ | 従来、非同期学習は勾配の遅延により性能が低下するというのが通説であったが、オプティマイザの選択（Muon等）と、今回提案した「Error Feedback」を用いた遅延補正により、性能劣化をほぼ解消した点。また、10B規模のモデルにおいても実用性を証明した。 |
| 技術や手法のキモはどこ？ | パイプラインスケジュールにPipeDream-2BWを採用して遅延を「1ステップ」に固定化した点と、過去の勾配差分を現在に加算して補正する「Error Feedback」をオプティマイザに対して適用した点。これにより、オプティマイザの性質に応じた堅牢な学習が可能となった。 |
| どうやって有効だと検証した？ | 135Mから10Bパラメータ規模までのモデルを用いて、様々なオプティマイザとハイパーパラメータの組み合わせで同期学習との比較を実施。最終的な検証損失が同期学習と同等になることを示し、主要なベンチマークタスクでも同様の性能であることを確認した。 |
| 議論はある？ | なぜ高いモメンタムが遅延に対して堅牢なのかというメカニズムの完全な解明には至っていない点や、さらなる巨大モデルでの実証が今後の課題であるとしている。 |
| 次に読むべき論文は？ | [PipeDream: Generalized Pipeline Parallelism for DNN Training](https://arxiv.org/abs/1806.03377) (Narayanan et al., 2019) や [Muon: An optimizer for hidden layers in neural networks](https://kellerjordan.github.io/posts/muon) (Jordan et al., 2024) が基礎として重要。 |
| PDFリンク | https://arxiv.org/pdf/2606.30634v1 |
