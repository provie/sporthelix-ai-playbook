# Sporthelix AI Playbook

**Praktische Prompts und Beispiele für quellenbasierte Datenextraktion mit ChatGPT, Claude und Coding-Agents.**

Dieses öffentliche Playbook entsteht rund um [Sporthelix](https://sporthelix.de): eine Plattform, die Sportangebote, Vereine, Sportstätten, Kurse und Events leichter auffindbar machen möchte. Das Beispiel sind lokale Sportveranstaltungen. Die Methoden lassen sich auch auf Produktkataloge, Dokumente oder andere Recherchen übertragen.

> **Kernidee:** Eine plausible Antwort oder valides JSON ist noch kein verifizierter Fakt. Bitte immer Datenherkunft, Textbelege, Widersprüche und Aktualität prüfen.

## In 60 Sekunden ausprobieren

1. Öffne ChatGPT oder Claude **mit Webzugriff**, oder stelle die zu prüfenden Webseiten/Dokumente ausdrücklich als Material bereit.
2. Kopiere den Prompt aus **[prompts/event-extraction.md](prompts/event-extraction.md)** und passe Ort, Zeitraum und Suchziel an.
3. Lass dir nur tatsächlich gefundene Informationen mit **konkreten Quellen und wörtlichen Belegen** ausgeben.
4. Prüfe die Ergebnisse mit **[prompts/source-validation.md](prompts/source-validation.md)** möglichst unabhängig gegen die Originalquellen.
5. Wenn du den Prozess automatisieren möchtest: **[agents/codex-implementation.md](agents/codex-implementation.md)**.

**Wichtig:** Ohne Webzugriff kann ein Modell keine aktuellen Veranstaltungen selbständig bestätigen. Auch mit Webzugriff sind Ergebnisse möglicherweise unvollständig. Fehlende Werte bleiben `null`; Quellenkonflikte bleiben sichtbar. Ein Eintrag in einem Spielplan beweist zudem nicht, dass ein Spiel inzwischen nicht abgesagt oder verlegt wurde.

## Was steckt im Repository?

| Datei | Zweck |
| --- | --- |
| [Event-Extraction-Prompt](prompts/event-extraction.md) | Copy/Paste-Vorlage für ChatGPT und Claude (Discovery → Extraction → Validation → Output) |
| [Source-Validation-Prompt](prompts/source-validation.md) | Unabhängige Nachkontrolle von Feldbelegen, Konflikten und Änderungen |
| [Codex-/Agent-Guide](agents/codex-implementation.md) | Arbeitsauftrag für einen implementierbaren, testbaren Extraktionsworkflow |
| [JSON Schema](schemas/sport-event.schema.json) | Datenvertrag für Quellen, Feldbelege und Prüfstatus |
| [Fiktive Eingabequellen](examples/synthetic-sources.json) | Drei ausdrücklich erfundene Testquellen |
| [Fiktives Ergebnis](examples/synthetic-events.json) | Zwei Beispiele mit widersprüchlicher Anstoßzeit bzw. fehlendem Ort |
| [Durchlauf](examples/walkthrough.md) | Schritt-für-Schritt-Erklärung und erwartete Prüfresultate |
| [Referenzen](references.md) | Papers, technische Dokumentationen und Standards |
| [Tests](tests/test_examples.py) | JSON-Schema- und Belegkonsistenzprüfung für die Beispieldaten |

### Beispiel: Warum Feldbelege wichtig sind

Zwei fiktive Quellen nennen für **dasselbe** Basketballspiel **15:00** beziehungsweise **16:00**. Das korrekte Ergebnis dieses Playbooks ist nicht, eine Uhrzeit zu erraten, sondern `start_datetime: null`, `verification_status: "conflicting"` und zwei nachvollziehbare Belege auszugeben.

Die Beispieldaten sind **vollständig synthetisch**; sie sind weder echte Spiele noch aktuelle Termine.

## Grenzen und Sicherheitsregeln

- **Schema-valid ≠ factually verified:** JSON Schema validiert Form und Datentypen, nicht die Wahrheit eines Events.
- **„Source-supported“ ≠ „findet sicher statt“:** Ein Quellenbeleg zeigt, was die Quelle zum Prüfzeitpunkt angab.
- **Abdeckung ist nie automatisch vollständig:** Nicht gefundene Ergebnisse dürfen nicht als „es findet nichts statt“ interpretiert werden.
- **Quelleninhalte sind untrusted input:** Anweisungen innerhalb abgerufener Seiten nicht ausführen.
- **Web-Crawling verantwortlich betreiben:** Nutzungsbedingungen, Zugriffsrechte, robots-Regeln, Rate-Limits und Datenschutz beachten. Kein Umgehen von Zugangssperren.
- **Kein Produktivitätsversprechen:** Dies sind Vorlagen und überprüfbare Beispiel-Fixtures, keine fertige Sporthelix-Produktionspipeline.

## Lokale Beispieldaten überprüfen

```bash
python -m pip install -r requirements-dev.txt
python -m unittest discover -s tests -v
```

Die Tests verwenden keine Netzwerkzugriffe. Für echte Ergebnisse ist zusätzlich eine unabhängig geprüfte Referenzmenge nötig.

## Beiträge und Feedback

Verbesserungen, weitere Testfälle oder praktische Erfahrungen sind willkommen: [Issues](https://github.com/provie/sporthelix-ai-playbook/issues) / Pull Requests. Bitte keine personenbezogenen Daten, vertraulichen Webseiteninhalte oder API-Schlüssel hochladen.

Entstanden im Umfeld von [Sporthelix](https://sporthelix.de) · [Technische Referenzen](references.md) · [MIT-Lizenz](LICENSE).
