---
title: "ShotStream: Streaming Multi-Shot Video Generation for Interactive Storytelling"
date: 2026-03-30
arxiv_id: 2603.25746v1
url: http://arxiv.org/abs/2603.25746v1
---

# ShotStream: Streaming Multi-Shot Video Generation for Interactive Storytelling

| 項目 | 内容 |
|---|---|
| どんなもの？ | 対話的なストーリーテリングとオンザフライでの動画生成を可能にする、因果的なマルチショット動画生成モデル「ShotStream」。過去のショットを条件付けとして順次生成する自己回帰モデルであり、単一GPUで16 FPSのリアルタイム生成を実現する。 |
| 先行研究と比べてどこがすごい？ | 従来の双方向アーキテクチャが抱えていた「プロンプトの一括入力が必要（非対話的）」かつ「生成レイテンシが高い」という欠点を克服した。リアルタイムのストリーミングプロンプト入力に対応し、ショットごとに生成を行うことで、生成途中での物語調整を可能にした点。 |
| 技術や手法のキモはどこ？ | ① 過去のショットのグローバルな文脈と、現在のショット内のローカルな文脈を保持する「デュアルキャッシュメモリ」② ショット境界を明示して曖昧さを解消する「RoPE不連続性インジケーター」③ 学習と推論の乖離を埋めるための「2段階の自己強制（self-forcing）蒸留戦略」。 |
| どうやって有効だと検証した？ | 320Kのマルチショット動画データセットで学習し、複数の既存手法（Mask2DiT, EchoShot, CineTrans等）と比較。定量的評価（Consistency, Prompt Alignment等）および54名の参加者によるユーザスタディを実施し、視覚的品質とプロンプトへの追従性で高い選好を得たことを示した。 |
| 議論はある？ | 複雑なシーンやプロンプトでは依然として視覚的なアーティファクトや不整合が生じる場合がある。これはモデルのバックボーンの容量に起因しており、バックボーンの拡大や、疎なアテンション、アテンションシンク技術の導入によるさらなる高速化・高精度化が今後の課題。 |
| 次に読むべき論文は？ | [12] Self forcing: Bridging the train-test gap in autoregressive video diffusion (arXiv:2506.08009)<br>[24] HoloCine: Holistic generation of cinematic multi-shot long video narratives (arXiv:2501.06261)<br>[49] From slow bidirectional to fast causal video generators (arXiv:2412.02259) |
| PDFリンク | https://arxiv.org/pdf/2603.25746v1 |
