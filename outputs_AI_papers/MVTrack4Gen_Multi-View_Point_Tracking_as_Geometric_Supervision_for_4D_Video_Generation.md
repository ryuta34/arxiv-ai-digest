---
title: "MVTrack4Gen: Multi-View Point Tracking as Geometric Supervision for 4D Video Generation"
date: 2026-06-25
arxiv_id: 2606.26087v1
url: http://arxiv.org/abs/2606.26087v1
---

# MVTrack4Gen: Multi-View Point Tracking as Geometric Supervision for 4D Video Generation

| 項目 | 内容 |
|---|---|
| どんなもの？ | 単眼ビデオから指定されたカメラ軌道に基づき、幾何学的整合性と動作の一貫性を保った新しい視点のビデオを生成するフレームワーク。明示的な3D再構成を行わず、カメラ条件付けのみを行うモデルの弱点を補完する手法。 |
| 先行研究と比べてどこがすごい？ | 明示的な3D再構成を行わない手法では困難だった「動的なオブジェクトの幾何学的・時間的一貫性」を、3Dアテンションマップの分析を通じて大幅に向上させた。推論時に重い3D再構成を必要とせず、既存のカメラ条件付けモデルの性能を底上げできる。 |
| 技術や手法のキモはどこ？ | ビデオ拡散モデルの特定の層（18層目など）が幾何学的な対応関係を学習していることを見出し、そのアテンションマップを補助的なマルチビュー追跡ヘッドと損失関数で直接監督することで、モデルに明示的な幾何学的・動作的制約を与える点。 |
| どうやって有効だと検証した？ | DAVISおよびiPhoneデータセットを用い、既存のReCamMasterやRedirector等のバックボーンに本手法を統合して評価。視覚品質（VBench等）、幾何学的整合性（MEt3R）、カメラ精度の各指標でSOTAを達成した。 |
| 議論はある？ | 現在のアーキテクチャの制限により解像度とフレーム数が固定されている点、および学習にマルチビューの正解データ（または擬似ラベル）が必要である点。また、拡散モデル特有の推論コストがリアルタイム性を制限している。 |
| 次に読むべき論文は？ | [3] ReCamMaster, [33] Redirector, [28] MV-TAP, [32] Emergent temporal correspondences from video diffusion transformers |
| PDFリンク | https://arxiv.org/pdf/2606.26087v1 |
