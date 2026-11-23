---
name: evidence-checks
description: Regeln und Katalog der Checks, die ein Geschäftsmodell im Agentic Business Model Canvas bestehen muss, bevor eine Aussage zählt – Annahme vs. Beleg, Interviews, Testschwellen, Widerspruchsfreiheit – mit dem Skript check_project.py. Verwenden beim Ausfüllen oder Prüfen von Canvas, Register, Modell und Tests, beim Review und wenn aus einer Überraschung ein Check werden soll.
---

# Checks

Ein Geschäftsmodell scheitert leise: Ein Canvas voller plausibler Annahmen sieht genauso fertig aus wie eines voller Belege. Ein **Check** ist eine Regel, die gelten muss, bevor eine Aussage zählt, mit einem erwarteten Wert aus einer unabhängigen Quelle – dem Annahmen-Register, den Interview-Notizen, der vorher festgelegten Schwelle.

## Regeln

- **Unabhängige Quelle.** Geprüft wird gegen das, was das Team dokumentiert hat (Notizen, Testergebnisse, Register), nie gegen den eigenen Eindruck „klingt richtig“.
- **Billigster Typ zuerst.** *Automatisch* (`check_project.py`), dann *beim Auswerten* (`/log-evidence`, `/review-model`), dann *durch das Team* (ein Mensch schaut hin).
- **Nie einen Check lockern, damit er besteht.** Ist ein Check falsch, ändert ihn das Team mit einer Entscheidung in `DECISIONS.md`.
- **Jede Überraschung wird ein Check** oder eine bewusste Entscheidung, keinen daraus zu machen (`/model-retro`).

## Katalog

| Check | Erwarteter Wert aus | Typ |
|---|---|---|
| Jede ID im Canvas, in `PROBLEM.md` und `MODEL.md` steht im Register | `ASSUMPTIONS.md` | automatisch |
| Jeder Status ist *Annahme*, *recherchiert*, *belegt* oder *widerlegt* | Regel in `assumptions` | automatisch |
| *recherchiert* hat einen Link als Quelle | Register | automatisch |
| *belegt* und *widerlegt* verweisen auf ein eigenes Interview (`I…`) oder einen eigenen Test (`T…`), das bzw. der existiert | `INTERVIEWS.md`, `TESTS.md` | automatisch |
| Jede kritische Annahme mit Status *Annahme* hat eine Testkarte mit Schwelle | `TESTS.md` | automatisch |
| Ein Test mit Ergebnis hatte seine Schwelle vorher (Schwelle ist ausgefüllt, Ergebnis nennt den Vergleich) | `TESTS.md`, Git-Verlauf | automatisch (Schwelle vorhanden) und beim Review (Reihenfolge) |
| Jede Testkarte prüft genau eine Annahme (eine Schwelle pro Annahme) | `TESTS.md` | automatisch |
| Jede *Voraussetzung* einer Karte verweist auf eine existierende andere Karte | `TESTS.md` | automatisch |
| Jedes Testergebnis ist ausgewertet; keine Karte ist über *Bis wann* ohne Ergebnis (außer *nicht durchgeführt*, mit Grund) | `TESTS.md` | automatisch |
| Keine widerlegte Annahme trägt noch ein Feld von `MODEL.md`; keine ersetzte Annahme steht noch in `PROBLEM.md` | Register, `MODEL.md`, `PROBLEM.md` | automatisch (meldet zur Prüfung) |
| Mindestens drei Interviews sind ausgewertet | `INTERVIEWS.md` (Handbuch) | automatisch |
| Eine *belegte* Aussage stimmt mit dem Wortlaut der Notiz überein und ist auf die befragte Person bzw. Organisation bezogen | Notizen in `INTERVIEWS.md` | beim Auswerten |
| Eine *recherchierte* Aussage steht wirklich in der verlinkten Quelle | die Quelle | beim Eintragen |
| Block 1, 2, 6 und 7 des Canvas passen zum aktuellen Stand von Register, `PROBLEM.md` und `MODEL.md` | Projektdateien | beim Auswerten und beim Review |
| Interviews fragen nach Erlebtem, nicht nach der Idee (kein Pitch, keine Suggestivfragen) | Leitfaden, Notizen | beim Auswerten |
| Zahlungsbereitschaft ist nur durch ein Angebot, eine Zusage oder Bezahlung belegt, nicht durch eine Umfrage | `TESTS.md` | beim Review |
| Die Schwelle einer Karte misst, was die Annahme sagt (nicht etwas Schwächeres) | `TESTS.md`, Register | bei `/to-tests` und beim Review |
| Kein Testergebnis, bevor die *Voraussetzung* der Karte abgeschlossen ist | `TESTS.md` | automatisch (*reihenfolge*, meldet zur Prüfung) |
| Eine kritische Annahme, deren Test ausgewertet ist, bleibt nicht ohne Entscheidung auf *Annahme* | Register, `TESTS.md` | automatisch (*kritische*) |
| Canvas und Modell widersprechen sich nicht (z. B. Wertangebot passt zu Problem und Zielgruppe; wer im Modell zahlt, steht in Block 2) | `CANVAS.md`, `MODEL.md` | beim Review |
| Sind Nutzer:innen und Kund:innen verschieden, sind *Lösung* und *Kund:innengruppen* in `MODEL.md` für beide ausgefüllt | `MODEL.md` (SEEd-Playbook) | beim Review |
| Die Vision beschreibt einen gesellschaftlichen Zielzustand, keine Lösung, in höchstens zwei Sätzen | Block 1 (Handbuch) | beim Review |
| Das Kernproblem beschreibt eine negative Situation der Betroffenen, keine fehlende Lösung | `PROBLEM.md` (Handbuch) | beim Review |

## Das Skript

```
python3 <Pfad dieses Skills>/scripts/check_project.py            # im Projektordner
python3 <Pfad dieses Skills>/scripts/check_project.py <Ordner>
```

Unter Windows heißt Python meist `python` (oder `py`) statt `python3`; nimm, was läuft.

**Ohne Python:** Ist kein Python verfügbar, prüf die automatischen Regeln des Katalogs selbst anhand der Dateien, sag ausdrücklich, dass es eine Handprüfung ist, und biete an, beim Installieren von Python 3 zu helfen (Windows: `winget install Python.Python.3.12`; macOS: die Abfrage zu den Command Line Tools bestätigen).

Es liest `ASSUMPTIONS.md`, `CANVAS.md`, `PROBLEM.md`, `MODEL.md`, `INTERVIEWS.md` und `TESTS.md` und meldet jede Prüfung als **OK**, **OFFEN** (noch nicht so weit, z. B. weniger als drei Interviews) oder **FEHLER** (eine Regel ist verletzt). Bei einem FEHLER endet es mit Exit-Code 1. Formate, die es erwartet: Register als Tabelle mit den Spalten `ID | Aussage | Kategorie | Status | Quelle | Kritisch | Test`; Interviews als `### I1 · …` mit der Zeile `- **Ausgewertet:** ja`; Testkarten als `### T1: …` mit den Zeilen `- **Annahme:**`, `- **Voraussetzung:**`, `- **Bis wann:**`, `- **Schwelle:**`, `- **Ergebnis:**`, `- **Status:**`, `- **Ausgewertet:**` (und bei Bedarf `- **Grund:**`).
