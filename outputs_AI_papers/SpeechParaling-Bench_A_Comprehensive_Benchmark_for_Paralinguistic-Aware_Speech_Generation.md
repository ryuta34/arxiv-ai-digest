---
title: "SpeechParaling-Bench: A Comprehensive Benchmark for Paralinguistic-Aware Speech Generation"
date: 2026-04-23
arxiv_id: 2604.20842v1
url: http://arxiv.org/abs/2604.20842v1
---

# SpeechParaling-Bench: A Comprehensive Benchmark for Paralinguistic-Aware Speech Generation

| 項目 | 内容 |
|---|---|
| どんなもの？ | 大規模オーディオ言語モデル（LALM）の副言語（感情、トーン、スタイル等）を考慮した音声生成能力を評価する、包括的なベンチマーク「SpeechParaling-Bench」を提案した研究。100以上の細分化された特徴量と1,000以上の英中バイリンガルクエリを備え、静的制御から文脈適応まで段階的なタスクを網羅している。 |
| 先行研究と比べてどこがすごい？ | 既存のベンチマークが50以下の特徴量しかカバーしていないのに対し、100以上のきめ細やかな副言語特徴を網羅した点。また、人間による評価に頼らず、LALMを判定者として用いる「ペアワイズ比較パイプライン」を導入し、主観性を抑えた安価でスケーラブルな自動評価を実現した点。 |
| 技術や手法のキモはどこ？ | Gemini 2.5 Flashを用いた高品質な命令とデータセットの合成、およびLLM判定者によるペアワイズ比較手法。絶対評価ではなく相対評価を採用し、評価の安定性を高める重み付けスコアリングメカニズムを導入したこと。 |
| どうやって有効だと検証した？ | 複数の主要なLALM（Doubao, GPT Audio, Gemini Audio, Qwen3-Omniシリーズ等）を対象に、提案ベンチマークを用いた広範な実験を実施。人間による評価との高い相関（Spearman相関0.90〜1.00）を確認し、モデルの弱点を特定した。 |
| 議論はある？ | 現在のLALMは副言語の制御や動的な変調に課題があり、特にSituational Adaptationにおける誤りの43.3%が副言語的合図の解釈ミスに起因することが明らかになった。モデルの「音声アシスタント」としてのアイデンティティが逆に多様な感情表現を制限している可能性が示唆された。 |
| 次に読むべき論文は？ | [18] EmergentTTS-Eval: Evaluating TTS Models on Complex Prosodic, Expressiveness, and Linguistic Challenges Using Model-as-a-Judge, [15] S2S-Arena, Evaluating Speech2Speech Protocols on Instruction Following with Paralinguistic Information, [34] ParaS2S: Benchmarking and Aligning Spoken Language Models for Paralinguistic-aware Speech-to-Speech Interaction |
| PDFリンク | https://arxiv.org/pdf/2604.20842v1 |
