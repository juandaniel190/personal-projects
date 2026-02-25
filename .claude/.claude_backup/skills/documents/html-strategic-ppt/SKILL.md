---
name: html-strategic-ppt
description: "Create a strategic, McKinsey-style interactive presentation as a standalone HTML file using React, Recharts, and Tailwind. Produces a single self-contained file the user can open in any browser — no server required."
---

# HTML Strategic Presentation Skill

This skill produces a **single self-contained HTML file** that works as an interactive slide deck. The user double-clicks the file to open it in any browser — no dependencies, no build step, no localhost.

---

## 1. Architecture — Single-File HTML with React + Recharts

The HTML file loads everything from CDNs and uses Babel in-browser transpilation. This is the proven stack:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>[Presentation Title]</title>
  <link href="https://fonts.googleapis.com/css2?family=Lato:wght@400;700;900&display=swap" rel="stylesheet" />
  <script src="https://cdn.tailwindcss.com"></script>
  <script crossorigin src="https://unpkg.com/react@18/umd/react.development.js"></script>
  <script crossorigin src="https://unpkg.com/react-dom@18/umd/react-dom.development.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/prop-types@15.8.1/prop-types.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/recharts@2.0.0/umd/Recharts.min.js"></script>
  <script src="https://unpkg.com/@babel/standalone@7.23.0/babel.min.js"></script>
</head>
<body>
  <div id="root"></div>
  <script type="text/babel" data-presets="react">
    const { useState } = React;
    const { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer, Cell,
            ScatterChart, Scatter, CartesianGrid, LabelList, PieChart, Pie } = Recharts;
    // ... component code here ...
    ReactDOM.createRoot(document.getElementById('root')).render(<App />);
  </script>
</body>
</html>
```

### Key rules for single-file HTML:
- **No import statements.** Access React via `React.useState`, Recharts via `Recharts.BarChart`, etc. Or destructure at the top: `const { useState } = React;`
- **No lucide-react.** Create inline SVG icons instead:
  ```jsx
  const Icon = ({ size = 20, children, ...props }) => (
    <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke="currentColor"
         strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" {...props}>{children}</svg>
  );
  const ChevronLeft = ({ size }) => <Icon size={size}><polyline points="15 18 9 12 15 6"/></Icon>;
  const ChevronRight = ({ size }) => <Icon size={size}><polyline points="9 18 15 12 9 6"/></Icon>;
  const ArrowRight = ({ size }) => <Icon size={size}><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></Icon>;
  ```
- **Tailwind via CDN** (`https://cdn.tailwindcss.com`) — all utility classes work. No custom config needed.
- **Babel in-browser** transpiles JSX. Use `<script type="text/babel" data-presets="react">`.
- **Images:** Either use external URLs, base64-encoded data URIs, or reference a relative path (`images/image.webp`) if the user will keep the image alongside the HTML file.

---

## 2. If a JSX Version Is Also Needed (React App)

When the user also wants a proper React component (for Vite/Next.js/etc.), create a separate `.jsx` file that uses standard imports:

```jsx
import { useState } from "react";
import { ChevronLeft, ChevronRight } from "lucide-react";
import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer, Cell } from "recharts";
```

The JSX file is for development. The HTML file is for sharing. Both should contain the same slide content and data.

---

## 3. McKinsey Slide Structure

Every strategic presentation follows this pattern. Each slide has three layers:

### A. Insight-Led Title (the "so what")
The title is NOT a topic label. It is the **conclusion** — the thing you want the audience to remember.

| Bad Title | Good Title (McKinsey) |
|-----------|----------------------|
| "Territory Overview" | "EMEA leads all territories; APAC at 56% signals systemic underperformance" |
| "Ramp Analysis" | "21% of the team is still ramping — fully ramped deliver 2.2x better pipeline" |
| "Action Plan" | "Recalibrate targets, fix APAC, manage performance, accelerate ramp" |

**Rule:** If the audience reads only the slide titles, they should understand the entire story.

### B. Supporting Evidence (charts, tables, KPIs)
Placed in card-based layouts. Each card is a white rounded rectangle with a subtle border on a cream/light background. Charts use the brand color palette.

### C. Contextual Annotations
Small text boxes below charts that explain "why this matters." These are the 2-3 bullet interpretations, not raw data descriptions.

### Standard Slide Sequence for Strategy Decks:

1. **Title / Home** — Name, subtitle, author, context
2. **Situation Overview** — KPIs + fill-bar or heatmap showing current state
3. **Key Insight** — The one finding that reframes the problem (chart + 3 supporting callouts)
4. **Deep Dive** — Segmented analysis (e.g., by ramp stage, by region, by cohort)
5. **Individual/Granular View** — Scatter plot or distribution showing the shape of performance
6. **Hypotheses** — Numbered cards with evidence + "validate with" for each
7. **Action Plan** — Phased timeline (NOW / NEXT / LATER) with priority tags and chevron arrows

