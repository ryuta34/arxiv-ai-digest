---
title: "AVA-Encoder: Towards Agent-Native Video Representation Learning"
date: 2026-08-13
arxiv_id: 2608.12313v1
url: http://arxiv.org/abs/2608.12313v1
---

# AVA-Encoder: Towards Agent-Native Video Representation Learning

| 項目 | 内容 |
|---|---|
| どんなもの？ | 映画制作プロセスをエージェントが推論・操作可能な形式に変換するための「AVA-Encoder」というビデオ自動符号化フレームワーク。動画を階層的な知識グラフ（KG）として表現し、再構成を通じた自己進化的な学習を行うことで、エージェントによる cinematic な動画制作を支援する。 |
| 先行研究と比べてどこがすごい？ | 既存の動画表現（ピクセルやキャプション）が理解・操作に不向きであるのに対し、本手法は構造化された知識グラフを用いることで、物語・ショット・アセット間の依存関係を保持。エージェントが直接編集・再生成可能な形式を実現し、最強のベースライン比でOverall評価で20.7ポイント向上させた点。 |
| 技術や手法のキモはどこ？ | 物語・ショット・キーフレームの階層構造を持つ知識グラフの採用と、その再構成誤差を「テキスト勾配」として還元するデュアルループ学習（Policy Pseudo-TrainingとKG Representation Refinement）。これにより、エージェント自身の推論能力を学習・改善する自己進化ループを構築した点。 |
| どうやって有効だと検証した？ | 18個の多様な動画クリップからなる独自ベンチマークを用い、再構成精度（V, KF, V-BC, KF-BCの4項目）で評価。また、人間による評価との整合性が97.3%であることを確認し、下流の動画生成エージェントにおける性能向上も実証した。 |
| 議論はある？ | 現在は固定されたデコーダーに依存しており、生成モデル自体を更新するわけではない。また、非常に長い動画における知識グラフの複雑性や、長期間にわたる整合性維持については今後の課題として残されている。 |
| 次に読むべき論文は？ | [Textgrad: Automatic "differentiation" via text (Yuksekgonul et al., 2024)](https://arxiv.org/abs/2406.07496)、[MA-LMM: Memory-augmented large multimodal model for long-term video understanding (He et al., 2024)](https://arxiv.org/abs/2410.13514) |
| PDFリンク | https://arxiv.org/pdf/2608.12313v1 |
