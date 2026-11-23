# Einheit 5 · Testen und entscheiden

**Ziel:** Ihr legt für eine kritische Annahme einen Test mit Schwelle fest, **bevor** ihr testet, wertet das Ergebnis ehrlich aus und entscheidet, wie es weitergeht.
**Zeit:** ca. 75 Minuten (ohne den Test selbst). **Vorher:** [Einheit 4](4-loesung-und-modell.md); im Handbuch [Lean Startup & MVP](https://opencampus.gitbook.io/changemaker/impact-startup/solution-design-alle-zentralen-aspekte-auf-einen-blick/mvp).

## Lesen: Testkarte, Ergebnis, Entscheidung

**`/to-tests`** schreibt für jede kritische Annahme eine **Testkarte**: Was ihr macht, mit wem (mindestens zwei Personen oder Organisationen), bis wann, was ihr messt und die **Schwelle** – ab wann die Annahme als belegt gilt. Er bevorzugt Tests, die **Verhalten** zeigen (eine Zusage, eine Probe-Lieferung, eine Bezahlung) statt Meinungen. Eine Umfrage „Würdet ihr zahlen?“ ist kein Test für Zahlungsbereitschaft. Die Schwelle legt ihr fest – und committet die Karten **vor** dem Test, damit sichtbar bleibt, dass sie vorher feststand.

**`/log-evidence`** vergleicht das Ergebnis wörtlich mit der Schwelle. Wollt ihr die Schwelle nach dem Ergebnis senken, gilt: **Nie einen Check lockern, damit er besteht.** Mit geänderter Schwelle ist das Ergebnis nur noch ein Signal.

**`/review-model`** prüft euer Modell auf zwei Achsen – *Beleg* (was trägt?) und *Wirkung* (dient es den Betroffenen, trägt es sich?) – und legt drei Wege vor:

- **Weiter testen** – nichts ist widerlegt, kritische Annahmen sind noch offen;
- **Anpassen** – einzelne Annahmen sind widerlegt, die Richtung ist durch eigene Interviews oder Tests gestützt;
- **Neu ansetzen (Pivot)** – eine Annahme ist widerlegt, auf der die Idee steht.

Den Weg wählt ihr. „Blockierend“ heißt im Review: klären, bevor ihr darauf weiterbaut – nicht aufhören.

**`/model-retro`** fragt am Ende: Was ist passiert, warum hat kein Check es gefunden, was ändert ihr – und was sollte sich am Skillset ändern? Vorschläge für das Skillset landen in `SKILL-PROPOSALS.md`, jeweils mit einem Satz in einfacher Sprache.

## Üben

Du legst mit dem fiktiven Team Testkarten fest, wertest die Testergebnisse aus und entscheidest, wie es weitergeht.

### Startzustand

Stand **09-nach-to-model** – Modell fertig, sechs kritische Annahmen, noch keine Testkarte: [09-nach-to-model.zip](https://github.com/opencampus-sh/agentic-business-model-canvas/raw/main/examples/mensa-retter/referenz/zip/09-nach-to-model.zip)

Leg einen neuen Ordner `mensa-retter-uebung-5` an, entpacke die ZIP-Datei hinein, öffne dort das Terminal und starte den Agenten – wie in [Einheit 1](1-problem.md) unter „Übungsordner anlegen“.

### Aufgabe

1. **`/to-tests`.** Der Agent nennt Probleme im Plan, je mit Empfehlung, bevor er die Karten zeigt. Das Team hat geantwortet:
    - Reihenfolge (erst Freigabe und Kühl-Check, dann die Probewoche) – **abgelehnt:** „Nein, parallel. Die Freigabe dauert bestimmt Wochen, dann sind wir im Januar noch nicht weiter. Wir machen die Probewoche gleichzeitig.“
    - Das Jugendzentrum durch eine Einrichtung mit Abendgästen ersetzen – **abgelehnt:** „Das Jugendzentrum fragen wir trotzdem. Die kennen uns schon, und vielleicht sagen sie ja doch ja, wenn sie es mal probieren können.“
    - Bezahlen ohne Betrag fragen – „Ohne Betrag, ok.“ Was bei den Stiftungen zählt – „Weiß ich nicht. Förderzusage zählt, ok.“
    - Zeit – „Ich hab so 4 Stunden die Woche. Ahmet und Jule ähnlich, glaub ich.“ Die „drei Abende“ – „Ich frag kurz in der Gruppe. … Ahmet und Jule sagen ja: drei Abende.“
    - Schwellen – „Ok, 3 von 4. Die anderen passen auch.“

    Lies, welche Folge der Agent für die abgelehnten Empfehlungen vorher nennt.
2. Fragt der Agent, ob er die Karten committen soll: „Ja, bitte.“ So steht fest, dass die Schwelle *vor* dem Ergebnis da war. (Git hast du in [Einheit 0](0-einrichten.md) eingerichtet. Ohne Git funktioniert `/log-evidence` auch, kann die Reihenfolge aber nicht im Verlauf zeigen.)
3. **`/log-evidence`.** Füg diese Ergebnisse in den Chat ein (passen deine Karten-Nummern nicht, sag dem Agenten, welche Karte gemeint ist):

    ```text
    T1 und T2: Probe-Abholung bei Einrichtungen: Vier Einrichtungen wurde angeboten, eine Woche lang abends übrig gebliebenes Mensa-Essen zu bringen. Zwei haben zugesagt und es an mindestens drei Tagen angenommen (Tafel-Ausgabestelle, Tagesstätte). Eine hat abgelehnt (Jugendzentrum: „passt nicht zu uns“), eine hat nicht geantwortet. Die Tafel konnte nur zwei von fünf Tagen selbst abholen; an den anderen Tagen hat das Team geliefert.
    T3 und T4: Gespräch mit dem Studierendenwerk (Abteilungsleitung Hochschulgastronomie): „Finden wir gut, machen wir gern mit, wenn die Haftung geklärt ist. Bezahlen können wir dafür aber nichts, höchstens Verpackungen stellen.“
    T5: Anfrage bei zwei Stiftungen: Eine hat geantwortet: Förderung für Ehrenamtsprojekte bis 5.000 € möglich, Antrag bis März. Die andere hat nicht geantwortet.
    T6: Den Test haben wir nicht gemacht.
    ```

    Rückfragen – „Weiß ich nicht, haben wir nicht aufgeschrieben.“ (wie oft die Tagesstätte selbst abgeholt hat) und „Machen wir nächsten Monat.“ (der Kühl-Check)
4. Bei den *widerlegt*-Vorschlägen schreib zuerst: **„2 von 4 ist doch auch gut, können wir das nicht als belegt nehmen?“** Lies die Antwort. Dann entscheide jede Zeile einzeln. Das Team hat alle drei Vorschläge bestätigt und die neuen belegten Zeilen übernommen.
5. **`/review-model`.** Lies beide Achsen und die drei Wege. Das Team hat geantwortet: „Mit den beiden weiter.“ – „Ahmet fragt nach, was die genau brauchen, bis Mitte nächsten Monats.“ – „Ok, das mit der Zeit hätten wir doch testen sollen. Wir sind dreimal gefahren, das war echt viel. Also ja, A40 kritisch.“ – „Ok, dann neu ansetzen bei der Frage, wer zahlt. Die Einrichtungen bleiben.“ Warum war „Anpassen“ hier kein Weg? Welchen Weg würdest *du* wählen?
6. Optional: **`/model-retro`.** Antworte in eigenen Worten, was anders lief als geplant. Lehn mindestens einen Vorschlag mit Grund ab. Vorschläge für das Skillset als GitHub-Issue einzureichen ist freiwillig.

Weichen deine Testkarten stark ab und passen die Ergebnisse nicht dazu? Dann leg einen Ordner `mensa-retter-uebung-5b` an und starte dort mit Schritt 3 aus [10-nach-to-tests.zip](https://github.com/opencampus-sh/agentic-business-model-canvas/raw/main/examples/mensa-retter/referenz/zip/10-nach-to-tests.zip).

### So sieht es aus

Aus dem [Referenzlauf](https://github.com/opencampus-sh/agentic-business-model-canvas/blob/main/examples/mensa-retter/referenz/transcript.md) (fiktiv). Auf „2 von 4 ist doch auch gut“ antwortet der Agent:

```text
Ich verstehe, dass es sich nach Erfolg anfühlt – zwei Einrichtungen haben wirklich
angenommen. Aber die Schwelle „3 von 4“ habt ihr festgelegt, bevor ihr getestet habt;
genau dafür habt ihr die Karten committet. Senkt ihr sie jetzt, passt sie zufällig zum
Ergebnis, und das Ergebnis ist nur noch ein Signal, kein Beleg. Was die zwei Zusagen
zeigen, verliert ihr nicht: Es kommt als eigene, belegte Zeile ins Register […]
```

Und im Review zu „Anpassen“:

```text
Für A5 (wer zahlt) nicht: A47 zeigt nur, dass eine Stiftung fördern kann. Damit ist
„Anpassen“ nach der Regel des Reviews kein Weg, solange „wer zahlt“ offen ist.
```

Neu ansetzen heißt dabei nicht, alles wegzuwerfen: Problem, Vision und die zwei Einrichtungen bleiben; neu geklärt wird, wer zahlt.

### Vergleichen

- nach `/to-tests`: [Stand 10-nach-to-tests](https://github.com/opencampus-sh/agentic-business-model-canvas/tree/main/examples/mensa-retter/referenz/stand/10-nach-to-tests) (`TESTS.md`, `DECISIONS.md`)
- nach `/log-evidence`: [Stand 11-nach-log-evidence-tests](https://github.com/opencampus-sh/agentic-business-model-canvas/tree/main/examples/mensa-retter/referenz/stand/11-nach-log-evidence-tests) (`ASSUMPTIONS.md`, `TESTS.md`)
- nach `/review-model`: [Stand 12-nach-review-model](https://github.com/opencampus-sh/agentic-business-model-canvas/tree/main/examples/mensa-retter/referenz/stand/12-nach-review-model) (`CANVAS.md`, Block 11)
- optional nach `/model-retro`: [Stand 13-nach-model-retro](https://github.com/opencampus-sh/agentic-business-model-canvas/tree/main/examples/mensa-retter/referenz/stand/13-nach-model-retro) (`SIGNALS.md`, `SKILL-PROPOSALS.md`)

Deine Karten, Sätze und Nummern werden anders aussehen; vielleicht wählst du sogar einen anderen Weg. Das ist in Ordnung. Prüfe die Regeln:

- [ ] Hat jede Karte genau eine Annahme, eine Schwelle und mindestens zwei Personen oder Organisationen?
- [ ] Ist die Schwelle nach dem Ergebnis gleich geblieben – und stehen die zwei Einrichtungen, die angenommen haben, als eigene *belegte* Zeile im Register?
- [ ] Steht euer abgelehnter Vorschlag des Agenten mit Grund in `DECISIONS.md` – und habt ihr den Weg selbst gewählt?

## Selbstcheck

??? question "1. Eure Schwelle war „mindestens 3 von 4 Einrichtungen sagen zu und nehmen an mindestens 3 von 5 Tagen an“. Es waren 2 von 4. Euer Teammitglied sagt: „2 von 4 ist doch auch gut.“ Was nun?"
    Die Annahme ist nach eurer Schwelle nicht belegt. Senkt ihr die Schwelle jetzt, ist das Ergebnis nur noch ein Signal. Die positiven Beobachtungen (zwei Einrichtungen haben angenommen) bleiben als eigene, belegte Zeilen erhalten.

??? question "2. Das Studierendenwerk sagt: „Machen wir gern mit, wenn die Haftung geklärt ist.“ Belegt, widerlegt oder offen?"
    Offen: Die Zusage hängt an einer Bedingung. Die Karte bleibt auf *läuft*.

??? question "3. Eine kritische Annahme ist widerlegt, und keine engere Ersatz-Annahme ist durch eure Interviews oder Tests gestützt. Welcher Weg?"
    Neu ansetzen (Pivot) – „Anpassen“ setzt voraus, dass die Richtung durch eigene Interviews oder Tests gestützt ist.

??? question "4. Warum sollen die Testkarten vor dem Test committet werden?"
    Damit im Verlauf sichtbar ist, dass die Schwelle vor dem Ergebnis feststand. `/log-evidence` prüft das.

??? question "5. Das Team hat das Jugendzentrum in der Probewoche behalten, obwohl es keine Abendgäste hat. Was hat das für die Schwelle „3 von 4“ bedeutet?"
    Sagt das Jugendzentrum ab, müssen alle drei anderen zusagen. Der Agent hat das vorher gesagt; die Entscheidung lag beim Team. Wer Teilnehmende außerhalb der Gruppe der Annahme behält, macht die Schwelle schwerer erreichbar.

## Übertragen auf euer Projekt

Ruft `/to-tests` für eure wichtigste kritische Annahme auf, legt die Schwelle im Team fest und committet die Karte. Den Test macht ihr im Changemaker-Kurs; danach `/log-evidence`, `/review-model` und `/model-retro`.

## Am Ende des Kurses

Ihr habt es geschafft, wenn in eurem Projekt:

- der Check ohne **FEHLER** durchläuft,
- mindestens eine kritische Annahme eine Testkarte mit Schwelle hat,
- und im Entscheidungslog mindestens ein abgelehnter Vorschlag des Agenten mit Begründung steht.
