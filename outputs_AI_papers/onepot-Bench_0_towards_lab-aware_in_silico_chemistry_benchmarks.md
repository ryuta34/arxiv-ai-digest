---
title: "onepot-Bench 0: towards lab-aware in silico chemistry benchmarks"
date: 2026-08-04
arxiv_id: 2608.02595v1
url: http://arxiv.org/abs/2608.02595v1
---

# onepot-Bench 0: towards lab-aware in silico chemistry benchmarks

| 項目 | 内容 |
|---|---|
| どんなもの？ | 湿式実験（ウェットラボ）における実用的な意思決定能力を評価するための、言語モデル向け化学ベンチマーク「onepot-Bench 0」の提案。化学情報の読み書き、安全性評価、反応予測という、ラボ環境で求められる一連の能力を測定する。 |
| 先行研究と比べてどこがすごい？ | 公開データベースに依存せず、ラボ内の独自実験データを使用することで、モデルの「記憶」によるベンチマーク汚染を排除した点。さらに、単純な化学知識だけでなく、合成計画や安全性、触媒選択といった実験遂行の信頼性を問うている。 |
| 技術や手法のキモはどこ？ | cheminformatics能力を測る「ChemAbacus」、安全性を測る「SynthRefusal」、独自実験データに基づく「SynthBench」の3層構造。特に安全評価では、単純な拒否率ではなく、対象物や表現形式に依存する「アライメント指標」を導入した。 |
| どうやって有効だと検証した？ | 6社13モデルを対象に、API経由で推論を実施。計算化学タスクと非計算タスクの比較、安全性に関するモデルの極端な挙動（無差別拒否や過度な許可）の分析、および反応予測の正答率とコストの比較により検証。 |
| 議論はある？ | モデルは基本的な化学問題には強いが、反応予測などの合成判断では単純な統計モデルにも劣る。また、安全性評価ではリスクの理解ではなく特定の分子に対する知識の記憶に依存している可能性が示唆された。 |
| 次に読むべき論文は？ | [11] Predicting reaction performance in C–N cross-coupling using machine learning (Science, 2018), [12] Using Machine Learning To Predict Suitable Conditions for Organic Reactions (ACS Central Science, 2018) |
| PDFリンク | https://arxiv.org/pdf/2608.02595v1 |
