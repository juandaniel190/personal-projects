# Bark.com — Trading Diagnostic

Trading diagnostic deck analyzing UK & US market performance (H2 2024 vs H2 2025). Interactive HTML deck + written analysis.

**Live Demo**
- 📊 [Interactive Deck](https://juandaniel190.github.io/personal-projects/Bark/Bark_Trading_Diagnostic.html)
- 📄 [Print Version](https://juandaniel190.github.io/personal-projects/Bark/Bark_Trading_Diagnostic_Print.html)

**Quick start**

- Open `Bark_Trading_Diagnostic.html` in a browser (charts load from CDN, no build required).
- For a 7-slide print-friendly version: open `Bark_Trading_Diagnostic_Print.html`, then use **Print to PDF** for a 16:9 landscape deck.
- Read the full written analysis in `docs/Bark_Trading_Diagnostic.md`.

**Layout**

```
Bark/
├── README.md
├── Bark_Trading_Diagnostic.html          ← interactive deck (open in browser)
├── Bark_Trading_Diagnostic_Print.html    ← 7 slides, print to PDF
├── Bark.com — Trading Diagnostic.pdf     ← PDF export
├── images/                               ← chart images (chart1–9.png)
└── docs/
    ├── Bark_Trading_Diagnostic.md        ← full written analysis
    ├── Bark_Trading_Diagnostic.xlsx      ← source data
    ├── build_channel_monthly.py          ← data rebuild script
    ├── channel_monthly_chart_data.js     ← chart data for HTML
    ├── IMAGES.md                         ← optional slide decoration guide
    ├── package.json                      ← NPM config
    └── package-lock.json
```

**Key Findings**

- UK revenue declined 16.7% despite +9.4% traffic growth — driven by collapsing submission rates
- Channel 2 scaled 127.8% in sessions but ROAS fell to near-breakeven (1.28x)
- US Web Design revenue collapsed -48.7% due to structural demand decline
- Motivational Speaking doubled revenue (+113%) through improved monetisation

**Data & Tools**

- **Data period:** July 2024 – December 2025 (H2 comparison)
- **Markets:** UK (core) & US (growth)
- **Categories:** 12 service categories × 3 marketing channels
- **Tech stack:** Recharts (charts), Python + pandas (data processing)

Prepared by Juan Daniel Amézquita | Revenue Operations Partner.
