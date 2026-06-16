---
title: "The Value Axis: Language Models Encode Whether They're on the Right Track"
date: 2026-06-16
arxiv_id: 2606.17056v1
url: http://arxiv.org/abs/2606.17056v1
---

# The Value Axis: Language Models Encode Whether They're on the Right Track

| 項目 | 内容 |
|---|---|
| どんなもの？ | 言語モデルが内部で保持する「現在の推論が目標達成に近づいているか（成功確率）」という価値判断の指標を線形軸（value axis）として特定し、その性質を解析した研究。この軸を操作することで、モデルの自信の度合い、自己修正行動、出力の冗長性を因果的に制御できることを示した。 |
| 先行研究と比べてどこがすごい？ | 従来手法とは異なり、強化学習環境で訓練することなく、合成的なインコンテキスト強化学習（ICRL）データを用いることで、汎用的な「価値軸」を特定した点。また、この軸が数学、コーディング、DPOによる選好学習など、多様なドメインを横断して一貫した機能を持つことを実証した点。 |
| 技術や手法のキモはどこ？ | 隠された基準（例：「ダッシュ記号を含める」）を推測するゲームをモデルにプレイさせ、成功（報酬+1）を得る直前と直後の隠れ層の活性化パターンの差分から「価値軸」を構築したこと。さらに、その軸に沿ってモデルの活性化ベクトルを直接操作（steering）する手法を採用したこと。 |
| どうやって有効だと検証した？ | AIME数学問題やLeetCodeコーディング問題を用いて、価値軸の操作が自信の度合いやコードの冗長性、自己修正（バックトラッキング）に与える因果的影響を測定。また、DPOによる学習がモデルの価値評価軸を変化させることや、Chatbot Arenaの現実的なデータセットでの有効性を検証した。 |
| 議論はある？ | 特定のドメイン（ICRL）から構築した価値軸が、他のタスクにおいても最適な指標であるかは未知数である。また、モデルの規模が大きくなった場合や、学習の初期段階（事前学習か事後学習か）による影響については詳しく調査されておらず、限定的なドメインでの検証に留まっている。 |
| 次に読むべき論文は？ | [Han et al. (2026) - "How’s it going? reinforcement learning in language models recruits a functional welfare axis"](https://arxiv.org/abs/2605.30232)、[Afzal et al. (2025) - "Knowing before saying: LLM representations encode information about chain-of-thought success before completion"](https://aclanthology.org/2025.findings-acl.1) |
| PDFリンク | https://arxiv.org/pdf/2606.17056v1 |
