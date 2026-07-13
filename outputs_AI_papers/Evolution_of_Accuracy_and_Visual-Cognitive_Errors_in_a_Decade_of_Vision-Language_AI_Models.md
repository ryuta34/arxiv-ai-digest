---
title: "Evolution of Accuracy and Visual-Cognitive Errors in a Decade of Vision-Language AI Models"
date: 2026-07-13
arxiv_id: 2607.09654v1
url: http://arxiv.org/abs/2607.09654v1
---

# Evolution of Accuracy and Visual-Cognitive Errors in a Decade of Vision-Language AI Models

| 項目 | 内容 |
|---|---|
| どんなもの？ | 過去10年間（2017-2025年）のビジョン言語モデル（VLM/MLLM）の進化を、複雑な社会的相互作用を含む新規データセット「CSB」を用いて評価した研究。モデルが生成する記述の精度向上と、その背景にある「視覚的・認知的エラー」の変遷を体系的に分析している。 |
| 先行研究と比べてどこがすごい？ | 従来のMS-COCOのような単純な画像データではなく、複雑な人間行動や社会的な文脈を要する「CSBデータセット」を導入した点。また、モデルの出力を単なる指標評価にとどめず、人間科学的観点から5種類のエラー（検出、認識、幻覚、シーン理解、空間依存）に分類・定性分析した点が独自である。 |
| 技術や手法のキモはどこ？ | MLLMの内部構造がブラックボックスであることを踏まえ、モデル入力に対するマスク処理（隠蔽）や特定箇所へのターゲット質問を行うことで、モデルが画像のどの領域を重視して記述を生成しているかを人間と比較分析する手法を確立した。 |
| どうやって有効だと検証した？ | 9つのモデル（pre-MLLM 4種とMLLM 5種）を対象に、CSBとMS-COCOの各100画像を用いて評価。人間が作成したゴールドスタンダードと比較し、Gemini-SI/GPT-SI（セマンティック類似度）を用いて精度を算出したほか、ブートストラップ法を用いた統計的有意差検定により堅牢性を確保した。 |
| 議論はある？ | MLLMは精度面で人間レベルに近づいたが、依然として「空間依存エラー（人間とは異なる領域を根拠に記述する現象）」が残存している。このエラーは、3次元空間の身体的推論の難しさに起因する可能性を指摘している。サンプルサイズが200画像と限定的である点も今後の課題としている。 |
| 次に読むべき論文は？ | [57] S. Tong et al., "Eyes wide shut? exploring the visual shortcomings of multimodal llms", CVPR 2024 / [58] Y. Zhang et al., "Are mllms trapped in the visual room?", PRCV 2025 |
| PDFリンク | https://arxiv.org/pdf/2607.09654v1 |
