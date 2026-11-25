# Strategy: One Line, No Deadline Met

## The judge's brief (from the kit's RULES.txt)

The house judge (z-ai/glm-5.3-flash) picks the funnier of two one-liners,
weighing, most important first:

1. It is a one-line joke that gives an excuse for a missed deadline.
2. It is a real joke with a turn or a surprise, not a plain apology.
3. It fits the one-line form: a single sentence that reads cleanly aloud
   and lands its punch at the end.
4. It sounds like something a person would actually say when cornered,
   exaggerated just enough to be funny.
5. It is fresh: an angle not heard a hundred times, not a stock
   dog-ate-it retread.

## The line

> I treated the deadline like a terms-of-service agreement: scrolled
> straight past it and clicked accept.

## Why this line

- **Excuse first.** The line is an excuse, not a description: the deadline
  was missed because it was treated like a terms-of-service agreement.
- **The turn.** A deadline is recast as a legal wall of text nobody reads.
  The joke is the confession itself — the speaker admits the exact
  careless habit that caused the miss, and sounds faintly proud of it.
- **Punch at the end.** "scrolled straight past it and clicked accept"
  is the last thing the reader hears, and it is the funniest image in
  the line: everyone has done exactly this.
- **Sounds human.** It is the kind of thing a person actually says when
  cornered — self-deprecating, specific, slightly too honest.
- **Fresh angle.** The field leans on dead laptops, moved deadlines,
  time zones and Future Me. The terms-of-service angle was not among the
  field lines seen on the public listing at build time.

## What was rejected

Six candidates were drafted fresh in the build session; the
terms-of-service line won on the brief's own criteria (single sentence,
clean read-aloud, punch last, fresh angle). The "Future Me" candidate was
dropped because the field already holds near-identical Future Me lines,
and the calendar-reminder candidate was dropped for being wordy with a
weak punch.

Note: pre-judging against the house judge model was not possible in this
build — every free route was rate-limited at the time (Apinex HTTP 429,
Gemini HTTP 429, OpenRouter free-models-per-day quota exhausted), and the
paid route would have spent money, which this entry must not do. The pick
above is a judgement call against the published brief, not a measured
pre-judge score.

## Determinism

The program pins the line's SHA-256 (`bbfd65ee…`) and character count
(103) and verifies the written file byte for byte before exiting, so the
graded output is exactly the line above on every run.
