#!/usr/bin/env python3
"""
figma_export.py — Render each slide of cs_apps_presentation.html
as a clean PNG (no navigation chrome) using Playwright's print mode,
then serve them on localhost:8787 for the Figma plugin to consume.

Usage:
    pip install playwright && python -m playwright install chromium
    python figma_export.py
"""

import os
import time
import threading
import http.server
import socketserver
from pathlib import Path

from playwright.sync_api import sync_playwright

SCRIPT_DIR = Path(__file__).parent
HTML_FILE  = SCRIPT_DIR / "cs_apps_presentation.html"
OUT_DIR    = SCRIPT_DIR / "figma_export"
PORT       = 8787

SLIDE_LABELS = [
    "01_Cover",
    "02_Exec_Summary",
    "03_P1_Acquisition",
    "04_P2_Adoption",
    "05_P3_Retention",
    "06_Action_Plan",
    "07_Monetization_Divider",
    "08_Monetization_Models",
    "09_Pricing_Tiers",
    "10_Usage_Data",
    "11_Health_Formula",
    "12_QA",
]


def take_screenshots() -> int:
    OUT_DIR.mkdir(exist_ok=True)
    # Use print mode so all slides render without navigation chrome
    url = HTML_FILE.as_uri() + "?print=1"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            viewport={"width": 1280, "height": 900},
            device_scale_factor=2,  # 2× → 2048×1120 per slide
        )
        page = context.new_page()

        print(f"Opening {url}")
        page.goto(url)
        page.wait_for_load_state("networkidle")
        # Extra wait for Babel transpile + Google Fonts CDN
        time.sleep(3)

        # Remove restrictive sizing/positioning from the root so all slides
        # are visible in the DOM (the HTML targets interactive mode by default)
        page.evaluate("""() => {
            const root = document.getElementById('root');
            if (root) {
                root.style.position  = 'relative';
                root.style.top       = 'auto';
                root.style.maxHeight = 'none';
                root.style.height    = 'auto';
            }
            // Also relax the body constraints
            document.body.style.maxHeight = 'none';
            document.body.style.height    = 'auto';
            document.body.style.overflow  = 'visible';
        }""")
        time.sleep(0.5)

        slides = page.locator(".slide-page-inner")
        count  = slides.count()
        print(f"Found {count} slide(s)")

        saved = 0
        for i in range(count):
            label    = SLIDE_LABELS[i] if i < len(SLIDE_LABELS) else f"{i+1:02d}_Slide"
            out_path = OUT_DIR / f"slide_{i+1:02d}.png"
            print(f"  [{i+1}/{count}] {label} → {out_path.name}")
            slides.nth(i).screenshot(path=str(out_path))
            saved += 1

        browser.close()
    return saved


def serve():
    class CORSHandler(http.server.SimpleHTTPRequestHandler):
        def end_headers(self):
            self.send_header("Access-Control-Allow-Origin", "*")
            super().end_headers()

        def log_message(self, fmt, *args):
            pass  # suppress per-request logs

    os.chdir(OUT_DIR)
    with socketserver.TCPServer(("", PORT), CORSHandler) as httpd:
        print(f"\nServing figma_export/ at http://localhost:{PORT}")
        print("Keep this terminal open, then run the Figma plugin.")
        print("Press Ctrl+C to stop.\n")
        httpd.serve_forever()


if __name__ == "__main__":
    n = take_screenshots()
    print(f"\nDone — {n} slide(s) saved to {OUT_DIR}/")
    serve()
