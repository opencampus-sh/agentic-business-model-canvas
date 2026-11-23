# Agentic Business Model Canvas

Ein Canvas, ein Prozess und Agent-Skills, mit denen Teams ihr Impact-Startup von der Problemanalyse bis zum getesteten Geschäftsmodell entwickeln – mit einem Coding-Agenten, ohne ihm die Entscheidungen zu überlassen.

> Status: **v0.9, erste öffentliche Fassung** (1.0 nach den Rückmeldungen der Kursleitung). Entwickelt für den Kurs „[Become a Changemaker](https://opencampus.gitbook.io/changemaker/)“ von opencampus.sh. Gebaut mit dem [Agentic Skillset Builder](https://github.com/steffen74/agentic-skillset-builder); gleiche Canvas-Grammatik und Skill-Konventionen wie [Agentic Data Science](https://github.com/steffen74/agentic-data-science) und [Agentic Course Creation](https://github.com/steffen74/agentic-course-creation).

**Website mit Kurs und Canvas:** https://opencampus-sh.github.io/agentic-business-model-canvas/

## Warum

Ein Agent füllt ein Business Model Canvas in Sekunden. Was er nicht kann:

- wissen, wie eure Zielgruppe das Problem wirklich erlebt,
- sagen, ob jemand für eure Lösung zahlt,
- unterscheiden, was ihr wisst und was ihr nur vermutet – wenn ihr es ihm nicht sagt.

Bittet man ihn „Füll mir das Canvas aus“, entsteht ein Canvas voller plausibler Sätze, das fertig aussieht und nur Annahmen enthält. Genau davor warnt der Lean-Startup-Ansatz, auf dem der Kurs aufbaut.

Dieses Skillset verankert eine andere Gewohnheit: **Der Agent fragt, recherchiert und prüft, das Team entscheidet, und jede Annahme wird getestet, bevor sie zählt.**

## Die drei Teile

### 1. Das Canvas

Das [Agentic Business Model Canvas](canvas/) hat elf Blöcke in drei Spalten: **Problem & Wirkung**, **Geschäftsmodell**, **Testen & Lernen**. Jeder Block hat einen Owner: 👤 das Team entscheidet, oder 🤖 der Agent entwirft und das Team bestätigt. Die Grenze ist Block 6, **Annahmen**: Jede Aussage steht im Annahmen-Register mit Status (*Annahme*, *recherchiert*, *belegt*, *widerlegt*) und Quelle. Das Social Business Model Canvas (nach SEEd) liegt als eigene Datei daneben.

Im Projekt liegt das Canvas als `CANVAS.md`. Eine Druckversion ist in [`canvas/`](canvas/).

[![Agentic Business Model Canvas](canvas/agentic-business-model-canvas.svg)](canvas/agentic-business-model-canvas.pdf)

### 2. Der Prozess

```
Problem ──► Interviews ──► Belege ──► bestehende Lösungen ──► Lösung ──► Modell ──► Tests ──► Belege ──► Review
   ▲                                                            ▲          ▲         ▲                      │
   │                                                            │          └─ anpassen ◄─ Lernen & Entscheiden ┤
   └────────────────────────── Pivot ◄───────────────────────────┴──────── Retro: Checks, Regeln ◄──────────────┘
```

Jeder Schritt endet an einem **Stop-Point**, an dem das Team entscheidet. Siehe [docs/process.md](docs/process.md) und die [Prinzipien](docs/principles.md).

### 3. Die Skills

Agent-Skills als Textdateien (`SKILL.md`) für Claude Code, OpenCode, Codex und andere Agenten, die Skills unterstützen.

| Skill | Wozu | Canvas-Blöcke |
|---|---|---|
| `/setup-model` | Projektordner einmal anlegen; bisherige Ergebnisse als Annahmen übernehmen | alle |
| `/ask-model` | Was ist jetzt dran? | – |
| `/show-canvas` | Das Canvas als Seite im Browser; `live` aktualisiert laufend | alle |
| `/grill-problem` | Kernproblem, Ursachen, Folgen, Problembaum, Zielgruppe, Problem-Hypothesen | 1, 2, 6 |
| `/to-interview-guide` | Interview-Leitfaden mit offenen Fragen, ohne Pitch | 5 |
| `/log-evidence` | Interview-Notizen oder Testergebnisse auswerten; ihr entscheidet, was belegt ist | 5, 6, 10 |
| `/map-solutions` | Bestehende Lösungen mit Quellen und SWOT | 5, 6 |
| `/grill-solution` | Vision, Lösung, Nutzer:innen und Kund:innen, Wertangebot, Erfolgskriterien, kritische Annahmen | 1–4, 6 |
| `/to-model` | Social Business Model Canvas, jedes Feld mit Verweis ins Register | 6, 7 |
| `/to-tests` | Testkarten mit Messgröße und Schwelle, bevor ihr testet | 4, 9 |
| `/review-model` | Zwei Achsen, Beleg und Wirkung; danach: weiter testen, anpassen oder neu ansetzen | 8, 11 |
| `/model-retro` | Aus Überraschungen Korrekturen, Checks und Verbesserungen machen | 10, 11 |

Referenz-Skills, die die anderen laden: `assumptions` (Annahme vs. Beleg), `evidence-checks` (Checks und `check_project.py`).

## Der Check, der es gefunden hätte

Ein Team schreibt ins Modell „Einrichtungen zahlen eine Monatspauschale“. Drei Interviews haben gezeigt, dass Einrichtungen das Problem kennen – nach Geld hat niemand gefragt. `check_project.py` meldet trotzdem nichts, solange die Aussage als *Annahme* im Register steht. Sobald jemand sie als *belegt* markiert, ohne Verweis auf ein eigenes Interview oder einen Test, meldet der Check einen **FEHLER**. Und `/to-tests` schlägt vor, die Zahlungsbereitschaft mit einem echten Angebot zu testen statt mit der Frage „Würdet ihr zahlen?“.

## Installation

```bash
# Bearbeitbare Kopien im Projektordner (jeder Agent; braucht Node.js 22.20 oder neuer)
npx skills@latest add opencampus-sh/agentic-business-model-canvas
# … mit -g für alle Projektordner auf diesem Rechner: npx skills@latest add -g opencampus-sh/agentic-business-model-canvas

# Claude Code Plugin
claude plugin marketplace add opencampus-sh/agentic-business-model-canvas
claude plugin install agentic-business-model-canvas@agentic-business-model-canvas
```

Dann, einmal pro Projekt: `/setup-model`. Danach hilft `/ask-model` weiter.

### Skills aufrufen

Die Skills heißen überall gleich, aber jeder Agent ruft sie anders auf:

| Agent | Aufruf | Beispiel |
|---|---|---|
| Claude Code (Skills im Projekt) | Schrägstrich | `/setup-model` |
| Claude Code (als Plugin) | Schrägstrich mit Plugin-Name | `/agentic-business-model-canvas:setup-model` |
| OpenCode | `@` im Prompt | `@setup-model` |
| Codex | `$` im Prompt, oder `/skills` | `$setup-model` |

In diesem README und in den Skills steht die Claude-Code-Form `/name`.

### Kurs

Ein Selbstlernkurs (etwa 7 Stunden) führt in sechs Einheiten durch Einrichtung und Arbeit mit dem Skillset, am fiktiven Fall Mensa-Retter: [`course/docs/`](course/docs/).

## Quellen und Lizenzen

- Skills: [MIT](LICENSE). Mehrere Skills folgen der Struktur von [Matt Pococks Skills](https://github.com/mattpocock/skills) (MIT); siehe [NOTICE.md](NOTICE.md).
- Canvas und Dokumentation: [CC BY 4.0](LICENSE-docs.md), Campus Business Box e.V. (opencampus.sh). Ausnahme: die Vorlage des Social Business Model Canvas (`MODEL.md`) steht unter CC BY-SA 4.0 – nach dem Handout von [SEEd](https://seed.schule/lehrmaterial/) / Campus Business Box e.V., einer Variante des Business Model Canvas von [Strategyzer.com](https://www.strategyzer.com).
- Das Value Proposition Canvas (Strategyzer.com, Strategyzer AG) wird nur verlinkt.
- Methoden aus dem Kurshandbuch „Become a Changemaker“, aufbauend auf Lean Startup (Eric Ries) und Lean Impact (Ann Mei Chang).
- Wie dieses Skillset entworfen wurde: [`design/`](design/).
