---
title: "Gaze Heads: How VLMs Look at What They Describe"
date: 2026-06-15
arxiv_id: 2606.14703v1
url: http://arxiv.org/abs/2606.14703v1
---

# Gaze Heads: How VLMs Look at What They Describe

| 項目 | 内容 |
|---|---|
| どんなもの？ | 視覚言語モデル（VLM）が内部的にどのように画像を処理し、記述に反映させているかを解明する研究。特定の少数のアテンションヘッドが「視線（Gaze）」のように機能し、モデルが現在記述している画像領域を追跡していることを突き止め、その操作による制御手法を提案した。 |
| 先行研究と比べてどこがすごい？ | 従来手法は特定のヘッダを「信号源」として利用するだけだったが、本研究はそれらのヘッダがモデルの出力を動的に制御する「因果的な制御面」であることを初めて特定した。再学習不要で、推論時に特定の領域へ視線を誘導し、出力内容を操作できる点が強力である。 |
| 技術や手法のキモはどこ？ | コミックのコマ割りという空間的な順序を利用し、クエリ（どのコマか）に応じてアテンションが再配置される様子を追跡して「Gaze Heads」を抽出した点。さらに、そのヘッダに対するアテンションマスク介入により、推論中にモデルの記述対象を自由かつ動的に操作する手法。 |
| どうやって有効だと検証した？ | 3,948枚のコミックデータセットを用い、VQAや自由記述生成において、介入したヘッダを操作することで意図した画像領域に関する正確な回答が導き出せるかを評価した。また、COCOデータセットによる自然画像での検証や、複数のVLMアーキテクチャ（Qwen, Ovis, InternVL等）への適用実験を実施した。 |
| 議論はある？ | この機構は、エンコーダーがLMと統合して学習されている場合にのみ機能し、エンコーダーが固定されているモデル（LLaVA等）では機能しにくいという限界がある。また、介入によりモデル性能が向上する一方で、過度な操作はモデルの生成能力を破壊する可能性がある。 |
| 次に読むべき論文は？ | [12] MaskCD: Mitigating lvlm hallucinations by image head masked contrastive decoding, [19] Your large vision-language model only needs a few attention heads for visual grounding, [30] Gaze-vlm: Bridging gaze and vlms through attention regularization for egocentric understanding |
| PDFリンク | https://arxiv.org/pdf/2606.14703v1 |
