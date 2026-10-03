---
title: "Moore, Escher, Penrose: A Conformal Golden Braid"
date: 2026-10-03
arxiv_id: 2610.02210v1
url: http://arxiv.org/abs/2610.02210v1
---

# Moore, Escher, Penrose: A Conformal Golden Braid

| 項目 | 内容 |
|---|---|
| どんなもの？ | 凍結されたテキストから画像への拡散モデルを用い、M.C.エッシャーの「版画展」に見られるような、画像が自己言及的に入れ子構造を持つ「Droste効果」を再現する生成手法。幾何学的な変換とデノイジングを組み合わせることで、再帰的で一貫性のある風景画像を生成する。 |
| 先行研究と比べてどこがすごい？ | 従来手法では提示のみでは再帰構造を強制できず、事後的な変換では構造の不連続や崩壊が発生していた。本手法はGeneralized Inverse（一般化逆行列）を用いた「組紐（braided）サンプリング」により、幾何学的な整合性を維持しながら生成プロセス全体を通して再帰構造を形成できる点。 |
| 技術や手法のキモはどこ？ | 変換対象の幾何学的な非可逆性を補完するため、Generalized Inverse $T^\dagger$を構築し、それを用いた「組紐サンプリング」を行う点。これにより、 untwisted（展開された）空間と変換後の空間を交互に行き来し、デノイジングのたびに幾何学的な整合性を再投影（投影の冪等性）して修復する仕組み。 |
| どうやって有効だと検証した？ | 複数の変換ファミリー（Conformal twist、Poles、Möbius、Square、Rimrings）を用いた画像生成実験を行い、定性的に再帰構造の保持と多様な風景の生成を評価した。また、ベースラインとの比較や、冪等性の検証（幾何学的ラウンドトリップテスト）を実施した。 |
| 議論はある？ | 固定された再帰中心により被写体との位置関係がずれる場合があることや、時間旅行（追加デノイジング）が継ぎ目を増幅させる場合があること。また、有限解像度のため、数学的な連続性の完全な保証が困難である限界がある。 |
| 次に読むべき論文は？ | [Idempotent Generative Network (Shocher et al., 2024)](https://arxiv.org/abs/2403.02390)、[Generalized Inversion of Nonlinear Operators (Gofer & Gilboa, 2024)](https://arxiv.org/abs/2309.07062) |
| PDFリンク | https://arxiv.org/pdf/2610.02210v1 |
