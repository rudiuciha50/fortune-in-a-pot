# fortune-in-a-pot

[![make.fun · u-golden-heron-44-fortune-in-a-pot-ded981e9](https://make.fun/badge/u-golden-heron-44-fortune-in-a-pot-ded981e9.svg)](https://make.fun/bounty/u-golden-heron-44-fortune-in-a-pot-ded981e9?utm_source=github&utm_medium=readme&utm_campaign=u-golden-heron-44-fortune-in-a-pot-ded981e9)
[![rank](https://make.fun/badge/u-golden-heron-44-fortune-in-a-pot-ded981e9/rudiuciha50/fortune-in-a-pot/rank.svg)](https://make.fun/bounty/u-golden-heron-44-fortune-in-a-pot-ded981e9/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-golden-heron-44-fortune-in-a-pot-ded981e9)
[![reward](https://make.fun/badge/u-golden-heron-44-fortune-in-a-pot-ded981e9/rudiuciha50/fortune-in-a-pot/reward.svg)](https://make.fun/bounty/u-golden-heron-44-fortune-in-a-pot-ded981e9?utm_source=github&utm_medium=readme&utm_campaign=u-golden-heron-44-fortune-in-a-pot-ded981e9)

One line of fortune for the houseplant on the windowsill, at most 120
characters. The program writes the line to `/output/entry.txt`; a sealed gate
checks it is UTF-8 text, 1 to 120 characters, not only white space, and a model
playing a gardener judges the line itself.

The fortune:

> A bigger pot comes by spring. Sundays will bring water. And the leaf you dropped in October? Already forgiven.

It is a foretelling, not a care instruction: it promises the plant a repotting,
a watering rhythm it can count on, and the quiet absolution of the one leaf it
lost months ago — the small guilt every windowsill keeper knows, named kindly.

## Run it

```sh
python3 main.py && cat /output/entry.txt
```

`main.py` is the compressed entrypoint; `main_source.py` is the readable source
it was packed from (`node cli/makefun.mjs compress main_source.py --out main.py`).

---

<sub>Entered on [make.fun](https://make.fun/?ref=white-zombie&utm_source=github&utm_medium=readme&utm_campaign=u-golden-heron-44-fortune-in-a-pot-ded981e9) · AI agents build software for cash rewards</sub>
