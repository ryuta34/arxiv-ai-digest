---
title: "Decoding the Past: An Uncertainty-Aware Deep Learning Framework for Sex Attribution in Prehistoric Hand Stencils"
date: 2026-08-17
arxiv_id: 2608.14539v1
url: http://arxiv.org/abs/2608.14539v1
---

# Decoding the Past: An Uncertainty-Aware Deep Learning Framework for Sex Attribution in Prehistoric Hand Stencils

| 項目 | 内容 |
|---|---|
| どんなもの？ | 先史時代の洞窟壁画における手形（ハンドステンシル）の生物学的性別を推定するための、不確実性を考慮した深層学習フレームワーク。不完全なデータや解釈の曖昧さを、単なるノイズとして排除するのではなく、分析パイプライン全体を通じて明示的にモデル化・伝播・集約する手法。 |
| 先行研究と比べてどこがすごい？ | 従来の手法（手作業による計測や単一モデル）が抱えていた、人為的なセグメンテーションの主観性や人口統計学的な一般化の困難さを克服。複数の画像処理、モデルの多様性、および不確実性指標を組み込むことで、確信度を定量化し、考古学的解釈に対する透明性と再現性の高い評価基盤を提供した点。 |
| 技術や手法のキモはどこ？ | 画像のトーン調整と手作業の輪郭抽出による「多重解釈の生成」、バイナリ演算等による構造的摂動を加えた「12種類のシルエット生成」、2種類のアーキテクチャ（EfficientNet-B3/MobileViT-S）を用いたアンサンブルによる「階層的予測集約」、およびUMAPとLayerCAMを用いた「不確実性の可視化」。 |
| どうやって有効だと検証した？ | RSNA Bone Age Challengeデータセット（14,036件のX線画像）を用いて現代人の手でモデルを訓練・検証し、88%以上の精度を達成。その後、エル・カスティージョ洞窟等を含む9つの先史時代の手形に適用し、アンサンブル予測の一貫性、潜在空間内の配置、説明可能なAI（LayerCAM）の地図の一致度によって結果の妥当性を評価した。 |
| 議論はある？ | 先史時代の個体群と現代の参照データとの間の進化・環境的な差異の可能性を認めており、あくまで現代データに基づく「確率的な推論」である点に注意を促している。また、輪郭抽出の手動プロセスに起因する主観性や、考古学的サンプル数の少なさが限界として挙げられる。 |
| 次に読むべき論文は？ | [Mollineda et al. 2025 (Sex classification from hand X-ray images)](https://doi.org/10.1016/j.compbiomed.2025.111060) や、[Fernández-Navarro et al. 2025 (Recognizing past shapes)](https://doi.org/10.1016/j.daach.2025.e00453) など、本手法の基礎となった関連研究。 |
| PDFリンク | https://arxiv.org/pdf/2608.14539v1 |
