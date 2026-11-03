# Walkthrough: Fictional sports events and conflicting sources

**Language:** **English** · [Deutsch](walkthrough.de.md) · [Home](../README.md)

**Warning: Not real events.** All teams, venues, dates and `example.org` sources are synthetic test data. Do not treat these as live fixtures.

## 1. Input material

Open [synthetic-sources.json](synthetic-sources.json). Three source snapshots describe two fictional events:

- `s1`: Basketball, **7 November 2026 at 15:00 CET**.
- `s2`: **The same basketball game**, but at **16:00 CET**.
- `s3`: Football, **8 November 2026 at 11:00 CET**, with **venue unknown**.

Here the `raw_text` fields are the provided source documents. URLs only serve as illustrative identifiers; there are no real live pages behind them.

## 2. Try it with ChatGPT or Claude

1. Provide all three `raw_text` blocks, with their `source_id` values, in your chat.
2. Copy the [extraction prompt](../prompts/event-extraction.md), using **no web search** in this deterministic offline test.
3. Ask for events, field-level source quotes, unknowns, and conflicting values.
4. Compare the result with [synthetic-events.json](synthetic-events.json).
5. Run the [separate validation prompt](../prompts/source-validation.md) against the same three original texts.

## 3. Expected output

| Event | Start time | Verification | Needs human review? |
| --- | --- | --- | --- |
| Beispielstadt Falcons vs. Nordpark Bears | **null** (conflict: 15:00 vs. 16:00) | `conflicting` | yes |
| SV Beispielstadt II vs. FC Süd | 8 Nov 2026, 11:00 CET | `source_supported` | yes, unknown venue |

`source_supported` means **the source contains a statement**, not that the game will definitely go ahead.

Both dates fall in CET (**UTC+01:00**), which is why the expected JSON values include that offset. Correct timezone conversion does not make a source fact correct.

## 4. Handling a conflict

- Keep **both** time candidates in `evidence`, with their exact quotations and `source_id`.
- Record the discrepancy in `conflicts`.
- Set canonical `start_datetime` to `null` and `review_required` to `true`.
- Do not pick the apparently more likely time.
- If a later source update resolves the discrepancy, keep the new snapshot and its check time.

## 5. Run automated checks

~~~bash
python -m pip install -r requirements-dev.txt
python -m unittest discover -s tests -v
~~~

The tests verify **the JSON Schema, source identifiers and whether evidence quotes occur in the corresponding input strings**. They cannot verify an actual sports event.

## 6. Next step

For meaningful evaluation, create an independently **human-reviewed** dataset of real permissible sources. Measure extraction precision, recall, freshness and review load, and document permissions and privacy requirements.
