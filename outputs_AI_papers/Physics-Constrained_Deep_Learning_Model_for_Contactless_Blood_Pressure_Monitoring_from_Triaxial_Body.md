---
title: "Physics-Constrained Deep Learning Model for Contactless Blood Pressure Monitoring from Triaxial Bodyseismography"
date: 2026-08-25
arxiv_id: 2608.23562v1
url: http://arxiv.org/abs/2608.23562v1
---

# Physics-Constrained Deep Learning Model for Contactless Blood Pressure Monitoring from Triaxial Bodyseismography

| 項目 | 内容 |
|---|---|
| どんなもの？ | 非侵襲的で長時間の血圧モニタリングを可能にする、3軸ボディサイスモグラフィ（BSG）を用いた物理制約付き深層学習フレームワーク「Phy-BP」。病院環境での日常的な動作や環境変化に耐えうる、頑健な連続血圧推定手法を提案している。 |
| 先行研究と比べてどこがすごい？ | 従来の1D BCGベースの手法が抱えていた、身体とベッドの相互作用による信号歪みや、データ駆動型モデルのブラックボックス性に起因する頑健性の欠如を解決。物理学的な波の伝播理論を深層学習モデルに組み込むことで、限られたデータでも高精度かつ安定した推定を実現した点。 |
| 技術や手法のキモはどこ？ | 3軸BSG信号の物理的な伝播モデル（粘弾性体中の波の伝播）を深層学習の層として統合し、ゲート制御を用いた特徴量のアライメントを行う点。また、 cardiogenic（心原性）なテンプレートを用いた適応的な品質管理アルゴリズムにより、低SNRのデータを効果的に除外している点。 |
| どうやって有効だと検証した？ | 21名の患者から収集した162時間の病院データセット（侵襲的ABPをゴールドスタンダードとする）を用い、Leave-one-subject-out法で検証。既存のBCGやPPG/ECGベースの手法と比較し、AAMI規格を満たす高い推定精度と、TPR（総末梢血管抵抗）変動に対する頑健性を実証した。 |
| 議論はある？ | 高い精度のために各患者ごとのキャリブレーション（校正）が必要であること。今後は、マルチ軸信号の融合から個別のTPR情報を推定し、完全なキャリブレーションフリー化を実現することが課題である。 |
| 次に読むべき論文は？ | [2] AI-driven system for non-contact continuous nocturnal blood pressure monitoring using fiber optic ballistocardiography (Huang et al., 2024), [22] BCG-BP-FSNet: A few-shot learning framework for personalized, non-invasive blood pressure prediction based on ballistocardiogram (Zhang et al., 2026) |
| PDFリンク | https://arxiv.org/pdf/2608.23562v1 |
