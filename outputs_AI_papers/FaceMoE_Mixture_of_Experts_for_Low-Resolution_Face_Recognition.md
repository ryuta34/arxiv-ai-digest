---
title: "FaceMoE: Mixture of Experts for Low-Resolution Face Recognition"
date: 2026-07-01
arxiv_id: 2606.32040v1
url: http://arxiv.org/abs/2606.32040v1
---

# FaceMoE: Mixture of Experts for Low-Resolution Face Recognition

| 項目 | 内容 |
|---|---|
| どんなもの？ | 低解像度顔認識（LR-FR）における精度低下とドメイン乖離、破滅的忘却の課題を解決するため、Mixture of Experts (MoE) をトランスフォーマー構造に導入した「FaceMoE」を提案している。複数の専門化されたフィードフォワードネットワーク（FFN）とトップkルーターを用いることで、解像度に応じた適応的な特徴抽出を可能にした。 |
| 先行研究と比べてどこがすごい？ | 単一エンコーダーの限界を克服し、解像度に応じた局所的・意味的な特徴抽出（resolution-aware feature extraction）を実現した点。また、MoEの疎な活性化により、学習済みの知識を保持したまま低解像度データへの適応を可能にし、計算コストの増大を抑えつつモデル容量を拡大した点が優れている。 |
| 技術や手法のキモはどこ？ | トランスフォーマーのMLP層を、複数の専門家（FFN専門家）に置き換え、入力トークンを解像度や重要度に応じて動的に適切な専門家へ割り当てる「トップkルーター」を導入したこと。さらに、ルーターz-lossと負荷分散lossを組み合わせて学習を安定化させたこと。 |
| どうやって有効だと検証した？ | WebFace4Mで事前学習を行い、TinyFace、IJB-S、BRIARなどの計11のデータセットを用いて、低解像度・高解像度・混合品質環境での評価を実施。既存のSOTAモデルと比較して、低解像度環境で大幅に高いTAR@FARやランク検索精度を達成した。 |
| 議論はある？ | 学習データが特定の層に偏っているためバイアスの増幅リスクがある点や、専門家の数（N）を増やしすぎると学習不安定化や過度な断片化が生じる点が指摘されている。今後は公平性の確保や、さらなる堅牢性の向上が課題。 |
| 次に読むべき論文は？ | [Switch Transformers (Fedus et al., 2022)](https://arxiv.org/abs/2101.03961)、[Outrageously Large Neural Networks (Shazeer et al., 2017)](https://arxiv.org/abs/1701.06538)、[PETALface (Narayan et al., 2025)](https://arxiv.org/abs/2412.16147 ※PDF内の参考文献より) |
| PDFリンク | https://arxiv.org/pdf/2606.32040v1 |
