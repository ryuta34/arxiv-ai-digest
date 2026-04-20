---
title: "FineCog-Nav: Integrating Fine-grained Cognitive Modules for Zero-shot Multimodal UAV Navigation"
date: 2026-04-20
arxiv_id: 2604.16298v1
url: http://arxiv.org/abs/2604.16298v1
---

# FineCog-Nav: Integrating Fine-grained Cognitive Modules for Zero-shot Multimodal UAV Navigation

| 項目 | 内容 |
|---|---|
| どんなもの？ | 無人航空機（UAV）の視覚言語ナビゲーション（VLN）のために、人間のような認知機能（知覚、注意、記憶、想像、推論、意思決定）を統合したゼロショット推論フレームワーク「FineCog-Nav」。複雑な3D環境下で、マルチステップの指示に従い長期的なナビゲーションを可能にする。 |
| 先行研究と比べてどこがすごい？ | 従来の大規模モデルに依存した手法とは異なり、中規模の基盤モデルをモジュール化して連携させることで、高い解釈性と効率性を実現した。また、従来のデータセットの品質課題を解決するために、精緻なベンチマーク「AerialVLN-Fine」を新たに構築した。 |
| 技術や手法のキモはどこ？ | 命令解析器、注意機構、想像モジュール、階層的メモリ（ステップ、サブゴール、指示レベル）という細かい認知モジュールを協調させた設計。これにより、大規模モデルを使わずとも、個別のモジュールが専門化されたプロンプトに基づいて相互に補完し合うことで、堅牢なナビゲーションを実現している。 |
| どうやって有効だと検証した？ | 構築した「AerialVLN-Fine」および既存の「AerialVLN-S-Val」データセットで評価し、ナビゲーション誤差（NE）や成功率（SR）などでベースラインを圧倒した。また、人間による評価試験を行い、本手法が人間のような探索行動により近いとして選好されたことを確認した。 |
| 議論はある？ | 現在のモデルは中規模であるものの、ゼロショット設定での成功率は依然として課題が残る。実世界での飛行試験では成功したが、センサーノイズや制御誤差への対処は今後の課題である。また、非常に巨大なモデル（GPT-4等）に比べれば性能面で制約がある可能性がある。 |
| 次に読むべき論文は？ | [11] Aerial vision-and-language navigation via semantic-topo-metric representation guided llm reasoning<br>[21] Aerialvln: Vision-and-language navigation for uavs<br>[45] Embodied navigation foundation model |
| PDFリンク | https://arxiv.org/pdf/2604.16298v1 |
