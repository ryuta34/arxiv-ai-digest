---
title: "LongE2V: Long-Horizon Event-based Video Reconstruction, Prediction, and Frame Interpolation with Video Diffusion Models"
date: 2026-07-10
arxiv_id: 2607.08770v1
url: http://arxiv.org/abs/2607.08770v1
---

# LongE2V: Long-Horizon Event-based Video Reconstruction, Prediction, and Frame Interpolation with Video Diffusion Models

| 項目 | 内容 |
|---|---|
| どんなもの？ | イベントカメラのデータから動画の再構成・予測・フレーム補間を行うための統合的な拡散モデルベースの手法「LongE2V」。事前学習済みの動画拡散モデル（CogVideoX）を基盤とし、イベントストリームを条件付けとして高精細な動画生成を実現する。 |
| 先行研究と比べてどこがすごい？ | 従来手法が個別のタスクに特化していたのに対し、単一のアーキテクチャで3つのタスクを網羅的に解決する。特に長時間の動画生成において問題となる誤差の蓄積やドリフトを、独自の学習戦略で劇的に改善し、SOTAを上回る視覚品質と安定性を達成した。 |
| 技術や手法のキモはどこ？ | 長期生成時のドリフトを防ぐ「Autoregressive Unrolling（自己回帰的な展開）」と「Adaptive Context Switching（動的な文脈切り替え）」、およびフレーム補間のための「Reencoding Alignment（再符号化アライメント）」と「Cross Residual Correction（交差残差補正）」の導入。 |
| どうやって有効だと検証した？ | ECD、MVSEC、HQF、BS-ERGBといった実環境のベンチマークデータセットを用い、既存の回帰ベース手法や拡散モデルベース手法と比較。定量的指標（PSNR, SSIM, LPIPS）および定性的な視覚比較を通じて、高い忠実度と安定性を証明した。 |
| 議論はある？ | 入力イベントストリームが極端にスパースな場合や品質が低い場合には性能が低下する。また、イベントデータに含まれるノイズ（いわゆるホットピクセル）を誤って再現・増幅してしまう可能性があるという限界がある。 |
| 次に読むべき論文は？ | [CogVideoX: Text-to-video diffusion models with an expert transformer](https://arxiv.org/abs/2408.06072) および [E2VID: Events-to-Video: Bringing modern computer vision to event cameras](https://arxiv.org/abs/1904.01581) |
| PDFリンク | https://arxiv.org/pdf/2607.08770v1 |
