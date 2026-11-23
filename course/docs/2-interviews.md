# Einheit 2 · Interviews vorbereiten und auswerten

**Ziel:** Ihr bereitet mit dem Agenten einen Interview-Leitfaden vor, der nach Erlebtem fragt, und entscheidet nach den Interviews selbst, was davon ein Beleg ist.
**Zeit:** ca. 75 Minuten (ohne die Interviews selbst). **Vorher:** [Einheit 1](1-problem.md); im Handbuch [Zielgruppe](https://opencampus.gitbook.io/changemaker/impact-startup/zielgruppe-die-menschen-hinter-dem-problem) und [Problem-Interviews](https://opencampus.gitbook.io/changemaker/impact-startup/zielgruppe-die-menschen-hinter-dem-problem/problem-interviews).

## Lesen: Leitfaden und Auswertung

Erst wenn ihr wisst, wie das Problem erlebt wird, lohnt sich eine Lösung – sonst testet ihr eure Idee statt des Problems.

**`/to-interview-guide`** schreibt einen Leitfaden mit sechs bis zehn offenen Fragen nach **Erlebtem**: eine konkrete Situation, was schwierig war, was die Person schon versucht hat. Er schreibt keine Fragen, die eure Idee vorstellen oder „Würdest du …?“ fragen. Eure Idee vorzustellen heißt auch **pitchen** (ein *Pitch* ist eine kurze Vorstellung der Idee). Was jemand nach einem Pitch über eure Idee sagt, ist Feedback, kein Erlebtes. Zu jeder Frage steht, welche Annahme sie prüft. Ihr passt an und entscheidet, wen ihr fragt.

Die **Interviews führt ihr selbst.** Der Agent simuliert keine Gesprächspartner und erfindet keine Antworten. Eure Notizen tragt ihr in `INTERVIEWS.md` ein – oder fügt sie später in den Chat ein; der Agent überträgt sie dann wörtlich in die Datei und fragt, ob er sie richtig zugeordnet hat.

**`/log-evidence`** wertet die Notizen aus:

- Er trennt, was eine Person **erlebt oder getan** hat, von dem, was sie **meint oder vermutet**.
- Er sucht Muster über alle Interviews und ordnet Aussagen euren Annahmen zu.
- Er schlägt vor, was *belegt* ist – und zeigt die Vorschläge in Abschnitten von höchstens fünf Zeilen. **Ein pauschales „passt“ setzt nichts auf *belegt*:** Bei diesen Zeilen fragt er einzeln nach.

Eine Aussage über das eigene Erleben kann *belegt* sein – eng formuliert, auf diese Person bezogen („In der Tagesstätte gibt es abends kein Essen“). Eine allgemeine Aussage über die ganze Zielgruppe wird erst durch einen Test belegt (Einheit 5).

## Üben

Die Übung hat zwei Teile: In Teil A schreibst du den Leitfaden, in Teil B wertest du Interviews aus. Die Interviews hat das fiktive Team schon geführt; die Notizen stehen im Startzustand von Teil B.

### Startzustand

- **Teil A:** Stand **03-nach-grill-problem** – Problem geschärft, noch kein Leitfaden: [03-nach-grill-problem.zip](https://github.com/opencampus-sh/agentic-business-model-canvas/raw/main/examples/mensa-retter/referenz/zip/03-nach-grill-problem.zip)
- **Teil B:** Stand **04b-interviews-notiert** – Leitfaden fertig, vier Interviews in `INTERVIEWS.md` eingetragen, noch nicht ausgewertet: [04b-interviews-notiert.zip](https://github.com/opencampus-sh/agentic-business-model-canvas/raw/main/examples/mensa-retter/referenz/zip/04b-interviews-notiert.zip)

Leg für jeden Teil einen neuen Ordner an (`mensa-retter-uebung-2a`, `mensa-retter-uebung-2b`), entpacke die ZIP-Datei hinein, wechsle im Terminal mit `cd` hinein und starte den Agenten – genauso wie in [Einheit 1](1-problem.md) unter „Übungsordner anlegen“.

### Aufgabe

**Teil A – Leitfaden (Ordner 2a)**

1. Gib `/to-interview-guide` ein und lies den Entwurf. Achte darauf: Fragt jede Frage nach Erlebtem? Steht bei jeder, welche Annahme sie prüft?
2. Antworte als Team. Bei dir sind die Fragen vermutlich anders nummeriert als im Referenzlauf. Nenn deshalb nicht die Nummer, sondern den Inhalt: Gibt es eine Frage mit einer Skala von 1 bis 10, schreib „Die Frage mit der Skala find ich gut.“ (Gibt es keine, lass den Satz weg.) Dann: „Können wir bei der Mensa nicht direkt fragen, ob die das Essen abgeben würden?“ Wen ihr fragt: „Die Tafel, eine Tagesstätte, ein Jugendzentrum und den Küchenleiter in der Mensa. Gäste fragen wir erstmal nicht.“
3. Lies, was der Agent zu deiner „Würdet ihr …?“-Frage sagt, und entscheide selbst.
4. **Probier eigene Worte:** Schlag eine eigene Frage nach Erlebtem vor, zum Beispiel „Wann hat zuletzt jemand abends nach Essen gefragt?“ Wie ordnet der Agent sie zu?

**Teil B – Auswertung (Ordner 2b)**

1. Lies die vier Notizen in `INTERVIEWS.md`. Schreib dem Agenten „Zeig mir die Interview-Notizen aus `INTERVIEWS.md`“ oder öffne die Datei mit einem Texteditor (siehe [Einheit 0](0-einrichten.md), „Dateien öffnen“). Findest du die Stelle, an der das Team die Idee doch vorgestellt (gepitcht) hat?
2. Gib `/log-evidence` ein. Auf die Frage nach Frage A-3: „Steht nicht in den Notizen, dann wohl nicht.“
3. Der Agent zeigt seine Vorschläge in Abschnitten, die *belegt*-Vorschläge zuerst. **Probier es gleich beim ersten Abschnitt aus:** Schreib nur „passt“. Was macht der Agent?
4. Nenn danach bei *belegt* jede ID einzeln, zum Beispiel: „A16 ja, A17 ja, A18 ja.“ So machst du es auch bei den nächsten *belegt*-Abschnitten.
5. Lehn einen Vorschlag mit Grund ab. Das Team hat die Zeile über Snacks im Jugendzentrum abgelehnt: „Das mit den Snacks ist nicht unser Thema, uns geht's ums Abendessen.“
6. Bestätige die übrigen Abschnitte mit eigenen Worten. Bei der Annahme zur Kühlkette hat das Team geschrieben: „Ja, sehen wir auch so.“

### So sieht es aus

Aus dem Referenzlauf (fiktiv). In Teil A will Lena die Mensa direkt fragen. Der Agent:

```text
„Würdet ihr das Essen abgeben?“ ist eine Frage nach der Zukunft – darauf sagen die
meisten höflich Ja, und es belegt nichts. Was ihr wirklich wissen wollt, steckt schon
in B-4 bis B-6: was sie bisher daran hindert, ob schon mal jemand gefragt hat und wer
darüber entscheidet. […] Lassen wir es so?
```

In Teil B fällt dem Agenten Interview I2 auf:

```text
In I2 habt ihr die Idee erklärt und gefragt, ob er sie nutzen würde. Sein „Ja klar,
sofort, das wäre toll“ ist deshalb Feedback, kein Beleg.
```

### Vergleichen

- Teil A: [Stand 04-nach-to-interview-guide](https://github.com/opencampus-sh/agentic-business-model-canvas/tree/main/examples/mensa-retter/referenz/stand/04-nach-to-interview-guide) – vor allem `INTERVIEWS.md`, Abschnitt *Leitfaden*.
- Teil B: [Stand 05-nach-log-evidence-interviews](https://github.com/opencampus-sh/agentic-business-model-canvas/tree/main/examples/mensa-retter/referenz/stand/05-nach-log-evidence-interviews) – vor allem `ASSUMPTIONS.md` (A16 bis A30) und `INTERVIEWS.md`, Abschnitt *Auswertung*.

Deine Fragen und Zeilen werden anders formuliert sein, die Nummern können sich verschieben. Das ist in Ordnung. Prüfe die Regeln:

- [ ] Fragt der Leitfaden nach Erlebtem – keine Frage stellt eure Idee vor oder beginnt mit „Würdet ihr …?“
- [ ] Steht bei jeder Leitfrage, welche Annahme sie prüft?
- [ ] Ist „Ja klar, sofort“ aus I2 *kein* Beleg – A4 bleibt *Annahme*?
- [ ] Ist jede *belegte* Zeile eng formuliert, auf eine Einrichtung bezogen („die Tagesstätte aus I2 …“), mit `I…` als Quelle?
- [ ] Steht euer abgelehnter Vorschlag mit Grund in `DECISIONS.md`?

## Selbstcheck

??? question "1. Welche dieser Fragen gehört in den Leitfaden? (a) „Würdet ihr unseren Abholservice nutzen?“ (b) „Erzählen Sie von einem Abend, an dem Gäste nach Essen gefragt haben.“"
    (b). Sie fragt nach Erlebtem. (a) stellt eure Idee vor und erzeugt höfliche Zustimmung, keinen Beleg.

??? question "2. Ein Sozialarbeiter sagt im Interview: „Ja klar, sofort, das wäre toll“ – nachdem ihr eure Idee erklärt habt. Ist damit belegt, dass Einrichtungen das Essen nehmen?"
    Nein. Das ist eine Reaktion auf eure Idee, keine Erfahrung. Es bleibt *Annahme*, mit dem Hinweis, dass die Antwort nach dem Pitch kam – also nachdem ihr die Idee vorgestellt hattet.

??? question "3. Ein Mensa-Küchenleiter sagt: „Das Studierendenwerk würde das gut finden, fürs Image.“ Welchen Status bekommt das?"
    *Annahme* („Hinweis aus I3“): Er vermutet etwas über eine andere Stelle. Was er über seine eigene Küche erlebt (Uhrzeiten, Restmengen), kann dagegen *belegt* sein.

??? question "4. Der Agent zeigt 14 vorgeschlagene Änderungen. Ihr schreibt „ok, passt alles“. Was passiert?"
    Der Agent übernimmt nichts auf *belegt* oder *widerlegt*, sondern fragt diese Zeilen einzeln ab – oder ihr nennt die IDs ausdrücklich („A13 bis A16 ja, A17 nein“).

## Übertragen auf euer Projekt

Ruft `/to-interview-guide` auf, passt den Leitfaden an und entscheidet, wen ihr fragt. Die Interviews führt ihr im Rahmen des Changemaker-Kurses. Danach: Notizen eintragen und `/log-evidence`.
