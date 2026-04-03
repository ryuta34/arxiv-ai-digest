---
title: "Generative World Renderer"
date: 2026-04-03
arxiv_id: 2604.02329v1
url: http://arxiv.org/abs/2604.02329v1
---

# Generative World Renderer

| 項目 | 内容 |
|---|---|
| どんなもの？ | AAAゲームエンジンから、RGB画像と5つのGバッファ（深度、法線、アルベド、金属度、粗さ）が同期した大規模・高品質なビデオデータセットを構築し、それを用いて動画の逆レンダリングおよび前方レンダリングを最適化する手法。 |
| 先行研究と比べてどこがすごい？ | 従来のデータセットが抱えていた「短時間・限定的なシーン・低品質」という問題を克服し、実世界の複雑な環境や気象条件を含む、400万フレームにおよぶ連続的な高品質動画データを提供することで、モデルの汎用性を飛躍的に向上させた点。 |
| 技術や手法のキモはどこ？ | グラフィックスAPIレベルでのGバッファインターセプトと、2画面を用いたモザイク合成手法により、エンジンを改変せずに高品質かつ時間同期したデータを取得するパイプラインを開発した点。また、VLM（Vision-Language Model）を用いた評価プロトコルを導入した点。 |
| どうやって有効だと検証した？ | 既存の逆レンダリングモデル（DiffusionRenderer等）を提案データセットでファインチューニングし、定量的評価および人間のCG専門家との比較を通じて、VLM評価指標が人間の判断と強く相関することを確認した。さらに、ゲーム編集や relighting タスクにおける応用可能性も示した。 |
| 議論はある？ | 現在のデータセット構築は特定のゲームに依存している点。また、VLMを用いた評価プロトコルは有用だが、依然として主観的な側面が残る点。今後はより多様なゲームエンジンや実世界データへの適用範囲拡大が課題となる。 |
| 次に読むべき論文は？ | [18] Z. Chen et al., "Uni-renderer: Unifying rendering and inverse rendering via dual stream diffusion", CVPR 2025. <br> [75] R. Liang et al., "Diffusion renderer: Neural inverse and forward rendering with video diffusion models", CVPR 2025. |
| PDFリンク | https://arxiv.org/pdf/2604.02329v1 |
