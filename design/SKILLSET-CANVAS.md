# Skillset Canvas

**Skillset:** Agentic Business Model Canvas
**Maintainers:** Steffen Brandt
**Language:** de
**Version:** 2026-11-22

> Owners: 👤 maintainer decides · 🤖 agent drafts, maintainer approves.
> Keep each block short. Details go in the files in `design/`; decisions go in `design/DECISIONS.md`.

---

## Purpose

### 1. Practice 👤
<!-- Which kind of work does the skillset support, for whom, and why with an agent? What goes wrong today when people do it with an agent and no skills? -->
<!-- print: Which work, for whom, why with an agent? | What goes wrong without skills? -->
Teams im Kurs „Become a Changemaker“ (opencampus.sh) entwickeln mit einem Agenten ihr Impact-Startup von der Problemanalyse bis zum getesteten Geschäftsmodell: Problem und Ursachen (5 Whys, Folgen, Problembaum), Zielgruppe und Problem-Interviews, Lösungshypothesen, Nutzer:innen vs. Kund:innen, Value Proposition Canvas, Social Business Model Canvas, MVP-Tests der kritischen Annahmen, Ergebnisse zurück ins Canvas (Lean-Schleife). Finanzierung, Rechtsform und Pitch werden nur verlinkt.

### 2. Users 👤
<!-- Who runs the skills: role, domain knowledge, experience with agents, language, setting (course, team, alone). The weakest user the skillset still serves. Link PERSONAS.md. -->
<!-- print: Who runs the skills, knowing what? | The weakest user we still serve -->
Die Teams selbst (allein oder im Team, Kurs im eigenen Tempo, 1–2 Wochen pro Thema); Coaches später optional. Agenten: Claude Code, OpenCode oder Codex. Arbeitsablage: ein Ordner mit Markdown-Dateien, Notion-Teamseite als optionaler Export. Personas: Annahmen, bis die Kursleitung sie bestätigt (siehe `PERSONAS.md`).

### 3. Outcomes 👤
<!-- What good work looks like when the skillset is used: the artefacts and decisions it should lead to. What it deliberately does not do. -->
<!-- print: What does good work look like? | What the skillset does not do -->
Am Ende hat ein Team: (1) Problembeschreibung mit Problembaum (Ursachen, Folgen); (2) konkrete Zielgruppe und mindestens 3 ausgewertete Problem-Interviews; (3) kurze Vision; (4) Lösungshypothesen mit markierten kritischen Annahmen; (5) geklärte Rollen von Nutzer:innen und Kund:innen (wer zahlt, bei wem entsteht Wirkung); (6) Value Proposition Canvas und Social Business Model Canvas, jeder Eintrag als *Annahme*, *recherchiert* oder *belegt* markiert; (7) Testplan für die kritischen Annahmen und MVP-Ergebnisse, eingearbeitet ins Canvas; (8) Entscheidungslog.

Nicht: Texte, die das Team als eigene Arbeit abgibt; die Idee bewerten oder auswählen; Finanzplan, Rechtsform, Pitch-Deck.

### 4. Evidence 👤
<!-- How users and maintainers know an outcome is reached: criteria for each artefact, signals from real use. Every outcome has evidence. -->
<!-- print: Criteria for each outcome | Which signals from real use? -->
- Jeder Canvas-Eintrag hat Status (*Annahme* · *recherchiert* · *belegt*) und Quelle (Interview Nr., Test, Link).
- Mindestens 3 ausgewertete Interviews (Handbuch).
- Jede kritische Annahme hat einen Test mit vorher festgelegtem Erfolgskriterium.
- Value Proposition Canvas und Social Business Model Canvas widersprechen sich nicht (z. B. Wertangebot passt zu den Pains).
- Aus echter Nutzung: Feedback der Kursleitung zu Canvases, die mit dem Skillset entstanden sind.

---

## Design

### 5. Sources 🤖
<!-- Handbook, methods, existing canvases, literature, own practice: what each contributes, its license, what is adopted, adapted or left out. Link SOURCES.md. -->
<!-- print: Handbook, methods, canvases, practice | License and what we adopt -->
- Kurshandbuch „Become a Changemaker“ (GitBook, 42 Seiten), Lizenz unbekannt
- Darin: Value Proposition Canvas, Social Business Model Canvas, Business Model Canvas, Sustainable Business Model Canvas (Abbildungen ohne Quellenangabe)
- Methodische Basis laut Handbuch: Lean Startup (Eric Ries), Lean Impact (Ann Mei Chang)
- Keine eigene Kurserfahrung des Maintainers

