---
title: "VideoMLA: Low-Rank Latent KV Cache for Minute-Scale Autoregressive Video Diffusion"
date: 2026-05-29
arxiv_id: 2605.30351v1
url: http://arxiv.org/abs/2605.30351v1
---

# VideoMLA: Low-Rank Latent KV Cache for Minute-Scale Autoregressive Video Diffusion

| 項目 | 内容 |
|---|---|
| どんなもの？ | 自己回帰型ビデオ拡散モデルのKVキャッシュを低ランクの潜在表現に圧縮し、メモリ消費を大幅に削減する「VideoMLA」を提案した論文。既存の密なKVキャッシュを置き換えることで、ビデオ生成の長時間化や高速化を実現している。 |
| 先行研究と比べてどこがすごい？ | 従来の手法がKVキャッシュの「どのトークンを保持するか」に焦点を当てていたのに対し、本手法はKVキャッシュの「レイアウト自体」を再設計した。結果として、KVキャッシュのメモリ使用量を92.7%削減しつつ、ビデオ生成の品質を維持し、B200 GPU上で1.23倍のスループット向上を達成した点。 |
| 技術や手法のキモはどこ？ | ヘッドごとに保持していたキーと値を、共有の低ランク潜在表現（content latent）とデカップルされた3D-RoPEによる位置キーに分離・圧縮したこと。推論時に密なテンソルを生成せず、潜在空間のままアテンション計算を行う再パラメータ化により、メモリと帯域の効率を最大化した点。 |
| どうやって有効だと検証した？ | Wan-2.1 T2V-1.3Bをベースモデルとして使用し、VBenchベンチマークで30秒および60秒の長時間ビデオ生成性能を評価した。また、メモリ削減効果についてバッチサイズと推論時のメモリ使用量の関係を実測し、従来手法との定量的・定性的比較を行った。 |
| 議論はある？ | 圧縮率と精度のトレードオフが存在し、極端に小さな次元（dc=64など）では詳細な描写が損なわれる。また、実験はWan-2.1-1.3Bに限定されており、より大規模なモデルや解像度、プロンプトスイッチングへの拡張は今後の課題としている。 |
| 次に読むべき論文は？ | [14] DeepSeek-V2: A strong, economical, and efficient mixture-of-experts language model<br>[27] From slow bidirectional to fast autoregressive video diffusion models (CausVid)<br>[31] Causal forcing: Autoregressive diffusion distillation done right |
| PDFリンク | https://arxiv.org/pdf/2605.30351v1 |
