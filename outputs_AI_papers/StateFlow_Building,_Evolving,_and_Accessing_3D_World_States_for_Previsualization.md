---
title: "StateFlow: Building, Evolving, and Accessing 3D World States for Previsualization"
date: 2026-08-13
arxiv_id: 2608.12314v1
url: http://arxiv.org/abs/2608.12314v1
---

# StateFlow: Building, Evolving, and Accessing 3D World States for Previsualization

| 項目 | 内容 |
|---|---|
| どんなもの？ | 生成AIによるプレビジュアライゼーション（事前可視化）のための、状態中心型フレームワーク「StateFlow」。ユーザーの意図に基づいて編集・進化可能な3D世界状態を構築し、それを利用したシネマティックなビデオ作成やゲームのプロトタイピングを実現する。 |
| 先行研究と比べてどこがすごい？ | 従来の動画生成モデルが「一発撮り（One-shot）」で編集困難かつ時空間的な整合性が低い課題を抱えるのに対し、本手法は明示的な3D世界状態を保持するため、一貫性を保ったままのシーン編集やカメラ操作、再利用が可能。 |
| 技術や手法のキモはどこ？ | ①Prior-Guided Conflict-Aware Dual-View Initialization（前方視点とBEVの統合による初期化）、②Intent-Guided Structured State Transition（意図に基づいた世界状態の更新）、③Render-Feedback Reflection（レンダリング結果に基づくフィードバックを用いたカメラ軌道の最適化）。 |
| どうやって有効だと検証した？ | VBenchを用いた既存のビデオ生成手法との定量比較、および30名の被験者によるユーザー調査とMLLMによる評価を実施。さらに、コンポーネントごとのアブレーションスタディを通じて、提案する3つの段階が品質と一貫性に貢献することを実証。 |
| 議論はある？ | 現在はサードパーティモデルの推論速度に依存しており、完全なリアルタイムインタラクションには未対応。今後はより効率的な推論と展開により、リアルタイム性を高めることが課題。 |
| 次に読むべき論文は？ | [1] Dui Ardal et al., "A collaborative previsualization tool for filmmaking in virtual reality." (2019)<br>[33] Team Seedance et al., "Seedance 2.0: Advancing video generation for world complexity." (2026)<br>[46] Weijia Wu et al., "Automated movie generation via multi-agent cot planning." (2025) |
| PDFリンク | https://arxiv.org/pdf/2608.12314v1 |
