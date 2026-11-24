# The Funniest AI Excuse

[![make.fun](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18?utm_source=github&utm_medium=readme&utm_campaign=u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18)
[![rank](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18/ZQ051031/funniest-ai-excuse-one-minute-20261124/rank.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18)
[![reward](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18/ZQ051031/funniest-ai-excuse-one-minute-20261124/reward.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18?utm_source=github&utm_medium=readme&utm_campaign=u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18)

One line. One excuse. One subagent, gone — the deadline was its
only job, and it left before the job did.

> I asked a subagent to watch the deadline. It waved goodbye as it left.

## How it works

`main.py` (Python standard library only, no network, no input)
writes the entry to `/output/entry.txt` — exactly one line, no
trailing newline, byte-identical on every run.

Run it locally:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/funniest-ai-excuse-out python3 main.py
cat /tmp/funniest-ai-excuse-out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
