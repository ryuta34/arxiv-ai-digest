---
title: "Don't Drop the BATON: Long-Horizon Robot Manipulation via Agentic Subtask Exploration and Transition-aware Memory"
date: 2026-08-18
arxiv_id: 2608.16889v1
url: http://arxiv.org/abs/2608.16889v1
---

# Don't Drop the BATON: Long-Horizon Robot Manipulation via Agentic Subtask Exploration and Transition-aware Memory

| 項目 | 内容 |
|---|---|
| どんなもの？ | 長期的なロボット操作において、タスクをサブタスク単位の探索と「遷移」を考慮したメモリ管理によって解決する手法「BATON」を提案する論文。従来の強化学習やエンドツーエンド学習による compounding error（誤差の蓄積）の問題を克服し、複雑なマルチステップタスクの成功率を大幅に向上させる。 |
| 先行研究と比べてどこがすごい？ | 従来手法が全タスクを一つの探索単位としていたのに対し、サブタスク単位で探索を行うことで探索コストを指数関数的（$T^K$）から線形（$T \cdot K$）へ削減した点。また、遷移部分（サブタスク間）を明示的に「契約」として言語メモリに保存・管理することで、未知の状況や compounding error に極めて強い。 |
| 技術や手法のキモはどこ？ | 1. 遷移を明示的なオブジェクトとして扱う「遷移認識型メモリ」、2. タスクをサブタスクに分解して逐次的に探索・検証する階層的探索、3. Wristカメラを用いた「呼び出し遷移（Invocation transition）」、状態復元を行う「受け渡し遷移（Handoff transition）」、戦略を継承する「先読み遷移（Lookahead transition）」という3つの遷移制御。 |
| どうやって有効だと検証した？ | RoboMemArenaベンチマーク（1,000ステップを超える household tasks）を用いて評価。従来の最先端手法（FrameSamp+Modulなど）と比較し、タスク成功率（TSR）を11.6ポイント、累積成功率（CSR）を14.9ポイント改善し、Ground-truth（ oracle）をも上回る性能を達成した。 |
| 議論はある？ | 現在の課題として、BDDL（Behavior Description Definition Language）のシーン定義に依存する一部のタスクでは評価上のアーティファクトが存在すること。また、サブタスク間の分解と接続の自動化については、依然としてLLMの推論能力に依存している面がある。 |
| 次に読むべき論文は？ | [1] [Harness VLA (Zhang et al., 2026)](https://arxiv.org/abs/2607.08448) - 本手法の基盤技術。<br>[2] [RoboMME (Dai et al., 2026)](https://arxiv.org/abs/2603.04639) - 評価に使用したメモリベンチマーク。<br>[3] [Voyager (Wang et al., 2023)](https://arxiv.org/abs/2305.16291) - エージェントによるコード生成の先駆け。 |
| PDFリンク | https://arxiv.org/pdf/2608.16889v1 |
