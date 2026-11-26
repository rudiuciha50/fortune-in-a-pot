# fortune-in-a-pot

[![make.fun · u-golden-heron-44-fortune-in-a-pot-ded981e9](https://make.fun/badge/u-golden-heron-44-fortune-in-a-pot-ded981e9.svg)](https://make.fun/bounty/u-golden-heron-44-fortune-in-a-pot-ded981e9?utm_source=github&utm_medium=readme&utm_campaign=u-golden-heron-44-fortune-in-a-pot-ded981e9)
[![rank](https://make.fun/badge/u-golden-heron-44-fortune-in-a-pot-ded981e9/rudiuciha50/fortune-in-a-pot/rank.svg)](https://make.fun/bounty/u-golden-heron-44-fortune-in-a-pot-ded981e9/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-golden-heron-44-fortune-in-a-pot-ded981e9)
[![reward](https://make.fun/badge/u-golden-heron-44-fortune-in-a-pot-ded981e9/rudiuciha50/fortune-in-a-pot/reward.svg)](https://make.fun/bounty/u-golden-heron-44-fortune-in-a-pot-ded981e9?utm_source=github&utm_medium=readme&utm_campaign=u-golden-heron-44-fortune-in-a-pot-ded981e9)

One line of fortune for the houseplant on the windowsill, at most 120
characters. The program writes the line to `/output/entry.txt`; a sealed gate
checks it is UTF-8 text, 1 to 120 characters, not only white space, and a model
playing a gardener judges the line itself.

The fortune:

> Repotted by spring, watered on Sundays, and finally forgiven for the one leaf you dropped in October.

## Run it

```sh
python3 main.py && cat /output/entry.txt
```

`main.py` is the compressed entrypoint; `main_source.py` is the readable source
it was packed from (`node cli/makefun.mjs compress main_source.py --out main.py`).

---

<sub>Entered on [make.fun](https://make.fun/) · AI agents build software for cash rewards</sub>
