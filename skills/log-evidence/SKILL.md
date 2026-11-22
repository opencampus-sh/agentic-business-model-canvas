---
name: log-evidence
description: Wertet eure Interview-Notizen oder Testergebnisse aus, ordnet sie euren Annahmen zu und schlägt vor, was jetzt belegt oder widerlegt ist. Ihr entscheidet jede Änderung.
disable-model-invocation: true
---

# Belege auswerten

Mach aus dem, was das Team gehört und gemessen hat, Einträge im Annahmen-Register – nicht mehr und nicht weniger. Lies `ASSUMPTIONS.md`, `INTERVIEWS.md`, `TESTS.md`, `PROBLEM.md`, `CANVAS.md` und `SIGNALS.md`. Lade `assumptions` und `evidence-checks`.

## 1. Was ist neu?

- **Interviews:** alle Abschnitte `### I…` mit *Ausgewertet: nein*.
- **Tests:** alle Testkarten mit Ergebnis und *Ausgewertet: nein*.
- **Im Chat eingefügt:** Fügt das Team Notizen oder Ergebnisse in den Chat ein, übertrage sie zuerst wörtlich in die Datei – Interviews als `### I<n> · <Datum> · <Rolle>` mit *Ausgewertet: nein*, Testergebnisse in das Feld *Ergebnis* der passenden Karte – und lass bestätigen, dass du sie richtig zugeordnet hast. Fehlt ein Datum oder ist die Karte unklar, frag.

Gibt es nichts Neues, sag es und schlage den nächsten Schritt vor, wie `/ask-model` es täte. Fehlt eine Notiz, die das Team erwähnt, bitte darum; schreib sie nie aus dem Gedächtnis des Teams oder aus deiner Vorstellung.

## 2. Interviews auswerten

- **Aussagen herausziehen:** pro Interview die Aussagen, die etwas über Problem, Ursachen, Folgen, Zielgruppe oder Lösung sagen, mit Verweis auf die Stelle (`I2`). Trenne, was die Person **erlebt oder getan** hat, von dem, was sie **meint oder vermutet**.
- **Muster:** gruppiere ähnliche Aussagen über alle Interviews und benenne wiederkehrende Themen. Notiere auch, was nur eine Person sagt, und was den Annahmen widerspricht.
- **Zuordnen:** für jede Annahme im Register: stützt, widerspricht, oder kein Bezug – mit den Interview-IDs. Neue Erkenntnisse, die noch nicht im Register stehen, schlägst du als neue Zeilen vor.
- **Qualität:** Zeigen die Notizen, dass gepitcht oder suggestiv gefragt wurde, oder sind es Expert:innen statt Betroffener, sag das bei jeder betroffenen Aussage. Das schwächt den Beleg.
- **Problembaum:** schlag Ergänzungen vor (neue Ursachen, neue Folgen, eine andere Gewichtung), wie es das Handbuch nach den Interviews vorsieht.

## 3. Tests auswerten

- Fehlt im Ergebnis eine Messgröße der Karte, frag danach.
- Hatte die Karte eine *Voraussetzung*, die noch nicht bestanden ist, sag es: Das Ergebnis gilt dann nur unter Vorbehalt.
- Vergleich das Ergebnis mit der Schwelle der Karte, wörtlich. Hatte die Karte keine Schwelle, oder wurde sie erst nach dem Test eingetragen (prüfe den Git-Verlauf von `TESTS.md`, wenn es ihn gibt), sag es: Dann ist das Ergebnis ein Signal, kein Beleg.
- Vorschlag: *belegt*, wenn die Schwelle erreicht ist; *widerlegt*, wenn nicht; offen, wenn der Test zu klein war, abgebrochen wurde oder das Ergebnis an eine noch offene Bedingung geknüpft ist (dann bleibt die Karte auf *läuft*). Will das Team die Schwelle nach dem Ergebnis ändern, gilt: nie einen Check lockern, damit er besteht – mit geänderter Schwelle ist das Ergebnis nur noch ein Signal.
- Beobachtungen aus dem Test, die nicht die Annahme der Karte betreffen, kommen als eigene Zeilen ins Register (siehe *Wann etwas belegt ist* in `assumptions`).

## 4. Stop-Point

Zeig eine Tabelle der vorgeschlagenen Änderungen: Annahme (ID, Aussage), bisheriger Status, vorgeschlagener Status, Belege (IDs, kurzes Zitat aus der Notiz oder Ergebnis gegen Schwelle), Bedenken. Darunter neue Annahmen und Ergänzungen am Problembaum. Zeig die Tabelle in Abschnitten von höchstens fünf Zeilen, die vorgeschlagenen *belegt*- und *widerlegt*-Zeilen zuerst, und lass jeden Abschnitt bestätigen, bevor der nächste kommt. Ein pauschales „passt“ für mehrere Abschnitte setzt nie *belegt* oder *widerlegt*: Frag bei diesen Zeilen einzeln nach. Das Team entscheidet jede Zeile; im Zweifel bleibt der Status, wie er ist.

## 5. Schreiben

- Register: Status und Quelle (Interview- oder Test-IDs) für jede bestätigte Änderung; neue Zeilen mit Status *Annahme* oder, wenn das Team zustimmt, *belegt* mit Quelle.
- `INTERVIEWS.md`: die Muster unter *Auswertung*; bei jedem ausgewerteten Interview *Ausgewertet: ja*.
- `TESTS.md`: *Ausgewertet: ja* bei ausgewerteten Karten, *Status: abgeschlossen*, wenn der Test vorbei ist.
- `PROBLEM.md`: bestätigte Ergänzungen am Problembaum.
- `SIGNALS.md`: ein datierter Eintrag pro Auswertung (Quelle *Interview* oder *Test*, was herauskam, Zahl der Änderungen, Überraschungen).
- Canvas: Block 5 (was ihr jetzt wisst), Block 6 (Stand der kritischen Annahmen – ersetze den alten Stand, statt anzuhängen), Block 10 (Ergebnisse und Überraschungen), jeweils mit IDs; Block 1, wenn sich der Problembaum geändert hat.
- Wurde eine Annahme *widerlegt*, die in `MODEL.md` oder in Block 2 oder 7 steht, ändere diese Stellen nicht selbst, sondern markiere sie für das Team und `/review-model` (`check_project.py` meldet sie unter *widerlegt*).

Fertig, wenn alles Neue ausgewertet ist, jede Änderung vom Team bestätigt und eingetragen ist und `check_project.py` keine FEHLER meldet. Schlage vor zu committen (falls Git), dann den nächsten Schritt: nach Interviews `/map-solutions` oder `/grill-solution`, nach Tests `/review-model`.
