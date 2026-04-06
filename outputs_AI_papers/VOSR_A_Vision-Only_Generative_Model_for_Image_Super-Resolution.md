---
title: "VOSR: A Vision-Only Generative Model for Image Super-Resolution"
date: 2026-04-06
arxiv_id: 2604.03225v1
url: http://arxiv.org/abs/2604.03225v1
---

# VOSR: A Vision-Only Generative Model for Image Super-Resolution

| 項目 | 内容 |
|---|---|
| どんなもの？ | 汎用的なテキストベースの拡散モデル（T2I）を流用せず、純粋な視覚データのみで訓練された画像超解像（SR）のための新しい生成フレームワーク「VOSR」。低解像度（LR）入力に対し、忠実かつ高精細な高解像度（HR）画像を生成することを目指す。 |
| 先行研究と比べてどこがすごい？ | T2Iモデル特有の余計な意味的幻覚（ハルシネーション）を抑えつつ、入力画像への忠実度を大幅に向上させた。また、T2Iベースの手法と比べて学習コストを1/10に抑えながら、推論速度と生成品質の両面で高い競争力を維持している点。 |
| 技術や手法のキモはどこ？ | 学習済みの視覚エンコーダーによる「視覚セマンティック条件付け」と、条件を完全除去する従来型CFGの代わりに、構造情報を適度に残す「復元指向ガイダンス（Restoration-oriented guidance）」を導入した点。また、効率的な推論のために蒸留による1ステップ生成を統合した。 |
| どうやって有効だと検証した？ | LSDIR、ScreenSR、RealSRといった複数のデータセットで、PSNRやSSIMなどの歪み指標に加え、LPIPSやMUSIQ等の知覚品質指標を測定。さらに、実用的なモバイル環境での推論速度の比較と、実ユーザーによる主観評価実験を実施し、その優位性を証明した。 |
| 議論はある？ | 現在の学習データの規模やモデル容量が、10B規模のパラメータを持つ巨大なT2I基盤モデルには依然として及ばない点。今後は、さらなるデータの大規模化とモデル容量の拡大、および他の画像復元タスクへの拡張を目指す。 |
| 次に読むべき論文は？ | [29] "Image super-resolution via iterative refinement" (SR3)、[45] "Seesr: Towards semantics-aware real-world image super-resolution"、[52] "Resshift: Efficient diffusion model for image super-resolution by residual shifting" |
| PDFリンク | https://arxiv.org/pdf/2604.03225v1 |
