---
title: "ProcFunc: Function-Oriented Abstractions for Procedural 3D Generation in Python"
date: 2026-04-30
arxiv_id: 2604.26943v1
url: http://arxiv.org/abs/2604.26943v1
---

# ProcFunc: Function-Oriented Abstractions for Procedural 3D Generation in Python

| 項目 | 内容 |
|---|---|
| どんなもの？ | Blenderベースのプロシージャル3D生成を効率化するためのPythonライブラリ「ProcFunc」。関数型の抽象化により、コードベースでの複雑な3Dアセット生成、合成、編集を直感的に行えるように設計されている。 |
| 先行研究と比べてどこがすごい？ | Blenderの複雑なGUI依存状態や低レベルなAPIを隠蔽し、型安全で明示的な引数を持つ関数群として提供する点。また、compute graphの自動抽出による静的解析や、大規模なコンポーザビリティ（構成可能性）を実現しており、VLM（視覚言語モデル）によるコード生成時のエラー率を劇的に低減できる。 |
| 技術や手法のキモはどこ？ | 497個の独立したアトミックなPython関数によるAPI定義、ノードグラフのPythonコードへの変換（トランスパイラ）、およびランダムサンプリングされた処理の静的解析を可能にするプログラムトレーサーの提供。 |
| どうやって有効だと検証した？ | BlenderGymを用いたVLMによるパラメータ編集・素材生成タスクでの精度とエラー率の比較。また、独自の室内生成器を用いたデータセット作成効率、生成速度、メモリ使用量、およびステレオマッチングモデルの学習結果を通じて有効性を評価した。 |
| 議論はある？ | 現在の室内生成器は汎用的な部屋の生成に限定されており、特定用途（浴室など）には対応していない点。また、モデルが訓練データに含まれていないため、学習済みモデルのポテンシャルを完全には引き出せていない可能性がある。 |
| 次に読むべき論文は？ | [Infinigen: Infinite Photorealistic Worlds using Procedural Generation](https://arxiv.org/abs/2306.00955) |
| PDFリンク | https://arxiv.org/pdf/2604.26943v1 |
