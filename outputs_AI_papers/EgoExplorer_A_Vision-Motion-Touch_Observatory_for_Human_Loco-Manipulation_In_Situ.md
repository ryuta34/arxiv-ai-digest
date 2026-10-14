---
title: "EgoExplorer: A Vision-Motion-Touch Observatory for Human Loco-Manipulation In Situ"
date: 2026-10-14
arxiv_id: 2610.18872v1
url: http://arxiv.org/abs/2610.18872v1
---

# EgoExplorer: A Vision-Motion-Touch Observatory for Human Loco-Manipulation In Situ

| 項目 | 内容 |
|---|---|
| どんなもの？ | 人間の loco-manipulation（移動と操作の統合）を記録・分析するための、ウェアラブルセンサーを用いた100時間規模の egocentric（一人称視点）データセット「EgoExplorer」。視覚、全身の動き、精密な指の関節運動、触覚、およびステップレベルのタスク記述を同期して保持している。 |
| 先行研究と比べてどこがすごい？ | 既存のデータセットが「視覚のみ（文脈欠如）」「全身のみ（手指や触覚欠如）」「手のみ（全身運動欠如）」という部分的な記録に留まっていたのに対し、EgoExplorerはこれらをすべて高精度に統合した。また、専門的な作業環境に特化し、移動と操作を連続的な一連の行動として捉えている点が優れている。 |
| 技術や手法のキモはどこ？ | sparse（疎）なセンサー配置から全身の動きを推定する「$C^3$ pipeline（Calibrate-Complete-Constrain）」の導入。プロトコルに基づいたキャリブレーションでセンサーと身体の幾何学的関係を分離し、時間的優先モデルで未観測の関節を補完後、層状の制約（骨格、表面クリアランス、接地整合性）によって物理的に妥当な軌道を生成する点。 |
| どうやって有効だと検証した？ | 評価用サブセットを構築し、全身再構成精度、手技の安定性、接触推定精度を既存手法と比較。また、Cosmos3-Edgeを用いたマルチモーダル生成実験や、Unitree G1人型ロボットへの全身制御ポリシーの転移実験を通じて、学習リソースとしての有用性を実証した。 |
| 議論はある？ | 再構成は完全な関節リカバリーを保証するものではなく、触覚センサーの信頼性にも変動がある。また、実世界の人型ロボット学習に対する直接的な貢献（リアルワールドでの汎化性能など）は、今後の課題として残されている。 |
| 次に読むべき論文は？ | [Ego4D (Grauman et al., 2022)](https://openaccess.thecvf.com/content/CVPR2022/html/Grauman_Ego4D_Around_the_World_in_3000_Hours_of_Egocentric_Video_CVPR_2022_paper.html)、[Ego-Exo4D (Grauman et al., 2024)](https://openaccess.thecvf.com/content/CVPR2024/html/Grauman_Ego-Exo4D_Understanding_Skilled_Human_Activity_from_First-_and_Third-Person_Perspectives_CVPR_2024_paper.html)、[ZeroWBC (Yang et al., 2026a)](https://arxiv.org/abs/2603.09170) |
| PDFリンク | https://arxiv.org/pdf/2610.18872v1 |
