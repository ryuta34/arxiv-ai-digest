---
title: "Solving Physics Olympiad via Reinforcement Learning on Physics Simulators"
date: 2026-04-14
arxiv_id: 2604.11805v1
url: http://arxiv.org/abs/2604.11805v1
---

# Solving Physics Olympiad via Reinforcement Learning on Physics Simulators

| 項目 | 内容 |
|---|---|
| どんなもの？ | 物理シミュレータを用いて多様な物理シーンを自動生成し、そこから得られたデータで大規模言語モデル（LLM）を強化学習させることで、物理推論能力を高める手法「Sim2Reason」を提案した論文。人間の注釈なしにシミュレータから大規模なQAデータセットを構築し、物理オリンピック等の現実世界ベンチマークで高い汎化性能を示した。 |
| 先行研究と比べてどこがすごい？ | インターネット上の既存QAデータは物理学分野で不足しているというボトルネックを、シミュレータを用いた合成データ生成により解消した点。また、シミュレータのAPIをLLMに直接操作させる手法（Toolformer等）と比較して、より安定した精度の高い物理推論を実現し、未知の物理問題へのゼロショット転移性能を飛躍的に向上させた。 |
| 技術や手法のキモはどこ？ | 物理パラメータを適切にランダム化・構成するドメイン固有言語（DSL）の設計と、シミュレーション過程で生じる不自然な事象を排除する動的なフィルタリング。さらに、単純な正解を導くだけの「ショートカット」問題を排除するアブレーション手法と、強化学習（RLVR）によるモデルの推論プロセス最適化を組み合わせた点。 |
| どうやって有効だと検証した？ | IPhO（国際物理オリンピック）、JEEBench、PHYSICS、OlympiadBenchなどの難関物理ベンチマークを用いたゼロショット評価を実施。Qwenモデルシリーズ（3B〜32B）に対し、提案手法で学習したモデルが他手法を上回る性能向上（IPhOで5-10%ポイントの改善）を達成したことで有効性を実証した。 |
| 議論はある？ | 現在は古典力学が中心であり、電磁気学や熱力学など他の物理分野への拡張が今後の課題。また、シミュレータの物理モデルに依存するため、シミュレータ自体が対応していない極端な物理条件下での推論には制限がある可能性があり、今後は他のシミュレータ（NVIDIA Omniverse等）との親和性向上を図る必要がある。 |
| 次に読むべき論文は？ | 1. [DeepSeek-R1: Incentivizing reasoning capability in llms via reinforcement learning](https://arxiv.org/abs/2501.12948)<br>2. [Dapo: An open-source llm reinforcement learning system at scale](https://arxiv.org/abs/2503.14476)<br>3. [Scaling physical reasoning with the physics dataset](https://arxiv.org/abs/2506.00022) |
| PDFリンク | https://arxiv.org/pdf/2604.11805v1 |
