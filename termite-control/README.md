# Termite Control (シロアリ駆除)

**Category ID:** `termite-control`
**Source data version:** 1.3
**Last updated:** 2026-04-19

## Overview

This dataset documents construction cost benchmarks for **Termite Control** (シロアリ駆除) in Japan, based on 30 years of field expertise from a registered Japanese construction Construction Manager-Researcher (CMR). The data represents **HORIZON SHIELD (HS) reference pricing**: a transparent costing rule combining material trade prices, labor day-rates, overhead, and *contractor-size-tier-appropriate* margins.

**Plans documented:** 13
**Fraud-detection patterns (red flags):** 13

## Files

- `plans.csv` — Plan-level pricing in English (recommended for academic citation)
- `plans_ja.csv` — Same data with original Japanese labels
- `red_flags.csv` — Fraud-detection patterns specific to this category

## Pricing Methodology

The **HS rule price** (`hs_rule_jpy`) is computed as:

```
hs_rule_jpy = (material_trade_price × 1.2)
            + (labor_man_days × prevailing_day_rate)
            + auxiliary_costs
            + (subtotal × overhead_rate)
            + tax (10% Japan consumption tax)
```

Each plan is then translated into **four contractor-size tiers** with empirically derived margin ranges from Japan's Ministry of Land, Infrastructure, Transport and Tourism (MLIT) construction industry analysis:

| Tier | Description | Margin range |
|------|-------------|---------------|
| 1 | Sole proprietor / local specialist | 25–35% |
| 2 | Small-mid local contractor | 25–35% |
| 3 | Premium specialist (brand-recognized) | 30–40% |
| 4 | Major national chain | 35–45% |

See [`../../METHODOLOGY.md`](../../METHODOLOGY.md) for full derivation.

## Data sources

- TOshi 30年大工・現場監督実務
- 公益社団法人 日本しろあり対策協会（JTCCA）公式
- 国民生活センター 消費生活センター情報
- JIS A 4703 木材保存剤の防蟻効力試験方法
- アサンテ・アリプロ・シロアリ110番等業界大手実績データ

## Citation

If you use this data in academic work, please cite:

> Oga, T. (2026). *Japan Construction Cost Database: Termite Control.* HORIZON SHIELD Open Data, Version 1.3. https://github.com/ogasurfproject-jpg/japan-construction-cost-database

## License

CC-BY 4.0 — Attribution required, commercial use allowed, derivative works allowed.

---

🌱 *Part of the Japan Construction Cost Database — published by HORIZON SHIELD (株式会社 The HORIZ音s) for academic research, consumer protection, and global comparative cost analysis.*
