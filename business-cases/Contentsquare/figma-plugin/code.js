// CSQ Investment Case — Figma Slides Generator
// Generates 8 presentation slides replicating the PDF case study

const W = 1920;
const H = 1080;
const GAP = 80;

// ─── Color palette ───────────────────────────────────────────────────────────
const C = {
  navy:       { r: 0.059, g: 0.082, b: 0.169 }, // #0F1530
  navyLight:  { r: 0.094, g: 0.125, b: 0.231 }, // #18203B
  white:      { r: 1,     g: 1,     b: 1     },
  offWhite:   { r: 0.973, g: 0.973, b: 0.980 }, // #F8F8FA
  textDark:   { r: 0.118, g: 0.157, b: 0.231 }, // #1E283B
  textGray:   { r: 0.380, g: 0.420, b: 0.490 }, // #616B7D
  green:      { r: 0.063, g: 0.663, b: 0.431 }, // #10A96E
  greenBg:    { r: 0.867, g: 0.969, b: 0.929 }, // #DDEEED
  red:        { r: 0.843, g: 0.212, b: 0.212 }, // #D73636
  redBg:      { r: 0.988, g: 0.882, b: 0.882 }, // #FCE1E1
  orange:     { r: 0.933, g: 0.502, b: 0.082 }, // #EE8015
  orangeBg:   { r: 0.996, g: 0.929, b: 0.871 }, // #FEEDD0
  blue:       { r: 0.141, g: 0.380, b: 0.925 }, // #2461EC
  blueBg:     { r: 0.878, g: 0.918, b: 0.992 }, // #E0EAFD
  divider:    { r: 0.878, g: 0.894, b: 0.925 }, // #E0E4EC
  accent:     { r: 0.141, g: 0.380, b: 0.925 }, // #2461EC
};

// ─── Helpers ─────────────────────────────────────────────────────────────────

function rgb(c) { return { type: 'SOLID', color: c }; }

function setFill(node, c) {
  node.fills = [rgb(c)];
}

function rect(parent, x, y, w, h, color) {
  const r = figma.createRectangle();
  r.x = x; r.y = y; r.resize(w, h);
  if (color) setFill(r, color);
  parent.appendChild(r);
  return r;
}

async function text(parent, content, x, y, w, size, color, weight, lineH) {
  const t = figma.createText();
  await figma.loadFontAsync({ family: 'Inter', style: weight || 'Regular' });
  t.fontName = { family: 'Inter', style: weight || 'Regular' };
  t.characters = content;
  t.fontSize = size || 14;
  t.fills = [rgb(color || C.textDark)];
  t.x = x; t.y = y;
  if (w) {
    t.textAutoResize = 'HEIGHT';
    t.resize(w, 40);
  } else {
    t.textAutoResize = 'WIDTH_AND_HEIGHT';
  }
  if (lineH) t.lineHeight = { value: lineH, unit: 'PIXELS' };
  parent.appendChild(t);
  return t;
}

function badge(parent, label, x, y, bgColor, textColor) {
  const bg = rect(parent, x, y, 1, 32, bgColor);
  bg.cornerRadius = 6;
  const t = figma.createText();
  figma.loadFontAsync({ family: 'Inter', style: 'Bold' }).then(() => {
    t.fontName = { family: 'Inter', style: 'Bold' };
    t.characters = label;
    t.fontSize = 12;
    t.fills = [rgb(textColor)];
    t.textAutoResize = 'WIDTH_AND_HEIGHT';
    t.x = x + 10;
    t.y = y + 8;
    parent.appendChild(t);
    bg.resize(t.width + 20, 32);
  });
}

function frame(name, index) {
  const f = figma.createFrame();
  f.name = name;
  f.resize(W, H);
  f.x = index * (W + GAP);
  f.y = 0;
  setFill(f, C.offWhite);
  figma.currentPage.appendChild(f);
  return f;
}

// Header bar with slide number + title
async function header(f, slideNum, title, subtitle) {
  const bar = rect(f, 0, 0, W, 112, C.navy);
  // Slide number
  await text(f, String(slideNum).padStart(2, '0'), 56, 36, null, 13, C.textGray, 'Regular');
  // Title
  await text(f, title, 88, 28, W - 280, 36, C.white, 'Bold');
  if (subtitle) {
    await text(f, subtitle, 88, 72, W - 280, 15, { r: 0.6, g: 0.65, b: 0.75 }, 'Regular');
  }
  // Accent line bottom
  rect(f, 0, 112, W, 3, C.blue);
}

// Section label (P1 / P2 / P3 chip)
function sectionChip(f, label, x, y, bg, fg) {
  const r = figma.createRectangle();
  r.resize(60, 28); r.x = x; r.y = y;
  r.cornerRadius = 4;
  setFill(r, bg);
  f.appendChild(r);
  figma.loadFontAsync({ family: 'Inter', style: 'Bold' }).then(() => {
    const t = figma.createText();
    t.fontName = { family: 'Inter', style: 'Bold' };
    t.characters = label;
    t.fontSize = 13;
    t.fills = [rgb(fg)];
    t.textAutoResize = 'WIDTH_AND_HEIGHT';
    t.x = x + 10; t.y = y + 6;
    f.appendChild(t);
  });
}

// Horizontal divider
function divider(f, x, y, w) {
  rect(f, x, y, w, 1, C.divider);
}

// Stat box
async function statBox(f, x, y, w, h, label, value, sub, bgColor) {
  const bg = rect(f, x, y, w, h, bgColor || C.white);
  bg.cornerRadius = 10;
  bg.strokes = [rgb(C.divider)];
  bg.strokeWeight = 1;
  await text(f, label, x + 20, y + 20, w - 40, 12, C.textGray, 'Regular');
  await text(f, value, x + 20, y + 44, w - 40, 32, C.textDark, 'Bold');
  if (sub) await text(f, sub, x + 20, y + 86, w - 40, 13, C.green, 'Semi Bold');
}

