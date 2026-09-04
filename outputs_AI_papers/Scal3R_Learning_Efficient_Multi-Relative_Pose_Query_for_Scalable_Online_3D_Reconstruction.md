---
title: "Scal3R: Learning Efficient Multi-Relative Pose Query for Scalable Online 3D Reconstruction"
date: 2026-09-04
arxiv_id: 2609.04201v1
url: http://arxiv.org/abs/2609.04201v1
---

# Scal3R: Learning Efficient Multi-Relative Pose Query for Scalable Online 3D Reconstruction

| 項目 | 内容 |
|---|---|
| どんなもの？ | 長時間のビデオストリームにおいて、オンラインで正確かつ一貫性のある3D再構成を行うためのフレームワーク「Scal3R」です。従来の絶対座標回帰による手法が抱える、長期推論時のドリフトや幾何学的な崩壊といった問題を解決します。 |
| 先行研究と比べてどこがすごい？ | 既存の学習済みバックボーンを完全に固定したまま、わずか約1%のパラメータ追加（学習可能なトークン）のみで、長距離・大規模シーケンスでの安定した再構成を実現した点です。単一のGPUで8時間のファインチューニングにより、オンラインで state-of-the-art の性能を達成しました。 |
| 技術や手法のキモはどこ？ | グローバルな絶対ポーズ回帰から、ローカルな複数参照先に対する相対ポーズクエリへと問題を再定式化した点です。具体的には、「非対称アテンション注入（Asymmetric Attention Injection）」により、画像表現を毀損せずに相対位置を学習し、オンラインの姿勢グラフ最適化（PGO）とループクロージャーを組み合わせることで長期的なドリフトを抑制しています。 |
| どうやって有効だと検証した？ | KITTI、Virtual KITTI、Sintel、TUM-Dynamic、ScanNet、7-Scenes といった多様なベンチマークで評価を行いました。特にKITTIでは、既存の最強オンライン手法と比較して、平均ATE（絶対軌跡誤差）を60%以上削減しました。 |
| 議論はある？ | 性能が凍結されたバックボーンの品質に依存するため、オクルージョンやテクスチャレスな領域での限界があります。また、オンラインバックエンドのループクロージャーやキーフレーム選択に閾値が必要であり、これらの自動化・強靭化が将来の課題です。 |
| 次に読むべき論文は？ | [CUT3R](https://arxiv.org/abs/2505.10510) (Wang et al., 2025) や [STream3R](https://arxiv.org/abs/2508.10893) (Lan et al., 2025) などのベースラインとなった先行研究。 |
| PDFリンク | https://arxiv.org/pdf/2609.04201v1 |
