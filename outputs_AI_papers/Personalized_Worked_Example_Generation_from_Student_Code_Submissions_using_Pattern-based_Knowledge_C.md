---
title: "Personalized Worked Example Generation from Student Code Submissions using Pattern-based Knowledge Components"
date: 2026-04-28
arxiv_id: 2604.24758v1
url: http://arxiv.org/abs/2604.24758v1
---

# Personalized Worked Example Generation from Student Code Submissions using Pattern-based Knowledge Components

| 項目 | 内容 |
|---|---|
| どんなもの？ | 学生のプログラミング提出物からAST（抽象構文木）ベースの知識コンポーネント（KC）を抽出し、LLMによるパーソナライズされた模範解答生成をガイドするシステム。学生の論理的誤りに直接アプローチすることで、学習効果の高い解説の自動生成を目指す研究。 |
| 先行研究と比べてどこがすごい？ | 従来のLLMによる模範解答生成は学生個別の誤りに適合しない場合があったが、本手法は学生のコード内の具体的な「知識の欠如」をパターンとして抽出し、それをプロンプトに組み込むことで、より relevance（関連性）と novice-friendly（初心者向け）な解説を生成できる点。 |
| 技術や手法のキモはどこ？ | ASTのサブツリーから学習済みモデルを用いて論理的誤りの兆候となるパターンを特定し、それを「知識コンポーネント（KC）」としてラベル付けしてLLMに制約として入力する点。 |
| どうやって有効だと検証した？ | 100件の学生の誤った提出物に対し、ベースラインとKC条件付き生成で計200件の模範解答を生成。専門家によるルーブリック評価（解説の質や学生の誤りへの適合性など）と、ペアワイズの好み調査を行い、KC条件付きの方が有意に高い評価を得たことを示した。 |
| 議論はある？ | KC条件付き生成では、複数のKCを盛り込もうとしてステップ構成が複雑になる（ステップ構造の評価がわずかに低下する）トレードオフがある。また、複数のKCが重なった際にどれを優先すべきかの決定メカニズムが今後の課題。 |
| 次に読むべき論文は？ | [5] Hoq et al., 2025: "Pattern-based Knowledge Component Extraction from Student Code Using Representation Learning" (arXiv:2508.09281) |
| PDFリンク | https://arxiv.org/pdf/2604.24758v1 |