### 6. Judgement boundary 👤
<!-- The line between what the agent does (facts, legwork, drafts, checks) and what the user decides. Which decisions must never be taken by the agent? Where would an agent typically cross the line in this domain? -->
<!-- print: Agent: facts, legwork, drafts, checks | User: every trade-off. Where it slips? -->
- **Agent macht:** Fragen stellen, strukturieren, Konsistenz zwischen den Canvases prüfen, Annahmen markieren, Interview-Notizen des Teams clustern.
- **Agent entwirft, Team bestätigt:** Interviewleitfaden, Hypothesen-Formulierungen, Recherche zu bestehenden Lösungen und SWOT (mit Quellen), Testplan.
- **Team entscheidet:** Problem, Zielgruppe, welche Bedürfnisse echt sind, Wertangebot, wer zahlt und Erlösmodell, welche Annahmen kritisch sind, Pivot oder weitermachen.
- **Nie:** Interview-Aussagen, Zitate oder Zahlungsbereitschaften erfinden; Ideen als gut oder schlecht bewerten; einen Canvas-Block ohne Input des Teams füllen. Desk-Research ist *recherchiert*, nie Beleg für ein Bedürfnis.
- **Typische Grenzüberschreitung:** Der Agent füllt das Canvas mit plausiblen Annahmen, die wie Erkenntnisse aussehen. Zentraler Check: **Annahme vs. Beleg**.

### 7. Process and stop points 👤
<!-- The domain process as steps, each ending at a stop point where the user decides. Loops back from signals. The domain canvas the skillset gives its users. Link SKILL-MAP.md. -->
<!-- print: Steps, each ending at a stop point | Loops back from signals -->
Domain-Canvas: **Agentic Business Model Canvas** (`skills/setup-model/templates/CANVAS.md`, 11 Blöcke in den Spalten Problem & Wirkung, Geschäftsmodell, Testen & Lernen; Grenze ist Block 6 „Annahmen“). Das Social Business Model Canvas liegt als Begleitdatei `MODEL.md` daneben. Prozess und Stop-Points folgen in `/to-skill-map`.

### 8. Checks 🤖
<!-- What the users' work must pass before it counts (domain checks), and what the skillset itself must pass before release (conventions, dry run). Where each expected value comes from. -->
<!-- print: Checks on the users' work | Checks on the skillset itself -->
- **Arbeit der Teams:** Katalog in `evidence-checks` (14 Checks), davon 7 automatisch in `check_project.py` (Verweise, Status, Quellen, Belege nur aus eigenen Interviews/Tests, Testkarten mit Schwelle, Schwellen vor Ergebnissen, mindestens 3 Interviews).
- **Skillset selbst:** `check_skillset.py` (alle grün seit 2026-11-22); Dry-Run am Beispielfall Mensa-Retter vor dem ersten Release.

---

## Build and improve

### 9. Skills 🤖
<!-- The skill list with roles, canvas blocks and status (planned, drafted, dry-run, released). Link SKILL-MAP.md. -->
<!-- print: Skills, roles, canvas blocks | Planned · drafted · dry-run · released -->
12 vom Team aufgerufene Skills und 2 Referenz-Skills, alle *drafted*; Gruppen 1–3 freigegeben, Gruppe 4 (`model-retro`) zur Freigabe. Siehe `SKILL-MAP.md`.

### 10. Dry-run signals 🤖
<!-- Dry runs on the example case before release; feedback and retros from real use after. Link SIGNALS.md. -->
<!-- print: Dry runs on the example case | Feedback from real use -->

### 11. Improvements 👤
<!-- What changes now and in the next version; which signal became a check, a skill rule or a core change. -->
<!-- print: What changes now, what next version | Which signal became a check or rule -->

---

## Open questions
<!-- Parking lot. Each item names who resolves it, by when. -->
<!-- print: Who resolves it, by when? -->
- Personas bestätigen: Fragenliste an die Kursleitung (`design/QUESTIONS-COURSE-LEAD.md`). Steffen leitet weiter, vor `/dry-run`.
- Kurs in `course/` mit Agentic Course Creation bauen (nach dem Dry-Run). Steffen + Agent.
- Lizenzen der Canvases und des Handbuchs (siehe `SOURCES.md`). Steffen bzw. Campus Business Box e.V., vor `/design-canvas`.

## Decision log
<!-- See design/DECISIONS.md. -->
<!-- print: Date · decision · reason · alternatives -->
