---
title: "When Should LLMs Abstain? Chain-of-Self-Questioning for Selective Risk Control"
date: 2026-09-16
arxiv_id: 2609.17516v1
url: http://arxiv.org/abs/2609.17516v1
---

# When Should LLMs Abstain? Chain-of-Self-Questioning for Selective Risk Control

| 項目 | 内容 |
|---|---|
| どんなもの？ | 大規模言語モデル（LLM）が自身の知識不足を自己評価し、回答すべきか棄権すべきかを判断するプロンプトベースのフレームワーク「Chain-of-Self-Questioning (CoSQ)」を提案した研究です。回答の正確性を高めつつ、根拠のない回答（ハルシネーション）を削減するための選択的な意思決定プロセスを実現します。 |
| 先行研究と比べてどこがすごい？ | 追加学習や複数モデルの利用、タスク固有のリソースを必要とせず、プロンプトのみでブラックボックスモデルやホスト型モデルに適用可能です。また、特定の閾値に固定せず、リスクとカバレッジのトレードオフを調整可能な「リスク・カバレッジ・フロンティア」を提示しました。 |
| 技術や手法のキモはどこ？ | モデルが回答に必要な情報を分解し、各要素に対する信頼度を自己評価する3段階（情報抽出・サポート評価・ゲート判断）のパイプラインです。Grounded, Critical, Adaptiveの3つのバリエーションにより、リスク回避の厳格さを選択できます。 |
| どうやって有効だと検証した？ | TruthfulQA（817項目）を用いた複数選択肢問題および、Natural Questions（300項目）のオープンフォーム質問を用い、11のモデルファミリーで実験を行いました。CoT（Chain-of-Thought）と比較し、一貫して誤回答の発生率（HR）を低減し、回答精度（AA）を向上させることを示しました。 |
| 議論はある？ | 信頼度はLLM自身から得られるため独立した確率ではなく、誤った回答のコストが高い状況での利用を想定しています。また、ドメインごとに最適な閾値が異なることや、モデルの性能はプロンプトの微調整でさらに向上する可能性がある点が指摘されています。 |
| 次に読むべき論文は？ | [SelectiveNet: A deep neural network with an integrated reject option](https://proceedings.mlr.press/v97/geifman19a.html) や、ハルシネーション検出に関する [SelfCheckGPT](https://aclanthology.org/2023.emnlp-main.557/) などの手法。 |
| PDFリンク | https://arxiv.org/pdf/2609.17516v1 |
