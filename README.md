# Japan Construction Cost Database (JCCDB) v2.0

[![DOI](https://img.shields.io/badge/DOI-10.31224%2F7007-blue)](https://doi.org/10.31224/7007)
[![SSRN](https://img.shields.io/badge/SSRN-6738701-orange)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6738701)
[![Zenodo](https://img.shields.io/badge/Zenodo-10.5281%2Fzenodo.20019573-cyan)](https://doi.org/10.5281/zenodo.20019573)
[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/)

## 概要 / Overview

**JCCDB（Japan Construction Cost Database）**は、日本の建設工事に使用される部材・設備・工事項目のスキーマデータベースです。

This is a schema database of materials, equipment, and work items used in Japanese construction projects.

| 項目 | 値 |
|---|---|
| 総品目数 | **65,729品目** |
| カテゴリ数 | **398カテゴリ** |
| 対象工種 | 戸建・マンション・店舗・ホテル・工場 全28工種 |
| データ形式 | JSON / CSV |
| バージョン | v2.0（2026-05-19） |

## ⚠️ 重要事項 / Important Notice

**このリポジトリには価格情報は含まれていません。**
品目名・カテゴリ・単位のみを収録したスキーマデータです。

**This repository contains NO price data.**
Only item names, categories, and units are included.

価格・仕入れ・マージン情報は [HORIZON SHIELD](https://shield.the-horizons-innovation.com) サービスを通じてのみ提供されます。

## ファイル構成 / Files

```
jccdb-v2-schema.json   メインJSONファイル（全65,729品目）
jccdb-v2-schema.csv    CSV形式（Excel等で開けます）
README.md              本ファイル
README_ja.md           日本語詳細版
LICENSE                CC BY-NC 4.0
```

## データ構造 / Data Structure

```json
{
  "_meta": {
    "version": "2.0",
    "total_items": 65729,
    "sha256_schema": "9c59ef1f91393e70...",
    "license": "CC BY-NC 4.0"
  },
  "categories": {
    "カテゴリ名": [
      {"name": "品目名", "unit": "単位"},
      ...
    ]
  }
}
```

## カバレッジ / Coverage

| 工種 | カテゴリ例 |
|---|---|
| 仮設・土工・基礎 | 足場部材・地盤改良・鉄筋・コンクリート |
| 木工事・鉄骨 | 構造材・接合金物・H形鋼・耐火被覆 |
| 内装・仕上げ | クロス・フローリング・タイル・石工事 |
| 設備工事 | 給排水・電気・空調・ガス・弱電 |
| 建具・サッシ | 室内ドア・窓・玄関ドア・内窓 |
| 住宅設備 | キッチン・浴室・トイレ・給湯器 |
| 外構・造園 | フェンス・カーポート・物置・照明 |
| 超高級設備 | サウナ・プール・ホームシアター・EV充電 |
| 店舗・施設 | 消防設備・業務用空調・厨房・什器 |

## 学術論文 / Academic Paper

**JCCDB v1.2 — Cryptographic Audit Hash and Macroeconomic Price Correction for Reproducible LLM-Based Construction Cost Diagnostics**

- SSRN: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6738701
- DOI (engrXiv): https://doi.org/10.31224/7007
- DOI (Zenodo): https://doi.org/10.5281/zenodo.20019573
- ORCID: https://orcid.org/0009-0000-9180-903X
- Bitcoin Anchor: Block #949356
- SHA-256: 9c59ef1f91393e70993ff99ec31c4a902a157bb7642dc0a2323bae923cc2258d

## 著者・運営 / Author

**大賀俊勝（Toshikatsu Oga）**
代表取締役 / The HORIZ音s株式会社
建設実務経験30年・大工→現場監督→CMR→AI engineer

- Web: https://shield.the-horizons-innovation.com
- LINE: @172piime

## ライセンス / License

[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)

**商用利用禁止。帰属表示必須。**
Non-commercial use only. Attribution required.

引用例 / Citation:
```
Oga, T. (2026). JCCDB v2.0: Japan Construction Cost Database Schema.
The HORIZ音s Corporation. https://github.com/ogasurfproject-jpg/japan-construction-cost-database
DOI: 10.31224/7007
```

## 免責事項 / Disclaimer

本データは参考情報です。実際の工事費用は現場条件・時期・地域・施工業者により大きく異なります。
The HORIZ音s株式会社は価格の正確性・完全性を一切保証しません。

This data is for reference purposes only. Actual construction costs vary significantly.
The HORIZ音s Corporation makes no warranty regarding price accuracy or completeness.
