---
title: "Personal Visual Context Learning in Large Multimodal Models"
date: 2026-05-12
arxiv_id: 2605.10936v1
url: http://arxiv.org/abs/2605.10936v1
---

# Personal Visual Context Learning in Large Multimodal Models

| 項目 | 内容 |
|---|---|
| どんなもの？ | ウェアラブルデバイスの映像ストリームから得られる個人の視覚履歴を用いて、ユーザー固有の質問に回答する「Personal Visual Context Learning (Personal VCL)」という概念を提唱し、その評価用ベンチマークと手法を提案した研究。 |
| 先行研究と比べてどこがすごい？ | 従来のパーソナライゼーション（特定概念の事前学習や単純なプロンプト付与）とは異なり、長期的な個人の生活習慣や活動履歴を「記憶バンク」として構造化し、推論時に必要な情報だけを選択的に活用する点。 |
| 技術や手法のキモはどこ？ | 「Agentic Context Bank」と呼ばれる、生データを構造化・自己洗練する記憶バンクを構築し、質問に応じて関連する視覚情報のみを動的に取得・検証するクエリ適応型の証拠選択プロセス。 |
| どうやって有効だと検証した？ | 「Personal-VCL-Bench」を構築し、人・物・行動の3軸および総合課題である「EgoWearer Identification」を用いて、複数の大規模マルチモーダルモデル（LMM）で既存のプロンプト手法と比較評価した。 |
| 議論はある？ | 関連情報の取得が前提となっており、検索と推論の共同評価が必要。また、モデルが詳細な視覚情報を確認せずにテキスト記述のみで判断を下してしまう「モダリティの逆説」などの課題が残る。 |
| 次に読むべき論文は？ | [Ego4D [29]](https://arxiv.org/abs/2112.02263), [EgoLife [78]](https://arxiv.org/abs/2503.03803), [CL-bench [18]](https://arxiv.org/abs/2602.03587) |
| PDFリンク | https://arxiv.org/pdf/2605.10936v1 |
