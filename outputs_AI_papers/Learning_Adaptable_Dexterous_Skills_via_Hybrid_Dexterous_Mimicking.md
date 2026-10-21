---
title: "Learning Adaptable Dexterous Skills via Hybrid Dexterous Mimicking"
date: 2026-10-21
arxiv_id: 2610.28628v1
url: http://arxiv.org/abs/2610.28628v1
---

# Learning Adaptable Dexterous Skills via Hybrid Dexterous Mimicking

| 項目 | 内容 |
|---|---|
| どんなもの？ | 数秒間の人間の手と物体の相互作用（HOI）動画から、器用な操作スキルを学習し、未知の状況や目標に対しても汎用的に適応できる強化学習フレームワーク「ADADEX」を提案している。|
| 先行研究と比べてどこがすごい？ | 従来の「モーション追従（模倣）」は汎用性が低く、「ゴール達成型強化学習」は不自然な動きになりやすいという欠点を克服した。人間らしい機能的動きと、未見の目標への高い適応能力を両立している。 |
| 技術や手法のキモはどこ？ | 「Hybrid Dexterous Mimicking」という手法。密な報酬による「モーション追従環境」で人間の動作先例を学習し、疎な報酬とノイズを加えた「汎化環境」で目標達成を学習する2種類の環境を共有ポリシーで同時に学習させる点。 |
| どうやって有効だと検証した？ | 12種類のGRABデータセットのオブジェクトと9種類の実動画から変換したHOI参照に対し、追従精度と未知の目標への到達率を評価。ベースライン（ManipTrans, SimToolReal等）を大きく上回る性能を実証した。 |
| 議論はある？ | 現状はオブジェクトと参照軌道ごとに1つのポリシーを学習する必要がある。今後は単一のポリシーで多様なオブジェクトや動作をカバーすることや、より複雑な形状（変形物体など）への対応が課題。 |
| 次に読むべき論文は？ | [Dex4D (Kuang et al., 2026)](https://arxiv.org/abs/2602.15828)、[SimToolReal (Kedia et al., 2026)](https://arxiv.org/abs/2602.16863)、[HIL (Wang et al., 2026b)](https://arxiv.org/abs/2602.20375) |
| PDFリンク | https://arxiv.org/pdf/2610.28628v1 |
