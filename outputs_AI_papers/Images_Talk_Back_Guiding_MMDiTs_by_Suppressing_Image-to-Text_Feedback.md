---
title: "Images Talk Back: Guiding MMDiTs by Suppressing Image-to-Text Feedback"
date: 2026-10-13
arxiv_id: 2610.13941v1
url: http://arxiv.org/abs/2610.13941v1
---

# Images Talk Back: Guiding MMDiTs by Suppressing Image-to-Text Feedback

| 項目 | 内容 |
|---|---|
| どんなもの？ | マルチモーダル拡散モデル（MMDiT）における「画像からテキストへのフィードバック」が、プロンプトに反する誤った内容を維持・増幅させてしまう現象を解明し、これを抑制することで生成品質を向上させる新しいガイダンス手法「Semantic Feedback Guidance (SFG)」を提案した論文。 |
| 先行研究と比べてどこがすごい？ | 従来手法（PAGやSEG等）がモデル自体を劣化させることで負の勾配を生成していたのに対し、本手法はモデルの「I2Tフィードバックパス」を測定・操作することで、モデルの性能を落とさずにオブジェクトの保持や属性の整合性を改善できる点。 |
| 技術や手法のキモはどこ？ | I2Tフィードバックを強化した「ネガティブブランチ」を意図的に作成し、その方向からガイダンスを遠ざけることでフィードバックを抑制する点。また、追加のモデル推論なしに適用可能な「iSFG」というインプレース（in-place）型の最適化手法も実現している点。 |
| どうやって有効だと検証した？ | SD3M、SD3.5M、FLUX等の生成モデルを用い、GenEvalやT2I-CompBench++などのベンチマークで評価。また、テキストから動画、画像から動画への転送においてもVBenchでベースラインを上回る結果を示し、消去プローブを用いてフィードバック抑制の有効性を確認した。 |
| 議論はある？ | ガイダンスウィンドウの最適化はタスクによって異なり、単純に全ステップで適用することが必ずしも最良ではないこと。また、フィードバック抑制が成功に寄与する一方で、過度な抑制が当初の成功例を損なう可能性があることも示唆されている。 |
| 次に読むべき論文は？ | [Classifier-free diffusion guidance (Ho & Salimans, 2022)](https://arxiv.org/abs/2207.12598) や [Self-rectifying diffusion sampling with perturbed-attention guidance (Ahn et al., 2024)](https://arxiv.org/abs/2403.02392) など、拡散モデルにおけるガイダンスの基礎論文。 |
| PDFリンク | https://arxiv.org/pdf/2610.13941v1 |
