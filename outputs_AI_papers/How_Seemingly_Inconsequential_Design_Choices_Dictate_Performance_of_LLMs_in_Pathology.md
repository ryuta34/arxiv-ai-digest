---
title: "How Seemingly Inconsequential Design Choices Dictate Performance of LLMs in Pathology"
date: 2026-06-11
arxiv_id: 2606.12407v1
url: http://arxiv.org/abs/2606.12407v1
---

# How Seemingly Inconsequential Design Choices Dictate Performance of LLMs in Pathology

| 項目 | 内容 |
|---|---|
| どんなもの？ | 病理画像診断における汎用LLM（大規模言語モデル）の評価において、パッチサイズや倍率などの入力構成が性能に決定的な影響を与えることを明らかにした論文。従来の標準的な評価プロトコルが非効率であることを示し、最適な入力設定により性能が大幅に向上することを示した。 |
| 先行研究と比べてどこがすごい？ | 従来研究で「専用モデルが汎用LLMより優れている」とされていた性能差の多くが、実は単なる「非最適化な入力設計」に起因していたことを証明した。特に「All-in-One」推論と適切な入力設定により、追加学習なしで従来比最大+33.5ppの大幅な精度向上を達成した。 |
| 技術や手法のキモはどこ？ | 推論モード（独立したパッチによる多数決投票 vs. 全パッチを一括入力する「All-in-One」）、パッチサイズ、倍率、パッチ数を変数とした完全要因計画法による体系的な分析。特に、推論モードを後者に変更するだけで、計算コストを下げつつコンテキストの統合的な理解が可能になった点。 |
| どうやって有効だと検証した？ | MultiPathQAベンチマークを用いた72通りの構成による実験。さらに、GPT-5だけでなくQwen 3.5 PlusやGemini 3 Flashを用いた検証や、未学習のCPTACデータセットを用いた外部検証を行い、提案手法の汎用性と妥当性を確認した。 |
| 議論はある？ | 入力構成の最適化は重要だが、タスク依存性が強いことや、Proprietary（プロプライエタリ）なAPIモデルに依存しているためモデルの更新による影響を受ける可能性がある点。また、より広範なデータセットでの検証が将来課題として残されている。 |
| 次に読むべき論文は？ | [2] Navigating gigapixel pathology images with large multimodal models (Buckley et al., 2025) や [8] SlideChat: A large vision-language assistant for whole-slide pathology image understanding (Chen et al., 2025) |
| PDFリンク | https://arxiv.org/pdf/2606.12407v1 |
