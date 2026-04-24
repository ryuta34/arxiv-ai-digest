---
title: "Seeing Without Eyes: 4D Human-Scene Understanding from Wearable IMUs"
date: 2026-04-24
arxiv_id: 2604.21926v1
url: http://arxiv.org/abs/2604.21926v1
---

# Seeing Without Eyes: 4D Human-Scene Understanding from Wearable IMUs

| 項目 | 内容 |
|---|---|
| どんなもの？ | ウェアラブルIMU（慣性計測ユニット）のみを用いて、カメラやLiDARなどの視覚情報に頼らずに4D人体モーションと3Dシーンレイアウトを推定するフレームワーク「IMU-to-4D」。LLM（大規模言語モデル）の推論能力を活用し、人体動作、テキスト説明、シーン構造を統合的に理解する。 |
| 先行研究と比べてどこがすごい？ | 従来のパイプライン手法（モジュールごとの逐次処理）が抱えていたエラー伝搬や一貫性の問題を解決し、統一的なマルチモーダル学習によってより空間的・時間的に安定した推論を実現した。プライバシーリスクの高いカメラを使用せず、軽量で常時稼働可能な環境理解を可能にした点。 |
| 技術や手法のキモはどこ？ | LLMを基盤モデルとして再利用し、IMU信号・人体モーション・シーンレイアウトを共通の埋め込み空間に投影して次トークン予測を行う点。特に、モーションを時系列で効率的に扱うための「1D VQ-VAEによるトークン化」と、シーンの曖昧性を解消するための「Joint Reasoning（共同推論）」アーキテクチャが核心。 |
| どうやって有効だと検証した？ | MotionMillion、LINGO、HUMOTO、ParaHomeなどの多様なデータセットで評価。ベースラインとなるパイプライン構成（MobilePoser+MotionGPT3+Summon等）と比較し、MPJPE等の精度指標および定性的なシーン再構成の質において、提案手法が優位であることを証明した。 |
| 議論はある？ | 入力データのスパース性や環境の曖昧さにより、特定の物体認識や詳細なシーン予測が困難なケースがある。また、物体同士の重なり（インターペネトレーション）を物理的に完全に防ぐ制約は明示的に導入されていない。今後はループクロージャー機構や、より強力な空間的先入観の導入が課題。 |
| 次に読むべき論文は？ | [93] Show-o: One single transformer to unify multimodal understanding and generation、[97] MobilePoser: Real-time full-body pose estimation and 3d human translation from imus in mobile consumer devices、[121] Motiongpt3: Human motion as a second modality |
| PDFリンク | https://arxiv.org/pdf/2604.21926v1 |
