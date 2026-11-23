---
name: review-model
description: "Prüft euer Geschäftsmodell nach einer Testrunde auf zwei Achsen: Beleg (was trägt, was ist nur Annahme) und Wirkung (dient es den Betroffenen, trägt es sich). Danach entscheidet ihr: weiter testen, anpassen oder neu ansetzen."
disable-model-invocation: true
---

# Das Modell prüfen

Zwei-Achsen-Review, bevor das Team die nächste Runde plant. Führe jede Achse als eigenen Sub-Agenten mit frischem Kontext aus, wenn deine Umgebung das kann; sonst nacheinander. Dann zusammenführen. Eingaben: alle Projektdateien, `check_project.py`, und die letzten Einträge in `SIGNALS.md`. Lade `evidence-checks` und `assumptions`.

## Achse 1: Beleg

- Führe `check_project.py` aus; jeder FEHLER ist ein Befund.
- Prüfe die Review-Checks aus `evidence-checks`: *belegte* Aussagen stimmen mit dem Wortlaut der Notizen und den Testergebnissen überein; Zahlungsbereitschaft ist durch Verhalten belegt, nicht durch Umfragen; Schwellen standen vor den Ergebnissen; Canvas und Modell widersprechen sich nicht.
- Fasse den Stand zusammen: Welche kritischen Annahmen sind belegt, welche widerlegt, welche offen? Auf welchen offenen Annahmen beruhen die meisten Felder von `MODEL.md`?

## Achse 2: Wirkung

- Dient das Modell der gesellschaftlichen Herausforderung und der Vision in Block 1, oder hat es sich davon entfernt?
- Entsteht die Wirkung bei den Betroffenen aus `PROBLEM.md`, und passen Nutzer:innen, Kund:innen und Fall in Block 2 zu `MODEL.md`?
- Trägt es sich: Gibt es jemanden, der zahlt oder ermöglicht, und ist das belegt? Decken die genannten Einnahmen die größten Kosten? Rechne nicht selbst; nenne, welche Zahlen fehlen.
- Erfüllt das Ergebnis die Erfolgskriterien aus Block 4?

## Bericht

Eine Liste, jeder Befund markiert als **blockierend** (das Team würde auf einer widerlegten oder ungeprüften kritischen Annahme weiterbauen, oder das Modell widerspricht sich) oder **Hinweis**, mit Beleg (Datei, ID) und einem Vorschlag. Erkläre dem Team in einem Satz: „Blockierend heißt: Das solltet ihr klären, bevor ihr darauf weiterbaut – es heißt nicht, dass ihr aufhören müsst.“ Bewerte nicht, ob die Idee gut ist; zeig, was trägt und was nicht.

Am Ende drei Wege, jeweils mit dem, was dafür und dagegen spricht:

- **Weiter testen:** keine Annahme ist widerlegt, kritische sind noch offen; nächste Tests. → danach `/to-tests`.
- **Anpassen:** einzelne Annahmen sind widerlegt, die Richtung trägt; was sich in Canvas und Modell ändert, und die nächsten Tests gehören dazu. → danach `/to-model`, dann `/to-tests`.
- **Neu ansetzen (Pivot):** eine Annahme ist widerlegt, auf der die Idee steht; wohin der Blick geht. → danach `/grill-solution` (Lösung, Zielgruppe, wer zahlt) oder `/grill-problem` (das Problem selbst).

Ist etwas widerlegt, steht „Weiter testen“ nicht zur Wahl, ohne dass das Team erklärt, warum die Widerlegung nichts ändert. Ist eine **kritische** Annahme widerlegt, ist „Anpassen“ nur dann ein Weg, wenn eine engere Ersatz-Annahme durch eigene Interviews oder Tests gestützt ist (nenne sie); sonst ist es ein Pivot.

## Entscheidungen

Die Wahl des Weges trifft das Team, ebenso jede Entscheidung über einen Befund mit mehr als einer vernünftigen Lösung. Stell sie als Auswahlfragen, mit dem Frage-Werkzeug deiner Umgebung, wenn es eines gibt, sonst nummeriert im Text. Jede Frage trägt ihren Kontext: was und wo; warum es wichtig ist; Einschränkungen (Entscheidungen, Belege); zwei bis vier Optionen mit Folgen; deine Empfehlung zuerst, markiert als *(Empfehlung)*. Frag den Weg zuletzt.

Wende nur an, was das Team wählt. `MODEL.md` änderst du hier nicht; das macht `/to-model` im nächsten Schritt. Trag ein: den Weg und die Entscheidungen in `DECISIONS.md`, Block 11 (was ihr entschieden habt, was als Nächstes kommt) und Block 8 (Stand der Checks) im Canvas; ändert das Team *Kritisch* im Register, auch die Liste der kritischen Annahmen in Block 6; einen Eintrag in `SIGNALS.md` (Quelle *Review*).

Fertig, wenn der Weg entschieden und eingetragen ist. Schlage vor zu committen (falls Git), dann `/model-retro`, danach den Skill, der zum gewählten Weg gehört.
