---
title: "Do as I Do: Dexterous Manipulation Data from Everyday Human Videos"
date: 2026-06-18
arxiv_id: 2606.19333v1
url: http://arxiv.org/abs/2606.19333v1
---

# Do as I Do: Dexterous Manipulation Data from Everyday Human Videos

| 項目 | 内容 |
|---|---|
| どんなもの？ | 日常的なモノクロRGB動画から、多指ロボットハンドで実行可能な器用な操作データを生成するアルゴリズム「DO AS I DO」を提案した研究。人間の動画を再構成し、ロボットの身体に合わせて動作をリターゲティングすることで、大規模なロボット学習データの自動生成を実現する。 |
| 先行研究と比べてどこがすごい？ | 従来手法では困難だった「in-the-wild（野良動画）」からの頑健なハンド・物体追跡を実現し、かつロボットの身体的制約を考慮した物理的に妥当な動作生成を可能にした点。特にノイズの多い動画やオクルージョン（遮蔽）に対しても、従来手法を凌駕する精度で物体追跡と動作抽出を達成している。 |
| 技術や手法のキモはどこ？ | ①物体追跡に「Guided Diffusion」を用い、形状とポーズを分離して適応的にガイダンスする手法、②物理シミュレーションを用いた「dynamics-aware」なリターゲティング（Warmupステップ、ランダムな力による摂動、遷移報酬の導入）、③これらを組み合わせることで、動画からインターネット上の任意の動画から実機へ展開可能なパイプラインを構築した点。 |
| どうやって有効だと検証した？ | DexYCBやHOI4Dなどの標準的なハンド・物体追跡ベンチマークでの定量的評価に加え、150本の多様なインターネット動画を用いた人間による評価を実施。さらに、UR3eアームとSharpa Waveハンドを用いた実機ロボットへの展開実験を行い、多様な操作タスク（計500件の高品質軌跡生成）で有効性を実証した。 |
| 議論はある？ | 現在は剛体オブジェクトと半正確な深度推定に依存しており、関節を持つ物体や環境制約の推論には対応していない。また、物理シミュレータの近似により実機性能に上限がある点や、人間の意図を完全には捉えきれない（ハンド-シーンの相互作用の欠如）点が限界として挙げられている。 |
| 次に読むべき論文は？ | [15] C. Pan et al., "Spider: Scalable physics-informed dexterous retargeting" (https://arxiv.org/abs/2511.09484) <br> [71] Y.-W. Chao et al., "DexYCB: A benchmark for capturing hand grasping of objects" (https://arxiv.org/abs/2109.11978) |
| PDFリンク | https://arxiv.org/pdf/2606.19333v1 |