// ─── Slide builders ──────────────────────────────────────────────────────────

async function slide01_title(i) {
  const f = figma.createFrame();
  f.name = '01 — Title';
  f.resize(W, H);
  f.x = i * (W + GAP);
  f.y = 0;
  setFill(f, C.navy);
  figma.currentPage.appendChild(f);

  // Background gradient bands
  rect(f, 0, 0, W, H, C.navy);
  const accent = rect(f, 0, H - 8, W, 8, C.blue);

  // Left accent bar
  rect(f, 56, 200, 4, 220, C.blue);

  // Eyebrow
  await text(f, 'CASE STUDY · SENIOR MANAGER, PRODUCT DATA ANALYST', 76, 200, W - 152, 13, { r: 0.4, g: 0.55, b: 0.85 }, 'Bold');

  // Main title
  const t1 = await text(f, 'CS Apps —', 76, 232, W - 200, 80, C.white, 'Bold');
  await text(f, 'Investment Case', 76, 316, W - 200, 80, { r: 0.4, g: 0.65, b: 1.0 }, 'Bold');

  // Subtitle
  await text(f, 'Revenue is growing but delivery is broken\nIncrease investment to fix adoption before the renewal cliff', 76, 424, 900, 22, { r: 0.65, g: 0.72, b: 0.85 }, 'Regular', 34);

  // Divider
  rect(f, 76, 510, 480, 1, { r: 0.2, g: 0.28, b: 0.45 });

  // Author + date
  await text(f, 'Daniel Amézquita', 76, 528, 400, 16, C.white, 'Semi Bold');
  await text(f, 'Product Data Analyst', 76, 554, 400, 14, { r: 0.45, g: 0.55, b: 0.7 }, 'Regular');

  // Right side — 3 pillars summary
  const pillars = [
    { label: 'P1 · Acquisition', status: 'STRONG', color: C.green, bg: C.greenBg, metric: '+37% ACV  ·  +30% accounts' },
    { label: 'P2 · Adoption',    status: 'BROKEN', color: C.red,   bg: C.redBg,   metric: '86% not live  ·  71% zero cert. users' },
    { label: 'P3 · Retention',   status: 'AT RISK', color: C.orange, bg: C.orangeBg, metric: '$16M Q4 cliff  ·  31 accounts' },
  ];

  for (let p = 0; p < pillars.length; p++) {
    const px = 1100;
    const py = 280 + p * 180;
    const card = rect(f, px, py, 700, 140, { r: 0.078, g: 0.102, b: 0.188 });
    card.cornerRadius = 12;

    // Status dot
    const dot = figma.createEllipse();
    dot.resize(10, 10);
    dot.x = px + 24; dot.y = py + 24;
    setFill(dot, pillars[p].color);
    f.appendChild(dot);

    await text(f, pillars[p].label, px + 48, py + 18, 400, 14, { r: 0.75, g: 0.8, b: 0.9 }, 'Regular');
    await text(f, pillars[p].status, px + 48, py + 44, 300, 26, C.white, 'Bold');
    await text(f, pillars[p].metric, px + 24, py + 90, 650, 13, { r: 0.5, g: 0.58, b: 0.72 }, 'Regular');
    rect(f, px, py + H - 8, 700, 3, pillars[p].color);
  }
}

async function slide02_exec(i) {
  const f = frame('02 — Executive Summary', i);
  await header(f, 2, 'Executive Summary', 'Revenue is growing but delivery is broken — increase investment before the renewal cliff');

  const bodyY = 140;

  // Narrative text
  await text(f, 'CS Apps shows strong revenue traction (+37% ACV, +30% accounts) but a clear gap between selling and delivering value. Only 15% of accounts are live, 71% have zero certified users, and the health metric is flawed — it blends CS Digital usage into CS Apps health, making non-users appear healthy. The real risk is renewal refusal from non-users with no ROI evidence, not active churn. $16.0M renews in Q4 across 31 accounts, creating concentrated exposure.', 56, bodyY, W - 112, 16, C.textGray, 'Regular', 26);

  // Arrow narrative
  const stages = [
    { label: 'Acquisition is strong', sub: 'Revenue & accounts growing' },
    { label: 'Adoption is fragile',   sub: 'Clients not going live' },
    { label: 'Latent renewal risk',   sub: 'No ROI evidence at renewal' },
  ];

  for (let s = 0; s < stages.length; s++) {
    const sx = 56 + s * 620;
    const sy = 280;
    const card = rect(f, sx, sy, 580, 120, C.white);
    card.cornerRadius = 12;
    card.strokes = [rgb(C.divider)];
    card.strokeWeight = 1;
    await text(f, stages[s].label, sx + 24, sy + 24, 530, 20, C.textDark, 'Bold');
    await text(f, stages[s].sub, sx + 24, sy + 56, 530, 14, C.textGray, 'Regular');

    if (s < 2) {
      await text(f, '→', sx + 590, sy + 44, null, 28, C.blue, 'Bold');
    }
  }

  // 3 pillars
  const pillars = [
    { id: 'P1', title: 'Acquisition & Growth', status: 'STRONG', color: C.green, bg: C.greenBg, summary: '+37% ACV, +30% accounts: demand is real', cq: 'Is CS Apps generating and growing revenue?' },
    { id: 'P2', title: 'Adoption & Engagement', status: 'BROKEN', color: C.red, bg: C.redBg, summary: '86% not live, 71% zero certified users, shallow engagement', cq: 'Are clients reaching time-to-value and engaging?' },
    { id: 'P3', title: 'Retention & ARR', status: 'AT RISK', color: C.orange, bg: C.orangeBg, summary: 'Health metric unreliable. 31 accounts renewing Q4 with no adoption to justify spend', cq: 'Will this revenue renew or churn?' },
  ];

  for (let p = 0; p < pillars.length; p++) {
    const px = 56 + p * 614;
    const py = 460;
    const card = rect(f, px, py, 584, 540, C.white);
    card.cornerRadius = 12;
    card.strokes = [rgb(C.divider)];
    card.strokeWeight = 1;

    // Colored top bar
    rect(f, px, py, 584, 6, pillars[p].color);

    // Badge bg
    const badgeBg = rect(f, px + 24, py + 32, 80, 32, pillars[p].bg);
    badgeBg.cornerRadius = 6;
    await text(f, pillars[p].id, px + 40, py + 40, null, 14, pillars[p].color, 'Bold');

    await text(f, pillars[p].title, px + 24, py + 80, 536, 20, C.textDark, 'Bold');

    // Status badge
    const stBg = rect(f, px + 24, py + 116, 100, 28, pillars[p].bg);
    stBg.cornerRadius = 6;
    await text(f, pillars[p].status, px + 36, py + 122, null, 12, pillars[p].color, 'Bold');

    divider(f, px + 24, py + 160, 536);

    await text(f, 'CORE QUESTION', px + 24, py + 176, 536, 11, C.textGray, 'Bold');
    await text(f, pillars[p].cq, px + 24, py + 198, 536, 14, C.textDark, 'Regular', 22);

    divider(f, px + 24, py + 268, 536);

    await text(f, 'SUMMARY', px + 24, py + 284, 536, 11, C.textGray, 'Bold');
    await text(f, pillars[p].summary, px + 24, py + 306, 536, 14, C.textDark, 'Regular', 24);
  }
}

