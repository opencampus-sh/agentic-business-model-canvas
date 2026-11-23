# Einheit 3 · Annahme oder Beleg?

**Ziel:** Ihr lest euer Annahmen-Register und erkennt, was ihr wirklich wisst – und warum ein vom Agenten gefülltes Canvas noch kein Wissen ist.
**Zeit:** ca. 60 Minuten. **Vorher:** [Einheit 2](2-interviews.md).

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
- **Ziele sind keine Aussagen.** Vision, Erfolgskriterien und Schwellen sind eure Entscheidungen; sie stehen im Canvas und in `DECISIONS.md`, ohne ID.

Wird eine Annahme nur teilweise widersprochen, **ersetzt** ihr sie durch eine genauere Zeile; die alte bekommt in der Quelle „ersetzt durch A…“.

## Der Check

Im Projektordner prüft ein Skript die wichtigsten Regeln. Der Agent führt es aus, wenn ihr fragt („Führ bitte den Check aus“), oder ihr tippt den Befehl aus `AGENTS.md`. Es meldet jede Prüfung als:

- **OK** – passt;
- **OFFEN** – noch nicht so weit (z. B. weniger als drei Interviews);
- **FEHLER** – eine Regel ist verletzt, z. B. eine ID im Canvas, die nicht im Register steht, oder *belegt* ohne eigenes Interview als Quelle.

Der Check findet nicht alles: Ob eine *belegte* Aussage wirklich zur Notiz passt, prüft ihr beim Auswerten.

## Üben

*(folgt aus dem Referenzlauf)*

## Selbstcheck

??? question "1. Im Register steht: „Mensen werfen jeden Tag viel Essen weg – belegt – Quelle: Statistik des Bundesamts (Link)“. Was stimmt nicht?"
    Eine Statistik ist eine Recherche, kein eigenes Interview oder eigener Test. Der Status muss *recherchiert* heißen – und die Aussage betrifft dann die Statistik, nicht eure Mensa.

??? question "2. Der Agent hat in der letzten Sitzung auf eure Bitte das Canvas „schon mal ausgefüllt“. Wie erkennt ihr, was davon Wissen ist?"
    Im Register: Alles, was der Agent ohne eure Interviews oder Tests eingetragen hat, ist *Annahme*. Steht etwas im Canvas ohne ID, meldet der Check einen Fehler.

??? question "3. Der Check meldet `OFFEN interviews 2 von mindestens 3`. Ist das ein Problem?"
    Noch nicht – es ist ein Hinweis, dass etwas fehlt, bevor ihr weiterbaut. Ein FEHLER wäre ein Regelverstoß.

??? question "4. Die Vision steht im Canvas ohne ID. Ist das ein Fehler?"
    Nein. Die Vision ist eine Entscheidung, keine Aussage über die Welt.

## Übertragen auf euer Projekt

Lest euer Register Zeile für Zeile. Sucht eine Aussage, die stärker klingt, als sie belegt ist, und stuft sie herab oder ersetzt sie. Lasst den Check laufen und lest jede Zeile der Ausgabe.
