---
title: "SyncWorld: Visual Calibration Enables World Models as Zero-Shot Simulators"
date: 2026-09-09
arxiv_id: 2609.09155v1
url: http://arxiv.org/abs/2609.09155v1
---

# SyncWorld: Visual Calibration Enables World Models as Zero-Shot Simulators

| 項目 | 内容 |
|---|---|
| どんなもの？ | ロボットの低レベルな制御信号と視覚的な変化の対応関係（Action–Visual Mapping）を、その場で視覚的にキャリブレーション（校正）することで、未知の環境やロボットでもゼロショットでシミュレーション可能にする世界モデル「SyncWorld」。 |
| 先行研究と比べてどこがすごい？ | 従来手法では、カメラ配置やロボットの違いによって数値上のアクションがピクセル空間で異なる意味を持つ「環境依存性」が課題だったが、本手法は明示的なキャリブレーション映像をコンテキストとして入力することで、追加学習なしでこの不整合を解消できる点。 |
| 技術や手法のキモはどこ？ | ロボットの6自由度（DoF）の動きを網羅した短いキャリブレーション動画をコンテキストとして入力し、未知の環境でのアクションと視覚変化の対応を「In-context」で学習させる点。また、キャリブレーションがない場合でも、過去の対話履歴からマッピングを推定する「蒸留技術」を併用している点。 |
| どうやって有効だと検証した？ | ManiSkill、LIBERO、および実機（xArm）を用いた評価を実施。動画予測精度（PSNR, SSIM, LPIPS, FID）や、多視点間の一貫性（Met3r）を測定し、さらに実タスクにおけるゼロショット・ポリシー改善（GPC-Rank）の有用性を確認した。 |
| 議論はある？ | 極端なカメラアングルや、訓練データに含まれない未知の物体との相互作用では、物体状態の変化予測が不正確になることがある。また、非常に繊細な動作が求められるケースでは、依然として細部の描写にわずかなぼけが生じる課題がある。 |
| 次に読むべき論文は？ | [1] [Genie: Generative interactive environments](https://arxiv.org/abs/2402.15391)<br>[2] [Ctrl-World: A controllable generative world model for robot manipulation](https://arxiv.org/abs/2501.07767)<br>[3] [DreamGen: Unlocking generalization in robot learning through video world models](https://arxiv.org/abs/2502.15391) |
| PDFリンク | https://arxiv.org/pdf/2609.09155v1 |