async function slide03_p1(i) {
  const f = frame('03 — P1: Acquisition & Growth', i);
  await header(f, 3, 'P1: Acquisition & Growth', 'Is CS Apps generating and growing revenue meaningfully?');

  // Status badge
  const sb = rect(f, 56, 136, 110, 32, C.greenBg);
  sb.cornerRadius = 6;
  await text(f, '● STRONG', 72, 143, null, 13, C.green, 'Bold');

  await text(f, 'H1 | Revenue & Account Growth', 56, 188, 800, 18, C.textDark, 'Bold');
  await text(f, '+37% ACV and +30% accounts in 12 months — demand is real, the problem is not sales', 56, 216, 900, 14, C.textGray, 'Regular');

  // Key metrics row
  const metrics = [
    { label: 'CS Apps ACV', before: '$11M', after: '$15M', delta: '+37%', color: C.green },
    { label: 'Total Relationship ACV', before: '$49M', after: '$63M', delta: '+29%', color: C.green },
    { label: 'Number of Accounts', before: '134', after: '174', delta: '+30%', color: C.green },
    { label: 'Mean Apps ACV / Account', before: '$84.1K', after: '$89.0K', delta: '+6%', color: C.green },
    { label: 'CS Apps Penetration', before: '23%', after: '25%', delta: '+2pp', color: C.green },
  ];

  for (let m = 0; m < metrics.length; m++) {
    const mx = 56 + m * 366;
    const my = 260;
    const card = rect(f, mx, my, 344, 160, C.white);
    card.cornerRadius = 10;
    card.strokes = [rgb(C.divider)]; card.strokeWeight = 1;
    await text(f, metrics[m].label, mx + 16, my + 16, 310, 12, C.textGray, 'Regular');
    await text(f, metrics[m].before + ' → ' + metrics[m].after, mx + 16, my + 44, 310, 22, C.textDark, 'Bold');
    const db = rect(f, mx + 16, my + 84, 70, 28, C.greenBg);
    db.cornerRadius = 6;
    await text(f, metrics[m].delta, mx + 26, my + 90, null, 14, C.green, 'Bold');
  }

  // Geo table
  await text(f, 'H7 | High-Value Segment Opportunity', 56, 458, 900, 18, C.textDark, 'Bold');

  const tableHeaders = ['GEO', 'Accounts', 'Total ACV', 'Apps ACV', 'UFR', 'Penetration'];
  const tableRows = [
    ['EMEA',        '121', '$38.6M', '$9.2M',  '$1.4M', '24%'],
    ['AMERICAS',    '42',  '$22.3M', '$4.8M',  '$6.5M', '22%'],
    ['APJ',         '11',  '$2.3M',  '$1.4M',  '$338K', '63%'],
    ['Grand Total', '174', '$63.1M', '$15.5M', '$8.2M', '25%'],
  ];

  const colWidths = [160, 130, 150, 150, 150, 150];
  const tableX = 56;
  const tableY = 490;
  const rowH = 50;

  // Header row
  const hBg = rect(f, tableX, tableY, colWidths.reduce((a, b) => a + b), rowH, C.navyLight);
  hBg.cornerRadius = 8;

  let cx = tableX;
  for (let h = 0; h < tableHeaders.length; h++) {
    await text(f, tableHeaders[h], cx + 16, tableY + 16, colWidths[h] - 32, 12, C.white, 'Bold');
    cx += colWidths[h];
  }

  for (let r = 0; r < tableRows.length; r++) {
    const ry = tableY + rowH + r * rowH;
    const isTotal = r === tableRows.length - 1;
    const rowBg = rect(f, tableX, ry, colWidths.reduce((a, b) => a + b), rowH, isTotal ? { r: 0.94, g: 0.96, b: 0.99 } : (r % 2 === 0 ? C.white : { r: 0.975, g: 0.977, b: 0.982 }));
    cx = tableX;
    for (let c = 0; c < tableRows[r].length; c++) {
      await text(f, tableRows[r][c], cx + 16, ry + 16, colWidths[c] - 32, 14, isTotal ? C.navy : C.textDark, isTotal ? 'Bold' : 'Regular');
      cx += colWidths[c];
    }
  }

  // Verdict
  const vb = rect(f, 56, 760, W - 112, 72, C.greenBg);
  vb.cornerRadius = 10;
  await text(f, 'P1 VERDICT', 80, 772, 200, 11, C.green, 'Bold');
  await text(f, 'Acquisition is strong. CS Apps is selling well and growing. The problem is not demand — it\'s what happens after the sale.', 80, 792, W - 160, 14, C.textDark, 'Regular');
}

