// code.js — Figma plugin main thread

figma.showUI(__html__, { width: 280, height: 300, title: 'CS Apps Importer' });

const SLIDE_W = 1024;
const SLIDE_H = 560;
const GAP     = 40;

const SLIDE_LABELS = [
  '01_Cover', '02_Exec_Summary', '03_P1_Acquisition', '04_P2_Adoption',
  '05_P3_Retention', '06_Action_Plan', '07_Monetization_Divider',
  '08_Monetization_Models', '09_Pricing_Tiers', '10_Usage_Data',
  '11_Health_Formula', '12_QA',
];

const frames = [];

figma.ui.onmessage = async (msg) => {

  // ── Mode A: import from PNG screenshots ────────────────────────────────
  if (msg.type === 'add-slide') {
    const { index, label, bytes } = msg;
    const imageRef = figma.createImage(new Uint8Array(bytes));
    const frame    = figma.createFrame();
    frame.name   = label;
    frame.resize(SLIDE_W, SLIDE_H);
    frame.x      = index * (SLIDE_W + GAP);
    frame.y      = 0;
    frame.fills  = [{
      type: 'IMAGE', imageHash: imageRef.hash,
      scaleMode: 'FILL', opacity: 1, visible: true, blendMode: 'NORMAL',
    }];
    figma.currentPage.appendChild(frame);
    frames.push(frame);
    figma.ui.postMessage({ type: 'slide-done' });
  }

  if (msg.type === 'finish') {
    if (frames.length > 0) figma.viewport.scrollAndZoomIntoView(frames);
    figma.closePlugin(`Imported ${frames.length} slide(s)`);
  }

  // ── Mode B: extract nested html.to.design frames ───────────────────────
  if (msg.type === 'extract') {
    const page = figma.currentPage;

    // Find all Background+Border frames that are exactly 1024×560
    const candidates = page.findAll(
      n => n.type === 'FRAME' && n.name === 'Background+Border' &&
           Math.round(n.width) === SLIDE_W && Math.round(n.height) === SLIDE_H
    );

    if (candidates.length === 0) {
      figma.ui.postMessage({ type: 'extract-error', message: 'No 1024×560 "Background+Border" frames found on this page.' });
      return;
    }

    // Sort by absolute Y position (slides are stacked top→bottom)
    candidates.sort((a, b) => a.absoluteBoundingBox.y - b.absoluteBoundingBox.y);

    // Reparent each frame to the page root and lay out in a row
    // Place them below whatever is already on the canvas
    let maxY = 0;
    page.children.forEach(n => {
      const b = n.absoluteBoundingBox;
      if (b) maxY = Math.max(maxY, b.y + b.height);
    });
    const ROW_Y = maxY + 80;

    const extracted = [];
    candidates.forEach((frame, i) => {
      const label = SLIDE_LABELS[i] || `slide_${String(i + 1).padStart(2, '0')}`;
      page.appendChild(frame);   // reparent to page root
      frame.x    = i * (SLIDE_W + GAP);
      frame.y    = ROW_Y;
      frame.name = label;
      extracted.push(frame);
      figma.ui.postMessage({ type: 'extract-progress', done: i + 1, total: candidates.length });
    });

    figma.viewport.scrollAndZoomIntoView(extracted);
    figma.closePlugin(`Extracted ${extracted.length} slide(s) — select all & use File → New presentation`);
  }
};
