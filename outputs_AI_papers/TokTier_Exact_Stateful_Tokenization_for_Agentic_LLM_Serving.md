---
title: "TokTier: Exact Stateful Tokenization for Agentic LLM Serving"
date: 2026-08-03
arxiv_id: 2607.29678v1
url: http://arxiv.org/abs/2607.29678v1
---

# TokTier: Exact Stateful Tokenization for Agentic LLM Serving

| 項目 | 内容 |
|---|---|
| どんなもの？ | エージェント型LLMサーバーにおいて、繰り返される長いコンテキストのトークン化コストを削減するステートフルなトークン化サービス「TokTier」。トークン化結果をキャッシュし、小さな変更点のみを増分修復することで、全体を再トークン化するコストを排除し、モデル入力として正確なトークンIDを維持する。 |
| 先行研究と比べてどこがすごい？ | 従来はリクエストごとにフルコンテキストを再スキャンしていたが、TokTierはセッション状態を保持して増分修復を行うことで、大規模なトークン化処理のレイテンシを大幅に削減。また、GPUによる高速なフルトークン化パスを備え、既存のトークン化器とバイト単位で完全に一致する正確性を保証している点。 |
| 技術や手法のキモはどこ？ | トークン化結果の「安定境界（stable boundary）」を特定し、変更点周辺の増分修復を安全に行うSplice定理の実装。また、GPTファミリーのトークン化を並列実行可能な「ラン分解（run decomposition）」へと変換し、GPU上で高速かつ正確に実行する手法。 |
| どうやって有効だと検証した？ | 17のトークン化器ファミリー、12.4TBの実データコーパス、93,000回以上のエージェントステップ、および実環境の負荷試験を用いた検証。vLLMと統合し、TTFT（Time to First Token）の16〜34%削減と、CPUフロントエンド比較で45倍以上のリクエスト処理能力を実現した。 |
| 議論はある？ | GPUトークン化器がバイトスパンを出力できないため、初期化時にCPUパスへの依存が発生する点や、一部の特殊な正規化を行うトークン化器がGPUパスの最適化対象外となること。また、極端に長い追記（>50K文字）の処理にはさらなるルーティング最適化の余地がある。 |
| 次に読むべき論文は？ | [11] Efficient Memory Management for Large Language Model Serving with PagedAttention (OSDI '23), [22] Gigatoken: SIMD and Cache Hierarchies for 1000x Faster Byte-Pair Encoding Tokenization (2026), [23] LoPT: Lossless Parallel Tokenization Acceleration for Long Context Inference (ACL '26) |
| PDFリンク | https://arxiv.org/pdf/2607.29678v1 |
