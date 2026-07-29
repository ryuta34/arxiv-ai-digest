---
title: "$π\mathbf{R}^2$: Reactive Real-time Flow Policies"
date: 2026-07-29
arxiv_id: 2607.26055v1
url: http://arxiv.org/abs/2607.26055v1
---

# $π\mathbf{R}^2$: Reactive Real-time Flow Policies

| 項目 | 内容 |
|---|---|
| どんなもの？ | 大規模な事前学習済みバックボーン（VLM）を用いつつ、ロボットの操作において高い反応性とリアルタイム性を実現する「πR²」という手法。拡散モデルやフローマッチングベースのポリシーにおける、推論遅延による「開ループ実行」の問題を解決した。 |
| 先行研究と比べてどこがすごい？ | 従来手法（ACT等）の大きな計算コストを抑えつつ、アクション予測の遅延を最大4倍削減できる点。 vision-languageの処理とアクション予測を非同期に分けることで、大規模モデルの表現力を維持しながら高頻度な（25Hzでの）クローズドループ制御を可能にした。 |
| 技術や手法のキモはどこ？ | ① 観測入力を、高速な「proprioception（固有感覚）」と低速な「vision-language」に分離する非同期チャネル設計。② 推論の計算遅延に応じて、アクションChunk内のノイズレベルを動的に調整する「latency-adaptive flow schedule」。 |
| どうやって有効だと検証した？ | MuJoCo Playgroundを用いたシミュレーションでの「Leap Cube Reorientation」課題と、実機（xArm6+XHand）を用いた「Don't Spill」「Tidy up Book」「Insert Box」「Catch Book」の4つのタスクで検証。従来手法に対して成功率を最大23%〜30%向上させた。 |
| 議論はある？ | モデル内部の計算遅延には対応したが、ネットワーク通信など外部由来の遅延には未対応。また、アーキテクチャ自体は固定であり、proprioceptiveな特徴量により特化した構造へ改良する余地がある。 |
| 次に読むべき論文は？ | [18] Diffusion forcing: Next-token prediction meets full-sequence diffusion, [29] Real-time execution of action chunking flow policies, [32] Faster: Rethinking real-time flow VLAs |
| PDFリンク | https://arxiv.org/pdf/2607.26055v1 |
