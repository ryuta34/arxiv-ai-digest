---
title: "Cross-sector generalization of accident-process role classification in occupational accident narratives"
date: 2026-09-21
arxiv_id: 2609.22081v1
url: http://arxiv.org/abs/2609.22081v1
---

# Cross-sector generalization of accident-process role classification in occupational accident narratives

| 項目 | 内容 |
|---|---|
| どんなもの？ | 労働災害報告書を「作業状況」「不利な条件」「事故イベント」「結果」の4つの機能的役割に分類する手法。モデルを建設業界のデータで学習させ、他業種や異なる組織環境のデータへ転移させることで、網羅的なリスク分析を支援する。 |
| 先行研究と比べてどこがすごい？ | 従来手法が報告書全体を単一のラベルで分類していたのに対し、本手法は報告書内の文章を最小構成単位（factual unit）に分割し、それぞれの機能的役割を個別に識別する。また、特定業界で学習したモデルの他業界へのクロスドメイン汎用性を体系的に検証している。 |
| 技術や手法のキモはどこ？ | Qwen3-Embedding-0.6Bを用いた事前学習済みモデルをベースとし、クロスエントロピー損失による微調整だけでなく、バッチハードトリプレット、教師あり対照学習（SupCon）、SoftTripleといった表現学習を適用し、特徴空間の分離を強化した点。 |
| どうやって有効だと検証した？ | 建設業界のデータでモデルを構築し、 metallurgy（冶金）、chemistry-plastics（化学・プラスチック）、および独立した企業のデータセットという計3つの未知のドメインに対し、再学習なしで評価を行い、平均均衡精度（balanced accuracy）で比較検証した。 |
| 議論はある？ | モデルは明示的に記述された事実の構造化を目的としており、隠れた因果関係や予防策の推論は行わない。また、異なる環境間での性能差は依然として存在しており、運用時には専門家による確認が不可欠であるとしている。 |
| 次に読むべき論文は？ | [Goldberg (2022) - "Characterizing accident narratives with word embeddings"](https://doi.org/10.1016/j.jsr.2021.12.024)や[Khosla et al. (2020) - "Supervised contrastive learning"](https://proceedings.neurips.cc/paper/2020/hash/d89a66c7c80a29b1bdbab0f2a1a94af8-Abstract.html)など、表現学習および安全管理へのNLP応用に関する文献。 |
| PDFリンク | https://arxiv.org/pdf/2609.22081v1 |
