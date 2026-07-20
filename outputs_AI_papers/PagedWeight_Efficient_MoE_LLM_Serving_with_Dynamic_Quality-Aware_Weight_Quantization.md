---
title: "PagedWeight: Efficient MoE LLM Serving with Dynamic Quality-Aware Weight Quantization"
date: 2026-07-20
arxiv_id: 2607.16184v1
url: http://arxiv.org/abs/2607.16184v1
---

# PagedWeight: Efficient MoE LLM Serving with Dynamic Quality-Aware Weight Quantization

| 項目 | 内容 |
|---|---|
| どんなもの？ | Mixture-of-Experts (MoE) モデルの推論時における、動的で品質を考慮した重みの量子化手法「PagedWeight」の提案。KVキャッシュの増大によるGPUメモリ不足に対し、重要度の低いエキスパートの重みを動的にオフロード/量子化することで、メモリを効率的に再利用し、精度の低下を抑えつつスループットを向上させる。 |
| 先行研究と比べてどこがすごい？ | 静的な量子化と異なり、実行時のKVキャッシュ圧力に応じて柔軟に重みのビット幅を調整できる。既存のAny-Precision LLM (APL) を拡張し、エキスパート単位の細粒度な精度制御と非同期なメモリ管理を実現することで、同等のメモリ予算で従来手法を最大39.3%上回る品質を達成し、最大1.94倍のスループット改善を実現した。 |
| 技術や手法のキモはどこ？ | エキスパートの重みをページ単位で管理し、オフラインの感度解析、オンラインのルーティング統計、プロンプトごとの残留誤差（Prompt Residual）を組み合わせて量子化の悪影響を予測する「品質を考慮したランタイムプランナー」にある。また、非同期なページ移動により、推論を中断させることなくGPUメモリの確保を行う点も特徴。 |
| どうやって有効だと検証した？ | Qwen1.5-MoE-A2.7B、Mixtral-8x7B、Gemma-4-26B-A4Bの3モデルを使用し、Wikitext2、C4、GSM8K、MATH-500等のベンチマークで性能を評価。さらに、長文コンテキスト推論でのメモリ効率とスループットを検証し、従来手法（APL、DP-LLM、MxMoE）との比較を行った。 |
| 議論はある？ | 現在は特定の量子化フォーマット（Any-Precision LLM形式）と感度指標に基づいている。将来の課題として、他フォーマットへの対応や、KVキャッシュ圧力下でのプロンプトごとの感度推定アルゴリズムのさらなる改善が挙げられている。 |
| 次に読むべき論文は？ | [1] [Dynamic expert quantization for scalable mixture-of-experts inference (arXiv:2511.15015)](https://arxiv.org/abs/2511.15015)、[16] [DP-LLM: Runtime model adaptation with dynamic layer-wise precision assignment (arXiv:2508.06041)](https://arxiv.org/abs/2508.06041)、[24] [Any-precision LLM: Low-cost deployment of multiple, different-sized LLMs](https://proceedings.mlr.press/v235/park24e.html) |
| PDFリンク | [https://arxiv.org/pdf/2607.16184v1](https://arxiv.org/pdf/2607.16184v1) |
