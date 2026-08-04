---
title: "AURORA-LM: Autoencoding Unified Representation for Continuous-Latent Diffusion Language Modeling"
date: 2026-08-04
arxiv_id: 2608.02602v1
url: http://arxiv.org/abs/2608.02602v1
---

# AURORA-LM: Autoencoding Unified Representation for Continuous-Latent Diffusion Language Modeling

| 項目 | 内容 |
|---|---|
| どんなもの？ | 言語生成を離散的なトークン予測ではなく、連続的な潜在空間での拡散モデルとして定式化した言語モデル「AURORA-LM」の提案。表現学習と生成分布のモデル化を分離し、高品質なデコードを維持したまま連続的な潜在拡散を可能にした。 |
| 先行研究と比べてどこがすごい？ | 既存の連続言語モデルが抱えていた「表現の圧縮による精度低下」というトレードオフを解消し、高容量でデコード可能な潜在表現を保持したまま diffusion を適用できる点。大規模言語モデルと比較しても同等以上の性能を達成している。 |
| 技術や手法のキモはどこ？ | クエリベースのEncoder-Decoderによる高容量な潜在シーケンスの構築、低ランクボトルネックを用いたノイズ入力経路の制約、および学習効率を高めるブロック因果デノイザーと「自己軌道一貫性（Self-trajectory consistency）」の導入。 |
| どうやって有効だと検証した？ | OpenWebTextを用いた自由生成およびXSumを用いた要約タスクで、既存の autoregressive、離散 diffusion、連続埋め込み拡散モデル群と比較評価。また、1Bパラメータへスケールさせ、大規模なベンチマークで従来モデルを上回る性能を示した。 |
| 議論はある？ | 潜在表現の圧縮を避けるためにモデルアーキテクチャが工夫されているが、生成コストや学習の複雑さは依然として課題となる。今後はより長い文脈への適用や、他モダリティとの統合が期待される。 |
| 次に読むべき論文は？ | [15] Continuous latent diffusion language model, [23] Elf: Embedded language flows, [29] Diffusion-LM improves controllable text generation |
| PDFリンク | https://arxiv.org/pdf/2608.02602v1 |
