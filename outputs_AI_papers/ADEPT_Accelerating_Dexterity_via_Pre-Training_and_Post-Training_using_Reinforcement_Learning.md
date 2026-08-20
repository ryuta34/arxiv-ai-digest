---
title: "ADEPT: Accelerating Dexterity via Pre-Training and Post-Training using Reinforcement Learning"
date: 2026-08-20
arxiv_id: 2608.19182v1
url: http://arxiv.org/abs/2608.19182v1
---

# ADEPT: Accelerating Dexterity via Pre-Training and Post-Training using Reinforcement Learning

| 項目 | 内容 |
|---|---|
| どんなもの？ | 高い自由度（DoF）を持つロボットアーム・ハンドシステムにおいて、汎用的な「物体配置（reposing）」タスクで事前学習を行い、それを接触を伴う複雑な後続タスクへと効率的に転移させる強化学習フレームワーク「ADEPT」の提案。 |
| 先行研究と比べてどこがすごい？ | スクラッチからの学習で必要となる低レベルなスキル（把持・持ち上げ等）の再学習を回避し、シミュレーションでの事前学習モデルを実機へゼロショットで適用可能にした点。また、従来の制約付きアプローチと異なり、関節空間全体を利用してヒューマンレベルの器用な操作を実現した点。 |
| 技術や手法のキモはどこ？ | 学習崩壊を防ぐ「行動クローニング蒸留」「Criticのウォームアップ」「保守的なオンポリシー更新」を組み合わせた構造化された後続学習レシピと、関節空間全体で動作を許容しつつ安全性を担保する「幾何学的ファブリック（Geometric Fabrics）」の導入。 |
| どうやって有効だと検証した？ | 23自由度のKuka-Allegroと29自由度のFlexiv-Sharpaを用い、Functional Manipulation Benchmark（FMB）等のpeg insertionおよび食器の配置タスクで実験。実機環境でのゼロショット適用に成功し、従来手法と比較して2〜14倍のタスク実行速度を達成した。 |
| 議論はある？ | 現在の課題として、遮蔽条件下での非対称物体の向き推定の困難さや、指先での把持不安定性が挙げられる。将来的な課題として、より多様な操作、道具の使用、両手操作への拡張や、学習済み事前分布が大きく異なるタスクへの転移限界の調査が必要。 |
| 次に読むべき論文は？ | [13] Geometric fabrics: a safe guiding medium for policy learning (ICRA 2024), [14] DextrAH-RGB: Visuomotor policies to grasp anything with dexterous hands (arXiv:2412.01791), [25] Play2Perfect: What matters in dexterous play pretraining for precise assembly? (arXiv:2606.26428) |
| PDFリンク | https://arxiv.org/pdf/2608.19182v1 |
