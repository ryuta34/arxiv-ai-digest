---
title: "Beyond Naturalness: Probing Automated Text-To-Speech Evaluators on Linguistically Grounded Dimensions"
date: 2026-08-11
arxiv_id: 2608.09930v1
url: http://arxiv.org/abs/2608.09930v1
---

# Beyond Naturalness: Probing Automated Text-To-Speech Evaluators on Linguistically Grounded Dimensions

| 項目 | 内容 |
|---|---|
| どんなもの？ | 自動テキスト音声合成（TTS）評価手法を、言語学的に根拠のある10の知覚次元に基づいて分析・メタ評価するフレームワーク。MOS予測器とAudio-LLMによる評価モデルが、人間の聴覚的な判断とどの程度一致するかを包括的に調査した。 |
| 先行研究と比べてどこがすごい？ | 従来の「自然さ」という曖昧な単一指標ではなく、発音や韻律、超分節音韻論などの詳細な分類に基づいた評価スキーマを構築した点。さらに、人間による専門的なアノテーション付きデータセットを用いて、自動評価器の「盲点」を定量的に可視化した。 |
| 技術や手法のキモはどこ？ | 言語レベル、韻律レベル、超言語（パラ言語）レベルの10次元に分解した評価軸の定義。また、意図的なエラー注入（IPA改変、テキスト改変、音響操作）を行い、モデルが特定の品質劣化を正確に検知できるかを問うベンチマーク設計にある。 |
| どうやって有効だと検証した？ | 4つのMOS予測器（UTMOSv2等）と4つのAudio-LLM（Gemini 3.5 Flash等）に対し、860件の言語学的にアノテーションされたデータセットを用いて検証。Kendallのτ係数を用い、各モデルがどの次元に敏感かを測定・分析した。 |
| 議論はある？ | 現在の自動評価器は信号レベルの歪み（ノイズやグリッチ）には強いが、言語的に重要な発音や韻律エラーを捉えきれていない。また、Audio-LLMのプロンプト（指示）の与え方により感度が大きく変動する点や、モデルが評価不能に陥る「出力崩壊」現象が課題である。 |
| 次に読むべき論文は？ | [EmergentTTS-Eval (Manku et al., 2025)](https://arxiv.org/abs/2506.16381) や [InstructTTS-Eval (Huang et al., 2025)](https://arxiv.org/abs/2506.16381) など、モデル・アズ・ア・ジャッジ（Model-as-a-Judge）を用いたTTS評価の先行ベンチマーク。 |
| PDFリンク | https://arxiv.org/pdf/2608.09930v1 |
