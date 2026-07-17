---
title: "SciDiagramEdit: Learning to Edit Scientific Diagrams from Paper Revisions"
date: 2026-07-17
arxiv_id: 2607.15272v1
url: http://arxiv.org/abs/2607.15272v1
---

# SciDiagramEdit: Learning to Edit Scientific Diagrams from Paper Revisions

| 項目 | 内容 |
|---|---|
| どんなもの？ | 科学技術論文の図（科学的図解）の修正・編集を自動化する、スキル進化型フレームワーク「SciDiagramEdit」。arXivの論文リビジョンから抽出された図の修正前後のペアを教師データとし、指示に基づいたSVG形式での図の編集を実現する。 |
| 先行研究と比べてどこがすごい？ | 従来の生成系手法（単一パスのラスター画像生成）と異なり、SVGのベクター形式で図を直接編集するため、ユーザーが後から修正を加えられる。また、手作業のテンプレートに依存せず、修正の実行トレースから「スキル仕様」を自律的に進化させる手法を採用している。 |
| 技術や手法のキモはどこ？ | 「エージェント・エディタ」「判定者（Judge）」「コーチ（Coach）」のループ構造。コーチが編集失敗トレースと筆者の修正済み図（Ground Truth）を比較し、再利用可能なルール（スキル仕様）をパッチとして追加していく「スキル進化（Skill Evolution）」プロセスが核心。 |
| どうやって有効だと検証した？ | arXivのリビジョンから収集した364組の図編集データセット（SciDiagramEdit）を使用。セマンティックな忠実度（checklist success rate）と、UniPerceptを用いた美的品質（IAA/ISTA）および盲検ペア比較試験により、既存の画像編集モデルやベースライン手法と比較評価した。 |
| 議論はある？ | 現在は明示的な修正指示に依存しており、図の背後にある科学的議論の意図を汲み取る推論能力には限界がある。また、学習は現在閉じたAPIモデルに依存しており、より広範なデータセットによるスケーリングや完全自律的な最適化が将来の課題。 |
| 次に読むべき論文は？ | [AutoFigure-Edit](https://arxiv.org/abs/2603.06674)、[Trace2skill](https://arxiv.org/abs/2603.25158)、[Textgrad](https://arxiv.org/abs/2406.07496) |
| PDFリンク | https://arxiv.org/pdf/2607.15272v1 |