async function slide04_p2(i) {
  const f = frame('04 — P2: Adoption & Engagement', i);
  await header(f, 4, 'P2: Adoption & Engagement', 'Are clients reaching time-to-value, adopting, and engaging?');

  const sb = rect(f, 56, 136, 110, 32, C.redBg);
  sb.cornerRadius = 6;
  await text(f, '● BROKEN', 70, 143, null, 13, C.red, 'Bold');

  // Implementation funnel
  await text(f, 'H4 | Implementation Status (latest snapshot)', 56, 190, 800, 18, C.textDark, 'Bold');

  const stages = [
    { label: 'NULL / Untracked', n: 48, pct: '28%', color: C.textGray },
    { label: 'Not Started',      n: 8,  pct: '5%',  color: C.red },
    { label: 'Started',          n: 14, pct: '8%',  color: C.orange },
    { label: 'Partially Impl.',  n: 17, pct: '10%', color: { r: 0.9, g: 0.7, b: 0.1 } },
    { label: 'Implemented',      n: 57, pct: '33%', color: C.blue },
    { label: 'Partially Lived',  n: 5,  pct: '3%',  color: { r: 0.2, g: 0.7, b: 0.5 } },
    { label: '✓ Lived',          n: 25, pct: '14%', color: C.green },
  ];

  for (let s = 0; s < stages.length; s++) {
    const sx = 56;
    const sy = 230 + s * 62;
    const barW = Math.round((stages[s].n / 174) * 600);
    const bar = rect(f, sx + 200, sy + 10, Math.max(barW, 4), 36, stages[s].color);
    bar.cornerRadius = 4;
    bar.opacity = s === stages.length - 1 ? 1 : 0.7;
    await text(f, stages[s].label, sx, sy + 18, 188, 14, s === stages.length - 1 ? C.green : C.textDark, s === stages.length - 1 ? 'Bold' : 'Regular');
    await text(f, String(stages[s].n), sx + 820, sy + 18, 60, 14, C.textDark, 'Bold');
    await text(f, stages[s].pct, sx + 870, sy + 18, 60, 14, C.textGray, 'Regular');
  }

  // Right side — certification gap + module engagement
  await text(f, 'H2 | Certification Gap', 1000, 190, 800, 18, C.textDark, 'Bold');

  const certCards = [
    { label: 'Avg certified users / account', value: '0.7', sub: 'vs. 18 on CS Digital', color: C.red },
    { label: 'Accounts with zero certified users', value: '71%', sub: '132 of 185 accounts', color: C.red },
    { label: 'Avg sessions / user (Dec)', value: '10', sub: 'down from 14.5 in Jan', color: C.orange },
  ];

  for (let c = 0; c < certCards.length; c++) {
    await statBox(f, 1000 + c * 304, 228, 284, 130, certCards[c].label, certCards[c].value, certCards[c].sub, C.white);
  }

  // Module engagement table
  await text(f, 'H6 | Module Engagement (high stickiness = upgrade lever)', 1000, 390, 880, 16, C.textDark, 'Bold');

  const mHeaders = ['Module', '% Sessions', 'Avg Sess/User', 'Note'];
  const mRows = [
    ['Homepage',        '25.7%', '2.9', 'Navigation, not value'],
    ['Zoning Analysis', '18.2%', '3.8', 'Core analytics'],
    ['Journey Analysis','11.3%', '2.8', 'Core analytics'],
    ['Workspace',       '7.4%',  '4.0', '★ High stickiness'],
    ['Session Replay',  '6.4%',  '3.6', 'Core analytics'],
    ['Error Analysis',  '0.6%',  '4.4', '★ Highest stickiness, lowest reach'],
  ];
  const mColW = [240, 140, 160, 340];
  const mTableX = 1000;
  const mTableY = 422;

  const mhBg = rect(f, mTableX, mTableY, mColW.reduce((a,b)=>a+b), 44, C.navyLight);
  mhBg.cornerRadius = 8;
  let mcx = mTableX;
  for (let h = 0; h < mHeaders.length; h++) {
    await text(f, mHeaders[h], mcx + 14, mTableY + 14, mColW[h] - 28, 12, C.white, 'Bold');
    mcx += mColW[h];
  }
  for (let r = 0; r < mRows.length; r++) {
    const ry = mTableY + 44 + r * 44;
    const isHighlight = r === 3 || r === 5;
    const rowBg = rect(f, mTableX, ry, mColW.reduce((a,b)=>a+b), 44, isHighlight ? C.greenBg : (r % 2 === 0 ? C.white : C.offWhite));
    mcx = mTableX;
    for (let c = 0; c < mRows[r].length; c++) {
      await text(f, mRows[r][c], mcx + 14, ry + 14, mColW[c] - 28, 13, isHighlight ? C.green : C.textDark, isHighlight ? 'Semi Bold' : 'Regular');
      mcx += mColW[c];
    }
  }

  // Verdict
  const vb = rect(f, 56, 710, W - 112, 72, C.redBg);
  vb.cornerRadius = 10;
  await text(f, 'P2 VERDICT', 80, 722, 200, 11, C.red, 'Bold');
  await text(f, 'Adoption is the broken link. 86% of accounts are not live. Those that are live have 0.7 certified users on average and shallow module engagement.', 80, 742, W - 160, 14, C.textDark, 'Regular');
}

