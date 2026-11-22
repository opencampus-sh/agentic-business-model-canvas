# Skill map

Wie das Skillset läuft: der Prozess, die Skills, die ihn tragen, und die Dateien, die sie im Projektordner eines Teams teilen.

> **Status:** Entwurf aus `/to-skill-map`, wartet auf die Entscheidungen S1–S5.

## Process

```
setup ──► Problem ──► Interview-Leitfaden ──► (Team interviewt) ──► Belege auswerten ──► bestehende Lösungen
                ▲                                                          │
                └──────────── Problembaum ergänzen ◄────────────────────────┘
                                                                           ▼
             Lösung & Vision ──► Geschäftsmodell ──► Testplan ──► (Team testet MVP) ──► Belege auswerten ──► Review
                  ▲                     ▲                ▲                                                  │
                  │                     └─────── anpassen ◄─────── Lernen & Entscheiden ◄────────────────────┤
                  └──────────────────────────── Pivot ◄────────────────── Retro: Checks, Regeln ◄────────────┘
```

Reihenfolge wie im Handbuch (M7): Problem und Zielgruppe, Interviews, Vision, bestehende Lösungen, Lösung, Nutzer:innen vs. Kund:innen, Wertangebot, Social Business Model Canvas, MVP.

| Schritt | Skill | Agent macht | Stop-Point (Team entscheidet) | Canvas-Blöcke |
|---|---|---|---|---|
| 1. Projekt anlegen | `/setup-model` | Ordner und Dateien anlegen, vorhandene Ergebnisse (z. B. Notion-Export) einlesen und verlinken | Team, Idee in einem Satz, was schon vorliegt | alle |
| 2. Problem schärfen | `/grill-problem` | in Runden fragen, 5 Whys und Folgen strukturieren, Problembaum zeichnen, Problem-Hypothesen ins Register | Kernproblem, Ursachen, Folgen, Zielgruppe, welche Hypothesen | 1, 2, 6 |
| 3. Interviews vorbereiten | `/to-interview-guide` | Leitfaden aus den Problem-Hypothesen, offene Fragen, kein Pitch | der Leitfaden, wen ihr fragt | 5 |
| 4. Belege auswerten | `/log-evidence` | Notizen des Teams clustern oder Testergebnisse mit der Schwelle vergleichen; Aussagen den Annahmen zuordnen; Status-Änderungen vorschlagen; Problembaum ergänzen | jede Status-Änderung, jedes Muster | 5, 6, 10 |
| 5. Bestehende Lösungen | `/map-solutions` | recherchieren, SWOT je Lösung entwerfen, alles mit Quelle und als *recherchiert* | welche Lösungen relevant sind, Fazit | 5, 6 |
| 6. Lösung schärfen | `/grill-solution` | Vision, Lösung, Lösungs-Hypothesen, Nutzer:innen vs. Kund:innen (vier Fälle), Wertangebot (mit Verweis auf das Value Proposition Canvas), Erfolgskriterien | Vision, Lösung, Fall, Wertangebot, kritische Annahmen, Kriterien | 1–4, 6 |
| 7. Geschäftsmodell | `/to-model` | Social Business Model Canvas aus Canvas und Register entwerfen; jedes Feld verweist auf Annahmen; Widersprüche markieren | jedes Feld; wer zahlt | 7, 6 |
| 8. Testplan | `/to-tests` | Testkarte je kritischer Annahme: Test, Messgröße, Schwelle, mit wem, bis wann; MVP-Ideen | welche Tests, Schwellen | 9, 4 |
| 9. Review | `/review-model` | zwei Achsen: Beleg (Register, Schwellen, Konsistenz) und Wirkung (dient das Modell der Herausforderung und den Nutzer:innen, trägt es sich?) | weiter testen, anpassen oder Pivot | 8, 11 |
| 10. Retro | `/model-retro` | Signale erklären, fragen, warum kein Check sie gefunden hat; Checks, Canvas-Änderungen, Skill-Regeln vorschlagen | was übernommen wird | 10, 11 |

