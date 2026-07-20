---
title: "MotionForesight: Re-purposing Video Models for Future 3D Scene-Flow Prediction"
date: 2026-07-20
arxiv_id: 2607.16192v1
url: http://arxiv.org/abs/2607.16192v1
---

# MotionForesight: Re-purposing Video Models for Future 3D Scene-Flow Prediction

| 項目 | 内容 |
|---|---|
| どんなもの？ | 単眼の人間と物体のインタラクション動画から、物体の未来の3D軌道を予測する手法「MotionForesight」の提案。動画モデルが持つ時間的・物理的先行知識を再利用し、言語や行動ラベルを用いずに幾何学的な未来予測を実現する。 |
| 先行研究と比べてどこがすごい？ | 既存の動画生成ベースの手法よりも、物体の動きの予測において高い精度と一貫性を実現した点。また、言語や行動指示といった外部入力に依存せず、かつ小規模なデータセット（40K動画）でも大規模モデルや言語モデルを活用する競合手法を凌駕する性能を達成した。 |
| 技術や手法のキモはどこ？ | 既存の動画拡散モデル（TrackCraft3R）のRetrospectiveな追跡機能を、未来のフレームを「未知のトークン（mask latents）」としてマスキングすることで、Forwardな予測タスクへ変換した点。 |
| どうやって有効だと検証した？ | Something-Something V2のデータセットを用いたSSv2 unseen clipsおよび、未知の環境で撮影されたphone videosを用いたOOD（分布外）評価を実施。ADE（平均変位誤差）、FDE（最終変位誤差）、PWT（閾値内予測割合）等の指標で既存手法と比較した。 |
| 議論はある？ | 現在は単一の未来を予測する決定論的なモデルであるため、不確実性や複数の妥当な未来を表現できない点。また、擬似ラベルの精度に依存しており、より多様な環境や視点への堅牢性が課題である。 |
| 次に読むべき論文は？ | [TrackCraft3R [11]](https://arxiv.org/abs/2605.12587), [MolmoMotion [5]](https://arxiv.org/abs/2606.18558), [ObjectForesight [7]](https://arxiv.org/abs/2601.05237) |
| PDFリンク | https://arxiv.org/pdf/2607.16192v1 |
