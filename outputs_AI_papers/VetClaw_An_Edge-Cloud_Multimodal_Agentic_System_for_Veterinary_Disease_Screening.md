---
title: "VetClaw: An Edge-Cloud Multimodal Agentic System for Veterinary Disease Screening"
date: 2026-07-29
arxiv_id: 2607.26042v1
url: http://arxiv.org/abs/2607.26042v1
---

# VetClaw: An Edge-Cloud Multimodal Agentic System for Veterinary Disease Screening

| 項目 | 内容 |
|---|---|
| どんなもの？ | 獣医療における早期疾患スクリーニングを目的とした、エッジ・クラウド構成のマルチモーダル・エージェントシステム「VetClaw」。ラズパイによる画像撮影と、クラウド上の視覚言語モデル（VLM）を組み合わせ、疾患の自動分類とリスク管理を行う。 |
| 先行研究と比べてどこがすごい？ | 単なる静的な画像分類モデルではなく、OpenClawとLangGraphを統合したエージェント技術により、ワークフローの自動制御、安全規則の適用、失敗時の再試行、専門家へのエスカレーションを可能にする動的なシステムである点。 |
| 技術や手法のキモはどこ？ | エッジ側（ラズパイ）でのセンシングやツール制御と、クラウド側での重いVLM推論を分離した階層構造。LangGraphを用いて、入力の検証や安全確認を含むステートフルなワークフローを構築している点。 |
| どうやって有効だと検証した？ | 2つの公開獣医用画像データセットを使用し、Qwen3-VL-32BおよびInternVL3-38Bの2モデルについて、「画像のみ」「テキストのみ」「テキスト＋画像」の3設定でゼロショット学習性能を評価した。 |
| 議論はある？ | 実験データセットの規模や多様性の限界、ゼロショット手法による精度、固定カメラによる撮影制限、また実際の臨床で必要な診断情報（検査データや行動観察等）との統合が今後の課題。 |
| 次に読むべき論文は？ | [11] Agentic AI in healthcare: A comprehensive survey of foundations, taxonomy, and applications (https://doi.org/10.36227/techrxiv.176238073.31262603/v1) |
| PDFリンク | https://arxiv.org/pdf/2607.26042v1 |
