---
title: "Retriever-Free Retrieval: Navigating Documents with Decision Models"
date: 2026-10-28
arxiv_id: 2610.35868v1
url: http://arxiv.org/abs/2610.35868v1
---

# Retriever-Free Retrieval: Navigating Documents with Decision Models

| 項目 | 内容 |
|---|---|
| どんなもの？ | 従来の検索ベースのRAGではなく、文書構造を階層的に探索（ナビゲーション）する新しい手法「DecisionRAG」を提案。LLMを決定モデルとして活用し、トークン生成なしの推論で関連文書を絞り込むことで、高速かつ高精度な検索を実現した。 |
| 先行研究と比べてどこがすごい？ | 検索エンジン不要で、大規模コーパスに対しても階層探索により対数時間で検索が可能。従来のランキング手法に比べ、LLMの推論能力を直接活用することで、MultiDoc2DialやNatural Questionsなどのベンチマークで大幅な精度向上を達成している。 |
| 技術や手法のキモはどこ？ | コーパスを木構造として扱い、各ノードの候補を「共有コンテキスト」内で一括評価（並列バイナリ判定）する点。また、トークン生成を行わず、確率分布のみを算出することで、生成ベースの推論より34〜145倍高速に処理できる点。 |
| どうやって有効だと検証した？ | 4つのデータセット（MultiDoc2Dial, ConditionalQA, MTRAG, Natural Questions）で評価。従来の高精度なDense Retrieval + Rerankerの手法と比較し、R@1やHit@1で有意な上回る精度を確認し、かつ応答速度とコストの大幅な削減を実証した。 |
| 議論はある？ | 文書構造の質に検索精度が依存するため、適切に整理されていない文書では性能が低下する可能性がある。また、階層探索における「剪定」が不可逆的であるため、上位レベルで関連情報を逃すとリカバリーできない限界がある。 |
| 次に読むべき論文は？ | [LATTICE: Gupta et al., 2026](https://arxiv.org/abs/2606.03247)、[RAPTOR: Sarthi et al., 2024](https://arxiv.org/abs/2401.18059)、[MemWalker: Chen et al., 2023](https://arxiv.org/abs/2310.05029) |
| PDFリンク | https://arxiv.org/pdf/2610.35868v1 |
