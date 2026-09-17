---
title: "A Zeroth-Order Paradigm for LLM Preference Alignment"
date: 2026-09-17
arxiv_id: 2609.19144v1
url: http://arxiv.org/abs/2609.19144v1
---

# A Zeroth-Order Paradigm for LLM Preference Alignment

| 項目 | 内容 |
|---|---|
| どんなもの？ | LLMの嗜好調整における「尤度逸脱（likelihood displacement）」問題に対処するための、比較オラクルに基づく新たなゼロ次最適化手法「ComPO」を提案した論文。低マージン（あいまい）な嗜好データを直接的な損失関数として利用するのではなく、比較シグナルとして活用することで、モデルの調整を安定化させる。 |
| 先行研究と比べてどこがすごい？ | 従来のDPOのような直接的な嗜好学習手法が抱えていた、尤度逸脱による安全性や質の低下という課題を、 noisy（低マージン）なペアを捨てることなく活用することで緩和した点。また、比較オラクルを用いることで、勾配計算を伴わずに頑健な最適化を実現している。 |
| 技術や手法のキモはどこ？ | モデルをパラメータ空間で摂動させ、好ましい応答の尤度を上げ、好ましくない応答の尤度を下げるような摂動を評価することで「1ビットの比較シグナル」を得る点。これを積み上げることで勾配を推定し、オンライン学習では生成データを用いた逆KL制約でステップサイズを制御する点。 |
| どうやって有効だと検証した？ | Mistral, Llama, Gemma, Qwenなどの様々なモデルファミリーに対し、AlpacaEval 2、Arena-Hard、MT-Benchを用いて評価。DPOやSimPOの既存チェックポイントに対してComPOを追加適用することで、主要なベンチマークで一貫して性能が向上することを示した。 |
| 議論はある？ | Arena-Hardのようなraw win rate重視の評価指標では、ComPOが意図せず生成を短くすることでスコアに影響する場合がある点。また、理論的な収束保証は単純化された基本スキームに対してのみであり、実用上のオンライン学習スキームはヒューリスティックな近似を含む点。 |
| 次に読むべき論文は？ | [Direct Preference Optimization (Rafailov et al., 2023)](https://arxiv.org/abs/2305.18290)、[Unintentional unalignment (Razin et al., 2025)](https://openreview.net/forum?id=uaMSBJDnRv)、[The importance of online data (Song et al., 2024b)](https://arxiv.org/abs/2402.04792) |
| PDFリンク | https://arxiv.org/pdf/2609.19144v1 |
