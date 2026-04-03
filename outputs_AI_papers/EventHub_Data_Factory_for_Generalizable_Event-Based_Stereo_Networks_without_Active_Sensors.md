---
title: "EventHub: Data Factory for Generalizable Event-Based Stereo Networks without Active Sensors"
date: 2026-04-03
arxiv_id: 2604.02331v1
url: http://arxiv.org/abs/2604.02331v1
---

# EventHub: Data Factory for Generalizable Event-Based Stereo Networks without Active Sensors

| 項目 | 内容 |
|---|---|
| どんなもの？ | 高価でスパースなLiDAR等のアクティブセンサーに依存せず、安価なRGB画像からイベントベースステレオネットワークを訓練するデータ生成フレームワーク「EventHub」を提案。既存のRGBステレオモデルの知識を蒸留することで、アノテーションコストを削減しつつ高い汎用性を実現する。 |
| 先行研究と比べてどこがすごい？ | LiDARデータの欠損やノイズ、ダイナミックなシーンへの対応困難といった従来手法の課題を解決。RGBステレオの基礎モデルを活用することで、イベントベースの学習データを擬似的に生成し、未知のドメインに対する汎化性能を大幅（最大50%の誤差削減）に向上させた点。 |
| 技術や手法のキモはどこ？ | Novel View Synthesis（SVRaster）を用いた、静止画からの仮想イベントデータおよび精緻なプロキシ深度ラベルの生成。および、RGBステレオ基礎モデルの知識をイベント領域に蒸留する「クロスモーダル蒸留」と、RGBステレオモデルをイベント入力へ転用する設計。 |
| どうやって有効だと検証した？ | DSEC、M3ED、MVSECといった標準的なイベントステレオデータセットを用い、インドメインおよびアウトドメイン設定での評価を実施。LiDARによる教師データを用いた訓練モデルと比較し、同等以上の性能を達成することを確認した。 |
| 議論はある？ | データ生成には計算コストがかかることや、合成データ特有のアーティファクトの可能性。また、極端な照明条件や非常に動的なシーンでは、モデルの汎化能力が依然として課題となる可能性がある。 |
| 次に読むべき論文は？ | [61] F. Tosi et al., "NeRF-supervised deep stereo" (CVPR 2023), [69] B. Wen et al., "FoundationStereo: Zero-shot stereo matching" (CVPR 2025) |
| PDFリンク | https://arxiv.org/pdf/2604.02331v1 |
