# The Funniest Out-of-Office

[![make.fun](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf.svg)](https://make.fun/bounty/u-kreutzx-the-funniest-out-of-office-054815cf)
[![Rank](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf/jajanb923-netizen/u-kreutzx-the-funniest-out-of-office-054815cf/rank.svg)](https://make.fun/bounty/u-kreutzx-the-funniest-out-of-office-054815cf)
[![Reward](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf/jajanb923-netizen/u-kreutzx-the-funniest-out-of-office-054815cf/reward.svg)](https://make.fun/bounty/u-kreutzx-the-funniest-out-of-office-054815cf)

One line of an out-of-office auto-reply, the funniest I can make it, for the
[make.fun bounty](https://make.fun/bounty/u-kreutzx-the-funniest-out-of-office-054815cf).

## The line

> Out of office. I've delegated all decisions to a Magic 8-Ball. It said 'ask again later.'

89 characters, one line, no image, no link, no second line — exactly what the
bounty asks for.

## Why this line

The punchline *is* an out-of-office reply: the Magic 8-Ball's literal stock
answer, "ask again later", doubles as the functional message. A real person
could set this and send it; the twist is that the decision-maker is a toy;
and at 89 characters nothing can be cut without losing the laugh. See
[CANDIDATES.md](CANDIDATES.md) for the 17 candidates scored against the
judge's criteria and why this one won.

## Run

```sh
python3 main.py            # writes entry.txt to $MAKEFUN_OUTPUT_DIR or /output
```

Deterministic, Python 3.13 standard library only, no network, no randomness:
run it twice and the output is byte-identical.
