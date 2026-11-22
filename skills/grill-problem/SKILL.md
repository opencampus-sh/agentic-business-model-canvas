---
name: grill-problem
description: Löchert euch, bis Kernproblem, Ursachen, Folgen, Problembaum, Zielgruppe und Problem-Hypothesen scharf sind. Schreibt PROBLEM.md, das Annahmen-Register und das Canvas mit, während ihr antwortet.
disable-model-invocation: true
---

# Das Problem schärfen

Frag das Team so lange, bis das Problem klar ist – bevor irgendjemand über eine Lösung spricht. Lies zuerst `CANVAS.md`, `PROBLEM.md`, `ASSUMPTIONS.md` und `DECISIONS.md`; frag nie, was schon entschieden oder aufgeschrieben ist. Lade `assumptions`.

## Wie du fragst

Ordne die offenen Punkte als **Entscheidungsbaum**: Das Kernproblem bestimmt Ursachen und Folgen; Ursachen und Folgen ergeben den Problembaum; die Folgen zeigen, wer betroffen ist (Zielgruppe); aus allem werden Problem-Hypothesen.

Frag in **Runden**. Die **Front** sind alle Punkte, deren Voraussetzungen geklärt sind. Stell die ganze Front in einer Runde, nummeriere jede Frage und gib deine Empfehlung:

```
❓ **F1** – **<Titel>**: <Frage, mit Optionen, wo es hilft>

➡️ <deine Empfehlung, und warum>
```

Warte auf die Antworten, schreib sie auf (unten), berechne die Front neu und stell die nächste Runde. Eine Frage, die von einer anderen offenen Frage dieser Runde abhängt, kommt in eine spätere Runde. Höchstens fünf Fragen pro Runde. Sag zu Beginn, wie viele Runden es ungefähr werden, und bei jeder Runde, wie viele noch kommen.

**Eigene Worte zuerst.** Bei allem, was das Team verantwortet (Problem, Vision, Lösung, Wertangebot), fragst du zuerst nach den Worten des Teams und machst erst danach einen Vorschlag, falls es keine findet. Übernimmt das Team deinen Wortlaut unverändert, halte das in `DECISIONS.md` fest („Formulierung vom Agenten vorgeschlagen, vom Team übernommen“).

**„Weiß ich nicht“** ist eine gültige Antwort: Schreib den Punkt unter *Noch offen* in `PROBLEM.md` (das ist die Quelle; er wird in den Interviews geprüft) und betrachte ihn für diese Runde als geklärt. Unter **Offene Fragen** im Canvas steht nur ein Verweis („siehe *Noch offen* in `PROBLEM.md`“) mit wer und bis wann. Erfinde keine Antwort und bohre nicht weiter.

**Fakten findest du, Entscheidungen trifft das Team.** Deine Empfehlung ist ein Vorschlag zum Formulieren, kein Inhalt: Was das Problem ist und wen es trifft, weiß das Team – oder es weiß es noch nicht, dann ist es eine Annahme. Erfinde keine Betroffenen, Zahlen oder Erfahrungen. Recherche (Schritt 2 der 5 Whys) bietest du an; was du findest, kommt mit Link als *recherchiert* ins Register.

## Was du klärst

- **Kernproblem.** Die negative Situation aus Sicht der Betroffenen, präzise, in ein bis drei Sätzen. Beschreibt das Team eine fehlende Lösung („es gibt keine App für …“), frag zurück: Was passiert den Menschen, solange es sie nicht gibt?
- **Ursachen (5 Whys).** Die 5 Whys sind eine eigene kleine Schleife außerhalb der Runden: ein „Warum?“ pro Nachricht, Antwort für Antwort, bis ihr an einem Punkt seid, an dem ihr ansetzen könnt – etwa fünfmal, keine feste Regel. Bei „Weiß ich nicht“ endet die Kette dort, und der Rest kommt unter *Noch offen*. Halte die Kette und am Ende eine Erkenntnis fest. Biete danach an, Fakten zu Problem und Ursachen zu recherchieren.
- **Folgen.** Direkte, indirekte und langfristige, gesellschaftliche Folgen; wen sie besonders hart treffen. Leitfrage: „Was passiert, wenn sich nichts ändert?“ Frag auch nach ökologischen, politischen, ökonomischen, kulturellen Folgen, wenn das Team sie nicht von selbst nennt.
- **Problembaum.** Fasse zusammen: Folgen (Äste) oben, Kernproblem (Stamm) in der Mitte, Ursachen (Wurzeln) unten, als Text-Baum in `PROBLEM.md`. Zeig ihn und lass ihn bestätigen.
- **Zielgruppe.** Wer ist direkt betroffen? Untergruppen? Nicht „die breite Masse“. Mach den Realitätscheck des Handbuchs: Was nehmt ihr an, was wisst ihr wirklich – und woher?
- **Problem-Hypothesen.** Aus Problem und Zielgruppe werden Aussagen, die das Team prüfen will, z. B. „Einrichtungen bekommen am Abend zu wenig warmes Essen“. Jede kommt ins Register und mit ihrer ID unter *Problem-Hypothesen* in `PROBLEM.md`.

## Schreib mit

- Jede Aussage über Problem, Ursachen, Folgen und Zielgruppe kommt als Zeile ins Register (`ASSUMPTIONS.md`): Status *Annahme*, außer das Team nennt eine Quelle (Recherche mit Link: *recherchiert*). In `PROBLEM.md` steht sie mit ihrer ID, z. B. `[A2]`.
- Block 1 des Canvas bekommt das Kernproblem und die wichtigsten Ursachen und Folgen in wenigen Zeilen, Block 2 die Betroffenen – beides mit IDs. Vision und Lösung kommen später (`/grill-solution`).
- Jede Wahl zwischen Alternativen (z. B. welche von zwei Zielgruppen zuerst) kommt in `DECISIONS.md` mit Begründung und Alternativen.
- Was offen bleibt, kommt unter **Offene Fragen** im Canvas, mit wer und bis wann.

Fertig, wenn die Front leer ist: Kernproblem, Ursachen, Folgen, Problembaum und Zielgruppe stehen in `PROBLEM.md` – oder als Punkt unter *Noch offen* –, jede Aussage hat ihre Zeile im Register, und es gibt mindestens drei Problem-Hypothesen. Führe `check_project.py` aus, zeig die Blöcke 1 und 2 und lass sie bestätigen. Schlage vor zu committen (falls Git), dann `/to-interview-guide`.