async function slide05_p3(i) {
  const f = frame('05 — P3: Retention & ARR', i);
  await header(f, 5, 'P3: Retention & ARR', 'Will the revenue CS Apps has created survive renewal, or is it at risk of churn?');

  const sb = rect(f, 56, 136, 110, 32, C.orangeBg);
  sb.cornerRadius = 6;
  await text(f, '● AT RISK', 72, 143, null, 13, C.orange, 'Bold');

  // Key callout
  await text(f, 'H5 | Renewal Pipeline at Risk', 56, 190, 900, 18, C.textDark, 'Bold');

  // Big callout
  const callout = rect(f, 56, 226, 560, 130, C.redBg);
  callout.cornerRadius = 12;
  await text(f, '$16.0M', 80, 250, 500, 48, C.red, 'Bold');
  await text(f, 'renews in Q4 2024 across 31 accounts — 47% of the full-year pipeline', 80, 308, 510, 14, C.textDark, 'Regular');

  const callout2 = rect(f, 636, 226, 340, 130, C.orangeBg);
  callout2.cornerRadius = 12;
  await text(f, '55.7%', 660, 250, 290, 48, C.orange, 'Bold');
  await text(f, 'of renewing ACV held by "healthy" accounts', 660, 308, 290, 14, C.textDark, 'Regular');

  const callout3 = rect(f, 996, 226, 340, 130, C.blueBg);
  callout3.cornerRadius = 12;
  await text(f, 'Target', 1020, 250, 290, 24, C.blue, 'Bold');
  await text(f, '≥90% renewal rate on Q4 cohort', 1020, 284, 290, 14, C.textDark, 'Regular');

  // Renewal pipeline table
  await text(f, 'Historical Renewal Pipeline', 56, 390, 900, 16, C.textDark, 'Bold');

  const rHeaders = ['Quarter', 'UFR', 'Accounts', '% Accts Healthy', '% UFR Healthy', 'Renewal Rate', 'ACV Retained'];
  const rRows = [
    ['Q4-2022', '$5M',   '20', '56%', '57%', '90%', '85%'],
    ['Q1-2023', '$2.7M', '15', '63%', '55%', '87%', '83%'],
    ['Q2-2023', '$5.1M', '23', '58%', '88%', '96%', '96%'],
    ['Q3-2023', '$5.4M', '17', '57%', '62%', '94%', '97%'],
    ['Q4-2023', '$16M',  '31', '54%', '56%', 'n/a', 'Target ≥90%'],
  ];
  const rColW = [140, 100, 120, 180, 160, 160, 180];
  const rTableX = 56;
  const rTableY = 418;

  const rhBg = rect(f, rTableX, rTableY, rColW.reduce((a,b)=>a+b), 44, C.navyLight);
  rhBg.cornerRadius = 8;
  let rcx = rTableX;
  for (let h = 0; h < rHeaders.length; h++) {
    await text(f, rHeaders[h], rcx + 12, rTableY + 14, rColW[h] - 24, 11, C.white, 'Bold');
    rcx += rColW[h];
  }
  for (let r = 0; r < rRows.length; r++) {
    const ry = rTableY + 44 + r * 50;
    const isQ4 = r === rRows.length - 1;
    const rowBg = rect(f, rTableX, ry, rColW.reduce((a,b)=>a+b), 50, isQ4 ? C.redBg : (r % 2 === 0 ? C.white : C.offWhite));
    if (isQ4) rowBg.cornerRadius = 8;
    rcx = rTableX;
    for (let c = 0; c < rRows[r].length; c++) {
      await text(f, rRows[r][c], rcx + 12, ry + 16, rColW[c] - 24, 13, isQ4 ? C.red : C.textDark, isQ4 ? 'Bold' : 'Regular');
      rcx += rColW[c];
    }
  }

  // Insight
  const insight = rect(f, 1100, 390, W - 1156, 320, C.white);
  insight.cornerRadius = 12;
  insight.strokes = [rgb(C.divider)]; insight.strokeWeight = 1;
  await text(f, 'Key Insight', 1124, 410, 700, 14, C.textGray, 'Bold');
  await text(f, 'Overall health scores don\'t predict renewals.\n\nWhat matters is whether the cohort of renewing accounts are healthy — and that signal is flashing red.\n\nQ4 enters with only 55.7% of renewing ACV held by healthy accounts.', 1124, 434, 700, 14, C.textDark, 'Regular', 24);

  // Verdict
  const vb = rect(f, 56, 730, W - 112, 90, C.orangeBg);
  vb.cornerRadius = 10;
  await text(f, 'P3 VERDICT', 80, 742, 200, 11, C.orange, 'Bold');
  await text(f, 'The health metric cannot be used as evidence of deterioration. The real retention risk is not active churn — it is renewal refusal: 31 accounts renew $16.0M in Q4 with no CS Apps adoption to justify the contract. Fix implementation now, not after renewals fail.', 80, 762, W - 160, 14, C.textDark, 'Regular', 24);
}

