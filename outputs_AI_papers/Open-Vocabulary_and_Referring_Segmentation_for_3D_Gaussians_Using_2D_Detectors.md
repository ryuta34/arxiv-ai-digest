---
title: "Open-Vocabulary and Referring Segmentation for 3D Gaussians Using 2D Detectors"
date: 2026-06-30
arxiv_id: 2606.30638v1
url: http://arxiv.org/abs/2606.30638v1
---

# Open-Vocabulary and Referring Segmentation for 3D Gaussians Using 2D Detectors

| 項目 | 内容 |
|---|---|
| どんなもの？ | 3Dガウシアンスプラッティング(3DGS)を用いたシーン理解において、CLIP等の高次元特徴量に頼らず、2D物体検出器を活用することで高精度なオープンボキャブラリーセグメンテーションと参照表現グラウンディングを実現するフレームワーク。 |
| 先行研究と比べてどこがすごい？ | 従来のCLIPベース手法が抱えていた「名詞句のみの制限」や「周辺コンテキストの欠如による意味表現の低下」を解決した。ゼロショット設定において、Ref-LeRFベンチマークで16.7%という大幅なmIoU向上を達成している。 |
| 技術や手法のキモはどこ？ | 各3Dインスタンスからレンダリングされたマスクを2D検出器と照らし合わせ、複数視点から得られたラベルを統合して確率分布を生成する「View-Aggregated Semantic Label Distribution (VASD)」と、背景を明示的に扱う「Semantic Background Regularizer (SBR)」の導入。 |
| どうやって有効だと検証した？ | LeRF-OVS、ScanNetでのオープンボキャブラリーセグメンテーション、およびRef-LeRFでの参照表現グラウンディングの各タスクで評価。既存のSOTA手法（LaGa、OpenGaussian等）と比較し、定量的かつ定性的な優位性を確認した。 |
| 議論はある？ | セマンティック理解の精度が使用する2D物体検出器の性能に依存することや、3Dシーン分解プロセスにおける構造的な誤差が依然として伝播する可能性があることが挙げられている。 |
| 次に読むべき論文は？ | [LaGa](https://arxiv.org/abs/2505.24746)、[OpenGaussian](https://arxiv.org/abs/2311.12321) (※論文内で言及されている基盤手法) |
| PDFリンク | https://arxiv.org/pdf/2606.30638v1 |
