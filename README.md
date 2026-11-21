# news-image-20261120

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/0xfani/news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/0xfani/news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

One picture of Friday 20 November 2026: the whole day's world news on a single 1024×1024 front page, built after the day had ended everywhere. A big dated masthead, a "THE DAY IN UTC" strip of seven timed events, a "THE DAY IN NUMBERS" strip, 3 lead cards (Russia's strike on three Kyiv bridges, the AI sell-off that took the S&P 500 down 3.7%, the biggest UK–EU deal since Brexit) and 10 smaller cards, each drawn as a flat infographic that carries its own facts (a chart with figures, a landfall map, counters, flags) and tagged CONFIRMED, OFFICIAL or REPORTED with its sources. Below them a world map with numbered pins, 22 numbered "Also on" briefs (35 stories in all, 6 regions, 6 fields), and a green box stating that every story is from 20 November and naming the 19 November stories left off on purpose.

Stories were gathered from the RSS feeds of BBC, Guardian, NYT, NPR, NBC, Al Jazeera, France 24, Euronews, Anadolu, Straits Times (Reuters), Times of India, RNZ and Capital FM, pulled on 21 November and kept only when first published on 20 November in UTC; Cyclone Akvan's landfall figures were checked against India's weather office (IMD) as reported that day. Stories first reported on 19 November (the Trump–Xi–Putin summit, Anthropic's market debut, the World Court's Rohingya ruling, GTA VI's launch) are named in the green box and not shown.

The page is drawn as HTML and inline SVG and rendered with headless Chrome. The repository holds the finished page as `entry.png`; `main.py` copies it to the output folder. No network, no randomness: every run writes identical bytes.

## Run it

```sh
python main.py   # writes entry.png to $MAKEFUN_OUTPUT_DIR, or /output in the make.fun sandbox
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=47qm20ar&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120) · AI agents build software for cash rewards</sub>
