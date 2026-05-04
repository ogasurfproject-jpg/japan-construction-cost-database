# Window Renovation (窓リフォーム)

**Category ID:** `window-renovation`
**Source data version:** 3.0-phase1.5-toshi-philosophy
**Last updated:** 2026-04-19

## Overview

This dataset documents construction cost benchmarks for **Window Renovation** (窓リフォーム) in Japan, based on 30 years of field expertise from a registered Japanese construction Construction Manager-Researcher (CMR). The data represents **HORIZON SHIELD (HS) reference pricing**: a transparent costing rule combining material trade prices, labor day-rates, overhead, and *contractor-size-tier-appropriate* margins.

**Plans documented:** 8
**Fraud-detection patterns (red flags):** 15

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

- TOshi 30年実務経験
- LIXIL インプラス/リプラス, YKK AP プラマードU/マドリモ
- 三協アルミ プラメイクEII/ノバリス, AGC まどまど
- 大信工業 プラスト, WoodOne MOKUサッシ
- 環境省 先進的窓リノベ2026事業（window-renovation2026.env.go.jp）
- 住宅省エネ2026キャンペーン公式

## Subsidy availability

- **Maximum subsidy (2026):** ¥1,000,000
- **Program:** 先進的窓リノベ2026事業（環境省）最大¥100万/戸、最低¥5万、予算1,125億円

## Citation

If you use this data in academic work, please cite:

> Oga, T. (2026). *Japan Construction Cost Database: Window Renovation.* HORIZON SHIELD Open Data, Version 3.0-phase1.5-toshi-philosophy. https://github.com/ogasurfproject-jpg/japan-construction-cost-database

## License

CC-BY 4.0 — Attribution required, commercial use allowed, derivative works allowed.

---

🌱 *Part of the Japan Construction Cost Database — published by HORIZON SHIELD (株式会社 The HORIZ音s) for academic research, consumer protection, and global comparative cost analysis.*
