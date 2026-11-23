# Tests

Für jede kritische Annahme eine Testkarte. Messgröße und Schwelle legt ihr fest, **bevor** ihr testet. Mindestens zwei Personen oder Organisationen.

Pro Karte eine Annahme und eine Schwelle. Format einer Karte (Vorlage, ersetzt `T?` durch die nächste Nummer):

<!--
Karte T?: <kurzer Titel>   ← als Überschrift: ### T1: <Titel>

- **Annahme:** A3
- **Voraussetzung:** welcher Test vorher bestanden sein muss (z. B. T1), oder „keine“
- **Test:** was ihr macht (MVP, Angebot gegen Geld, Interview, Probe-Lieferung …)
- **Mit wem:** wer, wie viele
- **Bis wann:** JJJJ-MM-TT
- **Messgröße:** was ihr zählt oder beobachtet
- **Schwelle:** ab wann die Annahme als belegt gilt (z. B. „mindestens 3 von 5 Einrichtungen sagen verbindlich zu“)
- **Ergebnis:** (nach dem Test) was herauskam, gemessen an der Schwelle
- **Status:** geplant | läuft | abgeschlossen
- **Ausgewertet:** nein
-->

Bevor ihr testet: Karten committen (falls Git), damit sichtbar bleibt, dass die Schwelle vorher feststand.

Testplan vom 2026-11-28 (`/to-tests`). Reihenfolge und Auswahl hat das Team entschieden (siehe `DECISIONS.md`, 2026-11-28).

### T1: Probewoche – nehmen Einrichtungen das Essen an?

- **Annahme:** A36
- **Voraussetzung:** keine (Entscheidung des Teams: parallel zu T3 und T6; vorgeschlagen war, T3 und T6 vorher abzuschließen)
- **Test:** Probe-Lieferung: Eine Woche lang (Mo–Fr) übrig gebliebenes Mensa-Essen für den Abend anbieten; jeden Tag notieren, ob die Einrichtung es annimmt.
- **Mit wem:** vier Einrichtungen: Tafel-Ausgabestelle (I1), Tagesstätte (I2), Jugendzentrum (I4), eine weitere Einrichtung mit Abendgästen (sucht Jule)
- **Bis wann:** 2026-12-18
- **Messgröße:** Zahl der Einrichtungen, die zusagen und an mindestens 3 von 5 Tagen Essen annehmen
- **Schwelle:** mindestens 3 von 4 Einrichtungen sagen zu und nehmen an mindestens 3 von 5 Tagen Essen an
- **Ergebnis:**
- **Status:** geplant
- **Ausgewertet:** nein

### T2: Holen die Einrichtungen selbst ab?

- **Annahme:** A37
- **Voraussetzung:** keine (läuft in derselben Probewoche wie T1)
- **Test:** In der Probewoche aus T1 holen die Einrichtungen das Essen selbst in der Mensa ab; das Team fährt nur, wenn keiner kann.
- **Mit wem:** die Einrichtungen, die in T1 zusagen (mindestens zwei)
- **Bis wann:** 2026-12-18
- **Messgröße:** pro Einrichtung: an wie vielen von 5 Tagen sie selbst abgeholt hat; an wie vielen Tagen das Team geliefert hat
- **Schwelle:** mindestens 2 Einrichtungen holen an mindestens 4 von 5 Tagen selbst ab
- **Ergebnis:**
- **Status:** geplant
- **Ausgewertet:** nein

### T3: Gibt das Studierendenwerk die Abholung frei?

- **Annahme:** A35
- **Voraussetzung:** keine
- **Test:** Gespräch mit dem Studierendenwerk mit der Bitte um Freigabe der Abholung und eine Haftungsregel (Zugang über den Küchenleiter aus I3).
- **Mit wem:** Abteilungsleitung Hochschulgastronomie des Studierendenwerks und der Küchenleiter aus I3 (zwei Personen)
- **Bis wann:** 2026-12-18
- **Messgröße:** schriftliche Freigabe mit Haftungsregel: ja oder nein
- **Schwelle:** das Studierendenwerk gibt die Abholung schriftlich frei und nennt eine Haftungsregel
- **Ergebnis:**
- **Status:** geplant
- **Ausgewertet:** nein

### T4: Zahlt das Studierendenwerk?

- **Annahme:** A5
- **Voraussetzung:** keine (gleiches Gespräch wie T3)
- **Test:** Im Gespräch aus T3 fragen, ob das Studierendenwerk für den Service Geld bezahlt – ohne Betrag, weil die Kosten noch offen sind (Entscheidung des Teams). Eine Zusage zeigt nicht, ob der Betrag die Kosten deckt.
- **Mit wem:** Abteilungsleitung Hochschulgastronomie des Studierendenwerks und der Küchenleiter aus I3 (zwei Personen)
- **Bis wann:** 2026-12-18
- **Messgröße:** Zusage, Geld für den Service zu zahlen: ja oder nein
- **Schwelle:** das Studierendenwerk sagt zu, Geld für den Service zu zahlen (Betrag offen)
- **Ergebnis:**
- **Status:** geplant
- **Ausgewertet:** nein

### T5: Fördert eine Stiftung das Projekt?

- **Annahme:** A39
- **Voraussetzung:** keine
- **Test:** Anfrage per Mail mit kurzer Projektbeschreibung an zwei Stiftungen.
- **Mit wem:** zwei Stiftungen (sucht Lena)
- **Bis wann:** 2026-12-18
- **Messgröße:** schriftliche Förderzusage mit Betrag: ja oder nein
- **Schwelle:** mindestens 1 von 2 Stiftungen sagt eine Förderung zu (nicht nur „förderfähig“)
- **Ergebnis:**
- **Status:** geplant
- **Ausgewertet:** nein

### T6: Können die Einrichtungen kühlen und aufwärmen?

- **Annahme:** A38
- **Voraussetzung:** keine
- **Test:** Besuch vor Ort: Die Einrichtungen zeigen, wo sie das Essen bis zum Abend kühlen und wie sie es aufwärmen.
- **Mit wem:** Tafel-Ausgabestelle (I1) und Tagesstätte (I2)
- **Bis wann:** 2026-12-18
- **Messgröße:** Zahl der Einrichtungen mit Kühlplatz und Aufwärmmöglichkeit für die Menge, die sie nehmen wollen
- **Schwelle:** mindestens 2 Einrichtungen zeigen Kühlplatz und Aufwärmmöglichkeit
- **Ergebnis:**
- **Status:** geplant
- **Ausgewertet:** nein
