---
title: "DiffusionBench: On Holistic Evaluation of Diffusion Transformers"
date: 2026-06-24
arxiv_id: 2606.24888v1
url: http://arxiv.org/abs/2606.24888v1
---

# DiffusionBench: On Holistic Evaluation of Diffusion Transformers

| 項目 | 内容 |
|---|---|
| どんなもの？ | 拡散モデル（DiT）の性能評価をImageNetのみに依存せず、テキスト・トゥ・イメージ（T2I）タスクと統合した包括的なベンチマーク「DIFFUSIONBENCH」を提案した研究。ImageNetの性能向上とT2Iの性能向上には強い相関がないことを実証し、より汎用的な評価の重要性を説いている。 |
| 先行研究と比べてどこがすごい？ | 従来は高コスト・高摩擦とされていたT2Iの評価を、ImageNet評価と同一コードベース・同一手法で実施可能にする「NANOGEN」フレームワークを導入した点。これにより、モデル開発者が低コストでクロスタスクの性能検証を行えるようになった。 |
| 技術や手法のキモはどこ？ | 単一のバックボーン、オプティマイザ、学習ループを共有しつつ、データセットとコンディショニングモジュールを差し替えるだけで両タスクに対応できる設計。クラス埋め込みからテキストエンコーダーへの切り替えなど、わずか12行の構成変更でタスク間移行を可能にした点。 |
| どうやって有効だと検証した？ | 21種類の潜在拡散モデルをNANOGEN上で学習させ、ImageNet FIDと3つのT2I評価指標（GenEval, DPG-Bench, GenAIBench）の相関を分析。Pearson相関係数が-0.377〜-0.580と低く、ImageNetの指標がT2Iの性能を予測できないことをデータで示した。 |
| 議論はある？ | 現在の相関分析は限られた計算リソース下のスケールでの結果であり、スケールが変われば相関性が変化する可能性がある。また、T2I指標は微調整によりハッキングされるリスクがあり、より耐性のある評価指標の策定が今後の課題である。 |
| 次に読むべき論文は？ | [DDT: Decoupled diffusion transformer](https://arxiv.org/abs/2505.02831), [Back to basics: Let denoising generative models denoise](https://arxiv.org/abs/2511.13720), [Pixelgen: Pixel diffusion beats latent diffusion with perceptual loss](https://arxiv.org/abs/2602.02493) |
| PDFリンク | https://arxiv.org/pdf/2606.24888v1 |
