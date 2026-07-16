---
title: "VideoRAE: Taming Video Foundation Models for Generative Modeling via Representation Autoencoders"
date: 2026-07-16
arxiv_id: 2607.14088v1
url: http://arxiv.org/abs/2607.14088v1
---

# VideoRAE: Taming Video Foundation Models for Generative Modeling via Representation Autoencoders

| 項目 | 内容 |
|---|---|
| どんなもの？ | 既存の動画生成用VAEが画素レベルの再構成に固執している問題を解消するため、学習済みの動画基盤モデル（VFM）をエンコーダーとして活用する動画自動符号化フレームワーク「VideoRAE」。連続的な拡散モデルと離散的な自己回帰モデルの両方で利用可能な、セマンティックで圧縮性の高い潜在空間を実現した。 |
| 先行研究と比べてどこがすごい？ | 画素レベルのMSEや敵対的損失に依存せず、VFMから得られる高度な構造的意味情報を直接活用することで、再構成性能を維持しつつ、ダウンストリームの生成モデルの収束を約5倍高速化する点。また、従来のVAEで必須だったKL正則化を不要とした。 |
| 技術や手法のキモはどこ？ | VFMの階層的特徴を統合する「1Dセルフアテンション・プロジェクター」による高圧縮化と、復号器の中間層をVFMの教師モデルに局所・大域的に一致させる「表現アライメント（REPA）」モジュール。離散化には、コードブック崩壊を防ぐ「マルチコードブックSimVQ」を採用。 |
| どうやって有効だと検証した？ | UCF-101データセットおよびTokenBenchにて、再構成性能（PSNR, LPIPS, rFVD）と、クラス条件付き動画生成性能（gFVD）を評価。さらにVBenchを用いたテキスト動画生成タスクで、既存モデル（LTX-VAE）と比較し、より高速な収束と高い生成品質を実証した。 |
| 議論はある？ | 再構成忠実度と生成品質にはトレードオフが存在する可能性を示唆。VideoMAEv2は画素再構成に強く、V-JEPA 2は高次元のセマンティクスに強いため、VFMの事前学習パラダイムが潜在空間の質に影響を与える。 |
| 次に読むべき論文は？ | [V-JEPA 2](https://arxiv.org/abs/2506.09985)、[VideoMAEv2](https://arxiv.org/abs/2304.14560)、[LTX-Video](https://arxiv.org/abs/2501.00103) |
| PDFリンク | https://arxiv.org/pdf/2607.14088v1 |
