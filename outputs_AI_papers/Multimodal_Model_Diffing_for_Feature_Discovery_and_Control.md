---
title: "Multimodal Model Diffing for Feature Discovery and Control"
date: 2026-08-11
arxiv_id: 2608.09928v1
url: http://arxiv.org/abs/2608.09928v1
---

# Multimodal Model Diffing for Feature Discovery and Control

| 項目 | 内容 |
|---|---|
| どんなもの？ | マルチモーダル大規模言語モデル（MLLM）の内部表現を、疎な自己符号化器（SAE）を用いて解釈・制御するためのフレームワーク「MMDiff」を提案した論文。ベースとなる言語モデルのSAEとマルチモーダル適応後のSAEを比較（モデル・ディフィング）することで、視覚情報に適応した特定の内部特徴量を特定し、介入を可能にする。 |
| 先行研究と比べてどこがすごい？ | 従来手法では、言語モデル由来の特徴とマルチモーダル適応による変化が混在していたが、モデル・ディフィングを用いることで、視覚的適応に特化した特徴量を精度高く分離できる点。また、特定の特徴量に対する介入（除去や増幅）が、モデル全体のタスク遂行能力を維持しつつ、空間推論や安全性の向上に寄与することを証明した。 |
| 技術や手法のキモはどこ？ | ベースLMとMLLMで学習したSAEのデコーダ方向を比較し、幾何学的な回転（再構成）と視覚入力への応答性の両方を示す「適応済み特徴量」を特定する点。さらに、コントラスティブ・トークン発火分析と辞書的なバイアスを除去するフィルタリングを組み合わせ、特定のタスクに関連する特徴量を高精度に抽出・操作する手法を確立した。 |
| どうやって有効だと検証した？ | 3つのMLLM（LLaVA-MORE, PaliGemma 2, InternVL3.5-2B）を対象に、空間推論、マルチモーダル安全性、OCRの各ドメインで検証。特徴量の causal removal（介入的除去）と、MMDiff-CAA（特徴量特化型の活性化ステアリング）を行い、タスク精度の大幅な向上や攻撃成功率の低下を定量的に示した。 |
| 議論はある？ | 現在は指導調教済みモデルからの抽出を前提としている点や、一部の安全関連特徴量では介入時にモデルの応答が破綻（生成崩壊）する可能性がある点を課題として挙げている。また、より大規模なモデルやMixture-of-Experts構成への適用が将来課題。 |
| 次に読むべき論文は？ | [8] Towards monosemanticity: Decomposing language models with dictionary learning, [9] Stage-wise model diffing, [74] Steering Llama 2 via contrastive activation addition |
| PDFリンク | https://arxiv.org/pdf/2608.09928v1 |
