---
title: "Streaming Multi-Agent Autoregressive Diffusion Model with World State Registers"
date: 2026-07-24
arxiv_id: 2607.21594v1
url: http://arxiv.org/abs/2607.21594v1
---

# Streaming Multi-Agent Autoregressive Diffusion Model with World State Registers

| 項目 | 内容 |
|---|---|
| どんなもの？ | マルチエージェント環境における、一貫性のある動画生成を可能にするストリーミング型ビデオ拡散モデル「WorldWeaver」です。各エージェントの観測を超えて共有される「世界状態レジスタ」を導入し、長期的な論理的整合性を維持します。 |
| 先行研究と比べてどこがすごい？ | 従来のモデルが過去のフレーム履歴のみに依存していたのに対し、明示的な「世界状態レジスタ」を保持することで、観測外の変化やエージェント間の整合性を高精度に管理できる点が優れています。 |
| 技術や手法のキモはどこ？ | エージェントのステータス、鳥瞰図、シーンテキストという3つの補助的な監督信号で学習させた「世界状態レジスタ（WSR）」を、Mixture-of-Transformers（MoT）アーキテクチャを用いてフレーム生成とは別の経路で処理・更新する仕組みです。 |
| どうやって有効だと検証した？ | Minecraftを用いたマルチエージェント環境において、Solaris等のベースラインと比較評価を行いました。VLM（Vision-Language Model）ベースの正確性指標や世界スコアを用い、状態保持と論理的一貫性の向上を実証しました。 |
| 議論はある？ | 実世界への適用においては、エージェント統計や鳥瞰図などの詳細な世界状態情報を取得することが困難であるという課題があります。将来課題として、より複雑な状態情報への対応が挙げられています。 |
| 次に読むべき論文は？ | [Solaris: Building a multiplayer video world model in minecraft](https://arxiv.org/abs/2602.22208) |
| PDFリンク | https://arxiv.org/pdf/2607.21594v1 |
