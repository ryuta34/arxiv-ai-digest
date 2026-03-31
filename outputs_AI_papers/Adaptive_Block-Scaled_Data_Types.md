---
title: "Adaptive Block-Scaled Data Types"
date: 2026-03-31
arxiv_id: 2603.28765v1
url: http://arxiv.org/abs/2603.28765v1
---

# Adaptive Block-Scaled Data Types

| 項目 | 内容 |
|---|---|
| どんなもの？ | 大規模言語モデル（LLM）の量子化における精度低下問題を解決する「適応的ブロック量子化（Adaptive Block-Scaled Data Types）」を提案した論文。FP4（浮動小数点）とINT4（整数）をグループ単位で動的に切り替えるIF4データ形式を導入し、トレーニングと推論の両面で精度と効率を両立させている。 |
| 先行研究と比べてどこがすごい？ | 従来のNVFP4や4/6量子化が抱えていた、最大値付近での量子化誤差や動的レンジの減少といった課題を克服した。IF4はメモリオーバーヘッドを一切追加せず、既存フォーマットと比較して量子化誤差を低減し、様々なタスクで高い精度を達成している。 |
| 技術や手法のキモはどこ？ | FP8スケール因子の未使用の符号ビットを「指標（Indicator）」として流用し、グループごとに最適な表現形式（FP4またはスケール済みINT4）を選択する点。また、INT4選択時には7/6倍のスケーリングを行い、FP4と表現範囲を統一する「6/7メソッド」により、ハードウェア効率を損なわずに適応的な量子化を実現した。 |
| どうやって有効だと検証した？ | 3.4億パラメータのTransformerモデルの事前学習や、Qwen3.5シリーズを用いたW4A4量子化による評価を実施。WikiText-2/C4のパープレキシティおよびARC、HellaSwag等の下流タスクで検証し、ハードウェアレベルでは28nm CMOSを用いたMACユニットの設計・合成により、低オーバーヘッドであることを示した。 |
| 議論はある？ | IF4および4/6量子化を確率的丸め（Stochastic Rounding）と組み合わせた際に発生する量子化バイアスが課題として挙げられる。ただし、この影響を受ける勾配は全体の極少数であり、性能低下は軽微であることを確認済み。今後はより大規模な実験による精査が必要である。 |
| 次に読むべき論文は？ | [Four Over Six: More Accurate NVFP4 Quantization with Adaptive Block Scaling](https://arxiv.org/abs/2512.02010)、[Quartet II: Accurate LLM Pre-Training in NVFP4 by Improved Unbiased Gradient Estimation](https://arxiv.org/abs/2601.22813) |
| PDFリンク | https://arxiv.org/pdf/2603.28765v1 |
