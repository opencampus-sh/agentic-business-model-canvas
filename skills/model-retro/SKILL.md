---
name: model-retro
description: Nach einem Review, einer Testrunde oder wenn etwas schiefgegangen ist – macht aus dem, was passiert ist, Korrekturen, neue Checks, Änderungen an Canvas und Modell und Verbesserungen am Skillset selbst.
disable-model-invocation: true
---

# Retro

Macht die nächste Runde, das Projekt und das Skillset besser aus dem, was passiert ist. Lies `SIGNALS.md`, `DECISIONS.md`, `CANVAS.md`, `ASSUMPTIONS.md`, `TESTS.md` und die Einträge von `/review-model`. Lade `assumptions` und `evidence-checks`.

## 1. Signale sammeln

Frag das Team in einer Runde: Was lief anders als geplant? Was hat überrascht? Wo habt ihr festgesteckt? Welche Entscheidung hat sich im Nachhinein als voreilig erwiesen? Wo hat der Agent etwas getan oder vorgeschlagen, das nicht gepasst hat? Ergänze, was du selbst nachsehen kannst (Testergebnisse, Check-Ausgabe, Git-Verlauf). Trag jedes Signal in `SIGNALS.md` ein, ohne Namen von Interviewpartner:innen.

## 2. Jedes Signal erklären

Finde zu jedem Signal die Ursache, bevor du etwas vorschlägst. Typische Ursachen: eine Annahme, die als belegt galt, aber nur recherchiert oder höflich bestätigt war; eine Schwelle, die erst nach dem Ergebnis kam; ein Leitfaden mit Suggestivfragen; Nutzer:innen und Kund:innen verwechselt; ein Test, der Meinung statt Verhalten maß; ein Vorschlag des Agenten, der als Entscheidung übernommen wurde. Dann frag: **Warum hat kein Check es gefunden?** Diese Antwort ist wichtiger als die Korrektur.

## 3. Vorschlagen

Eine nummerierte Liste, jeder Punkt mit Beleg und Empfehlung, in diesen Kategorien:

- **Jetzt korrigieren:** Einträge in Register, Canvas, Modell oder Tests, die nicht mehr stimmen. Formuliere die Änderung genau.
- **Check:** die Prüfung, die es gefunden hätte, mit Typ (automatisch, beim Auswerten, durch das Team). Eine Prüfung für dieses Projekt kommt in Block 8 des Canvas.
- **Canvas und Modell:** Blöcke oder Felder, die sich als falsch herausgestellt haben.
- **Skill-Regel:** eine Änderung an einem Skill dieses Skillsets (z. B. eine neue typische Grenzüberschreitung in `assumptions`, eine neue Prüfung in `evidence-checks` oder `check_project.py`). Lieber ein Check als eine Regel. Schreib jede in `SKILL-PROPOSALS.md` im Projektordner: zuerst ein Satz in einfacher Sprache (was sich ändern soll und warum), dann das Diff gegen die Skill-Datei. Schlage vor, die Datei als Issue im Repository des Skillsets einzureichen (https://github.com/opencampus-sh/agentic-business-model-canvas), damit andere Teams profitieren – ohne Inhalte eures Projekts. Das Team muss das Diff nicht verstehen, um zu entscheiden; der Satz reicht.

## 4. Anwenden

Wende nur an, was das Team auswählt. Setz in `SIGNALS.md` bei jedem Signal den Status, ergänze Block 11 im Canvas (was ihr jetzt ändert, was in der nächsten Runde) und halte Entscheidungen in `DECISIONS.md` fest. Führe `check_project.py` aus.

Fertig, wenn jeder ausgewählte Punkt in seiner Datei steht, jedes Signal einen Status hat und `check_project.py` keine FEHLER meldet. Schlage vor zu committen (falls Git), dann den nächsten Schritt, wie `/ask-model` es täte.
