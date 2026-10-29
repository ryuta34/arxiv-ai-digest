---
title: "Can Discrete Tokens Serve as Semantically Lossless Representations of Visual Signals?"
date: 2026-10-29
arxiv_id: 2610.37662v1
url: http://arxiv.org/abs/2610.37662v1
---

# Can Discrete Tokens Serve as Semantically Lossless Representations of Visual Signals?

| 項目 | 内容 |
|---|---|
| どんなもの？ | 離散的な視覚トークン（量子化）がセマンティックな情報を損失するという従来の通説に異を唱え、十分なビット予算があれば連続値表現に匹敵する性能を実現できることを示した研究。新しい量子化手法「FVQ (Factorized Vector Quantization)」を提案し、大規模なマルチモーダルモデルで最先端の性能を達成した。 |
| 先行研究と比べてどこがすごい？ | 従来の量子化手法（RVQやPQ）は、コードブックが増えるほど情報が飽和するという課題があったが、提案するFVQはスケールしても性能が向上し続け、連続値表現（Qwen3-VL等）と同等の理解能力を達成した点。特にOCRやドキュメント理解といった高精度が求められるタスクで顕著な改善が見られる。 |
| 技術や手法のキモはどこ？ | 特徴量を複数の固定次元の視覚に分解し、独立した対称的なコードブックで並列量子化を行うFVQの導入。さらに、情報損失を防ぐために「タイトフレーム（tight-frame）」条件を制約として課すことで、すべての特徴次元がバランスよく保持される設計になっている点。 |
| どうやって有効だと検証した？ | 8つの主要なマルチモーダル理解ベンチマーク（MMMU, MathVista, OCRBench等）において、既存の離散表現モデル（UniAR, Emu3-Chat）と比較し、平均スコアで大幅に上回る性能を確認した。また、高解像度の長いドキュメント読解などの難関ケースを用いた定性評価も実施。 |
| 議論はある？ | 量子化誤差とセマンティックな忠実度は直接相関しないことを指摘したが、さらなる高精度化に向けて、より大規模なデータやトークン長での挙動、また生成タスクへの適用におけるビット予算の最適配分などが今後の課題として挙げられる。 |
| 次に読むべき論文は？ | [Qwen3-VL technical report](https://arxiv.org/abs/2511.21631)、[UniAR: Unified multimodal autoregressive modeling](https://arxiv.org/abs/2606.18249)、[Emu3: Next-token prediction is all you need](https://arxiv.org/abs/2409.18869) |
| PDFリンク | https://arxiv.org/pdf/2610.37662v1 |
