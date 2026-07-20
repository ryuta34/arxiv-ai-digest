---
title: "Searching Videos as Trees: Self-Correcting Agents for Grounded Long Video QA"
date: 2026-07-20
arxiv_id: 2607.16189v1
url: http://arxiv.org/abs/2607.16189v1
---

# Searching Videos as Trees: Self-Correcting Agents for Grounded Long Video QA

| 項目 | 内容 |
|---|---|
| どんなもの？ | 長時間の動画を階層的な木構造に変換し、エージェントが「zoom_in（詳細化）」「zoom_out（遡行）」「shift（横移動）」という離散的な操作を行うことで、効率的に証拠区間を特定し質問に答えるフレームワーク「VideoTreeSearch (VTS)」。 |
| 先行研究と比べてどこがすごい？ | 従来の連続的なクロップ手法では一度間違えると復帰不能だったが、本作は明示的な遡行（backtracking）や修正を可能にし、長時間の動画に対する探索性能とQA精度を大幅に向上させた。 |
| 技術や手法のキモはどこ？ | 動画を視覚的な変化点に基づいてセマンティックな木構造として構築する点と、誤った探索からの復帰を含む訓練用軌跡を生成し、強化学習によって「自律的に軌道修正する探索政策」を学習させた点。 |
| どうやって有効だと検証した？ | CG-Bench、Haystack-LVBench、Haystack-Ego4Dなどのグラウンディングを伴うLVQAベンチマークで従来手法を圧倒し、さらに一般のビデオQAタスクでも精度向上を確認した。 |
| 議論はある？ | 現在は単一の区間を回答する仕様であり、証拠が複数の時間領域にまたがる質問には未対応。また、CLIPを用いたシーン境界検出が視覚的に均質な動画では不安定になる可能性がある。 |
| 次に読むべき論文は？ | [31] Ziyang Wang et al., "VideoTree: Adaptive tree-based video representation for LLM reasoning on long videos" (CVPR 2025) |
| PDFリンク | https://arxiv.org/pdf/2607.16189v1 |
