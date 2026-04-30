---
title: "Turning the TIDE: Cross-Architecture Distillation for Diffusion Large Language Models"
date: 2026-04-30
arxiv_id: 2604.26951v1
url: http://arxiv.org/abs/2604.26951v1
---

# Turning the TIDE: Cross-Architecture Distillation for Diffusion Large Language Models

| 項目 | 内容 |
|---|---|
| どんなもの？ | 拡散ベースの大規模言語モデル（dLLM）における、アーキテクチャやトークナイザーが異なるモデル間での知識蒸留を可能にする初のフレームワーク「TIDE」を提案する論文。従来は困難だった異種アーキテクチャ間の知識転移を実現し、小規模モデルの推論高速化と性能向上を両立させる。 |
| 先行研究と比べてどこがすごい？ | 従来の手法は同一アーキテクチャ内でのステップ圧縮に限定されていたが、TIDEは異種アーキテクチャ・トークナイザー間の知識転移を可能にした点。HumanEvalでベースライン比+16.5ポイント、推論速度5倍、メモリ使用量22倍削減という顕著な成果を達成した点。 |
| 技術や手法のキモはどこ？ | ①拡散過程と訓練段階の両軸で蒸留強度を調整するTIDAL、②マスク分割により教師モデルの推論を強化するCOMPDEMO、③異なるトークナイザー間での確率分布整合を可能にする逆方向のKL近似指標「Reverse CALM」の3要素による統合的パイプライン。 |
| どうやって有効だと検証した？ | 16B/8Bの教師モデルから0.6BのBD3LM学生モデルへの蒸留を行い、推論・コード生成・数学など8つのベンチマークで評価。非蒸留ベースラインを平均スコアで上回ることを確認し、さらに推論効率（スループット・メモリ消費）の観点からも実用性を検証した。 |
| 議論はある？ | 現在は0.6Bモデルでの検証にとどまる点や、現状の構成ではReverse CALMとTIDALの併用が最適化の競合を引き起こす点。将来課題として、より大規模な学生モデルへの適用や、連続値拡散モデルへの拡張、多教師蒸留の検討が挙げられている。 |
| 次に読むべき論文は？ | [BD3LM (Arriola et al., 2025)](https://arxiv.org/abs/2503.09573), [LLaDA 2.0 (Bie et al., 2025)](https://arxiv.org/abs/2512.15745), [WeDLM (Liu et al., 2025)](https://arxiv.org/abs/2512.22737) |
| PDFリンク | https://arxiv.org/pdf/2604.26951v1 |
