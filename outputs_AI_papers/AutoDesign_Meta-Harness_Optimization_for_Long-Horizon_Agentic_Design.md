---
title: "AutoDesign: Meta-Harness Optimization for Long-Horizon Agentic Design"
date: 2026-08-15
arxiv_id: 2608.13560v1
url: http://arxiv.org/abs/2608.13560v1
---

# AutoDesign: Meta-Harness Optimization for Long-Horizon Agentic Design

| 項目 | 内容 |
|---|---|
| どんなもの？ | 論文から学術ポスターなどの構造化されたメディア出力を自動生成する際、人間がデザインする際のデザイン優先順位（design priors）を学習・蓄積し、再帰的に改善していくメタハーネス最適化フレームワーク「AutoDesign」。 |
| 先行研究と比べてどこがすごい？ | 個別の編集や孤立した試行に留まる既存手法と異なり、生成プロセス全体を「デザインハーネス」として最適化対象とすることで、経験を蓄積・再利用して性能を永続的に向上させ、人間による評価で最高の結果を達成した点。 |
| 技術や手法のキモはどこ？ | 入力から出力を生成する「内側のループ（デザインハーネス）」と、生成結果に基づいてハーネス自体を最適化する「外側のループ（メタハーネス）」の2層構造。成功した改善のみをゲートを介して取り込み、モデルのパラメータを固定したままハーネスを洗練させる手法。 |
| どうやって有効だと検証した？ | 100本の学術論文を対象とした「PosterBench」という独自の評価プロトコルを構築。7つの指標による自動評価に加え、11名の評価者によるシステムブラインドの人間評価（ペア比較）を実施し、他システムと比較して最高スコアを獲得したことを示した。 |
| 議論はある？ | 現在は学術ポスター生成に特化しているが、スライドやWebページ、動画生成などへも拡張可能。評価指標への最適化が過学習（reward-hack）を招かないよう、バージョン管理された evaluator や人間による定期的な監査が必要である。 |
| 次に読むべき論文は？ | [Recursive harness self-improvement](https://arxiv.org/abs/2607.15524)、[Meta-Harness: End-to-end optimization of model harnesses](https://arxiv.org/abs/2603.28052)、[Agentic harness engineering](https://arxiv.org/abs/2604.25850) |
| PDFリンク | https://arxiv.org/pdf/2608.13560v1 |
