---
name: setup-model
description: "Legt den Projektordner für euer Impact-Startup an: Canvas, Annahmen-Register, Problem, Interviews, bestehende Lösungen, Geschäftsmodell, Tests, Entscheidungen und Signale. Einmal pro Projekt, vor allen anderen Skills."
disable-model-invocation: true
---

# Projekt anlegen

Lege die Dateien an, die alle anderen Skills lesen. Erst erkunden, dann zusammenfassen und bestätigen lassen, dann schreiben. Sprich mit dem Team auf Deutsch und duze.

## 1. Erkunden

Lies, was es gibt, und nimm nichts an:

- Ist der aktuelle Ordner leer, ein bestehendes Projekt oder etwas ganz anderes (z. B. das Home-Verzeichnis)? Ist es ein Git-Repository? Gibt es ein Remote (`git remote -v`), prüfe die Sichtbarkeit (`gh repo view --json visibility`, falls verfügbar); ohne Remote frag in Abschnitt A.
- Gibt es schon `AGENTS.md` mit einem Abschnitt `## Agentic Business Model Canvas`, oder schon `CANVAS.md`, `ASSUMPTIONS.md` und die anderen Dateien aus [`templates/`](templates/)?
- Gibt es bisherige Ergebnisse: einen Notion-Export, Dokumente, Notizen, Fotos von Plakaten? Lies Markdown- und Textdateien; bei anderen Formaten sag, welche du nicht lesen kannst.

## 2. Zusammenfassen und fragen

Fasse zusammen, was da ist und was fehlt. Dann frage in dieser Reihenfolge, je eine Antwort, deine Empfehlung zuerst. Überspringe, was die Erkundung schon geklärt hat.

- **A. Ort.** Ist dieser Ordner der richtige? Empfiehl einen eigenen, leeren Projektordner. Ist es ein öffentliches Repository, empfiehl, es privat zu machen: Interview-Notizen und Ideen gehören nicht ins Netz. Halte an, bis das Team entschieden hat.
- **B. Team und Idee.** Teamname oder Namen, die Idee in einem Satz. Mehr nicht: Problem und Lösung klären `/grill-problem` und `/grill-solution`.
- **C. Bisherige Ergebnisse.** „Liegen schon Ergebnisse vor, z. B. aus Notion, einem Dokument oder Notizen?“ Wenn ja: Wo stehen sie, und welche Kapitel des Handbuchs habt ihr schon bearbeitet?

## 3. Schreiben

- Kopiere alle Dateien aus [`templates/`](templates/) in den Projektordner. Überschreibe nie eine bestehende Datei; melde sie stattdessen.
- Fülle im Canvas den Kopf (Team, Idee, Version mit heutigem Datum).
- **Bisherige Ergebnisse:** Übertrage jede Aussage daraus als Zeile ins Annahmen-Register, mit Status *Annahme* und der Quelle (z. B. „Notion-Export, Seite Problem-Hypothesen“). Lade dazu `assumptions`. Schlag die Kategorie vor, lass *Kritisch* und *Test* leer; fast gleiche Aussagen werden eine Zeile mit beiden Quellen, im Wortlaut einer der beiden (nicht neu formuliert). Interview-Notizen kommen wörtlich unter *Notizen* in `INTERVIEWS.md`, mit *Ausgewertet: nein*. Nichts davon wird zu *belegt*: Das entscheidet erst `/log-evidence` mit dem Team. Liste die übernommenen IDs in Block 6 des Canvas; schreibe keine Aussage ins Canvas, die nicht im Register steht (die Kopfzeile mit Team und Idee ist davon ausgenommen).
- Ergänze in `.gitignore` (falls Git) die Zeile `build/`.
- Gibt es kein `CLAUDE.md`, lege es mit der einen Zeile `@AGENTS.md` an, damit Claude Code die Regeln in jeder Sitzung liest (andere Agenten lesen `AGENTS.md` direkt).
- Füge diesen Abschnitt in `AGENTS.md` ein (lege die Datei an, wenn nötig):

```markdown
## Agentic Business Model Canvas

- Canvas: `CANVAS.md` (vor jeder Arbeit lesen; aktualisieren, wenn etwas entschieden ist)
- Annahmen-Register: `ASSUMPTIONS.md`. Jede Aussage in Canvas, `PROBLEM.md` und `MODEL.md` steht dort mit Status und Quelle; im Text nur mit ID, z. B. [A3]. Der Agent erfindet keine Aussagen, Zitate oder Zahlen.
- Problem: `PROBLEM.md`; Interviews: `INTERVIEWS.md`; bestehende Lösungen: `SOLUTIONS.md`
- Geschäftsmodell: `MODEL.md` (Social Business Model Canvas, CC BY-SA 4.0, nach SEEd / Campus Business Box e.V. und Strategyzer.com)
- Tests: `TESTS.md`; Entscheidungen: `DECISIONS.md`; Signale: `SIGNALS.md`; Vorschläge für das Skillset: `SKILL-PROPOSALS.md` (legt `/model-retro` bei Bedarf an)
- Checks: Skript `scripts/check_project.py` im Skill `evidence-checks` (der Agent findet den Pfad, wenn er den Skill lädt; „Führ bitte den Check aus“ genügt)
- Language: de (Gespräch auf Deutsch, du)
- Bisherige Ergebnisse: <Quelle oder „keine“>
```

Erkläre den Abschnitt in einem Satz („Hier steht, wo eure Dateien liegen und welche Regeln ich in jeder Sitzung befolge“) und lass das Team den Inhalt bestätigen, nicht den Wortlaut.

Fertig, wenn alle Dateien existieren, jede übernommene Aussage im Register steht und das Team den Abschnitt in `AGENTS.md` bestätigt hat. Schlage vor zu committen (falls Git), samt der installierten Skills (z. B. `.claude/skills/`), damit alle im Team dieselbe Version nutzen – persönliche Einstellungen wie `.claude/settings.local.json` nicht. Dann `/grill-problem`.
