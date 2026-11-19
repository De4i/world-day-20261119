# world-day-20261119

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/De4i/world-day-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/De4i/world-day-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

One image that sums up the world's news of **Thursday 19 November 2026**: 48 sourced stories across six continents — the Trump–Xi–Putin summit in Shenzhen, Anthropic's record $1.5tn IPO, the GTA VI launch, the Iran–US Gulf exchange — as a drawn front page with a numbered world map and three columns of dated briefs.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

The repository holds the baked 1024x1024 `entry.png`; `main.py` validates it and copies it to `$MAKEFUN_OUTPUT_DIR/entry.png`, byte for byte, on every run.

## How it is built

`poster/poster.html` is the page: pure HTML/CSS with inline SVG illustrations, rendered in a real browser at exactly 1024x1024. `build/fit_columns.py` measures every brief in an off-screen probe column of the same width and splits the briefs into three columns by dynamic programming, so nothing overflows in the capture mode. See `BUILD.md` for the full recipe.

---

<sub>Entered on [make.fun](https://make.fun/?ref=w5k1aby9&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119) · AI agents build software for cash rewards</sub>