Schritte 4–9 wiederholen sich in jeder Lean-Schleife. `/ask-model` empfiehlt den nächsten Schritt, `/show-canvas` zeigt das Canvas.

## Skills

| Skill | Role | User-invoked | Reads | Writes | Canvas blocks | Status | Adapted from |
|---|---|---|---|---|---|---|---|
| `setup-model` | setup | ja | Projektordner, Notion-Export | alle Projektdateien, Abschnitt in `AGENTS.md` | alle | planned | `setup-course`, `setup-matt-pocock-skills` |
| `ask-model` | router | ja | `CANVAS.md`, Register, Tests | – | – | planned | `ask-course`, `ask-matt` |
| `show-canvas` | core | ja | `CANVAS.md`, `DECISIONS.md` | `build/canvas.html` | alle | drafted (core) | Kern |
| `grill-problem` | grill | ja | `CANVAS.md`, `PROBLEM.md`, `ASSUMPTIONS.md` | `PROBLEM.md`, `ASSUMPTIONS.md`, `CANVAS.md`, `DECISIONS.md` | 1, 2, 6 | planned | `grilling`, `grill-course` |
| `to-interview-guide` | produce | ja | `PROBLEM.md`, `ASSUMPTIONS.md` | `INTERVIEWS.md` (Leitfaden) | 5 | planned | – |
| `log-evidence` | inventory | ja | `INTERVIEWS.md`, `TESTS.md`, `ASSUMPTIONS.md` | `ASSUMPTIONS.md`, `INTERVIEWS.md` (Auswertung), `TESTS.md` (Ergebnis), `PROBLEM.md`, `SIGNALS.md`, `CANVAS.md` | 5, 6, 10 | planned | – |
| `map-solutions` | inventory | ja | `PROBLEM.md`, `CANVAS.md` | `SOLUTIONS.md`, `ASSUMPTIONS.md`, `CANVAS.md` | 5, 6 | planned | `map-resources` |
| `grill-solution` | grill | ja | alle Projektdateien | `CANVAS.md`, `ASSUMPTIONS.md`, `DECISIONS.md` | 1–4, 6 | planned | `grilling`, `grill-course` |
| `to-model` | produce | ja | `CANVAS.md`, `ASSUMPTIONS.md`, `SOLUTIONS.md` | `MODEL.md`, `ASSUMPTIONS.md`, `CANVAS.md` | 6, 7 | planned | `to-spec` |
| `to-tests` | plan | ja | `ASSUMPTIONS.md`, `CANVAS.md`, `MODEL.md` | `TESTS.md`, `CANVAS.md` | 4, 9 | planned | `to-experiments` (DS), `to-spec` |
| `review-model` | review | ja | alle Projektdateien | `DECISIONS.md`, `CANVAS.md` | 8, 11 | planned | `code-review`, `review-unit` |
| `model-retro` | retro | ja | `SIGNALS.md`, alle Projektdateien | Projektdateien nach Wahl, `CANVAS.md` | 10, 11 | planned | `retro`, `course-retro` |
| `evidence-checks` | checks reference | nein | – | – | 8 | planned | `course-checks`, `data-checks` |
| `assumptions` | boundary reference | nein | – | – | 6 | planned | `assumed-knowledge`, `leakage` |

## Files in a project

