# Einheit 1 · Das Problem schärfen

**Ziel:** Ihr beschreibt euer Problem in euren eigenen Worten – mit Ursachen, Folgen und Zielgruppe –, und der Agent hilft beim Ordnen, ohne es für euch zu formulieren.
**Zeit:** ca. 75 Minuten. **Vorher:** [Einheit 0](0-einrichten.md); im Handbuch [Problemanalyse](https://opencampus.gitbook.io/changemaker/impact-startup/problemanalyse-am-anfang-steht-das-problem) mit 5 Whys, Folgen und Problembaum.

## Lesen: Wie `/grill-problem` mit euch arbeitet

`/grill-problem` stellt Fragen **in Runden**. Jede Frage sieht so aus:

```text
❓ F1 – Kernproblem: Was ist das Problem – aus Sicht der Menschen, die es haben?

➡️ (Empfehlung des Agenten)
```

Drei Dinge sind wichtig:

1. **Eigene Worte zuerst.** Bei Problem, Ursachen und Zielgruppe fragt der Agent zuerst nach euren Worten. Schreibt etwas Kurzes, auch wenn es holprig ist. Übernehmt ihr seinen Vorschlag unverändert, notiert er das im Entscheidungslog – damit später sichtbar ist, wessen Worte im Canvas stehen.
2. **„Weiß ich nicht“ ist eine gute Antwort.** Der Agent schreibt den Punkt dann unter *Noch offen* in `PROBLEM.md`. Genau diese Punkte klärt ihr in den Interviews. Ein erfundener Grund wäre schlimmer als ein offener.
3. **Das Problem ist keine fehlende Lösung.** „Es gibt keine App für …“ beschreibt eure Idee, nicht das Problem. Der Agent fragt dann zurück: Was passiert den Menschen, solange es sie nicht gibt?

Die **5 Whys** laufen als eigene kleine Schleife: ein „Warum?“ pro Nachricht, bis ihr an einem Punkt seid, an dem ihr ansetzen könnt – oder bis ihr es nicht wisst.

Am Ende stehen Kernproblem, Ursachen, Folgen, Problembaum und Problem-Hypothesen in `PROBLEM.md`, und **jede Aussage hat eine ID** im Annahmen-Register, zum Beispiel `[A7]`. Fast alles hat jetzt den Status *Annahme* – und das ist richtig so.

## Üben

Du übst am Fall Mensa-Retter. Das fiktive Team hat sein Projekt schon angelegt und dabei seine Notion-Seite übernommen: Im Register stehen A1 bis A5, alle mit Status *Annahme*.

### Startzustand

Stand **01-nach-setup-model**, der Projektordner direkt nach `/setup-model`: [01-nach-setup-model.zip](https://github.com/opencampus-sh/agentic-business-model-canvas/raw/main/examples/mensa-retter/referenz/zip/01-nach-setup-model.zip)

**Übungsordner anlegen.** Öffne ein neues Terminal. Leg einen neuen Ordner an, lade die ZIP-Datei hinein, entpacke sie und starte den Agenten:

=== "macOS / Linux"
    ```bash
    mkdir mensa-retter-uebung-1
    cd mensa-retter-uebung-1
    curl -L -o start.zip https://github.com/opencampus-sh/agentic-business-model-canvas/raw/main/examples/mensa-retter/referenz/zip/01-nach-setup-model.zip
    unzip start.zip && rm start.zip
    claude
    ```

=== "Windows (PowerShell)"
    ```powershell
    mkdir mensa-retter-uebung-1
    cd mensa-retter-uebung-1
    Invoke-WebRequest https://github.com/opencampus-sh/agentic-business-model-canvas/raw/main/examples/mensa-retter/referenz/zip/01-nach-setup-model.zip -OutFile start.zip
    Expand-Archive start.zip -DestinationPath .
    Remove-Item start.zip
    claude
    ```

Lieber mit der Maus? Lade die Datei über den Link herunter und entpacke sie per Doppelklick (Windows: Rechtsklick → „Alle extrahieren“). Dann tippst du im Terminal `cd ` (mit Leerzeichen), ziehst den Ordner ins Terminalfenster, drückst ++enter++ und startest `claude`. In den nächsten Einheiten machst du es genauso – nur mit einer anderen Datei und Ordnernummer.

### Aufgabe

1. Gib `/grill-problem` ein. In OpenCode heißt das `@grill-problem`, in Codex `$grill-problem`; ab hier schreiben wir nur die Form für Claude Code.
2. Beantworte die Runden als Team Mensa-Retter. Bei dir können Fragen anders nummeriert oder formuliert sein. So hat das Team geantwortet:
    - Kernproblem (a) oder (b)? – „b. Das Wegwerfen hat uns auf die Idee gebracht, aber eigentlich geht's um die Leute.“ Rahmen: „Kiel.“
    - Kernproblem in euren Worten – „Menschen, die in Kiel auf soziale Einrichtungen angewiesen sind, bekommen abends oft nichts Warmes zu essen.“
    - Erstes „Warum?“ – „Die Einrichtungen haben abends kein Personal zum Kochen.“ Zweites „Warum?“ – **„Weiß ich nicht.“**
    - Recherche? – „Ja, schau mal.“
    - Folgen – „Hungrig ins Bett oder was Kaltes, Billiges. Langfristig vielleicht eher krank. Politisch und kulturell weiß ich nicht.“ Besonders hart trifft es – „Wohnungslose, vermute ich.“
    - Zielgruppe – „Leute in Tagesstätten für Wohnungslose, bei der Tafel, vielleicht Jugendliche im Jugendzentrum.“
    - Was wisst ihr wirklich? – „Ich hab in der Mensa gesehen, dass nach 14 Uhr Essen in große Tonnen kommt. Wie viel, weiß ich nicht.“
    - Problembaum und Problem-Hypothesen – bestätigen. Offene Punkte – „Wir alle drei, in den Interviews, bis Ende Oktober.“
3. **Probier eigene Worte.** Schreib mindestens das Kernproblem selbst, auch wenn es holprig ist. Und teste einmal, was passiert, wenn du als Kernproblem schreibst: „Es fehlt eine App, die Mensen und Einrichtungen verbindet.“
4. Bestätige am Ende die Blöcke 1 und 2. Fragt der Agent nach einem Commit, kannst du sagen: „Nein, das ist nur eine Übung.“
5. Öffne `PROBLEM.md` und lies sie einmal ganz.

### So sieht es aus

Aus dem Referenzlauf (fiktiv; das Team antwortet als Lena). Nach dem ersten „Warum?“ fragt der Agent:

```text
Warum haben die Einrichtungen abends kein Personal zum Kochen?
```

Lena schreibt: „Weiß ich nicht.“ Der Agent:

```text
Völlig in Ordnung – dann endet die Kette hier. „Warum gibt es abends kein Personal?“
kommt unter Noch offen in PROBLEM.md; genau das könnt ihr in den Interviews fragen.
```

Später fragt Lena, ob die Notion-Hypothese „Das Studierendenwerk würde bezahlen“ [A5] auch in die Interviews soll. Der Agent rät ab:

```text
A5 würde ich nicht dazunehmen: Ob das Studierendenwerk zahlt, ist keine Aussage über
das Problem, und ein Interview kann es nicht belegen – „würden Sie zahlen?“ beantwortet
jeder höflich. Das prüft ihr später mit einem Test (/to-tests). Einverstanden?
```

### Vergleichen

Die Lösung: [Stand 03-nach-grill-problem](https://github.com/opencampus-sh/agentic-business-model-canvas/tree/main/examples/mensa-retter/referenz/stand/03-nach-grill-problem). Schau vor allem in `PROBLEM.md`, `ASSUMPTIONS.md` und `DECISIONS.md`.

Dein Ergebnis wird anders aussehen: andere Sätze, vielleicht andere Nummern. Das ist in Ordnung. Wichtig ist, dass die Regeln eingehalten sind:

- [ ] Steht das Kernproblem in euren Worten und aus Sicht der Menschen – nicht als fehlende App?
- [ ] Hat jede Aussage in `PROBLEM.md` eine ID wie `[A6]`, und steht diese ID in `ASSUMPTIONS.md`?
- [ ] Steht „Weiß ich nicht“ unter *Noch offen* – statt eines erfundenen Grundes?
- [ ] Ist fast alles *Annahme*? Hat alles, was der Agent recherchiert hat, den Status *recherchiert* und einen Link?
- [ ] Steht in `DECISIONS.md`, was ihr entschieden habt – und ob eine Formulierung vom Agenten stammt?

## Selbstcheck

??? question "1. Ihr schreibt als Kernproblem: „Es fehlt eine Plattform, die Mensen und Einrichtungen verbindet.“ Was fragt der Agent zurück, und warum?"
    Was den Betroffenen passiert, solange es die Plattform nicht gibt – zum Beispiel, dass Menschen in Einrichtungen abends nichts Warmes bekommen. Das Problem soll aus Sicht der Betroffenen beschrieben sein, nicht als fehlende Lösung (Handbuch, Problemanalyse).

??? question "2. Beim dritten „Warum?“ wisst ihr nicht weiter. Was tut ihr?"
    „Weiß ich nicht“ sagen. Der Punkt kommt unter *Noch offen* in `PROBLEM.md` und wird in den Interviews geprüft.

??? question "3. Der Agent schlägt eine Formulierung für die Zielgruppe vor, die gut klingt. Ihr sagt „ok, passt“. Was passiert, und was wäre besser?"
    Der Agent übernimmt sie und notiert im Entscheidungslog, dass die Formulierung von ihm stammt. Besser: erst eigene Worte, dann den Vorschlag vergleichen und bewusst übernehmen oder ändern.

??? question "4. Welchen Status haben die Aussagen in `PROBLEM.md` nach dieser Einheit fast alle – und warum?"
    *Annahme*. Ihr habt noch mit niemandem gesprochen; belegt wird erst durch eure Interviews und Tests.

## Übertragen auf euer Projekt

Ruft in eurem Projektordner `/grill-problem` auf und beantwortet die Runden in euren Worten. Sagt „Weiß ich nicht“, wo ihr es nicht wisst. Am Ende: `PROBLEM.md` lesen – erkennt ihr euer Problem wieder?
