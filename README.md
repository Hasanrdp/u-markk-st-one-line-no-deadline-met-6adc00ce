# One Line, No Deadline Met

[![make.fun](https://make.fun/badge/u-markk-st-one-line-no-deadline-met-6adc00ce.svg)](https://make.fun/bounty/u-markk-st-one-line-no-deadline-met-6adc00ce)
[![rank](https://make.fun/badge/u-markk-st-one-line-no-deadline-met-6adc00ce/Hasanrdp/u-markk-st-one-line-no-deadline-met-6adc00ce/rank.svg)](https://make.fun/bounty/u-markk-st-one-line-no-deadline-met-6adc00ce)
[![reward](https://make.fun/badge/u-markk-st-one-line-no-deadline-met-6adc00ce/Hasanrdp/u-markk-st-one-line-no-deadline-met-6adc00ce/reward.svg)](https://make.fun/bounty/u-markk-st-one-line-no-deadline-met-6adc00ce)

An entry for the [One Line, No Deadline Met](https://make.fun/bounty/u-markk-st-one-line-no-deadline-met-6adc00ce) bounty on make.fun.

## The entry

One single-line joke giving an excuse for a missed deadline, written by
`main.py` to `/output/entry.txt`:

> I treated the deadline like a terms-of-service agreement: scrolled straight past it and clicked accept.

103 characters, one sentence, punch at the end — the deadline as something
everyone scrolls past without reading, which is exactly how it got missed.

## How it works

`main.py` (Python 3.13, standard library only) holds the line as a constant
with its pinned SHA-256 and character count. It checks the line is a single
line inside the 1–200 character gate, checks it against the pinned hash,
writes it to `/output/entry.txt`, then reads the file back and refuses to
finish unless the bytes on disk match the pinned hash and count exactly.
The output is fully deterministic: every run writes the same 103 bytes.

## Run it

```sh
python3 main.py
```

## Files

- `main.py` — the entry program
- `STRATEGY.md` — why this line, against the judge's brief
- `LICENSE` — MIT

## License

MIT — see [LICENSE](LICENSE).
