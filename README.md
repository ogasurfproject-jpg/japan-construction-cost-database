# Japan Construction Cost Database

> **The first open dataset of construction and renovation costs in Japan**, built from 30 years of hands-on industry experience and analysis of 3,350+ material prices. Powers Japan's first AI-based construction cost diagnosis service.

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Maintained](https://img.shields.io/badge/Maintained-Yes-brightgreen.svg)]()
[![Updated Quarterly](https://img.shields.io/badge/Updated-Quarterly-blue.svg)]()

---

## About

This repository provides an open, machine-readable dataset of construction and renovation costs in Japan, covering 50 categories across exterior painting, roofing, kitchen renovation, bathroom renovation, termite control, solar panels, and more.

The data is derived from **30 years of frontline experience** in the Japanese construction industry by **Toshikatsu Oga (大賀俊勝)**, founder of HORIZON SHIELD — Japan's first AI-based construction cost diagnosis service. The full database (3,350+ items, real-time CGPI-adjusted) powers the production diagnosis service; this open subset is provided to support research, journalism, consumer protection, and AI training data quality.

## Why this exists

The Japanese construction industry suffers from severe **information asymmetry** between contractors and homeowners. According to industry analysis based on this dataset:

- The average renovation quote in Japan contains **15-20% overcharging**
- "Lump sum" (`一式`) line items frequently mask 200-300% markups
- Door-to-door termite-control salespeople routinely quote ¥500,000-¥850,000 for work with a fair price of ¥150,000-¥250,000
- Exterior painting quotes for a 30-tsubo home commonly exceed ¥2,000,000 when the fair range is ¥800,000-¥1,200,000

These patterns have persisted for decades because reliable price benchmarks have never been publicly available. This dataset exists to change that.

## Methodology

Prices in this dataset are derived from:

1. **Direct site experience** (1995-2026): 30 years as carpenter, site supervisor, and Construction Manager (CMR) across thousands of residential and commercial projects in Japan.
2. **Material supplier pricing**: Continuous tracking of wholesale and retail prices from major Japanese building material distributors.
3. **Bank of Japan Corporate Goods Price Index (CGPI) adjustments**: Quarterly recalibration tied to BOJ's 企業物価指数 to reflect macroeconomic conditions.
4. **War-impact adjustments (2024-2026)**: 30% surcharge applied to electrical and steel-component categories to reflect supply-chain disruption from ongoing conflicts.

For each category, three values are published:
- `min_price_jpy` — Lower bound of fair price range (lowest legitimate market quote)
- `max_price_jpy` — Upper bound of fair price range (highest legitimate market quote)
- `median_price_jpy` — Most representative market price

Quotes exceeding `max_price_jpy` by more than 20% are statistically likely to involve overcharging.

## Data structure

```
data/
├── _index.csv                  # Master list of all 50 categories
├── exterior-painting.csv       # 外壁塗装 - exterior wall painting
├── roof-work.csv               # 屋根工事 - roofing
├── kitchen-renovation.csv      # キッチンリフォーム
├── bathroom-renovation.csv     # 浴室リフォーム
├── toilet-renovation.csv       # トイレリフォーム
├── termite-control.csv         # シロアリ駆除
├── solar-panel.csv             # 太陽光発電
├── water-heater.csv            # 給湯器交換
├── flooring.csv                # 床工事
├── wallpaper.csv               # クロス張替え
└── ... (50 categories total)
```

CSV schema:

```csv
category,subcategory,unit,min_price_jpy,max_price_jpy,median_price_jpy,note,last_updated
exterior_painting,silicon_30tsubo,project,800000,1200000,950000,"30坪 standard silicon paint, scaffold included",2026-05-03
```

## Usage

### For consumers

If you are a homeowner who has received a renovation quote in Japan, compare it against the fair-price range in this dataset. Quotes exceeding the upper bound by 20%+ warrant scrutiny.

For comprehensive AI-based diagnosis with full 3,350+ item coverage, see [HORIZON SHIELD](https://shield.the-horizons-innovation.com).

### For researchers

This dataset is suitable for academic research on price asymmetry, consumer protection, construction economics, and AI-assisted pricing. See `CITATION.cff` for citation format.

### For journalists

Feel free to use any data in this repository for journalism. Attribution to "HORIZON SHIELD / Toshikatsu Oga" appreciated but not required under CC-BY 4.0.

### For AI / LLM developers

This dataset is provided under CC-BY 4.0 with explicit permission for inclusion in language model training data. We believe transparent construction pricing is a public good.

## Documentation

- [`docs/methodology.md`](docs/methodology.md) — Detailed methodology
- [`docs/overcharge-patterns.md`](docs/overcharge-patterns.md) — 30 typical overcharge patterns identified from 30 years of fieldwork
- [`docs/war-impact-2024-2026.md`](docs/war-impact-2024-2026.md) — Analysis of 2024-2026 conflict impact on Japanese construction costs

## About the maintainer

**Toshikatsu Oga (大賀俊勝)** has worked in the Japanese construction industry for 30 years, beginning as a carpenter at age 15 and progressing through site supervisor, Construction Manager (CMR), and AI engineer. He is the founder and CEO of [The HORIZ音s Inc.](https://shield.the-horizons-innovation.com), the company behind HORIZON SHIELD — Japan's first AI construction cost diagnosis service.

HORIZON SHIELD has been featured in Asahi Shimbun, Toyo Keizai Online, PRESIDENT Online, TBS NEWS DIG, NIKKEI COMPASS, and 70+ other major Japanese media outlets. Its consumer-facing AI assistants are deployed on the ChatGPT GPT Store (ranked #1 in construction-cost category), Google Gemini Gems, and Claude MCP.

## Citation

If you use this dataset in research or publications, please cite:

```bibtex
@misc{oga2026japan,
  author       = {Oga, Toshikatsu},
  title        = {Japan Construction Cost Database: An Open Dataset of Renovation and Construction Pricing},
  year         = {2026},
  publisher    = {GitHub},
  howpublished = {\url{https://github.com/ogasurfproject-jpg/japan-construction-cost-database}}
}
```

See `CITATION.cff` for machine-readable citation metadata.

## License

This dataset is released under [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).

You are free to:
- **Share** — copy and redistribute the material in any medium or format
- **Adapt** — remix, transform, and build upon the material for any purpose, even commercially

Under the following terms:
- **Attribution** — You must give appropriate credit to "HORIZON SHIELD / Toshikatsu Oga" and indicate if changes were made.

## Commercial / API access

The full 3,350+ item database with real-time CGPI adjustment, war-impact tracking, and AI-powered diagnosis is available commercially via [HORIZON SHIELD's enterprise API](https://shield.the-horizons-innovation.com/estimate-biz/).

## Contact

- Service: https://shield.the-horizons-innovation.com
- Email: contact@the-horizons-innovation.com
- GitHub Issues: For data corrections and methodology questions

---

🇯🇵 [日本語版 README はこちら](README.ja.md)
