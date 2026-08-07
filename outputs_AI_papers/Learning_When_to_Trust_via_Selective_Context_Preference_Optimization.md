---
title: "Learning When to Trust via Selective Context Preference Optimization"
date: 2026-08-07
arxiv_id: 2608.06377v1
url: http://arxiv.org/abs/2608.06377v1
---

# Learning When to Trust via Selective Context Preference Optimization

| 項目 | 内容 |
|---|---|
| どんなもの？ | 外部からの誤った示唆（ミスリーディングな文脈）によって回答が歪められる問題に対し、「選択的信頼（Selective Trust）」の概念を提唱し、モデルが信頼すべき情報と無視すべき情報を適切に判断できるようにする学習手法「SCOPE」を提案した論文。 |
| 先行研究と比べてどこがすごい？ | 従来の手法（抵抗力の強化）は単にすべての文脈を無視するリスクがあったが、本手法は「clean」「misleading」「correct-context」「irrelevant-context」の4つの条件でバランスよく学習することで、正確性を損なわずに誤った信号への耐性を高める点。 |
| 技術や手法のキモはどこ？ | ミスリーディングな信号を含む失敗事例を「truth-consistent（真実と整合する）」な回答とペアにし、さらに他の3つのコンテキスト条件でバランスを取りながら、DPO（Direct Preference Optimization）を用いて学習させる点。 |
| どうやって有効だと検証した？ | 人手で注釈を付けた1,000項目（4,000条件行）のベンチマーク「MIST」を構築し、GPT-5.5を含む多数のモデルで評価。SC2W（信号に誘発された正誤反転率）の指標を用い、ベースモデルと比較して高い耐性と性能維持を実証した。 |
| 議論はある？ | 本研究はテキストベースの診断であり、実デプロイ環境での発生頻度とは異なる点や、Chain-of-Thoughtの真の忠実性を保証するものではないこと。また、使用したベンチマークの多くが公開データセット由来であり、汚染の可能性が完全には否定できないこと。 |
| 次に読むべき論文は？ | [1] [Turpin et al., 2023](https://arxiv.org/abs/2305.14388), [2] [Sharma et al., 2024](https://arxiv.org/abs/2402.13663), [3] [Rafailov et al., 2023](https://arxiv.org/abs/2305.18290) |
| PDFリンク | https://arxiv.org/pdf/2608.06377v1 |
