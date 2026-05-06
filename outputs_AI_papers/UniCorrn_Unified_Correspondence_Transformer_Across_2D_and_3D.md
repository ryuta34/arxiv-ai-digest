---
title: "UniCorrn: Unified Correspondence Transformer Across 2D and 3D"
date: 2026-05-06
arxiv_id: 2605.04044v1
url: http://arxiv.org/abs/2605.04044v1
---

# UniCorrn: Unified Correspondence Transformer Across 2D and 3D

| 項目 | 内容 |
|---|---|
| どんなもの？ | 2D画像間（2D-2D）、画像と点群間（2D-3D）、点群間（3D-3D）のすべての対応付けタスクを、単一の重み共有モデルで実行する初の統一的対応付けTransformer「UniCorrn」です。 |
| 先行研究と比べてどこがすごい？ | モダリティごとに個別のモデルを構築していた従来手法に対し、重みを共有しつつ、2D-3Dで8%、3D-3Dで10%の登録リコール（Registration Recall）向上を達成し、SOTAを更新しました。 |
| 技術や手法のキモはどこ？ | 外見情報（Appearance）と位置情報（Positional）のストリームを分離して処理する「デュアルストリームTransformerデコーダー」を採用し、Attentionメカニズムによりクロスモーダルな特徴類似性を直接学習できる点です。 |
| どうやって有効だと検証した？ | 7Scenesや3DLoMatchなどの標準的なベンチマークを用いて、Inlier Ratio（IR）や登録リコール（RR）などを測定。さらにアブレーション研究により、各提案コンポーネントの寄与を詳細に検証しました。 |
| 議論はある？ | 2D画像と3D点群の統計的性質の違いにより、正規化層で勾配競合が発生する課題を指摘。また、特定のケースでは誤った対応付けが発生する限界も示されています。 |
| 次に読むべき論文は？ | [1] [D3Feat](https://arxiv.org/abs/2002.10857), [31] [MASt3R](https://arxiv.org/abs/2405.04044), [69] [CroCo v2](https://arxiv.org/abs/2307.01362) |
| PDFリンク | https://arxiv.org/pdf/2605.04044v1 |
