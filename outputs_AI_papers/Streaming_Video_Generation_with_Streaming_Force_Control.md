---
title: "Streaming Video Generation with Streaming Force Control"
date: 2026-06-08
arxiv_id: 2606.07508v1
url: http://arxiv.org/abs/2606.07508v1
---

# Streaming Video Generation with Streaming Force Control

| 項目 | 内容 |
|---|---|
| どんなもの？ | 連続的な力（フォース）入力を用いて、動画生成をリアルタイムで制御・操作可能なストリーミング動画生成フレームワーク。ユーザーは生成中の動画に対して、風のような「全体的な力」や、押し引きのような「局所的な力」を随時与えることで、物理的に妥当な挙動を誘発できる。 |
| 先行研究と比べてどこがすごい？ | 従来手法（Force-Prompting等）が分離していた全体的・局所的な力を単一の表現で統合し、さらに双方向拡散モデルを因果的な自己回帰モデルへ蒸留することで、リアルタイムなストリーミング生成と時間変化する力への柔軟な応答を実現した点。 |
| 技術や手法のキモはどこ？ | ① 全体的・局所的な力を共通のピクセルアライメントされたマスク付き力マップとして符号化する「統一的力表現」、② 力の動的な変化を学習させるデータセット構築、③ 双方向教師モデルから因果的な学生モデルへ物理的な対応関係を保持したまま蒸留する「力認識蒸留パイプライン」の3点。 |
| どうやって有効だと検証した？ | 40ケースのテストセットを用いた人間による知覚評価（力への追従性、物理的妥当性、視覚品質）と、Physics-IQベンチマークに基づく物理的一貫性の定量評価を実施。さらに、力表現や diverse な学習データの寄与を検証するアブレーションスタディを行った。 |
| 議論はある？ | 現在の表現は2次元平面の力に限定されており、奥行き方向の力や多物体間の複雑な相互作用（衝突やスタッキング）、非剛体（流体や砂など）の力学応答には限界がある。今後はより高度な物理的推論や、多様な接触・非接触力への対応が課題。 |
| 次に読むべき論文は？ | [15] Force Prompting: Video generation models can learn and generalize physics-based control signals ([arXiv:2505.19386](https://arxiv.org/abs/2505.19386)), [26] Self forcing: Bridging the train-test gap in autoregressive video diffusion ([arXiv:2506.08009](https://arxiv.org/abs/2506.08009)) |
| PDFリンク | https://arxiv.org/pdf/2606.07508v1 |
