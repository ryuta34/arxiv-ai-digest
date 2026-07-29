---
title: "Pass the Baton: Trajectory-Relayed On-Policy Distillation"
date: 2026-07-29
arxiv_id: 2607.26057v1
url: http://arxiv.org/abs/2607.26057v1
---

# Pass the Baton: Trajectory-Relayed On-Policy Distillation

| 項目 | 内容 |
|---|---|
| どんなもの？ | 大規模言語モデルの強化学習・蒸留における「プレフィックス失敗（早期の誤った推論により、以降の生成が全て誤る問題）」を解決する「Relay-OPD」という新しい強化学習手法です。推論中に教師モデルが一時的に介入し、誤った推論方向を軌道修正することで、効率的かつ高精度な学習を実現します。 |
| 先行研究と比べてどこがすごい？ | 従来の固定長切り詰めや事後修正と異なり、推論の状態に基づきオンラインで介入を行います。これにより、教師による介入量を最小限（トークン比0.35%）に抑えつつ、平均学習軌道長を50%以上短縮し、複数の数学ベンチマークで最高性能を達成しました。 |
| 技術や手法のキモはどこ？ | 推論過程で「教師は方向転換し、生徒は直進する」という非対称性を検知する「Handoff trigger」です。これを発火点として教師が短い「Teacher leg」を生成し、推論を修正した後に生徒へ制御を戻す「Relay（中継）」構造を、推論エンジン内でシームレスに統合した点にあります。 |
| どうやって有効だと検証した？ | 8つの数学的推論ベンチマークを用い、Qwen3-4B-Instructを教師、0.6B/1.7Bモデルを生徒として評価しました。標準的なOPDや、既存の強力なベースラインであるFastOPDと比較し、高い精度向上と学習効率の改善を確認しました。 |
| 議論はある？ | 反射トークンの集合はモデルファミリ間で調整が必要な場合があること、教師と生徒の能力差が小さい場合には本手法の効果が限定的になる可能性があります。また、現在の予算設定は1.7Bモデルで最適化されており、モデルが変わるごとに再調整が望ましいとされています。 |
| 次に読むべき論文は？ | [On-policy distillation of language models: Learning from self-generated mistakes](https://arxiv.org/abs/2405.02102)、[Deepseek-r1: Incentivizing reasoning capability in llms via reinforcement learning](https://arxiv.org/abs/2501.12948) |
| PDFリンク | https://arxiv.org/pdf/2607.26057v1 |
