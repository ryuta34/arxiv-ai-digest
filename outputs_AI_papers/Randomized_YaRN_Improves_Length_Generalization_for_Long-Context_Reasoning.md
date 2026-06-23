---
title: "Randomized YaRN Improves Length Generalization for Long-Context Reasoning"
date: 2026-06-23
arxiv_id: 2606.23687v1
url: http://arxiv.org/abs/2606.23687v1
---

# Randomized YaRN Improves Length Generalization for Long-Context Reasoning

| 項目 | 内容 |
|---|---|
| どんなもの？ | 大規模言語モデル（LLM）において、短文の学習データのみを用いて長文コンテキストへの外挿性能（長さの汎化性能）を高める手法「Randomized YaRN」を提案した論文。YaRNをベースとしつつ、位置エンコーディングのランダムサンプリングと長さのカリキュラム学習を導入することで、学習時より遥かに長い文脈の推論タスクでの性能を改善した。 |
| 先行研究と比べてどこがすごい？ | 従来の長文拡張手法（RoPEの補間など）では、学習データ外の極端に長い文脈での推論性能が低下しやすいという課題があった。本手法は、モデルを学習段階から「訓練時よりも長い範囲」の分布に疑似的に晒すことで、未知の長い文脈でも安定した推論を可能にし、特に128Kといった遠い外挿範囲で既存手法を上回る性能を示した。 |
| 技術や手法のキモはどこ？ | 1. **ランダム位置サンプリング**: 短文学習データに対し、YaRNのエンコーディングを本来の範囲より長い分布からランダムに割り当てることで、OOD（分布外）の位置表現を経験させる。<br>2. **長さカリキュラム学習**: 学習エポックが進むにつれ、位置情報のサンプリング範囲を徐々に拡大し、徐々に長い文脈への適応を促す学習スケジュールを採用した点。 |
| どうやって有効だと検証した？ | 「BABILong」および「Multi-Round Coreference Resolution (MRCR)」という2つの長文推論ベンチマークを用い、Qwen2.5-7B-InstructおよびOlmo3-7B-Instructをベースに評価。16Kから128Kという非常に長いコンテキスト長において、従来のLoRA fine-tuningやRPE（Randomized Positional Encoding）ベースラインよりも一貫して高い精度を達成した。 |
| 議論はある？ | 実験が英語データに限定されている点や、7Bスケールのモデルでのみ検証されている点が挙げられる。また、推論時に学習時よりも大きなスケーリング係数（s' > s）を用いることで、さらなる汎化が可能であるという特性も報告されている。 |
| 次に読むべき論文は？ | [YaRN: Efficient Context Window Extension of Large Language Models](https://arxiv.org/abs/2309.00071)（ベースとなったYaRNの研究）、[Randomized Positional Encodings Boost Length Generalization of Transformers](https://arxiv.org/abs/2305.16853)（RPEの元論文） |
| PDFリンク | [https://arxiv.org/pdf/2606.23687v1](https://arxiv.org/pdf/2606.23687v1) |
