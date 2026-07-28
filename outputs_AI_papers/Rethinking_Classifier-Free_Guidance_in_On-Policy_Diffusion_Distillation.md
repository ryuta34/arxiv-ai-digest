---
title: "Rethinking Classifier-Free Guidance in On-Policy Diffusion Distillation"
date: 2026-07-28
arxiv_id: 2607.24731v1
url: http://arxiv.org/abs/2607.24731v1
---

# Rethinking Classifier-Free Guidance in On-Policy Diffusion Distillation

| 項目 | 内容 |
|---|---|
| どんなもの？ | 分類器フリーガイダンス（CFG）を用いた拡散モデルのオンポリシー蒸留（OPD）における、正・負のブランチ間の誤差が相殺し合う「負のブランチ非対称性（NBA）」を特定し、それを解消する新しい蒸留手法を提案する論文。 |
| 先行研究と比べてどこがすごい？ | 従来手法（Naive OPD）は、推論時のガイダンススケールを変化させると性能が急激に劣化する問題があった。提案手法（PDM）は、ブランチレベルで独立して制約をかけることで、推論時のスケール変化に対して極めて頑健な性能を達成した。 |
| 技術や手法のキモはどこ？ | CFG構成後の結合予測だけでなく、正ブランチの予測とCFG条件付き方向（正と負の差分）を個別にマッチングさせる「Positive–Direction Matching (PDM)」を導入し、ブランチ間の誤差補償を数学的に排除した点。 |
| どうやって有効だと検証した？ | テキストレンダリングおよびリファレンス条件付き画像生成での実験に加え、動画生成タスク（密な制御から疎なキーフレーム制御への蒸留）において、提案手法が様々なガイダンススケール下で高い忠実度を維持することを示した。 |
| 議論はある？ | PDMと、比較対象のIBMはどちらもブランチレベルでエラーをゼロにする解決策を持ち、なぜPDMの方が優れているかの理論的証明は不十分であり、現時点では実証的な利点に留まっている。 |
| 次に読むべき論文は？ | [DiffusionOPD](https://arxiv.org/abs/2605.15055) (Li et al., 2026b), [Flow-OPD](https://arxiv.org/abs/2605.08063) (Fang et al., 2026), [DanceOPD](https://arxiv.org/abs/2606.27377) (Zhou et al., 2026) |
| PDFリンク | https://arxiv.org/pdf/2607.24731v1 |
