---
title: "Spectral Gaps of Hit-and-Run and Coordinate Hit-and-Run"
date: 2026-08-18
arxiv_id: 2608.16878v1
url: http://arxiv.org/abs/2608.16878v1
---

# Spectral Gaps of Hit-and-Run and Coordinate Hit-and-Run

| 項目 | 内容 |
|---|---|
| どんなもの？ | 凸集合上のサンプリング手法であるHit-and-Run（HAR）およびCoordinate Hit-and-Run（CHAR）の収束速度を、従来の境界や導関数に基づく解析ではなく、関数解析的な「ポアンカレ定数」や「Babuška–Aziz定数」を用いて理論的に解明した研究。 |
| 先行研究と比べてどこがすごい？ | 従来手法（コンダクタンスに基づく解析）では困難だった、Hit-and-Runの収束と等周不等式（KLS定数）の関連付けに成功した点。これにより、次元依存性を改善し、等方的な凸体に対してほぼ二次多項式の収束時間を導出した。 |
| 技術や手法のキモはどこ？ | スペクトルギャップを「二重証明（dual certificate）」の手法で下界評価し、それをPDE解析で現れるBabuška–Aziz定数に帰着させた点。この定数が「改良型ポアンカレ定数」で上界評価できることを利用した解析フレームワーク。 |
| どうやって有効だと検証した？ | 関数解析的な証明によって、HARに対して $O(n^2 C_{PI} \log(M/\varepsilon))$、CHARに対して $O(n^3 C_{PI} \log(M/\varepsilon))$ という新しい混合時間の上界を理論的に導出した。 |
| 議論はある？ | 現在の証明は連続的な設定を主としている。また、CHARの $O(n^3)$ 収束は漸近的にタイトであると予想されているが、より詳細な最適性の検討や、さらに複雑な形状への適用が今後の課題。 |
| 次に読むべき論文は？ | [Chen & Eldan (2026) "Hit-and-Run mixing via localization schemes"](https://arxiv.org/abs/2608.16878)（本論文の参考文献 [CE26]） |
| PDFリンク | https://arxiv.org/pdf/2608.16878v1 |
