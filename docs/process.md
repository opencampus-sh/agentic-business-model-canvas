# Der Prozess

Der Prozess folgt dem Canvas von links nach rechts und dem Kurshandbuch „Become a Changemaker“ – aber er ist eine Schleife: Jede Testrunde führt über die Auswertung zu einer Entscheidung, und die Entscheidung führt zurück zu Tests, zum Modell oder zur Lösung.

## Hauptablauf

| Schritt | Skill | Agent macht | Stop-Point (Team entscheidet) | Canvas |
|---|---|---|---|---|
| 1. Projekt anlegen | `/setup-model` | Ordner und Dateien anlegen, bisherige Ergebnisse als Annahmen übernehmen | Ort, Team, Idee, bisherige Ergebnisse | alle |
| 2. Problem schärfen | `/grill-problem` | in Runden fragen, 5 Whys und Folgen ordnen, Problembaum zeichnen | Kernproblem, Ursachen, Folgen, Zielgruppe, Hypothesen | 1, 2, 6 |
| 3. Interviews vorbereiten | `/to-interview-guide` | Leitfaden mit offenen Fragen zu den Hypothesen | Leitfaden, Gesprächspartner:innen | 5 |
| – | *Team* | – | Interviews führen, Notizen eintragen | – |
| 4. Belege auswerten | `/log-evidence` | Aussagen herausziehen, Muster, Zuordnung zu Annahmen, Status-Vorschläge | jede Status-Änderung | 5, 6, 10 |
| 5. Bestehende Lösungen | `/map-solutions` | recherchieren mit Quellen, SWOT entwerfen | welche Lösungen, Fazit | 5, 6 |
| 6. Lösung schärfen | `/grill-solution` | in Runden fragen; kritische Annahmen vorschlagen | Vision, Lösung, Fall, Wertangebot, Kriterien, kritische Annahmen | 1–4, 6 |
| 7. Geschäftsmodell | `/to-model` | Gliederung, Social Business Model Canvas mit IDs, Widersprüche | jedes Feld | 6, 7 |
| 8. Testplan | `/to-tests` | Testkarten mit Messgröße und vorgeschlagener Schwelle | Tests, Reihenfolge, Schwellen | 4, 9 |
| – | *Team* | – | testen, Ergebnisse eintragen | – |
| 9. Belege auswerten | `/log-evidence` | Ergebnis gegen Schwelle, Status-Vorschläge | jede Status-Änderung | 6, 10 |
| 10. Review | `/review-model` | zwei Achsen: Beleg und Wirkung | weiter testen, anpassen oder neu ansetzen | 8, 11 |
| 11. Retro | `/model-retro` | Signale erklären, Checks und Regeln vorschlagen | was übernommen wird | 10, 11 |

Schritte 8–11 wiederholen sich in jeder Testrunde. Ein Pivot führt zurück zu Schritt 6 oder, wenn das Problem selbst falsch war, zu Schritt 2.

## Einstiege

- **Mitten im Kurs:** `/setup-model` mit euren bisherigen Ergebnissen (z. B. Notion-Export). Alles wird als *Annahme* übernommen; `/ask-model` sagt, wo ihr weitermacht.
- **Idee steht, keine Interviews:** `/grill-problem`, dann `/to-interview-guide`. Die Lösung kommt nach den Interviews.
- **Ein Test ist anders ausgegangen als gedacht:** `/log-evidence`, dann `/review-model`.

## Dateien im Projektordner

| Datei | Inhalt | Geschrieben von |
|---|---|---|
| `CANVAS.md` | Das Canvas | alle Skills |
| `ASSUMPTIONS.md` | Annahmen-Register: ID, Aussage, Kategorie, Status, Quelle, kritisch, Test | alle Skills; Status-Änderungen nur `/log-evidence` mit dem Team |
| `PROBLEM.md` | Kernproblem, 5 Whys, Folgen, Problembaum, Zielgruppe | `/grill-problem`, `/log-evidence` |
| `INTERVIEWS.md` | Leitfaden, Notizen (vom Team), Auswertung | `/to-interview-guide`, Team, `/log-evidence` |
| `SOLUTIONS.md` | Bestehende Lösungen, SWOT, Fazit | `/map-solutions` |
| `MODEL.md` | Social Business Model Canvas (CC BY-SA 4.0) | `/to-model` |
| `TESTS.md` | Testkarten mit Schwelle und Ergebnis | `/to-tests`, Team, `/log-evidence` |
| `DECISIONS.md` | Entscheidungen mit Begründung und Alternativen | alle Skills an Stop-Points |
| `SIGNALS.md` | Ergebnisse, Überraschungen, Feedback | `/log-evidence`, `/review-model`, `/model-retro` |
| `SKILL-PROPOSALS.md` | Vorschläge für das Skillset (Satz in einfacher Sprache plus Diff), zum Einreichen als Issue | `/model-retro` |
| `CLAUDE.md` | eine Zeile `@AGENTS.md`, damit Claude Code die Regeln liest | `/setup-model` |

`/setup-model` trägt alle Dateien in einen Abschnitt der `AGENTS.md` ein, damit jeder Skill sie findet.
