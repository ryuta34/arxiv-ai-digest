---
title: "ParVL: Parallel Scaling and Expandable Compute Allocation for Multimodal LLMs"
date: 2026-08-05
arxiv_id: 2608.04010v1
url: http://arxiv.org/abs/2608.04010v1
---

# ParVL: Parallel Scaling and Expandable Compute Allocation for Multimodal LLMs

| 項目 | 内容 |
|---|---|
| どんなもの？ | マルチモーダル大規模言語モデル（MLLM）において、共通のバックボーンを再利用しつつ、視覚（ViT）と言語（LLM）の各ブランチ数を動的に変更して計算量を拡張する「ParVL」フレームワーク。各ブランチに特定の接頭辞（Prefix）を付与することで、固定パラメータ予算内での柔軟な計算資源の割り当てを実現している。 |
| 先行研究と比べてどこがすごい？ | 既存研究が固定された計算配分や、単一の計算パスに依存していたのに対し、ParVLは視覚と言語の計算量を独立して制御できる2次元の拡張性を導入した。パラメータ数をわずか4%以内の増加に抑えつつ、複数のベンチマークでマルチモーダル推論の性能向上を達成した点。 |
| 技術や手法のキモはどこ？ | 学習可能な接頭辞（KV Prefix）を各ブランチのセルフアテンション層に導入し、バックボーンパラメータを共有しつつブランチごとに異なる振る舞いをさせる仕組み。また、トークン単位のMLPアグリゲータを介して、複数のブランチからの出力を重み付け統合する手法。 |
| どうやって有効だと検証した？ | InternVL3.5をベースに、1B、2B、8Bのモデルスケールで9つのマルチモーダルベンチマークを用いて評価。単一ブランチベースラインと比較し、タスクに応じて最適なブランチ構成（Pv:Pl）が異なることを実証。さらに、推論時の計算効率を向上させる「疎なルーティング（Sparse Routing）」の有効性も検証した。 |
| 議論はある？ | 現在はSFT段階での拡張に留まっており、事前学習段階からの並列スケーリングの影響は未知数である点。また、リソース制約によりSFTデータの一部（1/20）のみを使用しているため、より大規模なデータセットでのスケーリング効果は今後の検証が必要。 |
| 次に読むべき論文は？ | [Chen et al. 2025: Parallel Scaling Law for Language Models](https://arxiv.org/abs/2502.13158) や [Zhu et al. 2025b: Scaling latent reasoning via looped language models](https://arxiv.org/abs/2510.25741) |
| PDFリンク | https://arxiv.org/pdf/2608.04010v1 |
