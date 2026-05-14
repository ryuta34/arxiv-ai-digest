---
title: "WARDEN: Endangered Indigenous Language Transcription and Translation with 6 Hours of Training Data"
date: 2026-05-14
arxiv_id: 2605.13846v1
url: http://arxiv.org/abs/2605.13846v1
---

# WARDEN: Endangered Indigenous Language Transcription and Translation with 6 Hours of Training Data

| 項目 | 内容 |
|---|---|
| どんなもの？ | わずか6時間の訓練データしか存在しない絶滅危惧言語「ワーダマン語」を対象とした、高精度な自動書き起こし・翻訳システム「WARDEN」の提案。言語学的な専門知識とAIを組み合わせることで、低リソース言語の言語ドキュメント作成を支援する。 |
| 先行研究と比べてどこがすごい？ | 大規模データを必要とする従来の統一型モデルと異なり、音素の類似性や専門辞書を導入する2段階のアプローチを採用。わずか6時間のデータ量で、既存の大規模オープンソースモデルやプロプライエタリモデルを凌駕する性能を実現した点。 |
| 技術や手法のキモはどこ？ | 書き起こし時に音素構造が似たスンダ語を用いてモデルを初期化する点と、翻訳時に専門辞書から関連用語を検索してプロンプトに組み込み、LLMを知識ベースの翻訳機として活用する「レキシコン（語彙）拡張」手法。 |
| どうやって有効だと検証した？ | 実際にフィールドワークで収集された計6時間のワーダマン語音声コーパスを用いて評価。アブレーションスタディ（辞書なし・辞書あり、初期化手法の有無など）を行い、BLEUスコアやWER（単語誤り率）の改善を確認した。 |
| 議論はある？ | 辞書の品質に依存する点や、翻訳対象言語に合わせたモデルチューニングが必要である点。また、コミュニティ主導の保存・活性化に向け、先住民コミュニティからのフィードバックが不可欠であることを挙げている。 |
| 次に読むべき論文は？ | [13] [Robust speech recognition via large-scale weak supervision](https://arxiv.org/abs/2212.04356) や [15] [LoRA: Low-rank adaptation of large language models](https://arxiv.org/abs/2106.09685) |
| PDFリンク | https://arxiv.org/pdf/2605.13846v1 |
