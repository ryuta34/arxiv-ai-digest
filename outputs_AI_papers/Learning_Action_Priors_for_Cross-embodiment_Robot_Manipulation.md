---
title: "Learning Action Priors for Cross-embodiment Robot Manipulation"
date: 2026-06-25
arxiv_id: 2606.26095v1
url: http://arxiv.org/abs/2606.26095v1
---

# Learning Action Priors for Cross-embodiment Robot Manipulation

| 項目 | 内容 |
|---|---|
| どんなもの？ | 視覚言語行動（VLA）モデルの学習初期段階における学習の不安定さを解消するため、行動モジュールに対して事前に動作（モーション）の事前学習を行う手法。ビジュアルや言語指示に依存せず、行動データのみから時系列的な運動構造を学習させることで、VLA学習の収束性と性能を大幅に向上させる。 |
| 先行研究と比べてどこがすごい？ | 従来手法はVLA全体を同時に学習させるため、行動生成の初期段階での不安定さがバックボーン（VLM）の学習を妨げていた。本手法は「まず動くことを学び、次に見て理解して動く」という二段階の分離学習を採用することで、データが少ない環境でも安定した学習と高速な収束を実現した点。 |
| 技術や手法のキモはどこ？ | ①行動データのみを用いたフローマッチング型エンコーダ・デコーダによる事前学習、②事前学習済みデコーダをVLAの行動ヘッドとして再利用、③学習初期のみエンコーダの潜在空間を蒸留する「潜在空間アライメント蒸留」、④行動エンコーダを履歴圧縮器として利用する点。 |
| どうやって有効だと検証した？ | LIBEROおよびRoboCasaの2つのシミュレーションベンチマーク、および実機のFrankaアームを用いた計13のタスクで検証。特に、データ不足が深刻な実環境のタスクにおいて、行動事前学習と履歴圧縮の組み合わせが大幅な成功率向上と学習の安定化をもたらすことを示した。 |
| 議論はある？ | 現在のStage 1の学習データセットは比較的小規模であるため、より広範で多様な行動データを用いることで、さらなる汎化性能の向上が期待される。また、蒸留プロセスは初期段階で有効だが、長期間適用しすぎるとモデルの表現の柔軟性を制限する可能性があることが示唆されている。 |
| 次に読むべき論文は？ | [OpenVLA: An open-source vision-language-action model](https://arxiv.org/abs/2406.09246)、[Diffusion Policy: Visuomotor policy learning via action diffusion](https://arxiv.org/abs/2303.04137)、[π0: A vision-language-action flow model for general robot control](https://arxiv.org/abs/2410.24164) |
| PDFリンク | https://arxiv.org/pdf/2606.26095v1 |
