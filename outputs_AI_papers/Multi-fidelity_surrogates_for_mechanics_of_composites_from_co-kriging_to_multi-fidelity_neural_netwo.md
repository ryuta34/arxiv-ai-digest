---
title: "Multi-fidelity surrogates for mechanics of composites: from co-kriging to multi-fidelity neural networks"
date: 2026-05-05
arxiv_id: 2605.02871v1
url: http://arxiv.org/abs/2605.02871v1
---

# Multi-fidelity surrogates for mechanics of composites: from co-kriging to multi-fidelity neural networks

| 項目 | 内容 |
|---|---|
| どんなもの？ | 複合材料の力学解析におけるマルチフィデリティ（多忠実度）サロゲートモデリング（MFSM）に関する包括的なレビュー論文です。物理ベースの低忠実度モデルと限られた高忠実度データ（実験や高精度シミュレーション）を融合し、計算コストを抑えつつ高精度な予測を行う手法を体系化しています。 |
| 先行研究と比べてどこがすごい？ | 従来手法（ガウス過程・クリギング等）だけでなく、近年のニューラルネットワークベースの手法（MFNN, PINN, 転移学習等）まで網羅し、複合材料特有の階層的・非線形な課題に対して、どのように計算効率と信頼性を両立させるかを構造的に整理した点。 |
| 技術や手法のキモはどこ？ | ガウス過程を用いる手法（コクリギング、NARGP等）による不確実性の定量化と、ニューラルネットワークを用いる手法（融合型ネットワーク、転移学習）による高次元データや複雑な時系列データへの対応の両輪を、複合材料の特性に合わせて使い分けている点。 |
| どうやって有効だと検証した？ | 多岐にわたる複合材料の応用例（織物複合材料の不確実性定量化、層間剥離、プロセス誘起変形、衝撃位置特定など）を用いて、単一フィデリティモデルと比較し、計算時間の大幅な短縮と高い予測精度を実証しました。 |
| 議論はある？ | 忠実度の定義が問題依存であり普遍的ではない点、LFとHFのデータが不一致（ミスマッチ）である場合の負の転移リスク、NNモデルにおける解釈性の欠如、実用的なワークフロー統合におけるバリデーションの困難さが挙げられています。 |
| 次に読むべき論文は？ | [131] Mushi Li et al., "Multi-fidelity data-driven optimization design framework for self-piercing riveting process parameters" (本論文で引用されているワークフロー統合の好例) |
| PDFリンク | https://arxiv.org/pdf/2605.02871v1 |
