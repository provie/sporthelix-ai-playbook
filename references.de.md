# Quellen und weiterführende Literatur

**Sprache:** [English](references.md) · **Deutsch** (diese Seite) · [Startseite](README.de.md)

Diese Liste enthält ausgewählte Quellen und erklärt **wofür** sie praktisch nützlich sind. Keine einzelne Quelle beweist, dass ein Prompt Halluzinationen vollständig verhindert.

## Prompting, Grounding, Structured Outputs

1. **Anthropic – Reduce hallucinations**: [Dokumentation](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations). Praktisch: Unsicherheit explizit zulassen, wörtliche Textbelege verlangen und Aussagen anhand von Zitaten prüfen.
2. **OpenAI – Structured Outputs**: [Dokumentation](https://developers.openai.com/api/docs/guides/structured-outputs). Praktisch: Datentypen und Ausgabestruktur verlässlich erzwingen. **Grenze:** Schemavalidität belegt keine Tatsachen.
3. **Anthropic – Building effective agents** (19.12.2024): [Artikel](https://www.anthropic.com/research/building-effective-agents). Praktisch: Einfache und testbare Workflows bevorzugen; nur bei konkretem Nutzen agentische Komplexität einführen. Manche Tooling-Details sind inzwischen älter.

## Web-Information-Extraction und Datenqualität

4. **Yang et al. – LiveWeb-IE: A Benchmark For Online Web Information Extraction** (ICLR 2026): [Paper auf arXiv](https://arxiv.org/abs/2603.13773). Forschung zu Extraktion von realen, sich verändernden Websites. Das Paper stellt einen Benchmark und ein agentisches Verfahren vor; daraus folgt **keine** Garantie für realistische Event-Abdeckung.
5. **W3C PROV-O – Provenance Ontology** (2013): [W3C Recommendation](https://www.w3.org/TR/prov-o/). Praktisch: Herkunft, Ableitungen und Verarbeitungsschritte von Datensätzen nachvollziehbar modellieren.

## Sportdaten und Event-Modelle

6. **Schema.org – SportsEvent**: [Typdefinition](https://schema.org/SportsEvent). Praktisch: Semantik von Sportevents, Sportarten, Teilnehmern, Teams und Zeitangaben verstehen.
7. **OpenActive – Modelling Opportunity Data 2.1, Editor's Draft** (10.09.2026): [Entwurf](https://openactive.io/modelling-opportunity-data/EditorsDraft/). Praktisch: Datenmodell für die **Teilnahme** an sportlichen Aktivitäten, Sessions, Anlagen und Buchungsmöglichkeiten. **Grenze:** Zuschauer-Sportevents und Spielpläne sind nicht vollständig durch den primären Anwendungsfall des Modells abgedeckt.

## Was bedeutet das für einen konkreten Prompt?

- **Textbeleg und `null`:** Anthropic Grounding/Unsicherheit.
- **Schema und Felder:** OpenAI Structured Outputs sowie diese Repo-Schema-Datei.
- **Discovery → Extraction → Validation:** Einfache Workflow-Zerlegung, inspiriert durch Agent-Engineering-Praxis.
- **Quelle/Abrufzeit/Änderung:** Provenance-Ideen und dynamische Web-Information-Extraction.
- **Sportliche Domänenbegriffe:** Schema.org SportsEvent und – für Teilnahmeangebote – OpenActive.

Die **konkrete Kombination als Sporthelix-Playbook** ist eine praktische Synthese und **kein unverändert aus einem Paper übernommenes oder wissenschaftlich validiertes Verfahren**.
