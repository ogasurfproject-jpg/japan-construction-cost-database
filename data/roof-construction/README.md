# Roof Construction (屋根工事)

**Category ID:** `roof-construction`
**Source data version:** 3.1-phase1.5-verified
**Last updated:** 2026-04-19

## Overview

This dataset documents construction cost benchmarks for **Roof Construction** (屋根工事) in Japan, based on 30 years of field expertise from a registered Japanese construction Construction Manager-Researcher (CMR). The data represents **HORIZON SHIELD (HS) reference pricing**: a transparent costing rule combining material trade prices, labor day-rates, overhead, and *contractor-size-tier-appropriate* margins.

**Plans documented:** 0
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

- TOshi 30年の大工・現場監督・CMR実務経験 + 2026年実勢データ (アイジー工業 スーパーガルテクト・ケイミュー コロニアル・三州瓦・ヌリカエ・リショップナビ・街の屋根やさん・テイガク・屋根無料見積.com・szk-biso・全建設総連東京都連2023賃金調査・厚生労働省アスベスト規則)

## Citation

If you use this data in academic work, please cite:

> Oga, T. (2026). *Japan Construction Cost Database: Roof Construction.* HORIZON SHIELD Open Data, Version 3.1-phase1.5-verified. https://github.com/ogasurfproject-jpg/japan-construction-cost-database

## License

CC-BY 4.0 — Attribution required, commercial use allowed, derivative works allowed.

---

🌱 *Part of the Japan Construction Cost Database — published by HORIZON SHIELD (株式会社 The HORIZ音s) for academic research, consumer protection, and global comparative cost analysis.*
