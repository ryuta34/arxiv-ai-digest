---
title: "SimuScene: Simulation-Ready Compositional 3D Scene Reconstruction from a Single Image"
date: 2026-06-03
arxiv_id: 2606.03994v1
url: http://arxiv.org/abs/2606.03994v1
---

# SimuScene: Simulation-Ready Compositional 3D Scene Reconstruction from a Single Image

| 項目 | 内容 |
|---|---|
| どんなもの？ | 単一の画像から、物理的に安定しロボット操作等にそのまま利用可能な構成的3Dシーンを再構築するパイプライン「SimuScene」を提案した研究。物理シミュレーションを事後処理ではなく生成プロセスに組み込み、幾何学的な修正を行う。 |
| 先行研究と比べてどこがすごい？ | 既存の単一画像からの3D再構築手法は、シミュレータ上でオブジェクトが貫通や浮遊を起こし崩壊することが課題であった。本手法は物理シミュレーションを診断ツールとして活用し、重力軸方向の変形や amodal（隠蔽部を含む）形状の再サンプリングを行うことで、高い物理的妥当性を実現した点。 |
| 技術や手法のキモはどこ？ | オブジェクトを順次物理シミュレータへ投入するプロトコルを用い、貫通や支持失敗を定量的な「診断信号」へ変換して形状修正を駆動する点。特に、SAM3Dを amodal 形状生成のために fine-tune し、物理的な安定性を報酬とした preference 駆動の最適化（FM-DPO）を行っている点。 |
| どうやって有効だと検証した？ | GraspClutter6D、Aria Digital Twin、GenWildという3つの多様なデータセットで評価。物理的安定性（安定化率、貫通率）および再構築精度（ABO、IoU）を測定し、ロボットアームの操作やヒューマノイドの制御タスクへの応用で有用性を実証した。 |
| 議論はある？ | シーケンシャルな処理プロトコルのため、後段のオブジェクトが早期の推定エラーを修正できない制約がある。また、複雑な遮蔽下での形状復元には依然として改善の余地があり、シーン全体を通した共同最適化が今後の課題である。 |
| 次に読むべき論文は？ | [12] Sam 3d: 3dfy anything in images, [32] Dso: Aligning 3d generators with simulation feedback for physical soundness, [54] FoundationPose: Unified 6d pose estimation and tracking of novel objects |
| PDFリンク | https://arxiv.org/pdf/2606.03994v1 |
