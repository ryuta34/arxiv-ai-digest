---
title: "One Figure, Every Canvas: Editable Flowchart Relayout via Agentic Pipeline"
date: 2026-10-07
arxiv_id: 2610.06852v1
url: http://arxiv.org/abs/2610.06852v1
---

# One Figure, Every Canvas: Editable Flowchart Relayout via Agentic Pipeline

| 項目 | 内容 |
|---|---|
| どんなもの？ | 既存のフローチャート画像を、構造や接続関係を維持したまま、任意の縦横比のキャンバスへ再配置するエージェント型パイプライン。最終的な出力はdraw.ioで編集可能なXML形式である。 |
| 先行研究と比べてどこがすごい？ | 既存の画像生成系（I2I）が引き起こす歪みや、テキスト指示系（T2I）による情報の欠落・幻覚、解析・再描画系（Parse-then-render）の接続ミスを解消し、構造的忠実度と編集可能性を両立した点。 |
| 技術や手法のキモはどこ？ | タスクを「Parse（解析）」「Style（スタイル転写）」「Layout（再配置）」の3段階に分解し、各段階にVLMと決定論的検証器（Critic）をペアで配置して、接続の断絶やオーバーラップを反復的に修正する手法。 |
| どうやって有効だと検証した？ | 100件の学術論文由来フローチャートを用いた独自ベンチマーク「FLOWCHARTRELAYOUTBENCH」を構築し、VLM-as-a-Judgeプロトコルと人間による評価で、コンテンツ忠実度などを既存手法と比較検証した。 |
| 議論はある？ | 編集可能性を優先するためピクセル単位の完全一致は放棄されており、スタイル再現に若干のギャップがある。また、VLMの推論コストが高く、複雑な構造では不自然なルーティングが発生する可能性がある。 |
| 次に読むべき論文は？ | [LayoutLMv3 (Huang et al., 2022)](https://arxiv.org/abs/2204.04187)、[Diagram2Structure (Hu et al., 2026)](https://arxiv.org/abs/2606.23527)、[Reflexion (Shinn et al., 2023)](https://arxiv.org/abs/2303.11366) |
| PDFリンク | https://arxiv.org/pdf/2610.06852v1 |
