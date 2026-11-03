# References and further reading

**Language:** **English** · [Deutsch](references.de.md) · [Home](README.md)

Selected references with an explanation of **how to use them**. None of these resources guarantees that a prompt will eliminate hallucinations.

## Grounding, prompts, and structured outputs

1. **Anthropic — Reduce hallucinations:** [Docs](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations). **Try:** allow uncertainty, request short verbatim quotes, and cross-check claims against the quoted text.
2. **OpenAI — Structured Outputs:** [Docs](https://developers.openai.com/api/docs/guides/structured-outputs). **Try:** apply types and structure to model output. **Caution:** JSON that matches a schema may still describe an invented event.
3. **Anthropic — Building effective agents** (December 2024): [Engineering article](https://www.anthropic.com/research/building-effective-agents). **Try:** keep workflows simple and testable; add agentic planning only when it solves a measured problem. Some tool-related examples may have evolved.

## Web information extraction and data provenance

4. **LiveWeb-IE: A Benchmark for Online Web Information Extraction** (ICLR 2026): [arXiv paper](https://arxiv.org/abs/2603.13773). **Learn:** what makes extracting information from changing, live websites difficult. **Caution:** benchmark research does not establish completeness of real-world sports listings.
5. **W3C PROV-O — Provenance Ontology** (2013): [W3C Recommendation](https://www.w3.org/TR/prov-o/). **Learn:** how to represent the origins and derivation of information.

## Event and sports data standards

6. **Schema.org — SportsEvent:** [Type reference](https://schema.org/SportsEvent). **Learn:** common terminology for sports events, participants, and related metadata.
7. **OpenActive — Modelling Opportunity Data 2.1, Editor's Draft** (September 2026): [Draft specification](https://openactive.io/modelling-opportunity-data/EditorsDraft/). **Learn:** how to model opportunities to **participate** in sports activities, sessions, venues and bookings. **Caution:** spectator fixtures are not the central use case.

## Putting the ideas into practice

- **Source quote + explicit null:** grounded answers and uncertainty (Anthropic).
- **Output shape:** Structured Outputs plus this repository's JSON Schema (OpenAI).
- **Discovery → extraction → validation:** practical separation of testable workflow stages.
- **Source, retrieval time and changes:** provenance principles and dynamic web extraction.
- **Sports-specific fields:** Schema.org SportsEvent; OpenActive for participation opportunities.

**The Sporthelix playbook is an engineering synthesis, not a research-validated method copied directly from any single paper.**