async function slide06_actions(i) {
  const f = frame('06 — 5 Actions to Close the Gap', i);
  await header(f, 6, '5 Actions to Close the Delivery Gap Before Q4', 'Prioritized by impact on the renewal cliff');

  const actions = [
    {
      num: '1',
      priority: 'HIGH',
      priorityColor: C.red,
      priorityBg: C.redBg,
      pillar: 'P2 Adoption',
      title: 'Triage 31 Q4 accounts by go-live status',
      desc: 'Assign implementation owners to non-live accounts immediately. Identify which are at risk of entering renewal conversations with zero adoption.',
      kpi: 'KPI: "Lived" rate 14% → 40%+',
    },
    {
      num: '2',
      priority: 'HIGH',
      priorityColor: C.red,
      priorityBg: C.redBg,
      pillar: 'P2 Adoption',
      title: 'Drive certification to 3+ users per account',
      desc: 'Current avg: 0.7 certified users vs. 18 on CS Digital. Launch certification campaigns, assign CSM ownership, create in-app certification prompts.',
      kpi: 'KPI: 0 → 3+ certified users / account',
    },
    {
      num: '3',
      priority: 'HIGH',
      priorityColor: C.red,
      priorityBg: C.redBg,
      pillar: 'P2 Adoption',
      title: 'In-product activation flows for high-stickiness modules',
      desc: 'Homepage = 26% of sessions. Workspace and Error Analysis have highest stickiness (4.0–4.4 avg sessions/user) but lowest reach. Route users there.',
      kpi: 'KPI: Homepage share 26% → 15%',
    },
    {
      num: '4',
      priority: 'MEDIUM',
      priorityColor: C.orange,
      priorityBg: C.orangeBg,
      pillar: 'P3 Retention',
      title: 'Build ROI case before Q4 procurement conversations',
      desc: 'Identify non-live accounts in the $16M Q4 renewal cohort. Build evidence of value (even partial) before procurement starts. Benchmark Fashion account 73% health.',
      kpi: 'KPI: Renewal rate ≥90% on $16M Q4 UFR',
    },
    {
      num: '5',
      priority: 'LOW',
      priorityColor: C.blue,
      priorityBg: C.blueBg,
      pillar: 'P1 Acquisition',
      title: 'Segment playbooks: replicate APJ penetration',
      desc: 'APJ has 63% CS Apps penetration vs. 22–24% in other geos. Document the playbook and apply to Americas (Telco focus) and EMEA. Win/loss data vs. Glassbox/FullStory.',
      kpi: 'KPI: Expand CS Apps penetration in non-APJ geos',
    },
  ];

  for (let a = 0; a < actions.length; a++) {
    const ax = 56 + (a % 3 === 0 && a > 0 ? 0 : 0);
    const col = a < 3 ? a : a - 3;
    const row = a < 3 ? 0 : 1;
    const cardX = 56 + col * (a < 3 ? 612 : 912);
    const cardY = 148 + row * 380;
    const cardW = a < 3 ? 588 : 864;
    const cardH = 340;

    const card = rect(f, cardX, cardY, cardW, cardH, C.white);
    card.cornerRadius = 12;
    card.strokes = [rgb(C.divider)]; card.strokeWeight = 1;

    // Number
    const numBg = rect(f, cardX + 20, cardY + 20, 40, 40, actions[a].priorityBg);
    numBg.cornerRadius = 8;
    await text(f, actions[a].num, cardX + 32, cardY + 28, null, 18, actions[a].priorityColor, 'Bold');

    // Priority badge
    const pb = rect(f, cardX + 72, cardY + 26, 80, 28, actions[a].priorityBg);
    pb.cornerRadius = 6;
    await text(f, actions[a].priority, cardX + 84, cardY + 33, null, 12, actions[a].priorityColor, 'Bold');

    await text(f, actions[a].pillar, cardX + 164, cardY + 33, 200, 12, C.textGray, 'Regular');

    await text(f, actions[a].title, cardX + 20, cardY + 76, cardW - 40, 16, C.textDark, 'Bold');
    await text(f, actions[a].desc, cardX + 20, cardY + 108, cardW - 40, 13, C.textGray, 'Regular', 22);
    await text(f, actions[a].kpi, cardX + 20, cardY + 286, cardW - 40, 13, actions[a].priorityColor, 'Semi Bold');
  }

  // Data quality box
  const dqY = 900;
  const dq = rect(f, 56, dqY, W - 112, 100, { r: 0.98, g: 0.97, b: 0.95 });
  dq.cornerRadius = 10;
  await text(f, '⚠ DATA QUALITY PREREQUISITES', 80, dqY + 16, 600, 12, C.orange, 'Bold');
  await text(f, 'NULL Implementation Status (29% / 82 accounts)  ·  NULL Contract Dates (blocks cohort analysis)  ·  AVG_WAU_GLOBAL = 0 (49 accounts / 156 rows)', 80, dqY + 42, W - 160, 14, C.textDark, 'Regular');
  await text(f, 'All three must be fixed before cohort analysis and time-to-live calculations are possible.', 80, dqY + 66, W - 160, 13, C.textGray, 'Regular');
}

