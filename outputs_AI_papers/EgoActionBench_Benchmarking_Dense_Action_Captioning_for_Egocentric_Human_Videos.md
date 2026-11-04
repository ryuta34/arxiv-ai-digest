---
title: "EgoActionBench: Benchmarking Dense Action Captioning for Egocentric Human Videos"
date: 2026-11-04
arxiv_id: 2611.03646v1
url: http://arxiv.org/abs/2611.03646v1
---

# EgoActionBench: Benchmarking Dense Action Captioning for Egocentric Human Videos

| 項目 | 内容 |
|---|---|
| どんなもの？ | エゴセントリック（一人称視点）映像における微細な人間の動作を、左手・右手・両手の3つのトラックで時間的に詳細に記述（Dense Action Captioning）するための新しいベンチマーク「EgoActionBench」を提案しています。1,407エピソード、41,132件の人手で精査されたアノテーションを含み、動作の原子性（Atomicity）、時間的精度、および手と動作の対応関係の理解をモデルに求めます。 |
| 先行研究と比べてどこがすごい？ | 従来の手法は「何をしているか」という大まかな認識や活動の分類に留まっていましたが、本研究は連続する複雑な作業を微細な原子単位の動作に分解し、どの手が何を行ったかを個別に追跡できる点が画期的です。また、時間的な境界や意味内容を正確に評価するための、予測と正解を動的に照合する新しい評価プロトコルを確立しました。 |
| 技術や手法のキモはどこ？ | Human-in-the-loop（人間参加型）の5段階パイプラインによるアノテーション作成と、LLMを用いたセマンティックな評価プロトコルです。具体的には、手領域のマスク抽出、スライディングウィンドウによるキャプション提案、AIエージェントによる品質管理を経て、人手による最終確認を行うことで高精度なデータセットを構築しました。また、評価にはグループ相対的な報酬設計（GRPO）を用いた強化学習を取り入れています。 |
| どうやって有効だと検証した？ | 20種類の既存のVLMや動画理解モデルをベンチマークし、さらにQwen3-VL-4BとLLaVA-OneVision-2-8Bを本データセットで微調整して性能を比較しました。その結果、提案手法がベースラインを大幅に上回り、特に細かい動作の認識と時間的な追跡において従来モデルの限界を明らかにしました。 |
| 議論はある？ | 短い時間で発生する動作（1秒未満など）の正確な境界検知が依然として大きな課題であることが示されました。また、GPT-6 Astraのような強力なモデルであっても人間エキスパートの性能（EgoActionScore 90.4）には大きく及ばない（モデル最大値は59.6）ことから、 embodied intelligence（身体化知能）に必要なレベルの動作理解にはまだ大きな乖離があることを指摘しています。 |
| 次に読むべき論文は？ | [Ego4D: Around the world in 3,000 hours of egocentric video](https://openaccess.thecvf.com/content/CVPR2022/html/Grauman_Ego4D_Around_the_World_in_3000_Hours_of_Egocentric_Video_CVPR_2022_paper.html)、[Ego-Exo4D: Understanding skilled human activity from first- and third-person perspectives](https://openaccess.thecvf.com/content/CVPR2024/html/Grauman_Ego-Exo4D_Understanding_Skilled_Human_Activity_from_First-_and_Third-Person_Perspectives_CVPR_2024_paper.html) |
| PDFリンク | https://arxiv.org/pdf/2611.03646v1 |
