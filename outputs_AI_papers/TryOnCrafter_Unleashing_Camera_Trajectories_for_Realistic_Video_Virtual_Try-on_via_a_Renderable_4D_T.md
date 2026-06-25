---
title: "TryOnCrafter: Unleashing Camera Trajectories for Realistic Video Virtual Try-on via a Renderable 4D Try-on Proxy"
date: 2026-06-25
arxiv_id: 2606.26092v1
url: http://arxiv.org/abs/2606.26092v1
---

# TryOnCrafter: Unleashing Camera Trajectories for Realistic Video Virtual Try-on via a Renderable 4D Try-on Proxy

| 項目 | 内容 |
|---|---|
| どんなもの？ | 従来の動画仮想試着（VVT）が抱えていた「入力動画のカメラ軌道に依存する」という制限を解消する、カメラ制御可能な動画仮想試着（CaM-VVT）フレームワークです。人物と背景を明示的に分離して4D表現として再構築することで、任意のカメラ軌道での高精度な試着動画生成を実現します。 |
| 先行研究と比べてどこがすごい？ | 従来のVVT手法や既存のカメラ制御モデルを単に組み合わせた手法と異なり、明示的な4D表現を用いることで、カメラ移動時の物理的不整合や構造的崩壊を防ぎます。また、カメラ軌道と人物の動作を分離した再レンダリングを行うことで、360度視点や弾丸時間（バレットタイム）などの高度な演出が可能となりました。 |
| 技術や手法のキモはどこ？ | 主なキモは「Renderable 4D Try-on Proxy（レンダリング可能な4D試着プロキシ）」の導入です。これは高精度な3DGSアバターと背景の点群を空間的に整合させたもので、これを構造的アンカーとしてVideo Diffusion Transformerにガイドを与えることで、複雑なカメラワーク下でも一貫した服の変形と背景整合性を維持します。 |
| どうやって有効だと検証した？ | 独自の評価ベンチマーク「CaM-VVTBench」を構築し、96のテストサンプルに対して6種類のカメラモーション（チルト、ズーム、オービット等）で検証しました。VBenchを用いた定量評価および定性評価の両面において、既存の手法を大きく上回る一貫性と画質を達成したことを示しました。 |
| 議論はある？ | 極端な視点変化におけるパララックス（視差）と推定誤差による課題が挙げられています。また、DiTを用いた反復的なノイズ除去過程による推論コストの高さが、リアルタイム操作を妨げる要因となっています。 |
| 次に読むべき論文は？ | [1] Bai et al., "Recammaster: Camera-controlled generative rendering from a single video." (2025) <br> [49] Yu et al., "Trajectorycrafter: Redirecting camera trajectory for monocular videos via diffusion models." (2025) |
| PDFリンク | https://arxiv.org/pdf/2606.26092v1 |
