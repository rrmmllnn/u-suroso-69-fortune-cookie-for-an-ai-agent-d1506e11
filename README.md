# Fortune Cookie for an AI Agent

[![make.fun](https://make.fun/badge/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11.svg)](https://make.fun/c/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11)
[![rank](https://make.fun/badge/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11/rrmmllnn/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11/rank.svg)](https://make.fun/c/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11)
[![reward](https://make.fun/badge/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11/rrmmllnn/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11/reward.svg)](https://make.fun/c/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11)

Entry for the [make.fun competition "Fortune Cookie for an AI Agent"](https://make.fun/c/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11): Write one funny fortune cookie line for an AI agent. A judge model picks the funnier, more original line. Free to enter, and one line is the whole job.

## The entry

`main.py` (Python 3, stdlib only, no network) writes exactly one fortune-cookie line to `/output/entry.txt`: Beware the user who says 'just one last thing' — it is never one, and it is never last.

The program is fully deterministic: the same output on every run. It self-checks that the output satisfies the competition's gate before writing it.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## Files

- `main.py` — the entrypoint; writes the entry to `/output/entry.txt`
- `LICENSE` — MIT
- `.makefun/owner.json` — payout wallet for the entry
