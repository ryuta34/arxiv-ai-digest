---
title: "DreamFly: Causal Memory and Receding-Horizon Diffusion Planning for Aerial Vision-Language Navigation"
date: 2026-08-13
arxiv_id: 2608.12308v1
url: http://arxiv.org/abs/2608.12308v1
---

# DreamFly: Causal Memory and Receding-Horizon Diffusion Planning for Aerial Vision-Language Navigation

| 項目 | 内容 |
|---|---|
| どんなもの？ | 航空機（UAV）の視覚と言語によるナビゲーション（VLN）のための、拡散モデルベースのフレームワーク。履歴情報の統合、先読みによる計画、明示的な終了判定を統合し、自律的なナビゲーションを実現する。 |
| 先行研究と比べてどこがすごい？ | 過去の観測から「現在の判断に影響を与えない」因果的一貫性を保った履歴メモリ、Kステップ先読みと現在のフィードバックを両立する再帰的計画、およびアクション生成と分離された終了判定（LiteStop）を導入し、従来手法を凌駕する性能を達成した点。 |
| 技術や手法のキモはどこ？ | 1. 観察時刻に基づく因果的履歴メモリ（read-before-writeプロトコル）、2. 拡散モデルを用いた「計画K・実行1」の再帰的計画法、3. アクションログから終了確率を独立して推定するLiteStopモジュール。 |
| どうやって有効だと検証した？ | OpenFlyベンチマークを用い、Seen/Unseen環境でNE、SR、OSR、SPLを測定。各構成要素の有効性を検証するアブレーションスタディを実施し、定性分析でもその効果を実証した。 |
| 議論はある？ | 現在はシミュレーション環境での検証にとどまっており、実機へのデプロイにおけるセンサーノイズや環境変動、sim-to-realドメインシフトへの対応が今後の課題。 |
| 次に読むべき論文は？ | [33] J. Ye et al., "Dream-VL & Dream-VLA: Open Vision-Language and Vision-Language-Action Models with Diffusion Language Model Backbone" (https://arxiv.org/abs/2512.22615) |
| PDFリンク | https://arxiv.org/pdf/2608.12308v1 |
