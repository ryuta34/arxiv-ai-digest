---
title: "DnA: Denoising Attention for Visual Tasks"
date: 2026-06-26
arxiv_id: 2606.27372v1
url: http://arxiv.org/abs/2606.27372v1
---

# DnA: Denoising Attention for Visual Tasks

| 項目 | 内容 |
|---|---|
| どんなもの？ | 視覚タスクにおけるAttention機構の改善手法「DnA（Denoising Attention）」を提案した論文。従来のSoftmaxが抱える正負の相互作用の非対称性という課題に対し、正負それぞれのクエリと値のペアを用いたサブスペースへの射影により、ノイズを抑制する。 |
| 先行研究と比べてどこがすごい？ | 従来のDifferential Attentionが単一のサブスペースでノイズを除去しようとして有用な信号まで打ち消す可能性があるのに対し、DnAは2つの直交に近いサブスペースを分離して設計することで、より効果的に識別的な特徴を抽出できる点。 |
| 技術や手法のキモはどこ？ | 正の相互作用にはSoftmax、負の相互作用（ノイズ）にはSoftminを使い分け、それぞれを別々の値サブスペース（$V^+, V^-$）に射影してモデル化する点。これにより、モデルが有用なクラス特徴と無関係な競合特徴を明確に分離・抑制できる。 |
| どうやって有効だと検証した？ | ImageNet-1K画像分類においてViT-Bベースで0.8%の精度向上を達成したほか、Toyota SmarthomeやNTU RGB+D 60を用いたビデオ理解タスク、およびVideoLLaMA3を用いたエゴセントリック動画の質問応答タスクなどで性能向上を実証した。 |
| 議論はある？ | DnAの導入により、ビデオTransformersで約23%、Video LLMで約3%のパラメータ増加が伴う。また、現時点では学習コストの増加も避けられないが、追加パラメータは並列化可能なヘッド内に収まるためスループットは維持される。 |
| 次に読むべき論文は？ | Ye et al. "Differential Transformer" (ICLR 2025) [80], Dosovitskiy et al. "An Image is Worth 16x16 Words" (ICLR 2021) [20] |
| PDFリンク | https://arxiv.org/pdf/2606.27372v1 |
