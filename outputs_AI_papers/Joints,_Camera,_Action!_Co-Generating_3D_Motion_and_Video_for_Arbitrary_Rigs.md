---
title: "Joints, Camera, Action! Co-Generating 3D Motion and Video for Arbitrary Rigs"
date: 2026-10-21
arxiv_id: 2610.28632v1
url: http://arxiv.org/abs/2610.28632v1
---

# Joints, Camera, Action! Co-Generating 3D Motion and Video for Arbitrary Rigs

| 項目 | 内容 |
|---|---|
| どんなもの？ | 任意のトポロジーを持つ3Dリグ（骨格）に対し、動画と整合性のとれた3Dモーションを同時に生成する手法「Joints, Camera, Action! (JCA)」です。テキストプロンプトやキーフレーム、入力動画から、シーンに適合した3Dアニメーションと動画を生成・制御できます。 |
| 先行研究と比べてどこがすごい？ | 従来手法は特定の人間スケルトンに限定されるか、動画から後付けでモーションを推定する際にズレが生じやすかったのに対し、本手法はリグと動画を協調的に生成し、シーンへの登録（カメラ位置の自動推定）までを一貫して行える点が優れています。 |
| 技術や手法のキモはどこ？ | グラフニューラルネットワークを用いたリグエンコーダにより、任意の骨格を表現します。また、動画生成モデルとモーション生成モデルをゼロ初期化された交差アテンション（橋渡し層）で接続し、推論時に「ブリッジガイダンス」を用いることで、動画とモーションの整合性を高めています。 |
| どうやって有効だと検証した？ | 200K規模の動画・モーションペアによる大規模なデータセットを構築し、PuppeteerやActionMesh等のベースラインと比較。テキストからのアニメーション忠実度（GPT-6による評価）、メッシュ歪みの少なさ、シーン適合性などの観点で高い性能を示しました。 |
| 議論はある？ | 現在はカメラが静止している前提での推論が主であり、カメラワークの変化には未対応です。また、シーンの幾何学的形状が明示的にモデルに渡されないため、キャラクターと物体との物理的な接触や干渉回避（突き抜け防止）に課題が残ります。 |
| 次に読むべき論文は？ | [AnyTop: Character animation diffusion with any topology](https://arxiv.org/abs/2507.03063) (本研究のモーション表現のベース) および [EchoMotion: Unified human video and motion generation via dual-modality diffusion transformer](https://arxiv.org/abs/2601.07767) |
| PDFリンク | https://arxiv.org/pdf/2610.28632v1 |
