---
title: "HumanTracker: Towards Comprehensive and Human-Aligned Motion Tracking Benchmark"
date: 2026-08-15
arxiv_id: 2608.13555v1
url: http://arxiv.org/abs/2608.13555v1
---

# HumanTracker: Towards Comprehensive and Human-Aligned Motion Tracking Benchmark

| 項目 | 内容 |
|---|---|
| どんなもの？ | ヒューマノイドロボットの動作追従性能を評価するための、包括的かつ人間に寄り添った（Human-Aligned）ベンチマーク「HumanTracker」と、人間による評価を予測する報酬モデル「HumanScore」を提案した論文。従来の運動学的指標では捉えきれない、接触の安定性や人間らしい自然さを評価可能にする。 |
| 先行研究と比べてどこがすごい？ | 既存の評価指標（MPJPE等）がペナルティとして機能せず、人間が見た時の違和感（足の滑りや不自然な接触）を反映できない問題を解決した。約153時間という大規模かつ「日常」「ダイナミック」「インタラクション」「地面動作」の4カテゴリに分類された高品質なデータセットを提供し、細かい失敗要因の特定を可能にした点。 |
| 技術や手法のキモはどこ？ | ヒューマン・イン・ザ・ループによる比較データを用いて学習された、時間的Transformerベースの「HumanScore」報酬モデル。特定のフレームごとの誤差ではなく、5秒間の軌道全体をコンテキストとして評価することで、滑りや安定性といった動的な失敗を捉える点。 |
| どうやって有効だと検証した？ | 主要なヒューマノイドトラッカー（GMT, TWIST2, SONIC, Humanoid-GPT）をHumanTrackerベンチマーク上で評価。HumanScoreが従来の運動学的指標よりも、ドメイン専門家による人間評価と高い整合性（Align Rate 90.83%）を示すことを実証し、その感度分析も行った。 |
| 議論はある？ | 現在の指標はシミュレータ上の特権情報に依存しているため、実機適用には観測可能な特徴量への変換が必要。また、この指標をRLの報酬として直接利用すると、モデルの欠点を悪用した挙動を誘発する可能性があるため、独立した人間による評価を併用すべきとしている。 |
| 次に読むべき論文は？ | [4] Gmt: General motion tracking for humanoid whole-body control (https://arxiv.org/abs/2506.14770) や [24] Sonic: Supersizing motion tracking for natural humanoid whole-body control (https://arxiv.org/abs/2511.07820) などの、今回評価対象となった主要なトラッカーの論文。 |
| PDFリンク | https://arxiv.org/pdf/2608.13555v1 |
