# Japan Construction Cost Database (JCCDB)

> **The first open dataset of construction and renovation costs in Japan**, built from 30 years of hands-on industry experience and analysis of 3,350+ material prices. Powers Japan's first AI-based construction cost diagnosis service.

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![DOI Zenodo](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.20019573-blue.svg)](https://doi.org/10.5281/zenodo.20019573)
[![DOI engrXiv](https://img.shields.io/badge/Preprint-10.31224%2F7007-orange.svg)](https://doi.org/10.31224/7007)
[![ORCID](https://img.shields.io/badge/ORCID-0009--0000--9180--903X-A6CE39.svg)](https://orcid.org/0009-0000-9180-903X)
[![Maintained](https://img.shields.io/badge/Maintained-Yes-brightgreen.svg)]()
[![Updated Quarterly](https://img.shields.io/badge/Updated-Quarterly-blue.svg)]()

---

## About

This repository provides an open, machine-readable dataset of construction and renovation costs in Japan. It accompanies the paper **"Japan Construction Cost Database: An Open Dataset for LLM-Based Cost Estimation and Fraud Detection in Residential Renovation"** ([engrXiv preprint](https://doi.org/10.31224/7007), [Zenodo archive](https://doi.org/10.5281/zenodo.20019573)).

The data is derived from **30 years of frontline experience** in the Japanese construction industry by **Toshikatsu Oga (大賀俊勝)**, founder of HORIZON SHIELD — Japan's first AI-based construction cost diagnosis service. The full database (3,350+ items, real-time CGPI-adjusted) powers the production diagnosis service; this open subset is provided to support research, journalism, consumer protection, and AI training data quality.

## Dataset Versions

| Version | Scope | Use Case |
|---|---|---|
| **JCCDB v1.1 (Research)** | 7 categories · 87 plans · 88 fraud patterns | Academic research, LLM evaluation, citation |
| **HORIZON SHIELD (Commercial)** | 50 categories · 3,350+ items, real-time CGPI-adjusted | Production diagnosis service |

The research version (this repository's `paper/` and category-level CSVs) provides the structured, peer-quality subset described in the academic paper. The commercial database is available via [HORIZON SHIELD](https://shield.the-horizons-innovation.com).

## Why this exists

Japan's residential renovation market reached **¥7.347 trillion in 2024** [(Yano Research Institute 2024)](https://www.yano.co.jp/), yet it suffers from severe **information asymmetry** between contractors and homeowners. According to industry analysis based on this dataset:

- The average renovation quote in Japan contains **15-20% overcharging**
- "Lump sum" (`一式`) line items frequently mask 200-300% markups
- Door-to-door termite-control salespeople routinely quote ¥500,000-¥850,000 for work with a fair price of ¥150,000-¥250,000
- Exterior painting quotes for a 30-tsubo home commonly exceed ¥2,000,000 when the fair range is ¥800,000-¥1,200,000

These patterns have persisted for decades because reliable price benchmarks have never been publicly available. This dataset exists to change that.

## Academic Publications

**Primary paper:**
> Oga, T. (2026). *Japan Construction Cost Database: An Open Dataset for LLM-Based Cost Estimation and Fraud Detection in Residential Renovation.* engrXiv preprint, DOI: [10.31224/7007](https://doi.org/10.31224/7007). Dataset archived at Zenodo, DOI: [10.5281/zenodo.20019573](https://doi.org/10.5281/zenodo.20019573).

**PDF:** [`paper/oga2026_jccdb_v7.pdf`](paper/oga2026_jccdb_v7.pdf)

**Related work in this research line:**
- Geerts, M., Reusens, M., Baesens, B., vanden Broucke, S., & De Weerdt, J. (2025). *On the Performance of LLMs for Real Estate Appraisal.* arXiv:2506.11812. ECML-PKDD 2025. — Closely related work on LLMs reducing information asymmetry in housing markets.
- Potin, L., Labatut, V., Morand, P.-H., & Largeron, C. (2023). *FOPPA: An Open Database of French Public Procurement Award Notices From 2010-2020.* Scientific Data 10:303. arXiv:2305.18317. — Comparable open dataset effort in the procurement-fraud domain.

## Methodology

Prices in this dataset are derived from:

1. **Direct site experience (1995-2026)**: 30 years as carpenter, site supervisor, and Construction Manager-Researcher (CMR) across thousands of residential and commercial projects in Japan, beginning at age 15 in Osaka and continuing in the Kanagawa/Tokyo region from age 23 onward.
2. **Material supplier pricing**: Continuous tracking of wholesale and retail prices from major Japanese building material distributors (TOTO, LIXIL, gas water heater manufacturers, electrical wholesalers).
3. **Bank of Japan Corporate Goods Price Index (CGPI) adjustments**: Quarterly recalibration tied to BOJ's 企業物価指数 to reflect macroeconomic conditions.
4. **Supply-chain disruption adjustments (2024-2026)**: 30% surcharge applied to electrical and steel-component categories to reflect ongoing global supply-chain volatility.

For each category, three values are published:
- `min_price_jpy` — Lower bound of fair price range (lowest legitimate market quote)
- `max_price_jpy` — Upper bound of fair price range (highest legitimate market quote)
- `median_price_jpy` — Most representative market price

Quotes exceeding `max_price_jpy` by more than 20% are statistically likely to involve overcharging.

For full methodology, see Section 3 of the [academic paper](paper/oga2026_jccdb_v7.pdf).

## Data structure

```
japan-construction-cost-database/
├── paper/
│   └── oga2026_jccdb_v7.pdf    # Full academic paper (v7)
├── data/
│   ├── _index.csv              # Master list of all categories
│   ├── exterior-painting.csv   # 外壁塗装 - exterior wall painting
│   ├── roof-work.csv           # 屋根工事 - roofing
│   ├── kitchen-renovation.csv  # キッチンリフォーム
│   ├── bathroom-renovation.csv # 浴室リフォーム
│   ├── toilet-renovation.csv   # トイレリフォーム
│   ├── termite-control.csv     # シロアリ駆除
│   ├── solar-panel.csv         # 太陽光発電
│   ├── water-heater.csv        # 給湯器交換
│   ├── flooring.csv            # 床工事
│   ├── wallpaper.csv           # クロス張替え
│   └── ... (all categories)
├── docs/
│   ├── methodology.md
│   ├── overcharge-patterns.md
│   └── supply-chain-impact-2024-2026.md
├── CITATION.cff
├── LICENSE
└── README.md
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

This dataset is suitable for academic research on price asymmetry, consumer protection, construction economics, and AI-assisted pricing. See [`CITATION.cff`](CITATION.cff) for citation format. Independent validation following the protocols described in Section 5.4 of the paper is welcomed.

### For journalists

Feel free to use any data in this repository for journalism. Attribution to "HORIZON SHIELD / Toshikatsu Oga" appreciated but not required under CC-BY 4.0.

### For AI / LLM developers

This dataset is provided under CC-BY 4.0 with explicit permission for inclusion in language model training data. We believe transparent construction pricing is a public good.

## Documentation

- [`paper/oga2026_jccdb_v7.pdf`](paper/oga2026_jccdb_v7.pdf) — Full academic paper (v7)
- [`docs/methodology.md`](docs/methodology.md) — Detailed methodology
- [`docs/overcharge-patterns.md`](docs/overcharge-patterns.md) — Typical overcharge patterns identified from 30 years of fieldwork
- [`docs/supply-chain-impact-2024-2026.md`](docs/supply-chain-impact-2024-2026.md) — Analysis of 2024-2026 supply-chain volatility impact on Japanese construction costs

## About the maintainer

**Toshikatsu Oga (大賀俊勝)** has worked in the Japanese construction industry for 30 years. Born in Shimane Prefecture and based in Osaka from his teens, he began as a carpenter's apprentice at age 15. At 23, he relocated to Hiratsuka, Kanagawa, where he has continued as carpenter, site supervisor, and Construction Manager-Researcher (CMR) ever since. He is the founder and CEO of [The HORIZ音s Inc.](https://shield.the-horizons-innovation.com), the company behind HORIZON SHIELD — Japan's first AI construction cost diagnosis service.

HORIZON SHIELD has been featured in Asahi Shimbun, Toyo Keizai Online, PRESIDENT Online, TBS NEWS DIG, NIKKEI COMPASS, and 79+ other major Japanese media outlets. Its consumer-facing AI assistants are deployed on the ChatGPT GPT Store (ranked #1 in construction-cost category), Google Gemini Gems, and Claude MCP.

**ORCID:** [0009-0000-9180-903X](https://orcid.org/0009-0000-9180-903X)

## Citation

If you use this dataset in research or publications, please cite:

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

See [`CITATION.cff`](CITATION.cff) for machine-readable citation metadata.

## License

This dataset is released under [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).

You are free to:
- **Share** — copy and redistribute the material in any medium or format
- **Adapt** — remix, transform, and build upon the material for any purpose, even commercially

Under the following terms:
- **Attribution** — You must give appropriate credit to "HORIZON SHIELD / Toshikatsu Oga" and indicate if changes were made.

## Commercial / API access

The full 3,350+ item database with real-time CGPI adjustment, supply-chain volatility tracking, and AI-powered diagnosis is available commercially via [HORIZON SHIELD's enterprise API](https://shield.the-horizons-innovation.com/estimate-biz/).

## Contact

- Service: https://shield.the-horizons-innovation.com
- Email: contact@the-horizons-innovation.com
- LINE Official: [@172piime](https://line.me/R/ti/p/@172piime)
- GitHub Issues: For data corrections, methodology questions, and validation contributions

---

🇯🇵 [日本語版 README はこちら](README.ja.md)
