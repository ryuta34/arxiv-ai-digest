---
title: "ELF: Embedded Language Flows"
date: 2026-05-12
arxiv_id: 2605.10938v1
url: http://arxiv.org/abs/2605.10938v1
---

# ELF: Embedded Language Flows

| 項目 | 内容 |
|---|---|
| どんなもの？ | 言語生成のために、連続的な埋め込み空間上で学習する新しい拡散モデル「Embedded Language Flows (ELF)」を提案した。この手法は、生成プロセスの大半を連続的な埋め込み空間で行い、最終段階でのみ離散トークンへの変換（デコード）を行うことで、効率的かつ高性能な言語生成を実現する。 |
| 先行研究と比べてどこがすごい？ | 従来のDLM（拡散言語モデル）と比較して、推論に必要なサンプリングステップ数を1/10に削減し、学習データ量も1/10以下に抑えながら、より高い生成品質を達成した。また、追加の学習（蒸留）を必要とせずに、強力な生成性能と分類器なしガイダンス（CFG）の適用を可能にしている。 |
| 技術や手法のキモはどこ？ | 連続時間Flow Matchingを用いて、トークンを連続埋め込み空間にマッピングし、最終ステップまで連続空間でデノイジングを行う設計。デコーダーを別途用意せず、共有重みのネットワークでデノイジングと離散化（デコード）を完結させる minimalist な設計思想が特徴。 |
| どうやって有効だと検証した？ | OpenWebText (OWT) を用いた無条件生成、およびWMT14（翻訳）やXSum（要約）を用いた条件付き生成で評価。先行する離散型・連続型DLM（MDLM, Duo, FLM, LangFlow等）を上回る生成品質（PerplexityやBLEU/ROUGEスコア）を達成し、スケーリング則においても優位性を示した。 |
| 議論はある？ | 言語の持つ本質的な離散性と、連続的な拡散プロセスの間のインターフェースをいかに扱うかが焦点。現時点では最良の結果を示しているが、より大規模なモデルや長文生成における挙動、および言語特有の構造をより深く扱うためのアーキテクチャ改良の余地がある。 |
| 次に読むべき論文は？ | [1] [Flow Matching for generative modeling (Lipman et al., 2023)](https://arxiv.org/abs/2210.13472)<br>[2] [Back to basics: Let denoising generative models denoise (Li & He, 2025)](https://arxiv.org/abs/2511.13720)<br>[3] [Langflow: Continuous diffusion rivals discrete in language modeling (Chen et al., 2026)](https://arxiv.org/abs/2604.11748) |
| PDFリンク | https://arxiv.org/pdf/2605.10938v1 |