async function slide07_pricing(i) {
  const f = frame('07 — AI Pricing: Sense Analyst', i);
  await header(f, 7, 'Part 2: AI Pricing — Sense Analyst', 'Should Sense Analyst be priced as flat-fee add-on, success-based tier, or credit-based model?');

  await text(f, 'Recommendation: Quota + Tier model — daily Sense Analyst query caps by tier, Sense Chat free on all plans', 56, 136, W - 112, 15, C.textDark, 'Regular');

  // 4 pricing models comparison
  const models = [
    { name: 'Flat-Fee Add-On', status: 'DISCARDED', statusColor: C.red, statusBg: C.redBg, example: 'Gainsight', desc: 'Fixed $/year for unlimited AI. Simple but misaligned — heavy users subsidized by light users. Usage is too concentrated (top 20% = 65% of sessions).' },
    { name: 'Usage / Token-Based', status: 'NEEDS DATA', statusColor: C.orange, statusBg: C.orangeBg, example: 'PostHog, Anthropic API', desc: 'Pay per query or token. Transparent but volatile for procurement budgets. Cannot test — Sense query logs not yet available.' },
    { name: 'Outcome-Based', status: 'DISCARDED', statusColor: C.red, statusBg: C.redBg, example: 'Intercom Fin ($0.99/ticket)', desc: 'Pay per resolved outcome. Hard to measure in analytics context. Cannot prove usage drives outcomes with current data.' },
    { name: '★ Quota + Tier', status: 'RECOMMENDED', statusColor: C.green, statusBg: C.greenBg, example: 'Claude Pro, Salesforce Agentforce', desc: 'Daily/monthly cap per tier, upgrade for more. Natural breakpoints at P50 (1/day), P75 (2/day), P90. 5/day cap covers 96% of users. Regular friction drives upgrades without blocking work.' },
  ];

  for (let m = 0; m < models.length; m++) {
    const mx = 56 + m * 464;
    const my = 174;
    const isRec = m === 3;
    const card = rect(f, mx, my, 440, 280, isRec ? C.greenBg : C.white);
    card.cornerRadius = 12;
    card.strokes = [rgb(isRec ? C.green : C.divider)]; card.strokeWeight = isRec ? 2 : 1;

    const stBg = rect(f, mx + 20, my + 20, 120, 28, models[m].statusBg);
    stBg.cornerRadius = 6;
    await text(f, models[m].status, mx + 30, my + 27, null, 11, models[m].statusColor, 'Bold');

    await text(f, models[m].name, mx + 20, my + 62, 400, 18, C.textDark, 'Bold');
    await text(f, 'e.g. ' + models[m].example, mx + 20, my + 90, 400, 12, C.textGray, 'Regular');
    await text(f, models[m].desc, mx + 20, my + 118, 400, 13, C.textDark, 'Regular', 22);
  }

  // Tier cards
  await text(f, 'Pricing Tiers — Daily Sense Analyst Caps', 56, 486, 900, 18, C.textDark, 'Bold');

  const tiers = [
    { name: 'Free', price: '€0 / forever', cap: 'No Sense Analyst', capNote: 'Sense Chat included', bg: C.white, accent: C.textGray },
    { name: 'Growth', price: 'From €39 / month', cap: '5 queries / day', capNote: '★ Covers 96% of users', bg: C.white, accent: C.blue, popular: true },
    { name: 'Pro', price: 'Let\'s talk', cap: '25 queries / day', capNote: 'Multi-session summaries', bg: C.white, accent: C.blue },
    { name: 'Enterprise', price: 'Let\'s talk', cap: 'Unlimited', capNote: 'Custom sessions, error feeds', bg: C.white, accent: C.navy },
  ];

  for (let t = 0; t < tiers.length; t++) {
    const tx = 56 + t * 464;
    const ty = 520;
    const card = rect(f, tx, ty, 440, 200, tiers[t].bg);
    card.cornerRadius = 12;
    card.strokes = [rgb(t === 1 ? C.blue : C.divider)]; card.strokeWeight = t === 1 ? 2 : 1;

    if (tiers[t].popular) {
      const pop = rect(f, tx + 300, ty + 16, 120, 24, C.blueBg);
      pop.cornerRadius = 12;
      await text(f, 'Most popular', tx + 314, ty + 21, null, 11, C.blue, 'Bold');
    }

    await text(f, tiers[t].name, tx + 20, ty + 20, 260, 20, C.textDark, 'Bold');
    await text(f, tiers[t].price, tx + 20, ty + 50, 400, 14, C.textGray, 'Regular');
    rect(f, tx + 20, ty + 80, 400, 1, C.divider);
    await text(f, tiers[t].cap, tx + 20, ty + 100, 400, 24, tiers[t].accent, 'Bold');
    await text(f, tiers[t].capNote, tx + 20, ty + 138, 400, 13, C.textGray, 'Regular');
  }

  // Upgrade friction example
  const uf = rect(f, 56, 750, W - 112, 80, { r: 0.95, g: 0.97, b: 1 });
  uf.cornerRadius = 10;
  await text(f, 'Upgrade friction example (Growth tier)', 80, 762, 500, 12, C.blue, 'Bold');
  await text(f, '🔒 Your team hit today\'s 5-query limit. Upgrade to Pro for 25/day, or cap resets tomorrow.', 80, 784, W - 160, 14, C.textDark, 'Regular');
  await text(f, '→ Upgrade to Pro', 1600, 784, 300, 14, C.blue, 'Bold');

  // Usage concentration insight
  await text(f, 'Usage concentration: top 20% of accounts drive 65% of sessions — validates tiered quotas over flat-fee. P50=1/day, P75=2/day, P90=5/day natural breakpoints confirmed from session data.', 56, 856, W - 112, 13, C.textGray, 'Regular', 22);
}

