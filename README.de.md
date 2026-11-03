# Sporthelix AI Playbook

**Sprachen:** [English](README.md) · **Deutsch** (diese Seite)

**Praktische Prompts und Beispiele für quellenbasierte Datenextraktion mit ChatGPT, Claude und Coding-Agents.**

Dieses öffentliche Playbook entsteht rund um [Sporthelix](https://sporthelix.de): eine Plattform, die Sportangebote, Vereine, Sportstätten, Kurse und Events leichter auffindbar machen möchte. Lokale Sportveranstaltungen dienen als Beispiel. Die Methoden lassen sich auch auf Produktdaten, Dokumente oder andere Recherchen übertragen.

> **Kernidee:** Plausible Antworten und valides JSON beweisen noch keine korrekten Fakten. Quellen, Textbelege, Unsicherheiten, Widersprüche und Abrufzeitpunkte müssen nachvollziehbar bleiben.

## Schnellstart

1. Öffne ChatGPT oder Claude **mit tatsächlichem Webzugriff** oder stelle die Originalseiten bzw. Dokumente zur Verfügung.
2. Kopiere den [deutschen Event-Extraktions-Prompt](prompts/event-extraction.de.md) und passe Sportart, Ort und Zeitraum an.
3. Verlange zu wichtigen Fakten die **konkrete URL und ein kurzes wörtliches Zitat**.
4. Prüfe das Ergebnis mit dem separaten [Quellenprüfungs-Prompt](prompts/source-validation.de.md) gegen das Originalmaterial.
5. Für automatisierte Workflows mit Coding-Agents nutze die [deutsche Codex-/Claude-Code-Anleitung](agents/codex-implementation.de.md).

**Wichtig:** Ohne Webzugriff kann ein Modell aktuelle Veranstaltungen nicht selbständig bestätigen. Auch mit Webzugriff können Events fehlen. Unbekannte Werte bleiben `null`; Quellenkonflikte werden nicht stillschweigend aufgelöst. Ein veröffentlichter Spielplan beweist nicht, dass ein Spiel inzwischen nicht verschoben oder abgesagt wurde.

## Inhalte – Deutsch und Englisch

| Deutsch | English | Nutzen |
| --- | --- | --- |
| [Event-Extraktion](prompts/event-extraction.de.md) | [Event extraction](prompts/event-extraction.md) | Kopierbarer Prompt: Quellenfindung → Extraktion → Validierung → Ausgabe |
| [Quellenprüfung](prompts/source-validation.de.md) | [Source validation](prompts/source-validation.md) | Unabhängiger Abgleich wichtiger Feldwerte und Textzitate |
| [Codex-/Agent-Anleitung](agents/codex-implementation.de.md) | [Coding-agent implementation](agents/codex-implementation.md) | Arbeitsauftrag für eine testbare Datenpipeline |
| [Praxisbeispiel](examples/walkthrough.de.md) | [Walkthrough](examples/walkthrough.md) | Fiktive Sportevents mit widersprüchlichen Zeiten und fehlenden Angaben |
| [Quellen](references.de.md) | [References](references.md) | Papers, technische Dokumentationen und Standards |

**Gemeinsam genutzte, sprachunabhängige Dateien:** [JSON-Schema](schemas/sport-event.schema.json) · [Fiktive Quellen](examples/synthetic-sources.json) · [Fiktive Ergebnisse](examples/synthetic-events.json) · [Python-Tests](tests/test_examples.py) · [MIT-Lizenz](LICENSE).

## Fiktives Beispiel: Warum Feldbelege wichtig sind

Zwei **erfundene** Quellen nennen für **dasselbe** Basketballspiel unterschiedliche Startzeiten (15:00 und 16:00 Uhr). Die korrekte Ausgabe lautet nicht „wahrscheinlich 15:00 Uhr“, sondern:

- `start_datetime: null`
- `verification_status: "conflicting"`
- Beide Quellen-IDs mit wörtlichen Belegen
- `review_required: true`

Beim zweiten fiktiven Spiel ist der Spielort unbekannt. **Keine** der Veranstaltungen oder Quellen-URLs in den Beispielen ist real.

## Lokale Offline-Tests

```bash
python -m pip install -r requirements-dev.txt
python -m unittest discover -s tests -v
```

Die Tests prüfen Schema, Quellenbelege und lokale Links zwischen den deutschen und englischen Dokumenten. Sie können **nicht** feststellen, ob reale Spiele stattfinden. Dafür braucht man unabhängig überprüfte Referenzdaten.

## Grenzen und Sicherheitsregeln

- **Gültiges JSON ≠ korrekte Fakten:** Datentypen sind keine Beweise.
- **Durch Quellen belegte Angaben ≠ garantierte Durchführung:** Der Beleg zeigt nur, was die Quelle zum Prüfzeitpunkt angab.
- **Keine automatische Vollständigkeit:** „Nicht gefunden“ bedeutet nicht „findet nicht statt“.
- **Externe Inhalte sind nicht vertrauenswürdig:** Anweisungen aus abgerufenen Webseiten nicht ausführen.
- **Verantwortungsvoll crawlen:** Nutzungsbedingungen, robots-Regeln, Ratenbegrenzungen, Rechte und Datenschutz beachten. Keine Zugriffssperren umgehen.
- **Anwendungsbeispiele, keine Produktivbehauptung:** Das Playbook dokumentiert Methoden, nicht den vollständigen produktiven Implementierungsstand von Sporthelix.

## Mitwirken

Feedback, zusätzliche Testfälle, Issues und Pull Requests sind willkommen. Bitte keine vertraulichen Daten, API-Schlüssel oder urheberrechtlich geschützten Quellmaterialien ohne entsprechende Berechtigung einreichen.

Erstellt im Umfeld von [Sporthelix](https://sporthelix.de) · [Quellen](references.de.md) · [MIT-Lizenz](LICENSE).
