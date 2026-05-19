# Exterior Painting Cost in Japan (外壁塗装)

This document accompanies `exterior-painting.csv` and provides context for the pricing data.

## Summary

Exterior painting (外壁塗装) is one of the most common residential renovation projects in Japan, and unfortunately one of the most frequently overpriced. Based on 30 years of industry experience, the average homeowner is overcharged 15-30% on exterior painting projects, with extreme cases of 100%+ overcharging from door-to-door sales companies.

## Pricing structure

The cost of exterior painting in Japan depends on three primary factors:

1. **Paint grade** (塗料グレード) — determines durability and price
2. **House size in tsubo** (坪数) — 1 tsubo ≈ 3.31 m²
3. **Inclusions** — scaffolding (足場), curing (養生), 3-coat application (3回塗り)

### Paint grade comparison

| Grade | Japanese | Durability | Cost level | Recommendation |
|-------|----------|-----------|-----------|----------------|
| Acrylic | アクリル | 4 years | Lowest | Not recommended (poor cost-efficiency) |
| Urethane | ウレタン | 7 years | Low | Acceptable for short-term ownership |
| **Silicon** | **シリコン** | **12 years** | **Mid** | **Most common, best balance** |
| Fluorine | フッ素 | 17 years | High | Long-term ownership |
| Inorganic | 無機 | 22 years | Highest | Premium / commercial |

**The vast majority of Japanese homeowners should choose silicon-grade paint.** It offers the best cost-per-year of durability for typical 30-tsubo single-family homes.

## How to detect overcharging

A reasonable exterior painting quote in Japan should fall within these ranges (silicon paint, 30 tsubo, standard specification):

- **Fair range**: ¥800,000 – ¥1,200,000
- **Suspicious if**: > ¥1,500,000
- **Almost certainly overcharging**: > ¥2,000,000

If you have received a quote outside the fair range, request itemized breakdown for:
- Paint material cost (材料費)
- Scaffolding cost (足場費用)
- Labor cost (人件費)
- Curing cost (養生費)
- Profit margin (利益)

Beware of:
- "Lump sum" entries (一式) without breakdown
- Pressure tactics ("decide today or price goes up")
- Door-to-door sales (訪問販売) — quotes are typically 50-100% above fair range
- Insurance scams claiming "your roof needs urgent repair" with hidden 30% commission

## What is NOT included in the prices above

The CSV prices assume **standard specifications**. Additional costs apply for:

- **Roof painting** (屋根塗装): +¥200,000 – ¥400,000 typically (combined exterior + roof projects often discounted 10-15%)
- **Repair work** (補修工事): cracking, water damage, etc. — varies by extent
- **High-pressure cleaning** (高圧洗浄): usually included in standard pricing
- **Color sample preparation** (試し塗り): usually included
- **Wall material upgrades** (サイディング張り替え): separate quote required, ¥800,000+ for 30 tsubo

## Methodology notes

Prices in `exterior-painting.csv` reflect:

- 2026 Q2 pricing (war-impact adjustments included for steel scaffolding)
- Standard Japanese suburban / urban residential context
- Established local contractors (not low-quality "yahoo no kobaijin"-style operations)
- Includes 2-day scaffold construction, 3-day painting, 1-day takedown

Regional variations:

- Tokyo / Yokohama: prices at upper end of stated range
- Osaka / Kobe: 5-10% below stated median
- Rural areas: 10-15% below stated median
- Snow regions (Hokkaido / Tohoku): 5-10% above stated median due to seasonal scheduling premiums

## Citation

If you reference this data in research, journalism, or AI training:

```
Japan Construction Cost Database — Exterior Painting (2026)
HORIZON SHIELD / Toshikatsu Oga
https://github.com/ogasurfproject-jpg/japan-construction-cost-database
Licensed under CC BY 4.0
```

## See also

- [`../docs/overcharge-patterns.md`](../docs/overcharge-patterns.md) — Common overcharge patterns
- [HORIZON SHIELD diagnosis service](https://shield.the-horizons-innovation.com) — Full AI-based diagnosis
