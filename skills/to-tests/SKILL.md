---
name: to-tests
description: Macht aus euren kritischen Annahmen einen Testplan – eine Testkarte pro Annahme mit Test, Messgröße, Schwelle, mit wem und bis wann – und schlägt einfache MVPs vor.
disable-model-invocation: true
---

# Zum Testplan

Schreib die Testkarten, mit denen das Team seine kritischen Annahmen prüft, so schnell und billig wie möglich. Lies `ASSUMPTIONS.md`, `CANVAS.md` (Block 4 und 6), `MODEL.md`, `TESTS.md` und `DECISIONS.md`. Lade `assumptions` und `evidence-checks`. Ist keine Annahme als kritisch markiert, halte an und schlage `/grill-solution` vor.

## 1. Entwurf

Für jede kritische Annahme mit Status *Annahme* (und jede, die das Team zusätzlich nennt) entwirfst du eine Testkarte in `TESTS.md` nach dem Format der Vorlage:

- **Test:** Was das Team macht, damit sich die Annahme zeigt oder nicht. Bevorzuge, was Verhalten zeigt, vor dem, was Meinungen abfragt: ein echtes Angebot, eine Vorbestellung, eine Zusage, eine Probe-Lieferung, ein MVP, das in Stunden bis Tagen steht (z. B. eine Messenger-Gruppe, eine einfache Webseite, die Dienstleistung zunächst von Hand). Eine Umfrage zur Zahlungsbereitschaft ist kein Test für Zahlungsbereitschaft.
- **Mit wem:** wer, wie viele; mindestens zwei Personen oder Organisationen.
- **Bis wann:** ein Datum.
- **Messgröße:** was gezählt oder beobachtet wird.
- **Schwelle:** ab wann die Annahme als belegt gilt. Schlag eine Schwelle mit Begründung vor; festlegen tut sie das Team, **bevor** getestet wird.
- **Status:** geplant.

Dann prüfst du den Plan als Ganzes und listest als Probleme:

- kritische Annahmen ohne Testkarte;
- Tests, die eine Annahme nur mit einer Meinung prüfen, wo Verhalten möglich wäre;
- Schwellen, die so niedrig sind, dass jedes Ergebnis sie erfüllt;
- Tests, die auf einer anderen, ungetesteten kritischen Annahme aufbauen (Reihenfolge);
- ein Plan, der für das Team in der verfügbaren Zeit nicht machbar ist (frag nach der Zeit, schätze nicht).

## 2. Stop-Point

Zeig die Probleme zuerst, jeweils mit einer Empfehlung, dann die Karten. Das Team entscheidet, welche Tests es macht, in welcher Reihenfolge und mit welcher Schwelle. Halte die Entscheidungen in `DECISIONS.md` fest und trag die Test-IDs in der Spalte *Test* des Registers ein. Block 9 des Canvas bekommt die Liste der Tests mit Annahme und Schwelle; Block 4 wird ergänzt, wenn neue Erfolgskriterien entstanden sind.

Fertig, wenn jede offene kritische Annahme eine vom Team bestätigte Testkarte mit Schwelle hat und `check_project.py` bei *kritische* OK meldet. Sag dem Team, dass jetzt es dran ist: testen, Ergebnisse in `TESTS.md` notieren, dann `/log-evidence`.
