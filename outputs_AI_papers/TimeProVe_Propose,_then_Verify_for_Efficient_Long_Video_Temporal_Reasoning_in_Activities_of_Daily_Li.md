---
title: "TimeProVe: Propose, then Verify for Efficient Long Video Temporal Reasoning in Activities of Daily Living"
date: 2026-06-19
arxiv_id: 2606.20561v1
url: http://arxiv.org/abs/2606.20561v1
---

# TimeProVe: Propose, then Verify for Efficient Long Video Temporal Reasoning in Activities of Daily Living

| 項目 | 内容 |
|---|---|
| どんなもの？ | 長時間の未トリミング動画に対する効率的な質問応答（LVQA）フレームワーク「TIMEPROVE」。動画全体をVLM（大規模視覚言語モデル）で処理するのではなく、軽量なモジュールで関連箇所を特定し、必要なクリップのみをVLMで検証するハイブリッド手法です。 |
| 先行研究と比べてどこがすごい？ | 従来手法に比べ、VLMの推論回数を75%、計算コストを93%削減しながら、ベンチマーク（OTB）において既存手法を7.3%上回る精度を達成しました。また、専門的な訓練なしで時間的接地（Temporal Grounding）タスクでもSOTAに匹敵する性能を示しています。 |
| 技術や手法のキモはどこ？ | 軽量なアクション検出器で動画のイベントタイムラインを作成し、エッジLLMを用いて質問に関連する証拠区間を推論・生成する「ACE（Action-based Candidate Evidence）モジュール」です。これにより、動画全体を読み込むことなく、確度の高い候補区間のみを抽出して検証可能です。 |
| どうやって有効だと検証した？ | 新規のオープンエンド型ベンチマーク「OPENTSUBENCH (OTB)」を構築し、既存のSFT手法やエージェントベースの手法と比較評価しました。また、Charades-STAを用いた時間的接地タスクでの性能評価や、ノイズ耐性の検証も行っています。 |
| 議論はある？ | 短時間の行動ベースの推論には適していますが、非常に長い区間にまたがる拡散したシーンの理解には、さらなる証拠集約の手法が必要です。また、最終的な検証精度は使用するVLMの性能に依存します。 |
| 次に読むべき論文は？ | [VideoTree](https://arxiv.org/abs/2512.05774)、[VideoLLaMA3](https://arxiv.org/abs/2501.03106)、[Time-R1](https://arxiv.org/abs/2505.13508) |
| PDFリンク | https://arxiv.org/pdf/2606.20561v1 |
