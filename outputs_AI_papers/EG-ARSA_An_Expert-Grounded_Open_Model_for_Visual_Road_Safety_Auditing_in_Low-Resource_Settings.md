---
title: "EG-ARSA: An Expert-Grounded Open Model for Visual Road Safety Auditing in Low-Resource Settings"
date: 2026-08-25
arxiv_id: 2608.23563v1
url: http://arxiv.org/abs/2608.23563v1
---

# EG-ARSA: An Expert-Grounded Open Model for Visual Road Safety Auditing in Low-Resource Settings

| 項目 | 内容 |
|---|---|
| どんなもの？ | 低リソース環境下での道路安全監査を自動化するために、専門家による現地調査データを活用して小規模なオープンソースVLMを微調整する「Expert-Grounded Distillation (EGD)」フレームワーク。また、バングラデシュにおける初の専門家監修済み道路安全監査データセット「BD-ARSA」と、それを用いて学習したモデル「EG-ARSA」を提案している。 |
| 先行研究と比べてどこがすごい？ | 従来の道路安全監査（iRAP等）はコストと専門知識が必要でスケールせず、既存のVLMは汎用すぎて道路安全の詳細な判断が困難であった。本手法は、専門家の知見を蒸留することで、31Bパラメータの教師モデルやGemini-2.5-Flashを上回る精度（専門家評価でリスク予測81%の正解率）を、わずか8Bのパラメータで実現した点。 |
| 技術や手法のキモはどこ？ | 教師モデルのプロンプトを実際の専門家の現地調査結果と照らし合わせて厳密に「接地（Grounding）」させ、その結果をCompactな学生モデルに蒸留させる点。特に、教師モデルには詳細なガイド付きプロンプトを与え、学生モデルには情報を含まないシンプルなプロンプトを適用する「プロンプトの非対称性」を利用して知識を内部化させている。 |
| どうやって有効だと検証した？ | 専門家による盲検評価、Quadratic Weighted Kappa (QWK)を用いたリスク評価、ブートストラップ信頼区間を用いた統計的妥当性の検証を実施。また、教師モデルをリークなし（leakage-free）環境で実行し、蒸留された学生モデルが教師モデルやGemini等のfrontierモデルよりも優れていることを比較検証した。 |
| 議論はある？ | 単一のストリートビュー画像に依存しているため、路面の詳細な幾何学的形状や非視覚的な要因（道路材料の摩擦係数など）の評価には限界がある。また、現在バングラデシュの農村・郊外路に特化しており、他国や都市部、幹線道路への適用は今後の課題である。 |
| 次に読むべき論文は？ | [Burns et al. (2023) "Weak-to-strong generalization: Eliciting strong capabilities with weak supervision."](https://arxiv.org/abs/2312.09390) <br> [Hsieh et al. (2023) "Distilling step-by-step! outperforming larger language models with less training data and smaller model sizes."](https://aclanthology.org/2023.findings-acl.64/) |
| PDFリンク | https://arxiv.org/pdf/2608.23563v1 |
