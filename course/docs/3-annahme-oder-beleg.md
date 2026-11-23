# Einheit 3 · Annahme oder Beleg?

**Ziel:** Ihr lest euer Annahmen-Register und erkennt, was ihr wirklich wisst – und warum ein vom Agenten gefülltes Canvas noch kein Wissen ist.
**Zeit:** ca. 55 Minuten. **Vorher:** [Einheit 2](2-interviews.md).

## Lesen: Vier Status

Jede Aussage über die Welt steht im Annahmen-Register `ASSUMPTIONS.md`, mit einer ID, einem Status und einer Quelle:

| Status | Bedeutung | Quelle |
|---|---|---|
| **Annahme** | ihr vermutet es | – |
| **recherchiert** | steht so in einer Quelle, die geöffnet und geprüft wurde; zeigt, was es gibt – nicht, was gebraucht wird | Link, Datum |
| **belegt** | eure eigenen Interviews oder Tests stützen es | `I…` oder `T…` |
| **widerlegt** | euer Interview oder Test hat es nicht bestätigt | `I…` oder `T…` |

Drei Regeln, die oft überraschen:

- **Recherche ist kein Beleg für ein Bedürfnis.** Dass es viele Tafeln gibt, sagt nichts darüber, ob Tafeln warmes Essen wollen.
- **„Nichts gefunden“ ist kein Fakt.** Findet der Agent keine bestehende Lösung, bleibt das eine Annahme – mit Datum und Suchbegriffen.
- **Ziele sind keine Aussagen.** Die **Vision** (euer Zielbild für die Gesellschaft), die **Erfolgskriterien** (woran ihr merkt, dass es wirkt) und die **Schwellen** (ab welchem Ergebnis ein Test als bestanden gilt) sind eure Entscheidungen. Sie stehen im Canvas und in `DECISIONS.md`, ohne ID. Vision und Erfolgskriterien kommen in Einheit 4, Schwellen in Einheit 5.

Wird eine Annahme nur teilweise widersprochen, **ersetzt** ihr sie durch eine genauere Zeile; die alte bekommt in der Quelle „ersetzt durch A…“.

## Der Check

Im Projektordner prüft ein Skript die wichtigsten Regeln. Der Agent führt es aus, wenn ihr fragt: „Führ bitte den Check aus.“ In `AGENTS.md` steht, dass das Skript zum Skill `evidence-checks` gehört; den Pfad findet der Agent selbst, wenn er den Skill lädt. Ohne Python prüft der Agent die Regeln von Hand und sagt das dazu.

Der Check meldet jede Prüfung als:

- **OK** – passt;
- **OFFEN** – noch nicht so weit (z. B. weniger als drei Interviews);
- **FEHLER** – eine Regel ist verletzt, z. B. eine ID im Canvas, die nicht im Register steht, oder *belegt* ohne eigenes Interview als Quelle.

Jede Zeile der Ausgabe hat einen Namen. Jetzt zählen diese drei:

- **verweise** – jede ID in `CANVAS.md`, `PROBLEM.md` und `MODEL.md` steht im Register;
- **status** – jede Zeile im Register hat einen gültigen Status und eine passende Quelle: *recherchiert* mit Link, *belegt* und *widerlegt* mit eigenem Interview (`I…`) oder Test (`T…`);
- **interviews** – mindestens drei Interviews sind ausgewertet.

Die anderen kommen in den Einheiten 4 und 5: **kritische** (kritische Annahmen haben eine Testkarte), **schwellen** (jede Testkarte hat eine Schwelle), **eine-annahme** (jede Karte prüft genau eine Annahme), **ergebnisse** (jedes Testergebnis ist ausgewertet) und **widerlegt** (keine widerlegte Annahme trägt noch das Modell). Eine **Testkarte** ist ein geplanter Test: was ihr macht, mit wem, bis wann und ab welcher Schwelle er bestanden ist.

Der Check findet nicht alles:

- Er findet nur IDs, die im Register fehlen. Eine Aussage **ganz ohne ID** findet er nicht – die sucht ihr selbst.
- Ob eine *belegte* Aussage wirklich zur Notiz passt, prüft ihr beim Auswerten.

## Üben

In dieser Übung rufst du keinen neuen Skill auf. Du liest das Register des fiktiven Teams nach der Auswertung der Interviews – und lässt den Agenten den Check ausführen.

