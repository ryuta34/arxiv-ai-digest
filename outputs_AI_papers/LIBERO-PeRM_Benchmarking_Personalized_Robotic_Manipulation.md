---
title: "LIBERO-PeRM: Benchmarking Personalized Robotic Manipulation"
date: 2026-10-16
arxiv_id: 2610.22372v1
url: http://arxiv.org/abs/2610.22372v1
---

# LIBERO-PeRM: Benchmarking Personalized Robotic Manipulation

| 項目 | 内容 |
|---|---|
| どんなもの？ | パーソナライズされたロボット操作（PeRM）を評価するための新しいベンチマーク「LIBERO-PeRM」です。タスクの成功とユーザーの好み（嗜好）の満足度を分離して評価できる、312のタスクを含む包括的なデータセットとパイプラインを提案しています。 |
| 先行研究と比べてどこがすごい？ | 従来のロボット操作ベンチマークは主にタスク遂行能力のみを重視していましたが、本研究は「好み（モーション、スキル、ユーザープロフィール）」を明示的な評価軸として分離した点が新規です。また、自動生成パイプラインにより、言語ベースの嗜好とタスクを組み合わせた広範な評価を可能にしました。 |
| 技術や手法のキモはどこ？ | 嗜好のタクソノミー（モーション、スキル、ユーザープロフィールの3分類）を定義し、VLM（Vision-Language Model）を活用してレイアウト変更やプランニングを自動化する手続き型生成パイプラインを構築した点です。また、タスク成功と嗜好満足度を両立させるための「混合トレーニング（Mixed training）」手法を提案しています。 |
| どうやって有効だと検証した？ | 5つの主要なタスクスイート（SinglePref, PrefScale, PrefConflict, PrefCompose, ComprePref）を構成し、既存のVLAモデルを用いてゼロショット性能や、ファインチューニングによる学習効率、一般化能力、多重嗜好の合成と衝突処理を網羅的に評価しました。 |
| 議論はある？ | 言語化可能な嗜好のみを対象としており、暗黙的な好みや非言語的な嗜好、長期的なユーザーインタラクションの履歴は考慮されていません。また、人間による評価は初期段階のものであり、実機による長期的なユーザー評価は今後の課題です。 |
| 次に読むべき論文は？ | [23] Bo Liu et al., "LIBERO: Benchmarking knowledge transfer for lifelong robot learning" (https://arxiv.org/abs/2306.15447), [51] Alexander Khazatsky et al., "DROID: A Large-Scale In-The-Wild Robot Manipulation Dataset" (https://arxiv.org/abs/2403.12945) |
| PDFリンク | https://arxiv.org/pdf/2610.22372v1 |
