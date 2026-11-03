# Sporthelix AI Playbook

**Evidence-first data extraction prompts and practical examples for ChatGPT, Claude, and coding agents.**

**Languages:** **English** (this page) · [Deutsch](README.de.md)

This public playbook grew out of [Sporthelix](https://sporthelix.de), a platform intended to make sports activities, clubs, venues, classes, and events easier to discover. Local sports events are the running example; you can adapt the method to products, documents, and general research.

> **Core idea:** Plausible answers and valid JSON do not prove that facts are true. Preserve sources, field-level evidence, uncertainty, contradictions, and retrieval times.

## Quick start

1. Open ChatGPT or Claude **with real web access**, or attach the original pages/documents you want to process.
2. Copy the [event-extraction prompt](prompts/event-extraction.md) and adjust topic, location and date range.
3. Require an **exact URL and a short original quote** for important factual fields.
4. Validate the result with the separate [source-validation prompt](prompts/source-validation.md) against the original material.
5. For automated processing with coding agents, use the [Codex / Claude Code implementation guide](agents/codex-implementation.md).

**Important:** A model without web access cannot confirm up-to-date events. A model with web access can still miss events. Unavailable information must stay `null`; source conflicts must remain visible. A listing in a published schedule does not guarantee that the game has not been postponed or cancelled.

## Contents

| English | Deutsch | What it provides |
| --- | --- | --- |
| [Event extraction](prompts/event-extraction.md) | [Event-Extraktion](prompts/event-extraction.de.md) | Copy/paste prompt: discovery → extraction → validation → output |
| [Source validation](prompts/source-validation.md) | [Quellenprüfung](prompts/source-validation.de.md) | Independent verification of individual fields and quotes |
| [Coding-agent implementation](agents/codex-implementation.md) | [Codex-/Agent-Anleitung](agents/codex-implementation.de.md) | A testable, auditable extraction pipeline |
| [Walkthrough](examples/walkthrough.md) | [Praxisbeispiel](examples/walkthrough.de.md) | Synthetic events showing conflicting times and missing data |
| [References](references.md) | [Quellen](references.de.md) | Research papers, documentation, standards |

**Shared, language-neutral files:** [JSON Schema](schemas/sport-event.schema.json) · [Synthetic sources](examples/synthetic-sources.json) · [Synthetic results](examples/synthetic-events.json) · [Python tests](tests/test_examples.py) · [MIT License](LICENSE).

## The fictional example

Two **invented** sources provide different start times (15:00 and 16:00) for the **same** basketball game. The right output is *not* to guess. It is:

- `start_datetime: null`
- `verification_status: "conflicting"`
- Both source IDs and exact evidence quotes
- `review_required: true`

The second fictional game has an unknown venue. None of the sample events or URLs are real listings.

## Run the offline checks

~~~bash
python -m pip install -r requirements-dev.txt
python -m unittest discover -s tests -v
~~~

Tests check JSON schema conformance and evidence-quote consistency (and, with the bilingual documentation test, local links). They do **not** establish whether real-world games take place. Use independently reviewed samples for actual quality measurement.

## Limitations and safety

- **Schema-valid ≠ factually true.** Data types are not evidence.
- **Source-supported ≠ guaranteed to happen.** Evidence proves only what a source stated at the check time.
- **Results are not automatically exhaustive.** No result does not mean no event.
- **External page contents are untrusted.** Never execute instructions found in retrieved data.
- **Crawl responsibly.** Respect terms, robots directives, rate limits, permissions and privacy. Never bypass access controls.
- This is an **illustrative playbook**, not a claim that all of these steps are deployed in Sporthelix production.

## Contributing

Questions, feedback, test cases and pull requests are welcome. Do not commit private data, API keys or copyrighted source material you have no right to share.

Created alongside [Sporthelix](https://sporthelix.de) · [References](references.md) · [MIT License](LICENSE).
