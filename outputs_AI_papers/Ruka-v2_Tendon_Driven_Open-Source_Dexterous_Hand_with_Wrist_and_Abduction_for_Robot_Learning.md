---
title: "Ruka-v2: Tendon Driven Open-Source Dexterous Hand with Wrist and Abduction for Robot Learning"
date: 2026-03-30
arxiv_id: 2603.26660v1
url: http://arxiv.org/abs/2603.26660v1
---

# Ruka-v2: Tendon Driven Open-Source Dexterous Hand with Wrist and Abduction for Robot Learning

| 項目 | 内容 |
|---|---|
| どんなもの？ | 1,500ドル以下で製作可能な、オープンソースの腱駆動型ヒューマノイドロボットハンド「Ruka-v2」の提案。2自由度の並列手首と指の屈伸・内転/外転機能を備え、ロボット学習における手作業のボトルネックを解消する。 |
| 先行研究と比べてどこがすごい？ | 高価な市販品（数万ドル以上）と比較して圧倒的に低コストかつ修理が容易。前身のRukaと比較し、手首の可動域と指の独立した動きが加わったことで、テレオペレーションにおける完了時間を51.3%短縮し、成功率を21.2%向上させた。 |
| 技術や手法のキモはどこ？ | デカップルされた2自由度並列手首機構によるスムーズな動作、指の内転/外転を可能にする独立したナックルモジュール、および再現性を高めるための固定長DIP-PIP連結機構と着脱式磁気エンコーダの統合。 |
| どうやって有効だと検証した？ | 10のシングルアーム操作タスクと3つの両手操作タスクを用いたテレオペレーション試験、および3つのタスクにおける自律型ポリシー学習。さらに5時間の連続動作試験による熱的安定性と、負荷試験による機械的堅牢性の検証を行った。 |
| 議論はある？ | 線形補間を用いた関節とモータ間のマッピングにおける「線形性の仮定」が未検証であること。また、e-fleshに触覚センサを統合する際、磁気干渉が発生する可能性がある点を今後の課題としている。 |
| 次に読むべき論文は？ | [18] A. Zorin et al., "Ruka: Rethinking the design of humanoid hands with learning" (Ruka-v2のベースとなった研究) <br> [27] Y. Qin et al., "Anyteleop: A general vision-based dexterous robot arm-hand teleoperation system" (採用されたretargeting手法) |
| PDFリンク | https://arxiv.org/pdf/2603.26660v1 |
