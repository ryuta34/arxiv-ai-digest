---
title: "Pixel: A Co-Designed Full-Stack Robot System for Learning General-Purpose Mobile Manipulation"
date: 2026-11-04
arxiv_id: 2611.03648v1
url: http://arxiv.org/abs/2611.03648v1
---

# Pixel: A Co-Designed Full-Stack Robot System for Learning General-Purpose Mobile Manipulation

| 項目 | 内容 |
|---|---|
| どんなもの？ | 汎用的なモバイルマニピュレーション学習のために、ロボットハードウェア、データ収集インターフェース、制御スタック、学習パイプラインを統合的に共同設計したフルスタック・ロボットシステム「Pixel」。15,000ドル以下のコストで構築可能な、 wheeled humanoid（車輪型ヒューマノイド）プラットフォームを提案している。 |
| 先行研究と比べてどこがすごい？ | 個別に開発されがちなハードウェアと学習スタックを「共同設計」することで、人からロボットへのスキル転送におけるギャップ（身体性、センサー、制御の不一致）を最小化した点。安価なコストで高い再現性と、人間によるデモンストレーションからのスケーラブルな学習性能を実現した。 |
| 技術や手法のキモはどこ？ | ヒューマノイドの形態を模した車輪型ベースと垂直昇降機構、および共通の「Relative-base」アクションスペースの導入。また、Fabricsベースの全身制御と、人間とロボットで共通のタスク空間を用いることで、人間によるデモを直接ロボットの制御目標にマッピングできる設計にしたこと。 |
| どうやって有効だと検証した？ | 「Toy Cleanup」や「Tidy Pillow」等の複数の実世界タスクにおいて、本システムを用いたポリシー学習の成功率を評価。また、ハードウェア（各自由度の寄与度）、データ収集（リーダーアーム vs VR vs 人間）、学習スタック（観測空間、アクション空間）の各要素について体系的なアブレーション実験を行った。 |
| 議論はある？ | 構造が簡素化されているため、階段の昇降のような高度な地形走破能力はない。また、今回導入したウェアラブルなデータ収集装置は接触や細かな身体情報をすべては捉えきれない点。今後はよりリッチな全身トラッキングや、より複雑な操作スキルの階層的学習への拡張が課題。 |
| 次に読むべき論文は？ | [Pixel-UMI: Learning environment-aware whole-body manipulation from sensorized human demonstrations](https://pixel-robot.com/pixel-umi/) (本論文のcompanion paper) |
| PDFリンク | https://arxiv.org/pdf/2611.03648v1 |
