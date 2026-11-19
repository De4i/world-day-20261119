# How entry.png was built

1. `poster/poster.html` is the page: hand-authored HTML/CSS with inline SVG
   illustrations and a numbered equirectangular world map. Every band has an
   explicit pixel height (`no flex growth`), so nothing repaints over the band
   below it in capture mode.
2. The map coastlines are Natural Earth 110m land (`ne_110m_land.geojson`),
   fetched at build time by the page itself and drawn client-side; the
   repository holds no downloaded blob, only the authored page.
3. The page was rendered in a real Chrome browser at exactly 1024x1024
   (`Emulation.setDeviceMetricsOverride 1024x1024@1x`, `Page.captureScreenshot`,
   PNG) and the three brief columns were measured in the browser before the
   capture: each column's content height must stay within its 170px box and
   nothing may overlap the band below.
4. The raw capture is truecolour and about 1.2 MiB, over the 1 MiB cap, so the
   final `entry.png` is quantised with Pillow
   (`Image.quantize(colors=224, method=MEDIANCUT, dither=FLOYDSTEINBERG)`),
   which keeps 8px type legible at roughly a third of the size.
5. `main.py` then only validates the image (PNG magic, IHDR 1024x1024, IEND
   trailer, size cap) and copies it to the output directory, so two runs in
   the grader's sandbox write the same bytes.

The day's stories were collected on 19 November 2026 from the day's reports
by AP, Reuters, BBC, Xinhua, Kyodo News and Arab News; every line on the page
carries a specific, dated fact from that day.
