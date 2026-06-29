---
title: "DexCompose: Reusing Dexterous Policies for Multi-Task Manipulation with a Single Hand"
date: 2026-06-29
arxiv_id: 2606.28323v1
url: http://arxiv.org/abs/2606.28323v1
---

# DexCompose: Reusing Dexterous Policies for Multi-Task Manipulation with a Single Hand

| 項目 | 内容 |
|---|---|
| どんなもの？ | 1つの手で複数のタスクを連続して実行する際、先行するスキルの把持状態を維持しながら、別の操作スキルを同時に実行するための構成的フレームワーク。事前学習された単一タスク用ポリシーを再利用し、指ごとの制御権を動的に割り当てることで、タスク間の干渉を抑制する。 |
| 先行研究と比べてどこがすごい？ | 従来手法（単純なポリシーの連結）で見られた指の動作競合による把持の失敗を、指単位の所有権（Action Ownership）と残差学習を用いたデュアル安定化機構によって大幅に改善した点。タスクごとの再学習なしで、既存の強力なポリシーを効率的に組み合わせて成功率77.4%を達成した。 |
| 技術や手法のキモはどこ？ | 指の「所有権」を明示するマスク生成（指のリリース試験とLLMによる選択）と、把持維持用とタスク遂行用の2つの独立した残差（Dual Residual）を用いた学習。把持を維持すべき指とタスクに使う指を分離し、残差によって制約下での適応的な動作を可能にした点。 |
| どうやって有効だと検証した？ | 4つの把持スキルと4つの操作スキルを組み合わせた計16の複合タスク環境（Isaac Lab）で評価。ベースライン（Frozen Graspや単純な残差学習）と比較し、複合成功率で15.8%の大幅な向上を確認し、消去試験（Ablation Study）で各コンポーネントの有効性を実証した。 |
| 議論はある？ | 現在は2つのシーケンシャルなスキルの合成に焦点を当てており、より長期間の複数のタスクを組み合わせた連続的な操作への拡張が今後の課題である。また、LLMを用いたマスク選択の推論コストについても更なる検討が必要。 |
| 次に読むべき論文は？ | [1] [HANDFUL: Sequential grasp-conditioned dexterous manipulation with resource awareness](https://arxiv.org/abs/2606.00000)（※該当論文の引用文献を参照）や、拡散ポリシーを用いた[Diffusion policy: Visuomotor policy learning via action diffusion](https://arxiv.org/abs/2303.04137) |
| PDFリンク | https://arxiv.org/pdf/2606.28323v1 |
