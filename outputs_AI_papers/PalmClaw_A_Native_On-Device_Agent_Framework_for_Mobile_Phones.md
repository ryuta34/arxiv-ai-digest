---
title: "PalmClaw: A Native On-Device Agent Framework for Mobile Phones"
date: 2026-07-15
arxiv_id: 2607.13027v1
url: http://arxiv.org/abs/2607.13027v1
---

# PalmClaw: A Native On-Device Agent Framework for Mobile Phones

| 項目 | 内容 |
|---|---|
| どんなもの？ | スマートフォン上で動作し、エージェントのセッション、メモリ、ツール実行などをネイティブに管理するモバイル用エージェントフレームワーク「PalmClaw」。従来のGUI操作に頼る手法とは異なり、デバイスの機能を明示的な引数を持つツールとして直接扱う。 |
| 先行研究と比べてどこがすごい？ | 外部のデスクトップやクラウドサーバーを介さずスマホ単体で完結するため、セットアップが容易（約2分）で環境依存が少ない。また、GUI操作のような画面変化に弱い手法ではなく、デバイス機能をAPI的に制御することで、タスク成功率を11.5%向上させ、完了時間を94.9%短縮した。 |
| 技術や手法のキモはどこ？ | デバイス機能を「device tools」として定義し、明確なスキーマ、権限管理、実行境界（Boundary）を設けた点。モデルからの指示が適切な権限やワークスペース内に収まっているかを実行前に検証し、必要に応じてユーザーに確認や権限付与を求める制御構造を持つ。 |
| どうやって有効だと検証した？ | 「MobileTask（70タスク）」および「AssistantBench（19タスク）」を用いて評価。MobileClawやApkClaw等の既存手法と比べ、タスク成功率、完了時間、アクション数、トークン数などの指標で比較実験を行い、その効率性と有効性を立証した。 |
| 議論はある？ | セキュリティ面では、LLMプロバイダに対してプロンプトやタスクコンテキストを送信する必要があるため、ユーザーデータのフローを明確に管理する必要がある。また、現在サポート外の操作に対する挙動や、複雑な権限要件への対応が課題となる。 |
| 次に読むべき論文は？ | [1] [ReAct: Synergizing reasoning and acting in language models](https://arxiv.org/abs/2210.03629) <br> [4] [OpenClaw: Personal ai assistant](https://github.com/openclaw/openclaw) <br> [17] [AndroidWorld: A dynamic benchmarking environment for autonomous agents](https://arxiv.org/abs/2405.14573) |
| PDFリンク | https://arxiv.org/pdf/2607.13027v1 |