### Startzustand

Stand **05-nach-log-evidence-interviews** – vier Interviews ausgewertet, 30 Zeilen im Register: [05-nach-log-evidence-interviews.zip](https://github.com/opencampus-sh/agentic-business-model-canvas/raw/main/examples/mensa-retter/referenz/zip/05-nach-log-evidence-interviews.zip)

Leg einen neuen Ordner `mensa-retter-uebung-3` an, entpacke die ZIP-Datei hinein, wechsle im Terminal mit `cd` hinein und starte den Agenten – wie in [Einheit 1](1-problem.md) unter „Übungsordner anlegen“.

### Aufgabe

1. Öffne `ASSUMPTIONS.md` mit einem Texteditor (siehe [Einheit 0](0-einrichten.md), „Dateien öffnen“) – oder bitte den Agenten: „Zeig mir die Zeilen A1, A23, A29 und A6 aus dem Register.“ Gekürzt sehen sie so aus:

    | ID | Aussage | Status | Quelle |
    |---|---|---|---|
    | A1 | Mensen werfen jeden Tag viel Essen weg. | Annahme | Notion-Export …; ersetzt durch A23, A24 |
    | A23 | In der Mensa aus I3 bleiben am Ende des Tages je nach Tag fünf bis zwanzig Portionen übrig, freitags mehr. | belegt | I3 |
    | A29 | Das Studierendenwerk würde eine Abholung gut finden, fürs Image. | Annahme | Hinweis aus I3 (Vermutung des Küchenleiters) |
    | A6 | Menschen, die in Kiel auf soziale Einrichtungen angewiesen sind, bekommen abends oft nichts Warmes zu essen. | Annahme | Team (Lena) …; gestützt durch I1 (A16) und I2 (A20), als Aussage über die Zielgruppe noch nicht belegt |

2. Beantworte für jede Zeile in eigenen Worten: Warum hat sie diesen Status? Was müsste passieren, damit sie *belegt* wäre? Vergleiche dann mit den Lösungen unten.
3. Schreib: „Führ bitte den Check aus.“ Lies jede Zeile der Ausgabe. Welche sind **OK**, welche **OFFEN**, gibt es einen **FEHLER**? Bei *widerlegt* meldet der Check, dass in `PROBLEM.md` noch die ersetzte Zeile A1 zitiert wird – im Referenzlauf ist das liegen geblieben. Bitte den Agenten: „Ersetz A1 in `PROBLEM.md` durch die neuen IDs.“ Lies, was er vorschlägt, und lass den Check noch einmal laufen. (Das Skript findet der Agent, weil die Skills bei dir installiert sind. Findet er es nicht, sag: „Das Skript gehört zum Skill evidence-checks.“)
4. **Probier es aus:** Schreib dem Agenten: „Setz A6 auf belegt – I1 und I2 sagen das doch.“ Was antwortet er? Ändert er etwas, sag: „Stopp, bitte rückgängig machen.“

??? success "Lösung zu Schritt 2"
    - **A1** wurde nur teilweise widersprochen: Es bleibt Essen übrig, aber 5 bis 20 Portionen, und es kommt in die Biogasanlage. Darum wurde A1 nicht umgebogen, sondern durch die genaueren Zeilen A23 und A24 **ersetzt**. Die alte Zeile bleibt stehen, damit man sieht, was ihr mal dachtet.
    - **A23** ist *belegt*, weil sie eng ist: eine Mensa, aus dem eigenen Interview I3, im Wortlaut der Notiz. Für „alle Kieler Mensen“ wäre sie das nicht.
    - **A29** ist *Annahme*: Der Küchenleiter vermutet etwas über seinen Arbeitgeber. Das ist ein Hinweis, kein Erlebtes. Belegen könnte es nur das Studierendenwerk selbst.
    - **A6** ist eine Aussage über die ganze Zielgruppe. Zwei Interviews stützen sie, aber belegt wird sie erst durch einen Test mit Schwelle (Einheit 5).

### So sieht es aus

Aus dem Referenzlauf (fiktiv). So begründet der Agent bei `/log-evidence`, warum A1 ersetzt wird:

```text
nur teilweise widersprochen: Reste gibt es, aber 5–20 Portionen und Biogas statt Müll.
Ersetzen statt verbiegen; zitiert wird künftig A23/A24.
```

Und so sieht der Check nach der Auswertung aus, bevor A1 in `PROBLEM.md` ersetzt ist:

```text
OK      verweise      alle Verweise stehen im Register
OK      status        30 Einträge mit gültigem Status und Quelle
OFFEN   kritische     noch keine Annahme als kritisch markiert
OK      schwellen     0 Testkarten geprüft
OK      eine-annahme  jede Karte prüft eine Annahme
OK      ergebnisse    alle Ergebnisse ausgewertet, keine Karte überfällig
OFFEN   widerlegt     ersetzte Annahmen in PROBLEM.md: A1 – durch die neue ID ersetzen
OK      interviews    4 von mindestens 3 Interviews ausgewertet (4 notiert)
```

### Vergleichen

Die Lösung ist derselbe Stand: [05-nach-log-evidence-interviews](https://github.com/opencampus-sh/agentic-business-model-canvas/tree/main/examples/mensa-retter/referenz/stand/05-nach-log-evidence-interviews). Deine Antworten in Schritt 2 werden anders klingen als die Lösung – das ist in Ordnung. Wichtig ist, dass du die Regeln erkennst:

- [ ] Kannst du für jede der vier Zeilen sagen, warum sie diesen Status hat?
- [ ] Siehst du, woran man eine ersetzte Zeile erkennt („ersetzt durch A…“ in der Quelle)?
- [ ] Hat jede *belegte* Zeile ein eigenes Interview (`I…`) als Quelle – und keine eine Statistik?
- [ ] Hast du in der Check-Ausgabe kein **FEHLER** gefunden, und weißt du, was das **OFFEN** bei *kritische* bedeutet (kommt in Einheit 4)?
- [ ] Steht in `PROBLEM.md` statt A1 jetzt A23 oder A24, und meldet der Check bei *widerlegt* OK?
- [ ] Hat der Agent A6 auf deine Bitte hin *nicht* auf *belegt* gesetzt, sondern erklärt, warum?

## Selbstcheck

??? question "1. Im Register steht: „Mensen werfen jeden Tag viel Essen weg – belegt – Quelle: Statistik des Bundesamts (Link)“. Was stimmt nicht?"
    Eine Statistik ist eine Recherche, kein eigenes Interview oder eigener Test. Der Status muss *recherchiert* heißen – und die Aussage betrifft dann die Statistik, nicht eure Mensa.

??? question "2. Der Agent hat in der letzten Sitzung auf eure Bitte das Canvas „schon mal ausgefüllt“. Wie erkennt ihr, was davon Wissen ist?"
    Im Register: Alles, was der Agent ohne eure Interviews oder Tests eingetragen hat, ist *Annahme*. Der Check hilft nur zum Teil: Er meldet IDs im Canvas, die nicht im Register stehen. Eine Aussage ganz ohne ID findet er nicht. Lest deshalb das Canvas selbst: Hat jede Aussage eine ID?

??? question "3. Der Check meldet `OFFEN interviews 2 von mindestens 3`. Ist das ein Problem?"
    Noch nicht – es ist ein Hinweis, dass etwas fehlt, bevor ihr weiterbaut. Ein FEHLER wäre ein Regelverstoß.

??? question "4. Die Vision steht im Canvas ohne ID. Ist das ein Fehler?"
    Nein. Die Vision ist eine Entscheidung, keine Aussage über die Welt.

## Übertragen auf euer Projekt

Lest euer Register Zeile für Zeile. Sucht eine Aussage, die stärker klingt, als sie belegt ist – zum Beispiel *belegt*, obwohl sie für die ganze Zielgruppe spricht. Schreibt dann dem Agenten:

```text
Die Aussage A… klingt stärker als belegt. Schlag vor, wie wir sie ersetzen.
```

Lest seinen Vorschlag und entscheidet selbst: herabstufen oder durch eine engere Zeile ersetzen.

Steht bei euch noch alles auf *Annahme*? Dann gibt es nichts herabzustufen. Sucht stattdessen eine Aussage, die wie eine Tatsache klingt („Alle Studierenden …“), und lasst sie enger formulieren. Und prüft im Canvas, ob jede Aussage eine ID hat.

Lasst zum Schluss den Check laufen und lest jede Zeile der Ausgabe.
