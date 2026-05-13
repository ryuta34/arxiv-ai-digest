---
title: "Covering Human Action Space for Computer Use: Data Synthesis and Benchmark"
date: 2026-05-13
arxiv_id: 2605.12501v1
url: http://arxiv.org/abs/2605.12501v1
---

# Covering Human Action Space for Computer Use: Data Synthesis and Benchmark

| 項目 | 内容 |
|---|---|
| どんなもの？ | コンピュータ操作エージェント（CUA）が複雑なGUIインタラクションを正確に実行するためのベンチマーク「CUActSpot」と、それに対応する学習用データ合成パイプライン。従来のクリック中心の評価から脱却し、ドラッグ、ドロー、範囲選択などを含む広範なアクション空間をカバーしている。 |
| 先行研究と比べてどこがすごい？ | 従来手法がGUIウィジェットへのクリック操作に限定されていたのに対し、GUI、テキスト、表、キャンバス、自然画像の5つのモダリティにまたがる複雑な操作を網羅している。また、データ合成パイプラインを通じて生成した5000万サンプルの活用により、パラメータ数32B未満のモデルとして最高性能（Phi-Ground-Any-4B）を実現した点。 |
| 技術や手法のキモはどこ？ | コードベースのレンダリングにより、正確な座標情報を含むスクリーンショットと操作のペアを自動生成する点。また、単なるデータ量（scaling）よりもタスクとモダリティの多様性を重視する「variety scaling」という概念を導入し、多様なタスクを通じた compositional generalization を促進している。 |
| どうやって有効だと検証した？ | 206の多様かつ複雑なタスクからなる「CUActSpot」ベンチマークで性能を評価し、ScreenSpot-ProやUI-Visionといった既存ベンチマークとの性能ギャップを分析した。また、OSWorldを用いたエージェント評価を通じて、実環境における本手法の優位性を実証した。 |
| 議論はある？ | 現在のベンチマークは手動構築された診断用であり、長期間のタスクや状態変化を伴う実世界のワークフローを網羅できていない。また、合成データと実データ分布の整合性をさらに向上させることが今後の重要な課題である。 |
| 次に読むべき論文は？ | [10] Navigating the digital world as humans do (arXiv:2410.05243) や [17] Osworld: Benchmarking multimodal agents (NeurIPS 2024) が関連性の高い主要な研究として挙げられる。 |
| PDFリンク | https://arxiv.org/pdf/2605.12501v1 |
