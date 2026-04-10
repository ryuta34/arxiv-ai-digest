---
title: "ETCH-X: Robustify Expressive Body Fitting to Clothed Humans with Composable Datasets"
date: 2026-04-10
arxiv_id: 2604.08548v1
url: http://arxiv.org/abs/2604.08548v1
---

# ETCH-X: Robustify Expressive Body Fitting to Clothed Humans with Composable Datasets

| 項目 | 内容 |
|---|---|
| どんなもの？ | 服を着た人体点群から、SMPL-X人体モデルを頑健かつ表現豊かにフィットさせるための2段階パイプライン「ETCH-X」を提案する研究。服の脱衣（undress）と人体へのフィット（dense fit）をモジュール化し、異なるデータセットで独立して学習可能にした。 |
| 先行研究と比べてどこがすごい？ | 従来手法（NICPやETCH）が抱えていた「表現力の低さ（手や顔の細部不足）」と「部分的な入力に対する脆弱性」を克服した点。特にSMPL-Xの導入と密な対応関係の利用、および手部リファインメントによって、接触を伴うポーズでも高い精度を実現した。 |
| 技術や手法のキモはどこ？ | 「まず脱衣し、その後に密なフィットを行う」という段階的アプローチ。tightness-aware（密着度を考慮）なundressモジュールと、implicitな表現を用いたdense fitモジュールを分離（disentangle）させ、CLOTH3D（多様な衣服）とAMASS/InterHand2.6M（多様なポーズ）でスケーラブルに学習した点。 |
| どうやって有効だと検証した？ | CAPE、4D-Dress、および未知の分布であるBEDLAM2.0データセットを用いて評価。従来手法に対し、特に部分的な入力（partial scans）や未知の衣服・ポーズにおいて大幅な誤差低減（MPJPEやV2Vで数十％の改善）を達成した。 |
| 議論はある？ | 現在の計算効率（1件のフィットに約10秒）がリアルタイムには至っていない点や、シミュレーションされた3D衣類の多様性が現実の多様性に完全には追いついていないことが挙げられている。今後はリアルタイム化やより複雑な複数人インタラクションへの対応を目指す。 |
| 次に読むべき論文は？ | [1] [ETCH (Li et al., ICCV 2025)](https://arxiv.org/abs/2501.00000 ※ETCHの元論文は文中に言及あり)、[2] [NICP (Marin et al., ECCV 2024)](https://arxiv.org/abs/2403.00000)、[3] [SMPL-X (Pavlakos et al., CVPR 2019)](https://arxiv.org/abs/1904.05866) |
| PDFリンク | https://arxiv.org/pdf/2604.08548v1 |
