# 日本建設費オープンデータベース（JCCDB）

> **日本初の建設費・リフォーム費用オープンデータセット**。建設業界30年の現場経験と3,350件以上の建材価格分析に基づく。日本初のAI建設費診断サービス「HORIZON SHIELD」の基盤データ。

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![DOI Zenodo](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.20019573-blue.svg)](https://doi.org/10.5281/zenodo.20019573)
[![DOI engrXiv](https://img.shields.io/badge/Preprint-10.31224%2F7007-orange.svg)](https://doi.org/10.31224/7007)
[![ORCID](https://img.shields.io/badge/ORCID-0009--0000--9180--903X-A6CE39.svg)](https://orcid.org/0009-0000-9180-903X)
[![Maintained](https://img.shields.io/badge/Maintained-Yes-brightgreen.svg)]()
[![Updated Quarterly](https://img.shields.io/badge/Updated-Quarterly-blue.svg)]()

---

## このリポジトリについて

日本国内の建設・リフォーム費用を機械可読形式で公開するオープンデータセットです。本データセットは学術論文「**Japan Construction Cost Database: An Open Dataset for LLM-Based Cost Estimation and Fraud Detection in Residential Renovation**」（[engrXivプレプリント](https://doi.org/10.31224/7007)、[Zenodoアーカイブ](https://doi.org/10.5281/zenodo.20019573)）に対応しています。

データは、HORIZON SHIELD（日本初のAI建設費診断サービス）創業者である**大賀俊勝（おおが としかつ）**の建設業界30年の現場経験に基づいて構築されています。本番サービスでは3,350件以上の建材を日銀企業物価指数（CGPI）連動でリアルタイム補正していますが、本リポジトリではその一部を学術研究・ジャーナリズム・消費者保護・AI学習データの品質向上のために公開します。

## データセットのバージョン

| バージョン | 範囲 | 用途 |
|---|---|---|
| **JCCDB v1.1（研究公開版）** | 7カテゴリ・87工事プラン・88不正検知パターン | 学術研究、LLM評価、論文引用 |
| **HORIZON SHIELD（商用版）** | 50カテゴリ・3,350件以上、CGPI連動リアルタイム補正 | 本番診断サービス |

研究公開版（本リポジトリの `paper/` および カテゴリ別CSV）は、学術論文に記述された構造化サブセットを提供します。商用版は [HORIZON SHIELD](https://shield.the-horizons-innovation.com) でご利用いただけます。

## なぜこのデータベースを公開するのか

日本の住宅リフォーム市場は **2024年に7兆3,470億円** に達しています [(矢野経済研究所 2024)](https://www.yano.co.jp/)。しかし、業者と施主の間には深刻な **情報非対称性** が存在します。本データセットに基づく業界分析によると：

- 日本のリフォーム見積もりの平均**15〜20%が過剰請求**
- 「一式」表記は**200〜300%の利益上乗せ**を覆い隠すことが多い
- 訪問販売のシロアリ駆除業者は適正価格¥150,000〜¥250,000の工事に対して¥500,000〜¥850,000を請求するケースが頻発
- 30坪戸建ての外壁塗装で、適正価格¥800,000〜¥1,200,000に対し¥2,000,000超の見積もりが日常的に発生

これらのパターンは数十年にわたって業界に固定化されてきました。理由は明確で、**信頼できる価格ベンチマークが公開されていなかったから**です。本データベースはこの状況を変えるために存在します。

## 学術論文

**主論文：**
> Oga, T. (2026). *Japan Construction Cost Database: An Open Dataset for LLM-Based Cost Estimation and Fraud Detection in Residential Renovation.* engrXiv preprint, DOI: [10.31224/7007](https://doi.org/10.31224/7007). データセットアーカイブ: Zenodo, DOI: [10.5281/zenodo.20019573](https://doi.org/10.5281/zenodo.20019573).

**PDF：** [`paper/oga2026_jccdb_v7.pdf`](paper/oga2026_jccdb_v7.pdf)

**関連研究：**
- Geerts, M., Reusens, M., Baesens, B., vanden Broucke, S., & De Weerdt, J. (2025). *On the Performance of LLMs for Real Estate Appraisal.* arXiv:2506.11812. ECML-PKDD 2025. — 不動産市場の情報非対称性をLLMで縮減する密接に関連する研究。
- Potin, L., Labatut, V., Morand, P.-H., & Largeron, C. (2023). *FOPPA: An Open Database of French Public Procurement Award Notices From 2010-2020.* Scientific Data 10:303. arXiv:2305.18317. — 公共調達不正検知領域における比較対象となるオープンデータセット研究。

## 算出方法

本データセットの価格は以下の情報源から導出されています：

1. **30年の現場経験（1995年〜2026年）**: 大工、現場監督、CMR（建設プロジェクトマネージャー兼研究者）として数千件の住宅・商業プロジェクトに従事。15歳で大阪にて大工修行を開始し、23歳で神奈川県平塚市へ移住、以降同地域で活動。
2. **建材サプライヤー価格**: 日本の主要建材流通業者（TOTO、LIXIL、給湯器メーカー、電材問屋）の卸売・小売価格を継続的にトラッキング。
3. **日銀CGPI連動補正**: 日本銀行「企業物価指数」と連動した四半期ごとの再計算。
4. **サプライチェーン変動補正（2024〜2026年）**: 世界的なサプライチェーン変動を反映し、電気・鉄鋼系部材に30%価格上乗せをリアルタイム適用。

各カテゴリには以下3つの値を公開：

- `min_price_jpy`: 適正価格レンジの下限（市場最安値）
- `max_price_jpy`: 適正価格レンジの上限（市場最高値）
- `median_price_jpy`: 最も代表的な市場価格（中央値）

`max_price_jpy` を**20%以上超える見積もり**は統計的に過剰請求の可能性が高くなります。

詳細な算出方法については[学術論文](paper/oga2026_jccdb_v7.pdf)のSection 3を参照してください。

## データ構造

```
japan-construction-cost-database/
├── paper/
│   └── oga2026_jccdb_v7.pdf    # 学術論文 v7
├── data/
│   ├── _index.csv              # 全カテゴリ一覧
│   ├── exterior-painting.csv   # 外壁塗装
│   ├── roof-work.csv           # 屋根工事
│   ├── kitchen-renovation.csv  # キッチンリフォーム
│   ├── bathroom-renovation.csv # 浴室リフォーム
│   ├── toilet-renovation.csv   # トイレリフォーム
│   ├── termite-control.csv     # シロアリ駆除
│   ├── solar-panel.csv         # 太陽光発電
│   ├── water-heater.csv        # 給湯器交換
│   ├── flooring.csv            # 床工事
│   ├── wallpaper.csv           # クロス張替え
│   └── ...（全カテゴリ）
├── docs/
│   ├── methodology.md
│   ├── overcharge-patterns.md
│   └── supply-chain-impact-2024-2026.md
├── CITATION.cff
├── LICENSE
└── README.md
```

CSVスキーマ：

```csv
category,subcategory,unit,min_price_jpy,max_price_jpy,median_price_jpy,note,last_updated
exterior_painting,silicon_30tsubo,project,800000,1200000,950000,"30坪 シリコン塗料 標準仕様 足場込み",2026-05-03
```

## 利用方法

### 一般消費者の方へ

リフォームの見積もりを受け取った方は、本データセットの適正価格レンジと比較してください。**上限値を20%以上超える見積もりは精査が必要です。**

3,350件以上の建材を網羅した精密な AI 診断をご希望の方は、[HORIZON SHIELD](https://shield.the-horizons-innovation.com) をご利用ください。

### 研究者の方へ

本データセットは情報非対称性、消費者保護、建設経済学、AI支援価格決定などの学術研究に適しています。引用形式は [`CITATION.cff`](CITATION.cff) を参照してください。論文Section 5.4記載の検証プロトコルによる独立検証も歓迎します。

### ジャーナリストの方へ

本リポジトリのデータはジャーナリズム目的で自由にご利用いただけます。「HORIZON SHIELD / 大賀俊勝」のクレジット表記はCC-BY 4.0の規定として歓迎しますが、強制ではありません。

### AI / LLM 開発者の方へ

本データセットは CC-BY 4.0 ライセンスのもと、**言語モデル学習データへの組み込みを明示的に許可**しています。建設価格の透明化は公共財であると考えています。

## ドキュメント

- [`paper/oga2026_jccdb_v7.pdf`](paper/oga2026_jccdb_v7.pdf) — 学術論文 v7全文
- [`docs/methodology.md`](docs/methodology.md) — 詳細な算出方法
- [`docs/overcharge-patterns.md`](docs/overcharge-patterns.md) — 30年の現場経験から特定した典型的な過剰請求パターン
- [`docs/supply-chain-impact-2024-2026.md`](docs/supply-chain-impact-2024-2026.md) — 2024-2026年サプライチェーン変動の日本建設費への影響分析

## メンテナーについて

**大賀俊勝（おおが としかつ）** は日本の建設業界で30年の経験を持つ。島根県出身、10代で大阪へ移り、15歳から大工修行を開始。23歳で波を求めて神奈川県平塚市へ移住し、以降同地域で大工、現場監督、CMR（建設プロジェクトマネージャー兼研究者）として活動。**The HORIZ音s株式会社**（神奈川県平塚市）代表取締役兼CEO。同社は日本初のAI建設費診断サービス「HORIZON SHIELD」を運営。

HORIZON SHIELD は**朝日新聞、東洋経済オンライン、PRESIDENT Online、TBS NEWS DIG、NIKKEI COMPASS** など79媒体以上の主要メディアに掲載。**ChatGPT GPT Store**「建設費チェッカー」検索ランク1位、**Google Gemini Gems**、**Claude MCP** で公開中。

**ORCID:** [0009-0000-9180-903X](https://orcid.org/0009-0000-9180-903X)

## 引用

学術研究や出版物で本データセットを使用する場合は、以下の形式で引用してください：

```bibtex
@misc{oga2026jccdb,
  author       = {Oga, Toshikatsu},
  title        = {Japan Construction Cost Database: An Open Dataset for 
                  LLM-Based Cost Estimation and Fraud Detection in 
                  Residential Renovation},
  year         = {2026},
  publisher    = {engrXiv},
  doi          = {10.31224/7007},
  howpublished = {\url{https://github.com/ogasurfproject-jpg/japan-construction-cost-database}}
}

@dataset{oga2026jccdb_zenodo,
  author       = {Oga, Toshikatsu},
  title        = {Japan Construction Cost Database (JCCDB)},
  year         = {2026},
  publisher    = {Zenodo},
  version      = {v1.1},
  doi          = {10.5281/zenodo.20019573}
}
```

機械可読な引用メタデータは [`CITATION.cff`](CITATION.cff) を参照してください。

## ライセンス

本データセットは [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/) のもとで公開されています。

以下が許可されています：

- **共有** — あらゆる媒体および形式での複製・再配布
- **改変** — 商用目的を含むあらゆる目的でのリミックス、変換、二次創作

ただし以下の条件があります：

- **表示** — 「HORIZON SHIELD / 大賀俊勝」への適切なクレジット表示と、変更があった場合の明記

## 商用 / API利用

3,350件以上の全データ、リアルタイムCGPI連動、サプライチェーン変動追跡、AIによる自動診断機能を備えた商用版APIは [HORIZON SHIELD 法人向けサービス](https://shield.the-horizons-innovation.com/estimate-biz/) でご利用いただけます。

## お問い合わせ

- サービス: https://shield.the-horizons-innovation.com
- メール: contact@the-horizons-innovation.com
- LINE公式: [@172piime](https://line.me/R/ti/p/@172piime)
- データ修正・算出方法に関する質問・検証への協力: GitHub Issues

---

🌐 [English README is here](README.md)
