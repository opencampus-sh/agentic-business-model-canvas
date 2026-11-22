---
name: ask-model
description: Frag, welcher Skill jetzt dran ist. Ein Wegweiser durch die Skills des Agentic Business Model Canvas.
disable-model-invocation: true
---

# Was ist jetzt dran?

Lies `CANVAS.md` und den Abschnitt `## Agentic Business Model Canvas` in `AGENTS.md`. Fehlt eins davon, ist die Antwort `/setup-model`.

Sonst führe den Check aus (`check_project.py`, Pfad steht in `AGENTS.md`) und lies `ASSUMPTIONS.md`, `INTERVIEWS.md` und `TESTS.md`. Empfiehl dann **einen** nächsten Skill, mit einem Satz Begründung, anhand der ersten Lücke, die du findest:

| Wenn … | Empfiehl |
|---|---|
| Block 1 oder 2 ist leer, oder `PROBLEM.md` hat kein Kernproblem und keinen Problembaum | `/grill-problem` |
| Es gibt Problem-Hypothesen, aber keinen Interview-Leitfaden in `INTERVIEWS.md` | `/to-interview-guide` |
| In `INTERVIEWS.md` oder `TESTS.md` stehen Notizen oder Ergebnisse, die noch nicht ausgewertet sind | `/log-evidence` |
| Der Leitfaden steht, aber es sind weniger als drei Interviews ausgewertet | Interviews führen (kein Skill: das macht ihr), danach `/log-evidence` |
| Mindestens drei Interviews sind ausgewertet, aber `SOLUTIONS.md` ist leer | `/map-solutions` |
| Block 3 oder 4 ist leer, oder die Vision fehlt, oder keine Annahme ist als kritisch markiert | `/grill-solution` |
| Lösung und Wertangebot stehen, aber `MODEL.md` ist leer | `/to-model` |
| Eine kritische Annahme mit Status *Annahme* hat keine Testkarte mit Schwelle | `/to-tests` |
| Testkarten stehen, aber noch ohne Ergebnis | Testen (kein Skill: das macht ihr), danach `/log-evidence` |
| Alle Tests der aktuellen Runde haben ein Ergebnis, aber Block 11 ist für diese Runde leer | `/review-model` |
| Ein Review oder eine Testrunde ist abgeschlossen, oder etwas ist schiefgegangen | `/model-retro` |

„Leer“ heißt: Die Datei oder der Block enthält nur Text aus der Vorlage (Überschriften, Kommentare). Hat das Team Notizen oder Ergebnisse nur in den Chat geschrieben, empfiehl `/log-evidence`: Es überträgt sie zuerst in die Datei.

Wenn zwei Zeilen passen, empfiehl die obere. Fehler aus dem Check (z. B. eine Aussage ohne Register-Eintrag) gehen vor: Dann empfiehl den Skill, der die betroffene Datei schreibt.

Beschreibt das Team eine Situation, statt zu fragen („wir haben morgen drei Interviews“), ordne sie der Tabelle zu. Empfiehl nie einen Skill, der für das Team etwas tut, das nur das Team tun kann: Interviews führen, testen, entscheiden.
