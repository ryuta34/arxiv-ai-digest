---
title: "MotiMotion: Motion-Controlled Video Generation with Visual Reasoning"
date: 2026-05-22
arxiv_id: 2605.22818v1
url: http://arxiv.org/abs/2605.22818v1
---

# MotiMotion: Motion-Controlled Video Generation with Visual Reasoning

| 項目 | 内容 |
|---|---|
| どんなもの？ | ユーザーの意図を汲み取り、物理法則や因果関係に基づいた自然な動画生成を実現する、動画生成モデル「MotiMotion」を提案している。視覚言語モデル（VLM）を活用した推論と、不完全な入力を許容する柔軟な制御スキームを組み合わせた枠組みである。 |
| 先行研究と比べてどこがすごい？ | 従来のモデルがユーザーの不完全な軌跡入力をそのまま強制的に実行する「機械的な命令」にとどまっていたのに対し、本作は「推論に基づく計画」として動画生成を再定義した。物理的な二次的影響や相互作用を予測し、より plausibility（尤もらしさ）の高い結果を得られる点が優位である。 |
| 技術や手法のキモはどこ？ | VLMを用いた「推論」フェーズによる詳細なモーション計画の生成と、ユーザー入力の不確実性を考慮する「Confidence-Aware（信頼度認識）制御」の組み合わせ。特に、入力軌跡の信頼度に応じて生成モデルがモデル自身の先験的知識を優先させる弾力的な制御機構が鍵である。 |
| どうやって有効だと検証した？ | 物理的推論や因果伝播を伴う62個のプリイベント画像セット「MotiBench」を独自に構築し、VLMによる自動評価および12名による人間によるTwo-Alternative Forced Choice (2AFC)試験を実施。既存手法と比較して、物理的リアリズム、フォトリアリズム、意味的一貫性において高い勝率を達成した。 |
| 議論はある？ | 現在のフレームワークは推論時のレイテンシ（応答速度）が課題であり、外部APIへの依存がリアルタイム制御を制限する可能性がある。将来的には、より小さなローカルVLMの活用や、推論結果をモデル自体に蒸留する手法が期待される。 |
| 次に読むべき論文は？ | [Wan-Move: Motion-controllable video generation via latent trajectory guidance (Chu et al., 2025)](https://arxiv.org/abs/2505.22818) ※本論文のベースモデル、または引用文献の[Motion Prompting (Geng et al., 2025)](https://arxiv.org/abs/2505.22818) |
| PDFリンク | https://arxiv.org/pdf/2605.22818v1 |
