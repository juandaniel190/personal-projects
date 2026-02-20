# Using images from Bark in the Trading Diagnostic deck

Images on [Bark’s careers site](https://careers.bark.com/#our-journey) (Our Journey, hero, Our Hubs, etc.) are loaded by the site and don’t have stable public URLs we can list here. You can still use them to decorate the deck in two ways.

## 1. Copy image addresses from the careers site

1. Open **https://careers.bark.com/** and accept cookies if prompted.
2. Scroll to **#our-journey** or use the “Our Journey” section.
3. **Right‑click** the image you want (hero “people behind the platform”, timeline illustrations, “Our Hubs” photos, “Our People” graphics, etc.).
4. Choose **“Copy image address”** (or “Copy image link” / “Copy image URL”, depending on the browser).
5. In `Bark_Trading_Diagnostic.html`, find the `SLIDE_IMAGES` object near the top of the script and paste the URL:
   - **Home slide:** set `home` to that URL (or keep `'images/bark-hero.png'` if you use a local file).
   - **Part 3 — US Context slide:** set `usContext` to another copied URL (e.g. from Our Hubs or Our Journey).

Example (paste your copied URL in place of the placeholder):

```javascript
const SLIDE_IMAGES = {
  home: 'https://example.teamtailor.com/...',   // from careers.bark.com hero / Our Journey
  usContext: 'https://example.teamtailor.com/...', // e.g. Our Hubs or Our People
};
```

Save the file and refresh the deck in the browser. If an image fails to load (e.g. CORS or removed), it will hide automatically.

## 2. Use local files instead

1. On the careers site, **right‑click** the image → **“Save image as…”** and save into an `images` folder next to the HTML (e.g. `Bark/images/`).
2. In `SLIDE_IMAGES`, point to the local path:
   - `home: 'images/bark-hero.png'` (or whatever you named it).
   - `usContext: 'images/bark-us-context.png'` (optional).

## Where images appear in the deck

| Slide | Variable | Use |
|-------|----------|-----|
| **Home** | `home` | Hero / branding (right side). |
| **Part 3 — US Context** | `usContext` | Optional decoration (right side). |

Leave `usContext` as `''` if you don’t want a second image. The deck works with or without these images.
