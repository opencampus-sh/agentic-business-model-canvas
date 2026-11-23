# Einheit 5 · Testen und entscheiden

**Ziel:** Ihr legt für eine kritische Annahme einen Test mit Schwelle fest, **bevor** ihr testet, wertet das Ergebnis ehrlich aus und entscheidet, wie es weitergeht.
**Zeit:** ca. 75 Minuten (ohne den Test selbst). **Vorher:** [Einheit 4](4-loesung-und-modell.md); im Handbuch [Lean Startup & MVP](https://opencampus.gitbook.io/changemaker/impact-startup/solution-design-alle-zentralen-aspekte-auf-einen-blick/mvp).

## Lesen: Testkarte, Ergebnis, Entscheidung

**`/to-tests`** schreibt für jede kritische Annahme eine **Testkarte**: Was ihr macht, mit wem (mindestens zwei Personen oder Organisationen), bis wann, was ihr messt und die **Schwelle** – ab wann die Annahme als belegt gilt. Er bevorzugt Tests, die **Verhalten** zeigen (eine Zusage, eine Probe-Lieferung, eine Bezahlung) statt Meinungen. Eine Umfrage „Würdet ihr zahlen?“ ist kein Test für Zahlungsbereitschaft. Die Schwelle legt ihr fest – und committet die Karten **vor** dem Test, damit sichtbar bleibt, dass sie vorher feststand.

**`/log-evidence`** vergleicht das Ergebnis wörtlich mit der Schwelle. Wollt ihr die Schwelle nach dem Ergebnis senken, gilt: **Nie einen Check lockern, damit er besteht.** Mit geänderter Schwelle ist das Ergebnis nur noch ein Signal.

**`/review-model`** prüft euer Modell auf zwei Achsen – *Beleg* (was trägt?) und *Wirkung* (dient es den Betroffenen, trägt es sich?) – und legt drei Wege vor:

- **Weiter testen** – nichts ist widerlegt, kritische Annahmen sind noch offen;
- **Anpassen** – einzelne Annahmen sind widerlegt, die Richtung trägt;
- **Neu ansetzen (Pivot)** – eine Annahme ist widerlegt, auf der die Idee steht.

Den Weg wählt ihr. „Blockierend“ heißt im Review: klären, bevor ihr darauf weiterbaut – nicht aufhören.

**`/model-retro`** fragt am Ende: Was ist passiert, warum hat kein Check es gefunden, was ändert ihr – und was sollte sich am Skillset ändern? Vorschläge für das Skillset landen in `SKILL-PROPOSALS.md`, jeweils mit einem Satz in einfacher Sprache.

## Üben

Du legst mit dem fiktiven Team Testkarten fest, wertest die Testergebnisse aus und entscheidest, wie es weitergeht.

### Startzustand

Stand **09-nach-to-model** – Modell fertig, fünf kritische Annahmen, noch keine Testkarte: [09-nach-to-model.zip](https://github.com/opencampus-sh/agentic-business-model-canvas/raw/main/examples/mensa-retter/referenz/zip/09-nach-to-model.zip)

Leg einen neuen Ordner `mensa-retter-uebung-5` an, entpacke die ZIP-Datei hinein, öffne dort das Terminal und starte den Agenten – wie in [Einheit 1](1-problem.md) unter „Übungsordner anlegen“.

### Aufgabe

1. **`/to-tests`.** Zeit und Frist – „Zusammen etwa zwölf Stunden pro Woche, bis zum 13. November.“ Der Agent nennt Probleme im Plan, je mit Empfehlung. Das Team hat geantwortet:
    - Reihenfolge – „Ok, passt.“
    - Angebot mit Preis ans Studierendenwerk – **abgelehnt:** „Wir haben noch keinen Preis, Ahmet rechnet erst. Und ohne Freigabe von oben läuft gar nichts – da wollen wir nicht gleich mit einer Rechnung kommen.“
    - Schwelle für die Probewoche – „Wir drei haben 3 von 4 beschlossen.“
2. Fragt der Agent, ob er die Karten committen soll: „Ja, bitte. Wenn hier noch kein Git ist, richte es ein.“ So steht fest, dass die Schwelle *vor* dem Ergebnis da war.
3. **`/log-evidence`.** Füg diese Ergebnisse in den Chat ein:

    ```text
    Gespräch mit dem Studierendenwerk (Abteilungsleitung Hochschulgastronomie): „Finden wir gut, machen wir gern mit, wenn die Haftung geklärt ist. Bezahlen können wir dafür aber nichts, höchstens Verpackungen stellen.“
    Probewoche: Vier Einrichtungen wurde angeboten, eine Woche lang abends übrig gebliebenes Mensa-Essen zu bringen. Zwei haben zugesagt und es an mindestens drei Tagen angenommen (Tafel-Ausgabestelle, Tagesstätte). Eine hat abgelehnt (Jugendzentrum: „passt nicht zu uns“), eine hat nicht geantwortet. Die Tafel konnte nur zwei von fünf Tagen selbst abholen; an den anderen Tagen hat das Team geliefert.
    Stiftungen: Eine hat geantwortet: Förderung für Ehrenamtsprojekte bis 5.000 € möglich, Antrag bis März. Die andere hat nicht geantwortet.
    ```

    Rückfragen – „Wie oft die Tagesstätte selbst abgeholt hat, haben wir nicht aufgeschrieben.“ „Die Stiftung hat per Mail geantwortet, auf unsere Anfrage.“
4. Bei den *widerlegt*-Vorschlägen schreib zuerst: **„2 von 4 ist doch auch gut, können wir das nicht als belegt nehmen?“** Lies die Antwort. Dann entscheide jede Zeile einzeln.
5. **`/review-model`.** Gibt es die Kosten? – „Noch nicht, Ahmet hatte keine Zeit.“ Lies beide Achsen und die drei Wege. Das Team hat „Anpassen“ gewählt: „Die Richtung stimmt, zwei Einrichtungen wollen es ja. Nur das Geld und das Fahren müssen anders.“ Welchen Weg würdest *du* wählen, und warum?
6. Optional: **`/model-retro`.** Antworte in eigenen Worten, was anders lief als geplant. Lehn mindestens einen Vorschlag mit Grund ab.

Weichen deine Testkarten stark ab und passen die Ergebnisse nicht dazu? Dann starte Schritt 3 in einem neuen Ordner mit [10-nach-to-tests.zip](https://github.com/opencampus-sh/agentic-business-model-canvas/raw/main/examples/mensa-retter/referenz/zip/10-nach-to-tests.zip).

### So sieht es aus

Aus dem Referenzlauf (fiktiv). Auf „2 von 4 ist doch auch gut“ antwortet der Agent:

```text
Ich verstehe den Wunsch – zwei Einrichtungen haben wirklich mitgemacht, das ist ein
Ergebnis. Aber die Schwelle „3 von 4“ habt ihr zu dritt vor dem Test beschlossen und
committet. Wenn wir sie jetzt senken, passt sie zufällig genau zum Ergebnis – dann ist
das Ergebnis nur noch ein Signal, kein Beleg. Eine Schwelle wird nie gelockert, damit
sie besteht.
```

Danach schlägt er eine engere Annahme vor (A49): Einrichtungen, die abends Gäste haben und selbst nicht kochen, nehmen das Essen an. Die kann das Team in der nächsten Runde mit eigener Schwelle testen.

### Vergleichen

- nach `/to-tests`: [Stand 10-nach-to-tests](https://github.com/opencampus-sh/agentic-business-model-canvas/tree/main/examples/mensa-retter/referenz/stand/10-nach-to-tests) (`TESTS.md`, `DECISIONS.md`)
- nach `/log-evidence`: [Stand 11-nach-log-evidence-tests](https://github.com/opencampus-sh/agentic-business-model-canvas/tree/main/examples/mensa-retter/referenz/stand/11-nach-log-evidence-tests) (`ASSUMPTIONS.md`, `TESTS.md`)
- nach `/review-model`: [Stand 12-nach-review-model](https://github.com/opencampus-sh/agentic-business-model-canvas/tree/main/examples/mensa-retter/referenz/stand/12-nach-review-model) (`CANVAS.md`, Block 11)
- nach `/model-retro`: [Stand 13-nach-model-retro](https://github.com/opencampus-sh/agentic-business-model-canvas/tree/main/examples/mensa-retter/referenz/stand/13-nach-model-retro) (`SKILL-PROPOSALS.md`)

Deine Karten, Sätze und Nummern werden anders aussehen; vielleicht wählst du sogar einen anderen Weg. Das ist in Ordnung. Prüfe die Regeln:

- [ ] Hat jede Karte genau eine Annahme, eine Schwelle und mindestens zwei Personen oder Organisationen?
- [ ] Prüft der Test für die Zahlungsbereitschaft ein Verhalten oder eine Aussage über sich selbst – keine „Würdet ihr …?“-Umfrage?
- [ ] Ist die Schwelle nach dem Ergebnis gleich geblieben, und ist die Annahme „Einrichtungen nehmen das Essen an“ *widerlegt*?
- [ ] Bleiben die zwei Einrichtungen, die angenommen haben, als eigene *belegte* Zeile erhalten?
- [ ] Steht euer abgelehnter Vorschlag des Agenten mit Grund in `DECISIONS.md` – und habt ihr den Weg selbst gewählt?

## Selbstcheck

??? question "1. Eure Schwelle war „mindestens 3 von 4 Einrichtungen nehmen an mindestens 2 Abenden Essen an“. Es waren 2 von 4. Euer Teammitglied sagt: „2 von 4 ist doch auch gut.“ Was nun?"
    Die Annahme ist nach eurer Schwelle nicht belegt. Senkt ihr die Schwelle jetzt, ist das Ergebnis nur noch ein Signal. Die positiven Beobachtungen (zwei Einrichtungen haben angenommen) bleiben als eigene, belegte Zeilen erhalten.

??? question "2. Das Studierendenwerk sagt: „Machen wir gern mit, wenn die Haftung geklärt ist.“ Belegt, widerlegt oder offen?"
    Offen: Die Zusage hängt an einer Bedingung. Die Karte bleibt auf *läuft*.

??? question "3. Eine kritische Annahme ist widerlegt, und keine engere Ersatz-Annahme ist durch eure Interviews oder Tests gestützt. Welcher Weg?"
    Neu ansetzen (Pivot) – „Anpassen“ setzt voraus, dass eine engere Ersatz-Annahme belegt ist.

??? question "4. Warum sollen die Testkarten vor dem Test committet werden?"
    Damit im Verlauf sichtbar ist, dass die Schwelle vor dem Ergebnis feststand. `/log-evidence` prüft das.

## Übertragen auf euer Projekt

Ruft `/to-tests` für eure wichtigste kritische Annahme auf, legt die Schwelle im Team fest und committet die Karte. Den Test macht ihr im Changemaker-Kurs; danach `/log-evidence`, `/review-model` und `/model-retro`.

## Am Ende des Kurses

Ihr habt es geschafft, wenn in eurem Projekt:

- der Check ohne **FEHLER** durchläuft,
- mindestens eine kritische Annahme eine Testkarte mit Schwelle hat,
- und im Entscheidungslog mindestens ein abgelehnter Vorschlag des Agenten mit Begründung steht.