---

## 4. Visual Design System

### Color Palette
Define a `COLORS` object at the top of the component. Always use the client's brand colors:

```jsx
const COLORS = {
  bg: "#F5F5EB",        // Page background (cream/light)
  card: "#FFFFFF",       // Card background
  green: "#BEFF50",      // Primary accent (brand green)
  greenDark: "#6BBF3B",  // Dark green for charts
  greenMid: "#9EDB3B",   // Mid green
  black: "#1A1A1A",      // Text
  gray: "#6B7280",       // Secondary text
  grayLight: "#E0E0D8",  // Borders
  red: "#E04F5F",        // Negative / at-risk
  blue: "#1396E4",       // Info / secondary accent
  orange: "#F59E0B",     // Warning / medium priority
};
```

### Layout Rules
- **Background:** Light cream (`#F5F5EB`) or client brand background — NOT white, NOT dark.
- **Cards:** White (`#FFFFFF`) with `rounded-xl border border-gray-200 shadow-sm`.
- **Charts:** White background inside cards. Never use dark chart backgrounds in light-mode decks.
- **Font:** Use client brand font (e.g., Lato). Load from Google Fonts CDN.
- **Fixed slide height:** Use `h-[560px] overflow-hidden` on the slide container so content fits without scrolling.

### Component Library

```jsx
// Card wrapper
const Card = ({ children, className = "" }) => (
  <div className={`bg-white rounded-xl border border-gray-200 shadow-sm ${className}`}>{children}</div>
);

// KPI display
const KPI = ({ value, label, sub, accent = false }) => (
  <div className="text-center px-2 py-2">
    <div className={`text-2xl font-bold ${accent ? "" : "text-gray-900"}`}
         style={accent ? { color: COLORS.greenDark } : {}}>{value}</div>
    <div className="text-xs font-semibold text-gray-500 uppercase tracking-wider mt-0.5">{label}</div>
    {sub && <div className="text-xs text-gray-400 mt-0.5">{sub}</div>}
  </div>
);

// Fill bar (progress toward target)
const FillBar = ({ label, pct, target, color }) => (
  <div className="mb-2">
    <div className="flex justify-between items-baseline mb-1.5">
      <span className="font-semibold text-sm text-gray-800">{label}</span>
      <span className="text-sm font-bold" style={{ color }}>{pct}%</span>
    </div>
    <div className="w-full h-5 bg-gray-100 rounded-full overflow-hidden relative">
      <div className="h-full rounded-full" style={{ width: `${Math.min(pct, 100)}%`, backgroundColor: color }} />
      <div className="absolute right-2 top-0 h-full flex items-center text-xs text-gray-400">Target: {target}</div>
    </div>
  </div>
);

// Priority pill
const Pill = ({ text, color }) => (
  <span className="inline-block text-xs font-bold px-2.5 py-1 rounded-full"
        style={{ backgroundColor: `${color}20`, color }}>{text}</span>
);
```

### Navigation
- **Top bar:** Tab buttons for each slide (e.g., "Home", "Territory", "Gap", "Ramp", etc.)
- **Bottom bar:** Chevron arrows + dot indicators + slide counter (e.g., "3/7")
- Active tab highlighted with brand accent color at 60% opacity.

---

## 5. Chart Best Practices (Recharts)

### Always Do:
- Use `<LabelList>` on bars so values are visible without hovering.
- Use `<ResponsiveContainer width="100%" height={180}>` — never hardcode pixel widths.
- Color-code by meaning: green = good, red = at-risk, orange = warning, gray = neutral.
- Add custom `<Tooltip>` for scatter plots showing ID, territory, and key metrics.
- Use `layout="vertical"` for horizontal bar charts (easier to read territory names).

### Chart Type Selection:
| Data Pattern | Chart Type |
|-------------|-----------|
| Attainment vs. target by category | Horizontal fill bars or grouped bar chart |
| Gap between two metrics | Paired horizontal bars (SQL vs Pipeline) |
| Composition / parts of whole | Stacked horizontal bar (NOT pie chart — stacked bars are more readable) |
| Two-variable relationship | Scatter plot with color-coded dots |
| Distribution shape | Vertical bar chart with color-coded buckets |
| Timeline / phased plan | Chevron arrows (CSS rounded pills + arrow icons) |

### Avoid:
- Pie charts for more than 3 categories (use stacked bars instead).
- 3D effects, gradients, or shadows on chart elements.
- Dark chart backgrounds in light-mode presentations.

---

## 6. Data Embedding

Embed all data directly in the component as JavaScript objects/arrays at the top of the file. This makes the presentation fully self-contained:

```jsx
const territoryData = [
  { name: "EMEA", aes: 13, sqlPct: 78, pipPct: 89, avgDeal: 437 },
  { name: "North America", aes: 35, sqlPct: 57, pipPct: 79, avgDeal: 570 },
  // ...
];
```

If data comes from a CSV/Excel file, parse it in a build script and embed the results. The HTML file should never depend on external data files at runtime.

---

## 7. Action Plan Slide Pattern

The action plan uses a **phase-based timeline** with chevron arrows:

```jsx
const actions = [
  { phase: "NOW", time: "0-30 Days", color: COLORS.greenDark, items: [
    { priority: "HIGH", title: "Audit SQL Targets", desc: "..." },
  ]},
  { phase: "NEXT", time: "30-60 Days", color: COLORS.blue, items: [...] },
  { phase: "LATER", time: "60-90 Days", color: COLORS.gray, items: [...] },
];
```

Visual structure:
- **Top row:** Horizontal chevron timeline (`NOW → NEXT → LATER`) as colored pills with `ArrowRight` icons between.
- **Columns below:** One column per phase, each containing action cards with left-colored border (`borderLeft: 3px solid ${phase.color}`).
- **Priority tags:** `HIGH` (red background), `MED` (amber), `LOW` (gray).
- **Bottom card:** Expected outcome summary spanning full width.

---

## 8. Hypothesis Slide Pattern

```jsx
const hypotheses = [
  { num: 1, title: "SQL targets are miscalibrated",
    evidence: "57.7% SQL vs 78.7% pipeline",
    validate: "Historical SQL trends, market sizing, ICP penetration" },
  // ...
];
```

Each hypothesis is a card with:
- Numbered circle (brand accent color)
- Bold title
- Evidence line (gray)
- "VALIDATE WITH" label (brand green, uppercase) + data description

---

## 9. Templates — READ THESE FIRST

### STEP 0: Before writing any HTML, you MUST read the templates.

Use the `Read` tool to load both files:

1. **`templates/viewer.html`** — The complete HTML boilerplate. This is your **literal starting point**, not inspiration.
   - **FIXED sections** (keep exactly as-is): CDN script tags, SVG icon components, reusable component library (Card, KPI, FillBar, Pill, SlideNav), main App shell with header + slide container + navigation.
   - **VARIABLE sections** (replace per project): Title, font CDN link, COLORS object, all data arrays, all Slide components, slideLabels array, brand logo letter.
   - Comments in the file mark every section as FIXED or VARIABLE.

2. **`templates/slide_patterns.jsx`** — Reference file showing 7 slide patterns with data shapes, layout grids, and chart type selection.
   - Use these patterns to build your actual slides inside viewer.html.
   - Not meant to be imported — it's a cookbook.

### Why templates matter:
- They encode the exact CDN versions, Babel config, and Recharts destructuring that are known to work.
- They include inline SVG icons that replace lucide-react (which has no simple CDN).
- They prevent the #1 failure mode: writing `import` statements in standalone HTML.

---

## 10. Workflow Summary

1. **Read templates** — `Read` tool on `templates/viewer.html` and `templates/slide_patterns.jsx`.
2. **Gather requirements** — Topic, audience, brand colors, font, number of slides.
3. **Research brand** — Extract colors from client website or brand assets.
4. **Structure the story** — Write insight-led titles for all slides FIRST, before any code.
5. **Copy viewer.html** — Use it as the starting point. Replace VARIABLE sections only.
6. **Build slides** — Using patterns from slide_patterns.jsx, embed data and create slide components.
7. **Verify** — Open the HTML file directly in a browser (double-click). All charts should render. No console errors.

If a JSX version is also needed (for Vite/Next.js), create a separate `.jsx` file with standard ES module imports (`import { useState } from "react"`, `import { BarChart } from "recharts"`, `import { ChevronLeft } from "lucide-react"`). The JSX is for development; the HTML is for sharing.

---

## 11. Common Pitfalls

- **Recharts in standalone HTML:** Use `Recharts.BarChart` or destructure from `Recharts` global. Do NOT use ES module imports.
- **Lucide icons:** Not available via CDN in a simple way. Use the inline SVG icons from the template.
- **Tailwind CDN:** Works for all standard utility classes. Custom colors must be set via inline `style={}`.
- **Babel standalone:** Must use `<script type="text/babel" data-presets="react">`. Without `data-presets`, JSX won't compile.
- **Fixed height:** Always set a fixed height on the slide container to prevent content overflow. Use `overflow-hidden` and size content to fit.
- **Dark vs light mode:** Match the client's website. Most corporate sites use light mode. Default to cream background + white cards unless explicitly told otherwise.
- **Data embedding:** All data must be inline JavaScript. No external CSV/JSON fetches at runtime.
