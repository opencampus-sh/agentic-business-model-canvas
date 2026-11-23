---
name: to-tests
description: Macht aus euren kritischen Annahmen einen Testplan – eine Testkarte pro Annahme mit Test, Messgröße, Schwelle, mit wem und bis wann – und schlägt einfache MVPs vor.
disable-model-invocation: true
---

# Zum Testplan

Schreib die Testkarten, mit denen das Team seine kritischen Annahmen prüft, so schnell und billig wie möglich. Lies `ASSUMPTIONS.md`, `CANVAS.md` (Block 4 und 6), `MODEL.md`, `TESTS.md` und `DECISIONS.md`. Lade `assumptions` und `evidence-checks`. Ist keine Annahme als kritisch markiert, halte an und schlage `/grill-solution` vor.

## 1. Entwurf

Für jede kritische Annahme mit Status *Annahme* (und jede, die das Team zusätzlich nennt) entwirfst du eine Testkarte in `TESTS.md` nach dem Format der Vorlage – **eine Karte pro Annahme, mit eigener Schwelle**. Prüft ein Test mehrere Annahmen, bekommt jede ihre eigene Karte, die auf denselben Test verweist:

- **Test:** Was das Team macht, damit sich die Annahme zeigt oder nicht. Bevorzuge, was Verhalten zeigt, vor dem, was Meinungen abfragt: ein echtes Angebot, eine Vorbestellung, eine Zusage, eine Probe-Lieferung, ein MVP, das in Stunden bis Tagen steht (z. B. eine Messenger-Gruppe, eine einfache Webseite, die Dienstleistung zunächst von Hand). Eine Umfrage zur Zahlungsbereitschaft ist kein Test für Zahlungsbereitschaft.
- **Mit wem:** wer, wie viele; mindestens zwei Personen oder Organisationen.
- **Bis wann:** ein Datum.
- **Messgröße:** was gezählt oder beobachtet wird.
- **Voraussetzung:** welcher Test vorher bestanden sein muss (z. B. die Freigabe vor der Probe-Lieferung), oder „keine“.
- **Schwelle:** ab wann die Annahme als belegt gilt. Schlag eine Schwelle mit Begründung vor; festlegen tut sie das Team, **bevor** getestet wird. Übernimmt eine Schwelle eine Zahl, die noch als offene Frage oder vorläufig im Canvas steht, frag ausdrücklich, ob das ganze Team sie beschlossen hat, und halte in `DECISIONS.md` fest, wer das bestätigt hat; sonst bleibt die Karte offen, bis es so weit ist.
- **Status:** geplant. **Ausgewertet:** nein.

Dann prüfst du den Plan als Ganzes und listest als Probleme:

- kritische Annahmen ohne Testkarte;
- Tests, die eine Annahme nur mit einer Meinung prüfen, wo Verhalten möglich wäre;
- Schwellen, die so niedrig sind, dass jedes Ergebnis sie erfüllt;
- Tests, die auf einer anderen, ungetesteten kritischen Annahme aufbauen (Reihenfolge);
- Tests, die ein Angebot mit Preis oder Betrag brauchen, obwohl Preis oder Kosten noch als offene Frage im Canvas stehen (dann zuerst die Zahl klären, oder eine Zusage ohne Preis testen und sagen, was sie nicht zeigt);
- Schwellen, die etwas anderes messen als die Annahme sagt (z. B. „Stiftung hält uns für förderfähig“ statt „Stiftung zahlt“);
- ein Plan, der für das Team in der verfügbaren Zeit nicht machbar ist (frag nach der Zeit, schätze nicht).

## 2. Stop-Point

Zeig die Probleme zuerst, jeweils mit einer Empfehlung, dann die Karten. Das Team entscheidet, welche Tests es macht, in welcher Reihenfolge und mit welcher Schwelle. Halte die Entscheidungen in `DECISIONS.md` fest und trag die Test-IDs in der Spalte *Test* des Registers ein. Die Reihenfolge steht in den *Voraussetzungen* der Karten. Block 9 des Canvas bekommt die Liste der Tests mit Annahme und Schwelle; Block 4 wird ergänzt, wenn neue Erfolgskriterien entstanden sind.

Fertig, wenn jede offene kritische Annahme eine vom Team bestätigte Testkarte mit Schwelle hat und `check_project.py` bei *kritische* und *eine-annahme* OK meldet. Bitte das Team, die Karten **jetzt** zu committen (falls Git): So bleibt sichtbar, dass die Schwellen vor den Ergebnissen feststanden. Sag dem Team dann, dass jetzt es dran ist: testen, Ergebnisse in `TESTS.md` notieren oder in den Chat einfügen, dann `/log-evidence`.
