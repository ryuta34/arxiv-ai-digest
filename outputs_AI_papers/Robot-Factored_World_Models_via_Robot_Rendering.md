---
title: "Robot-Factored World Models via Robot Rendering"
date: 2026-07-27
arxiv_id: 2607.22535v1
url: http://arxiv.org/abs/2607.22535v1
---

# Robot-Factored World Models via Robot Rendering

| 項目 | 内容 |
|---|---|
| どんなもの？ | ロボットの動作をビデオ世界モデルの条件付け信号として適切に提示するための手法「Robot-Factored World Models」です。ロボット固有の制御信号を直接用いるのではなく、カメラ視点でレンダリングされたロボットの幾何学的情報を用いることで、多様なロボット形態への汎用化と高精度なビデオ生成を実現します。 |
| 先行研究と比べてどこがすごい？ | 従来のベクトルベースの制御信号はロボットの実施プロセスに依存していましたが、本手法は動作を「nominal trajectory（名目上の軌道）」に変換してレンダリングすることで、 embodiment（身体性）に依存しない共通の視覚インターフェースを構築しました。これにより、未知のロボットや人間によるデモ動画への汎用的な適応を可能にしています。 |
| 技術や手法のキモはどこ？ | ロボットのコントローラーとキネマティクスを通した「名目上の軌道」を、URDFを用いてカメラ視点でレンダリングし、RGBメッシュとエンドエフェクタ深度として入力する点です。これにより、モデルはアクションを「視覚的なロボット形状の変化」として直接学習し、シーンの反応を予測できます。 |
| どうやって有効だと検証した？ | DROIDおよびRoboCasa-GR1データセットを用い、SVDやWan 2.1ベースのモデルで比較検証を実施。既存のAdaLN状態ベクトルベースの手法と比較し、PSNR、SSIM、LPIPS等の指標で上回る精度を達成しました。さらに、未知のロボットやヒューマンデモからのリターゲティングによるゼロショット推論で有効性を示しました。 |
| 議論はある？ | 知られているロボットのURDFモデルと、カメラとロボット間の正確なキャリブレーションが必要です。また、静的な背景の仮定（動的なシーン変化の扱いに課題）、および学習データに成功事例が多く失敗事例への堅牢性が不足している点を将来の改善課題として挙げています。 |
| 次に読むべき論文は？ | [1] [D. Ha et al. Recurrent world models facilitate policy evolution](https://arxiv.org/abs/1809.04849)<br>[44] [B. Kim et al. Dexterous world models](https://arxiv.org/abs/2512.17907)<br>[52] [T. Ma et al. Dit4dit: Jointly modeling video dynamics and actions](https://arxiv.org/abs/2603.10448) |
| PDFリンク | https://arxiv.org/pdf/2607.22535v1 |