async function slide08_health(i) {
  const f = frame('08 — Redefining Account Health', i);
  await header(f, 8, 'Redefining Account Health — 3-Pillar Formula', 'The current metric masks adoption failure. A new AI-aware formula fixes it.');

  // Problem callout
  const prob = rect(f, 56, 136, W - 112, 64, C.redBg);
  prob.cornerRadius = 10;
  await text(f, 'Current problem:', 80, 148, 200, 12, C.red, 'Bold');
  await text(f, 'The current health metric blends CS Digital usage into CS Apps health scores, making non-adopters appear healthy and masking true adoption failure.', 200, 148, W - 260, 14, C.textDark, 'Regular');

  // Formula
  await text(f, 'New Health Formula', 56, 226, 900, 18, C.textDark, 'Bold');

  const fmBg = rect(f, 56, 256, W - 112, 110, C.navyLight);
  fmBg.cornerRadius = 12;
  await text(f, 'If NON-LIVE:', 80, 272, 200, 14, { r: 0.6, g: 0.7, b: 0.9 }, 'Regular');
  await text(f, 'Score = (0.15 × P1) + (0.25 × P2) + (0.60 × P3)', 220, 272, 900, 18, C.white, 'Bold');
  await text(f, 'If LIVE:', 80, 314, 200, 14, { r: 0.6, g: 0.7, b: 0.9 }, 'Regular');
  await text(f, 'Score = (0.30 × P2) + (0.70 × P3)', 220, 314, 900, 18, C.white, 'Bold');
  await text(f, 'Healthy = Score ≥ 50', 1400, 292, 400, 18, C.green, 'Bold');

  // 3 pillars
  const pillars = [
    {
      id: 'P1',
      name: 'Implementation Velocity',
      scope: 'Non-Live only. Dropped once account goes Live.',
      formula: '100 if within 90-day window\nLinear decay beyond window',
      color: C.blue,
      bg: C.blueBg,
    },
    {
      id: 'P2',
      name: 'Adoption (ACV-Normalized)',
      scope: 'All accounts.',
      formula: 'min(CertUsers / (ACV × α), 1) × 100\nNormalizes adoption vs. account size.',
      color: C.orange,
      bg: C.orangeBg,
    },
    {
      id: 'P3',
      name: 'Engagement Quality (AI-Aware)',
      scope: 'All accounts. Avoids penalizing AI migration.',
      formula: 'max(0, 100 − ACV / (WAU + Sense Q/wk) × β)\nWAU + Sense Queries/week combined signal.',
      color: C.green,
      bg: C.greenBg,
    },
  ];

  for (let p = 0; p < pillars.length; p++) {
    const px = 56 + p * 614;
    const py = 392;
    const card = rect(f, px, py, 590, 260, C.white);
    card.cornerRadius = 12;
    card.strokes = [rgb(pillars[p].color)]; card.strokeWeight = 1;
    rect(f, px, py, 590, 6, pillars[p].color);

    const idBg = rect(f, px + 20, py + 22, 44, 32, pillars[p].bg);
    idBg.cornerRadius = 6;
    await text(f, pillars[p].id, px + 31, py + 29, null, 14, pillars[p].color, 'Bold');

    await text(f, pillars[p].name, px + 78, py + 28, 490, 16, C.textDark, 'Bold');
    await text(f, pillars[p].scope, px + 20, py + 70, 550, 13, C.textGray, 'Regular');
    divider(f, px + 20, py + 98, 550);
    await text(f, pillars[p].formula, px + 20, py + 114, 550, 13, C.textDark, 'Regular', 22);
  }

  // Examples table
  await text(f, 'Illustrative Examples', 56, 686, 900, 16, C.textDark, 'Bold');

  const eHeaders = ['Account', 'ACV', 'Status', 'Impl Days', 'WAU', 'Sense Q/wk', 'Cert Users', 'P1', 'P2', 'P3', 'Score'];
  const eRows = [
    ['Acme Corp', '$200K', 'Non-Live', '210', '2', '0',  '1', '0',   '50',  '0',   '15 ✗'],
    ['Gamma Inc', '$200K', 'Live',     '—',   '20','10', '5', '—',   '100', '87',  '92 ✓'],
  ];
  const eColW = [160, 80, 100, 110, 60, 110, 110, 60, 60, 60, 100];
  const eTableX = 56;
  const eTableY = 714;

  const ehBg = rect(f, eTableX, eTableY, eColW.reduce((a,b)=>a+b), 40, C.navyLight);
  ehBg.cornerRadius = 8;
  let ecx = eTableX;
  for (let h = 0; h < eHeaders.length; h++) {
    await text(f, eHeaders[h], ecx + 10, eTableY + 13, eColW[h] - 20, 11, C.white, 'Bold');
    ecx += eColW[h];
  }
  for (let r = 0; r < eRows.length; r++) {
    const ry = eTableY + 40 + r * 48;
    const isHealthy = r === 1;
    const rowBg = rect(f, eTableX, ry, eColW.reduce((a,b)=>a+b), 48, isHealthy ? C.greenBg : C.redBg);
    ecx = eTableX;
    for (let c = 0; c < eRows[r].length; c++) {
      const isScore = c === eRows[r].length - 1;
      await text(f, eRows[r][c], ecx + 10, ry + 16, eColW[c] - 20, 13, isScore ? (isHealthy ? C.green : C.red) : C.textDark, isScore ? 'Bold' : 'Regular');
      ecx += eColW[c];
    }
  }

  // Calibration note
  await text(f, '⚠ Calibration needed: Sense query logs at account level  ·  Historical time-to-go-live by tier  ·  Distribution of (Cert Users / ACV) across live accounts  ·  Renewal outcomes by usage tier', 56, 826, W - 112, 13, C.textGray, 'Regular');
}

// ─── Main ─────────────────────────────────────────────────────────────────────

(async () => {
  await figma.loadFontAsync({ family: 'Inter', style: 'Regular' });
  await figma.loadFontAsync({ family: 'Inter', style: 'Bold' });
  await figma.loadFontAsync({ family: 'Inter', style: 'Semi Bold' });

  await slide01_title(0);
  await slide02_exec(1);
  await slide03_p1(2);
  await slide04_p2(3);
  await slide05_p3(4);
  await slide06_actions(5);
  await slide07_pricing(6);
  await slide08_health(7);

  // Zoom to fit all slides
  figma.viewport.scrollAndZoomIntoView(figma.currentPage.children);

  figma.notify('✅ CSQ Investment Case — 8 slides generated!');
  figma.closePlugin();
})();
