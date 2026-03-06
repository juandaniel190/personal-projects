# CS Apps — Investment Decision Analysis

**Case Study: Senior Manager, Product Data Analyst — Contentsquare**

Data-driven investment recommendation for Contentsquare’s CS Apps (mobile analytics): acquisition, adoption, and retention analysis. Interactive HTML deck + written analysis.

**Live Demo**

- 📊 [Interactive Deck](https://juandaniel190.github.io/personal-projects/business-cases/Contentsquare/cs_apps_presentation.html)

**Quick start**

- Open `cs_apps_presentation.html` in a browser (React + Tailwind via CDN; keep the `figures/` folder next to it for slide assets).
- Read the full written analysis in `docs/cs_apps_case_study.md`.
- Run the analysis pipeline (optional): from **Contentsquare/** run `python script/cs_apps_analysis.py`, or from **repo root** run `python business-cases/Contentsquare/script/cs_apps_analysis.py`. Requires Python 3 and dependencies (see `script/Analysis.ipynb`). For exploration, open `script/Analysis.ipynb`.

**Layout**

```
Contentsquare/
├── README.md                       ← start here (live demo link above)
├── cs_apps_presentation.html      ← interactive deck (main)
├── figures/                        ← slide images (Sense AI, fig_01–14, etc.)
├── script/                         ← Python & notebooks
│   ├── cs_apps_analysis.py        ← data processing / deck data
│   └── Analysis.ipynb              ← exploratory analysis
├── data/                           ← source data
│   ├── Account Data Case Study Result 1.csv
│   └── User Data Case Study Result 1.csv
├── docs/                           ← written analysis & reference
│   ├── cs_apps_case_study.md       ← full written analysis
│   ├── Case Study Senior Manager Product Data Analyst.pdf
│   └── brand_colors.txt
└── .gitignore
```

**Key findings**

- **Value creation (P1):** Strong — +37% ACV, +30% accounts; CS Apps is gaining wallet share.
- **Value delivery (P2):** Broken — 85% of accounts not live, 71% with zero certified users; adoption is the bottleneck.
- **Value protection (P3):** At risk — health metric is unreliable; $16M+ Q4 renewals with many accounts having no CS Apps adoption to justify renewal.

**Recommendation:** Increase investment — conditionally. Focus on implementation and adoption before renewals, not only on growth.

**Data & tools**

- **Scope:** CS Apps–contracted accounts only (ACV, health, implementation, certification).
- **Tech:** React (deck), Python + pandas (analysis), Jupyter (exploration).

Prepared by Juan Daniel Amézquita · Product & Data Analysis.
