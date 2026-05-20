---
title: "TIDE: Efficient and Lossless MoE Diffusion LLM Inference with I/O-aware Expert Offload"
date: 2026-05-20
arxiv_id: 2605.20179v1
url: http://arxiv.org/abs/2605.20179v1
---

# TIDE: Efficient and Lossless MoE Diffusion LLM Inference with I/O-aware Expert Offload

| 項目 | 内容 |
|---|---|
| どんなもの？ | 拡散モデルベースの大規模言語モデル（dLLM）におけるMixture-of-Experts（MoE）推論を効率化する、リソース制約環境向けのI/O認識型推論システム「TIDE」。モデルの重みを学習なしでロスレスにオフロードし、推論処理を高速化する。 |
| 先行研究と比べてどこがすごい？ | 拡散モデルの推論過程において、隣接するステップ間で専門家（Expert）の活性化パターンが極めて類似している点に着目。既存のAR（自己回帰）モデル向け手法が抱えていた過剰なCPU-GPU間のI/Oボトルネックを解消し、最大1.5倍のスループット向上を実現した。 |
| 技術や手法のキモはどこ？ | 推論過程を「リフレッシュステップ」と「スキップステップ」に分け、専門家の配置更新間隔（τ）を数学的な最適化問題として定式化して決定する点。さらに、CPU側での並列処理を非同期で行うことで、GPUの待ち時間を最小化している。 |
| どうやって有効だと検証した？ | LLaDA2.0-miniおよびLLaDA2.0-flashモデルを用い、NVIDIA A100/H100 GPUとCPUの構成で、MBPPデータセットに基づく推論スループットを測定。既存のFiddlerやMixtral-Offloadと比較して、一貫した高速化を確認した。 |
| 議論はある？ | 現在は単一GPU-CPUシステムに特化しており、複数GPUや分散環境への対応が今後の課題。また、分析はブロック内の活性化パターンに限定されており、より広範囲なブロック間相関の解析がさらなる性能向上の余地として残されている。 |
| 次に読むべき論文は？ | [LLaDA2.0: Scaling up diffusion language models to 100b](https://arxiv.org/abs/2512.15745), [Fiddler: Cpu-gpu orchestration for fast inference of mixture-of-experts models](https://arxiv.org/abs/2402.07033), [MoE-infinity: Activation-aware expert offloading for efficient moe serving](https://arxiv.org/abs/2401.14361) |
| PDFリンク | https://arxiv.org/pdf/2605.20179v1 |
