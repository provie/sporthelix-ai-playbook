**Sprache:** [English](walkthrough.md) · **Deutsch** · [Startseite](../README.de.md)

# Walkthrough: Fiktive Sportevents mit widersprüchlichen Quellen

**Achtung: Keine echten Veranstaltungen.** Alle Teams, Termine, Veranstaltungsorte und Quellen unter `example.org` sind explizit fiktive Testdaten. Bitte nicht als aktuelle Spielpläne verwenden.

## 1. Quellen

Öffne [synthetic-sources.json](synthetic-sources.json). Die drei Text-Snapshots simulieren zwei Arten lokaler Sportevents:

- `s1`: Basketballspiel, **07.11.2026, 15:00 Uhr (MEZ)**.
- `s2`: **dasselbe** Basketballspiel, aber **07.11.2026, 16:00 Uhr (MEZ)**.
- `s3`: Fußballspiel, **08.11.2026, 11:00 Uhr (MEZ)**, **Spielort nicht bekannt**.

Hier sind die Rohtexte die „Quellen“. Die URLs dienen nur als illustrative IDs und sind nicht real abrufbar.

## 2. ChatGPT / Claude: manuell testen

1. Stelle die drei `raw_text`-Blöcke samt `source_id` im Chat bereit.
2. Kopiere [den Extraction-Prompt](../prompts/event-extraction.de.md); arbeite **ohne Live-Websuche**, damit der Fixture-Vergleich reproduzierbar bleibt.
3. Frage nach Event-Liste, Feldbelegen, Konflikten und unbekannten Werten.
4. Vergleiche das Resultat mit [synthetic-events.json](synthetic-events.json).
5. Kopiere [den separaten Validation-Prompt](../prompts/source-validation.de.md) und lass Belege erneut mit den drei Raw-Texten abgleichen.

## 3. Erwartetes Ergebnis

| Event | Extrahierte Startzeit | Prüfstatus | Review? |
| --- | --- | --- | --- |
| Beispielstadt Falcons – Nordpark Bears | **null**, weil 15:00 vs. 16:00 | `conflicting` | ja |
| SV Beispielstadt II – FC Süd | 08.11.2026 11:00 MEZ | `source_supported` | ja, da Spielort fehlt |

Der Status `source_supported` zeigt **nur**, dass eine Quelle einen Wert angibt. Er ist keine aktuelle Durchführungsbestätigung.

Beachte die Zeitzone: `MEZ` am 7./8. November 2026 entspricht `+01:00`. Eine ableitbare Zeitzone ersetzt aber nicht die Prüfung auf Schreib- oder Quellenfehler.

## 4. Wie Quellenkonflikte behandelt werden

- Beide alternativen Uhrzeiten in `evidence` mit jeweiligem `source_id` und **exaktem** Zitat erhalten.
- Einen Konflikt unter `conflicts` dokumentieren.
- Den kanonischen Wert `start_datetime` auf `null` setzen und `review_required=true`.
- Keine Zeit aufgrund vermeintlicher „höherer Wahrscheinlichkeit“ auswählen.
- Wenn eine spätere Änderung Quellenkonflikte auflöst, neue Snapshots und einen neuen Prüfzeitpunkt dokumentieren.

## 5. Automatisierte Prüfung

```bash
python -m pip install -r requirements-dev.txt
python -m unittest discover -s tests -v
```

Die Tests prüfen **Schema, Quellverweise und ob jedes Belegzitat im betreffenden Rohtext vorkommt**. Eine echte externe Veranstaltung kann man damit nicht bestätigen.

## 6. Nächster sinnvoller Ausbauschritt

Für eine belastbare Evaluation eine separate **manuell geprüfte** Stichprobe echter Quellen erstellen, Berechtigungen und Nutzungsbedingungen berücksichtigen, Precision/Recall und Freshness messen und Modell-/Promptvarianten vergleichen.