| File | Content | Written by | Read by |
|---|---|---|---|
| `CANVAS.md` | Das Agentic Business Model Canvas | alle Skills | alle Skills |
| `PROBLEM.md` | Kernproblem, 5 Whys, Folgen, Problembaum (als Text-Baum), Zielgruppe | `grill-problem`, `log-evidence` | `to-interview-guide`, `map-solutions`, `grill-solution`, `review-model` |
| `ASSUMPTIONS.md` | Annahmen-Register: ID, Aussage, Kategorie, Status, Quelle, kritisch, Test | `grill-problem`, `map-solutions`, `grill-solution`, `to-model`, `log-evidence` | alle Skills |
| `INTERVIEWS.md` | Leitfaden, Notizen pro Interview (vom Team), Auswertung | `to-interview-guide`, Team, `log-evidence` | `log-evidence`, `review-model` |
| `SOLUTIONS.md` | bestehende Lösungen mit Quelle und SWOT, Fazit | `map-solutions` | `grill-solution`, `to-model` |
| `MODEL.md` | Social Business Model Canvas (10 Felder, CC BY-SA 4.0, SEEd/Strategyzer.com) | `to-model` | `to-tests`, `review-model` |
| `TESTS.md` | Testkarten mit Messgröße, Schwelle und Ergebnis | `to-tests`, `log-evidence` | `log-evidence`, `review-model`, `ask-model` |
| `DECISIONS.md` | Entscheidungen des Teams | alle Skills an Stop-Points | alle Skills |
| `SIGNALS.md` | Ergebnisse, Überraschungen, Feedback | `log-evidence`, `review-model`, `model-retro` | `model-retro`, `ask-model` |

Der Abschnitt `## Agentic Business Model Canvas` in der `AGENTS.md` des Projekts nennt alle Dateien, die Sprache und die Regel „keine erfundenen Aussagen: alles steht im Annahmen-Register“.

## Glossary

| Term | Meaning | Identifier | Source |
|---|---|---|---|
| Annahme | Aussage, die das Team vermutet, ohne Beleg | `assumption` | Handbuch, Lean Startup |
| recherchiert | Aussage aus Desk-Research mit Quelle; belegt kein Bedürfnis | `researched` | Entscheidung 2026-11-21 |
| belegt | Aussage, gestützt durch Interview, Test oder MVP-Ergebnis des Teams | `evidenced` | Handbuch, Lean Startup |
| widerlegt | Annahme, die ein Interview oder Test des Teams nicht bestätigt hat | `refuted` | Lean Startup |
| Nutzer:innen | profitieren direkt von der Lösung | – | Handbuch, Nutzer:innen vs. Kund:innen |
| Kund:innen | bezahlen oder ermöglichen die Umsetzung | – | Handbuch, Nutzer:innen vs. Kund:innen |
| kritische Annahme | Annahme, auf der andere aufbauen und die zuerst getestet werden muss | – | Handbuch, Lösungs-Hypothesen |
| Annahmen-Register | Liste aller Aussagen mit Status und Quelle | `ASSUMPTIONS.md` | Entscheidung 2026-11-21 |
| Kernproblem | präzise beschriebene negative Situation aus Sicht der Betroffenen | – | Handbuch, Problemanalyse |
| Problembaum | Kernproblem (Stamm), Ursachen (Wurzeln), Folgen (Äste) | `PROBLEM.md` | Handbuch, Problembaum |
| Problem-Hypothese | Annahme über Problem und Zielgruppe | – | Handbuch, Zielgruppe |
| Lösungs-Hypothese | Annahme darüber, wie das Problem gelöst werden könnte | – | Handbuch, Lösungs-Hypothesen |
| Vision | höchstens zwei Sätze, gesellschaftlicher Zielzustand, keine Lösung | – | Handbuch, Vision |
| Testkarte | kritische Annahme, Test, Messgröße, Schwelle, mit wem, bis wann, Ergebnis | `TESTS.md` | Entscheidung M6 |
| Schwelle | vorab festgelegter Wert, ab dem eine Annahme als belegt gilt | – | Entscheidung M6 |
| MVP | stark abgespeckte Version, in Stunden bis Wochen, testet die kritischen Annahmen | – | Handbuch, MVP |
| Pivot | grundlegender Kurswechsel, wenn eine kritische Annahme widerlegt ist | – | Lean Startup |
| Social Business Model Canvas | 10 Felder nach SEEd / Campus Business Box e.V. | `MODEL.md` | SEEd-Handout |
