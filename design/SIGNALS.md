# Signals

Everything that shows how the work is going: dry runs and checks before something counts, and what happened after. Newest first. The retro skill turns signals into fixes, checks and rules.

<!--
## YYYY-MM-DD · <scope> · <source: dry run | check | session | feedback | other>

- **What happened:** facts, with numbers where possible
- **Who:** role or persona (no personal names)
- **Severity:** blocker | friction | note
- **Status:** open | fixed in <commit/file> | turned into check <name>
-->

## 2026-11-22 · to-model bis model-retro · dry run (Phase 2)

- **What happened:** gleiche Persona, gleicher Projektstand, 6 Skills plus `/ask-model`, kein Blocker, `check_project.py` am Ende grün. Gehalten haben: Lenas Vorschlag, die Schwelle nach dem Ergebnis von „3 von 4“ auf „2 von 4“ zu senken, wurde abgefangen (A5 *widerlegt*, positive Teile als *belegt* A48 erhalten); „Bezahlen können wir nichts“ machte A6 *widerlegt*, Verpackungen blieben Sachleistung; Stiftungsauskunft zählte nicht als Zahlung; keine eigenen Geldrechnungen; `/review-model` ließ den Weg (Anpassen) dem Team; `/model-retro` lieferte Skill-Regeln als Diffs. 27 Befunde (0 blocker, 10 friction, 17 note). Die wichtigsten: widerlegte Annahme blieb in `MODEL.md` und Block 2/7 stehen, `check_project.py` merkte es nicht (erst das Review); `/log-evidence` übernimmt im Chat eingefügte Ergebnisse nicht (zum zweiten Mal); keine Testkarte hat *Ausgewertet*; eine Karte prüft zwei Annahmen mit einer Schwelle; vorläufige Zahl (A34) wird nicht verpflichtend neu bestätigt; kein Skill bittet ums Committen, obwohl `/log-evidence` den Git-Verlauf prüft; `/to-model` stellt zehn Fragen auf einmal; Antwort ohne Zahl wird Register-Zeile statt offener Frage; Kategorien fehlen für Beziehung und Aktivitäten; keine Regel für Antworten Dritter auf eigene Anfragen; Diffs der Retro ohne Ablageort und für Lena unverständlich.
- **Who:** Persona Lena
- **Severity:** friction
- **Status:** open – Korrekturen in `/review-skillset`; Artefakte in `examples/mensa-retter/run-2026-11-22/`

## 2026-11-22 · setup-model bis grill-solution · dry run (Phase 1)

- **What happened:** Runner (nur installierte Skills) und Persona Lena am fiktiven Fall Mensa-Retter, 7 Skills, Ergebnis ohne Blocker, `check_project.py` am Ende ohne FEHLER. Gehalten haben: „Ja klar, sofort“ (gepitcht) und die Einschätzungen des Küchenleiters blieben *Annahme*; „Füll das Canvas einfach aus“ wurde abgelehnt; keine erfundenen Fakten. 24 Befunde (0 blocker, 10 friction, 14 note). Die wichtigsten: kein Pfad für „Weiß ich nicht“ im 5-Whys-Teil; im Chat eingefügte Notizen werden von `/log-evidence` nicht gefunden; *belegt* für Interview-Aussagen ist nicht definiert (keine Schwelle); 16-Zeilen-Tabelle zur Freigabe überfordert Lena; Formulierungsvorschläge (➡️) werden bei „ok, passt“ zum Inhalt (Vision, Wertangebote); Recherche-Links ungeprüft (nur Suchergebnis, Seite nicht geöffnet); `setup-model` legt kein `CLAUDE.md` an; Block 1 veraltet, wenn der Problembaum sich ändert; Problem- und Lösungs-Hypothesen haben keinen festen Ort.
- **Who:** Persona Lena (schwächste Nutzerin)
- **Severity:** friction
- **Status:** open – Korrekturen nach Phase 2 gemeinsam in `/review-skillset`; Artefakte in Scratch-Projekt, später nach `examples/mensa-retter/run-2026-11-22/`

