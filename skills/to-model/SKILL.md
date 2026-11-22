---
name: to-model
description: Macht aus Canvas und Annahmen-Register euer Social Business Model Canvas in MODEL.md – jedes Feld mit Verweis auf seine Annahmen, Widersprüche markiert.
disable-model-invocation: true
---

# Zum Geschäftsmodell

Schreib das Social Business Model Canvas, auf dem Tests und Review aufbauen. Lies `CANVAS.md`, `ASSUMPTIONS.md`, `PROBLEM.md`, `SOLUTIONS.md` und `DECISIONS.md`. Lade `assumptions` und `evidence-checks`. Frag nicht erneut ab, was schon geklärt ist: Sind Block 1–3 leer, halte an und schlage `/grill-solution` vor.

## 1. Gliederung zuerst

Bevor du ein Feld füllst, zeig dem Team eine Tabelle: die zehn Felder von `MODEL.md` (gesellschaftliche Herausforderung, gesellschaftliche Veränderung, Lösung, Schlüsselaktivitäten, Schlüsselpartner:innen, Kund:innengruppen, Kund:innenbeziehung, Kanäle, Einnahmequellen, Kostenstruktur) und für jedes Feld:

- die Register-Einträge, die es schon gibt (mit ID und Status),
- die **Lücken**: Felder, zu denen noch nichts im Register steht. Für die ersten drei Felder und die Kund:innengruppen kommt alles aus dem Canvas; Aktivitäten, Partner, Beziehung, Kanäle, Einnahmen und Kosten sind oft neu.

Für jede Lücke stellst du eine Frage, mit Vorschlägen als Optionen, und deine Empfehlung. Vorschläge sind Formulierungshilfen: Was das Team dort einträgt, ist seine Entscheidung und zunächst eine Annahme. Erfinde keine Preise, Kosten, Partner oder Zahlen.

**Stop-Point:** Das Team beantwortet die Fragen und bestätigt die Gliederung.

## 2. Schreiben

- Fülle `MODEL.md` Feld für Feld, so einfach wie möglich, ohne Details, die das Team nicht genannt hat. Jede Aussage steht mit ihrer ID, z. B. `[A12]`. Neue Aussagen kommen zuerst ins Register (Status *Annahme*, Kategorie passend zum Feld).
- Sind Nutzer:innen und Kund:innen verschieden (Block 2), füllst du *Lösung* und *Kund:innengruppen* für beide getrennt aus.
- Lass den Quellenvermerk am Ende von `MODEL.md` stehen.
- Block 7 des Canvas bekommt nur die Kernentscheidungen: Wer zahlt, wofür, woher kommen die Einnahmen, was sind die größten Kosten – mit IDs.

## 3. Prüfen

Führe `check_project.py` aus und prüfe zusätzlich die Review-Checks aus `evidence-checks`, die das Modell betreffen:

- Widersprüche zwischen Canvas und Modell (z. B. jemand zahlt im Modell, der in Block 2 nicht vorkommt; das Wertangebot passt nicht zum Kernproblem).
- Ein Modell, in dem niemand zahlt, oder Einnahmen, die die größten Kosten offensichtlich nicht decken. Rechne nicht selbst; frag nach.
- Annahmen, auf denen viele Felder aufbauen, die aber nicht als kritisch markiert sind: Schlag vor, sie als kritisch zu markieren. Das Team entscheidet.

Zeig die Funde zuerst, jeweils mit einem Vorschlag, und frag als Auswahlfragen mit Kontext (was und wo, warum es wichtig ist, Optionen mit Folgen, Empfehlung zuerst). Halte Entscheidungen in `DECISIONS.md` fest.

Fertig, wenn alle zehn Felder gefüllt sind oder als offene Frage im Canvas stehen, jede Aussage eine ID hat, `check_project.py` keine FEHLER meldet und das Team das Modell bestätigt hat. Schlage dann `/to-tests` vor.
