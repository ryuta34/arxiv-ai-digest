---
title: "ATLAS: Agentic or Latent Visual Reasoning? One Word is Enough for Both"
date: 2026-05-15
arxiv_id: 2605.15198v1
url: http://arxiv.org/abs/2605.15198v1
---

# ATLAS: Agentic or Latent Visual Reasoning? One Word is Enough for Both

| 項目 | 内容 |
|---|---|
| どんなもの？ | 視覚的な推論過程を「機能トークン（functional token）」として離散的なテキストトークンとして扱う、効率的でスケーラブルな視覚推論フレームワーク「ATLAS」を提案している。外部ツールや画像生成を介さず、標準的な自己回帰生成モデル内で視覚的な操作を完結させる。 |
| 先行研究と比べてどこがすごい？ | 外部コード実行による遅延や、連続的な潜在表現による学習の不安定さを解消している。標準的なVLMのアーキテクチャを変更せず、追加の画像生成も行わないため、高い推論効率と学習の並列性を実現した。 |
| 技術や手法のキモはどこ？ | 5つの汎用的な機能トークン（`<|Manip|>`, `<|Shape|>`, `<|Line|>`, `<|Arrow|>`, `<|Text|>`）を導入し、次トークン予測の一部として学習する点。また、RL訓練時の「勾配希釈」を防ぐため、機能トークンの位置に焦点を当てた補助損失「LA-GRPO（Latent-Anchored GRPO）」を導入した点。 |
| どうやって有効だと検証した？ | V*, BLINK, WeMathといった視覚推論ベンチマークを用い、他のVLM（統一モデル、エージェントモデル、潜在モデル）と性能を比較。さらに、アブレーションスタディによって報酬設計の妥当性を、アテンション可視化によって機能トークンの有効性を検証した。 |
| 議論はある？ | 現在の機能トークン集合は限定的であり、より多様な操作への拡張が今後の課題。また、シーケンスレベルの強化学習において、特定のタスク（IQや多視点推論など）では性能の変動が見られるため、さらなる安定化が求められる。 |
| 次に読むべき論文は？ | [Visual CoT (Shao et al., 2024)](https://arxiv.org/abs/2403.09629), [V-Thinker (Qiao et al., 2025b)](https://arxiv.org/abs/2511.04460), [Latent Visual Reasoning (Li et al., 2025a)](https://arxiv.org/abs/2509.24251) |
| PDFリンク | https://arxiv.org/pdf/2605.15198v1 |
