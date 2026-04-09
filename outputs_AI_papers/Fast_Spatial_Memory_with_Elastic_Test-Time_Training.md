---
title: "Fast Spatial Memory with Elastic Test-Time Training"
date: 2026-04-09
arxiv_id: 2604.07350v1
url: http://arxiv.org/abs/2604.07350v1
---

# Fast Spatial Memory with Elastic Test-Time Training

| 項目 | 内容 |
|---|---|
| どんなもの？ | 長い動画シーケンスから時空間表現を効率的に学習・再現する4D再構成モデル「Fast Spatial Memory (FSM)」の提案。従来のテスト時学習（TTT）における過学習や破滅的忘却の問題を解決し、長尺シーケンスに対するスケーラブルな適応を実現した。 |
| 先行研究と比べてどこがすごい？ | 既存のLaCT（Large-Chunk Test-Time Training）は完全な可塑性ゆえの重みのドリフトが課題であったが、本手法は「弾性的な重み統合（Elastic Weight Consolidation）」を導入することで、安定性と適応性のバランスを両立。メモリ消費を抑えつつ、長期間の動的な環境変化にも対応可能な点。 |
| 技術や手法のキモはどこ？ | LaCTを拡張した「LaCET (Large Chunk Elastic Test-Time Training)」ブロック。 Fisher情報行列を用いた正規化により、重要なパラメータをアンカー（初期状態）の近くに維持しつつ、新しいデータへの適応を許容する弾性的な更新メカニズム。 |
| どうやって有効だと検証した？ | Stereo4D、DL3DV、NVIDIAのベンチマークを用い、PSNR/SSIM/LPIPS等の指標で評価。特に長尺の動的なシーンにおいて、既存のレンダリングベースの手法や最適化ベースの手法よりも、高いレンダリング品質と適応安定性を示すことを実験的に確認した。 |
| 議論はある？ | 現在はポーズ付きの画像を入力として前提としており、未学習の未知シーンへの対応や、幾何学的な整合性の厳密な保証には課題が残る。また、レンダリングのみの監視では、一部で隣接フレームの補間に頼る傾向が見られる。 |
| 次に読むべき論文は？ | [LaCT (Zhang et al., 2026)](https://arxiv.org/abs/2602.21204), [4D-LRM (Ma et al., 2025)](https://arxiv.org/abs/2502.16982), [LVSM (Jin et al., 2025)](https://arxiv.org/abs/2501.10986) |
| PDFリンク | https://arxiv.org/pdf/2604.07350v1 |
