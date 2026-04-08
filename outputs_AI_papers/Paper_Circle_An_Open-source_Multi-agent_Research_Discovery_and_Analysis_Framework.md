---
title: "Paper Circle: An Open-source Multi-agent Research Discovery and Analysis Framework"
date: 2026-04-08
arxiv_id: 2604.06170v1
url: http://arxiv.org/abs/2604.06170v1
---

# Paper Circle: An Open-source Multi-agent Research Discovery and Analysis Framework

| 項目 | 内容 |
|---|---|
| どんなもの？ | 学術文献の発見から分析、批判的検討、合成までをサポートする、マルチエージェント型の総合研究プラットフォーム「Paper Circle」。研究者の負荷を軽減し、AIによる補助のもとで人間とAIの共同作業を促進するワークベンチを提供する。 |
| 先行研究と比べてどこがすごい？ | 完全に自動化されたシステムとは異なり、決定論的な検索と構造化されたデータ出力を重視し、研究者の意思決定を支援する「force multiplier（戦力倍増）」として機能する点。さらに、論文を知識グラフ化し、グラフ構造を活用した質問応答や検証機能を備えている。 |
| 技術や手法のキモはどこ？ | 検索・分析・抽出を行う各エージェントが、共有された状態（Shared State）に基づいて同期的に動作する点と、PDFから概念・手法・実験・図表を抽出し「MindGraph」として知識グラフを構築するパイプライン。また、多様性を考慮したランキングアルゴリズムや、人間による検証プロセスを組み込んでいる。 |
| どうやって有効だと検証した？ | 50のクエリからなるベンチマークと、実際の研究者による81の探索セッションを通じて評価。MRRやRecall@Kなどの指標を用いた定量的比較と、NASA-TLXによる認知的負荷およびユーザビリティ調査を実施。 |
| 議論はある？ | 査読生成エージェントと人間による評価の相関が低い（r < 0.25）ことが指摘されており、複雑な学術的判断についてはさらなる改善が必要。完全な自動化ではなく、あくまで研究者の補助ツールとしての立ち位置を強調している。 |
| 次に読むべき論文は？ | [PaperQA (Lála et al., 2023)](https://arxiv.org/abs/2312.07559), [STORM (Shao et al., 2024)](https://arxiv.org/abs/2405.02809), [DORA AI agent (Naumov et al., 2025)](https://www.biorxiv.org/content/10.1101/2025.01.27.635035v1) |
| PDFリンク | https://arxiv.org/pdf/2604.06170v1 |
