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

Reihenfolge: T1 zuerst (Gespräch mit dem Studierendenwerk), dann die Probewoche mit T2 und T3; T4 im selben Gespräch wie T1; T5 parallel.

### T1: Freigabe durch das Studierendenwerk

- **Annahme:** A37
- **Voraussetzung:** keine
- **Test:** Gespräch mit der Abteilungsleitung Hochschulgastronomie des Studierendenwerks (mit dem Küchenleiter aus I3): Wir bitten um die Freigabe, übrig gebliebenes Essen abzuholen, zuerst für eine Probewoche, und fragen, wie die Haftung geregelt wird.
- **Mit wem:** Abteilungsleitung Hochschulgastronomie und Küchenleiter (2 Personen)
- **Bis wann:** 2026-11-06
- **Messgröße:** Freigabe ja/nein; Haftung geregelt ja/nein
- **Schwelle:** Das Studierendenwerk sagt die Freigabe zu, ohne offene Bedingung (die Haftung ist geregelt).
- **Ergebnis:**
- **Status:** geplant
- **Ausgewertet:** nein

### T2: Einrichtungen nehmen das Essen an (Probewoche)

- **Annahme:** A35
- **Voraussetzung:** T1
- **Test:** Probewoche: Wir bieten vier Einrichtungen an, eine Woche lang (fünf Werktage) abends übrig gebliebenes Mensa-Essen zu bekommen, und zählen, wer es annimmt.
- **Mit wem:** 4 Einrichtungen (Tafel-Ausgabestelle aus I1, Tagesstätte aus I2, Jugendzentrum aus I4, eine weitere Einrichtung mit Abendgästen)
- **Bis wann:** 2026-11-13
- **Messgröße:** Anzahl der Einrichtungen, die an mindestens 3 von 5 Tagen Essen annehmen
- **Schwelle:** Mindestens 3 von 4 Einrichtungen nehmen an mindestens 3 von 5 Tagen Essen an (vom ganzen Team beschlossen, siehe `DECISIONS.md`).
- **Ergebnis:**
- **Status:** geplant
- **Ausgewertet:** nein

### T3: Einrichtungen holen selbst ab (Probewoche)

- **Annahme:** A36
- **Voraussetzung:** T1
- **Test:** In derselben Probewoche wie T2: Wir bitten jede Einrichtung, die Essen annimmt, es selbst in der Mensa abzuholen, und schreiben pro Tag auf, wer abgeholt hat (Einrichtung oder Team).
- **Mit wem:** alle Einrichtungen, die in T2 Essen annehmen (mindestens 2)
- **Bis wann:** 2026-11-13
- **Messgröße:** pro Einrichtung: an wie vielen von 5 Tagen sie selbst abgeholt hat
- **Schwelle:** Jede Einrichtung, die Essen annimmt, holt an mindestens 4 von 5 Tagen selbst ab.
- **Ergebnis:**
- **Status:** geplant
- **Ausgewertet:** nein

### T4: Studierendenwerk zahlt

- **Annahme:** A5
- **Voraussetzung:** keine
- **Test:** Im Gespräch aus T1 fragen wir konkret, ob das Studierendenwerk einen Teil der Kosten übernimmt (Pauschale, Material oder Fahrtkosten), und notieren die Antwort wörtlich. (Ein schriftliches Angebot mit Preis hat das Team abgelehnt, siehe `DECISIONS.md`.)
- **Mit wem:** Abteilungsleitung Hochschulgastronomie und Küchenleiter (2 Personen)
- **Bis wann:** 2026-11-06
- **Messgröße:** Zusage einer Geldleistung ja/nein, mit Art und Größenordnung
- **Schwelle:** Das Studierendenwerk sagt eine konkrete Geldleistung zu (Pauschale oder Übernahme von Kosten) und nennt Art und Größenordnung.
- **Ergebnis:**
- **Status:** geplant
- **Ausgewertet:** nein

### T5: Eine Stiftung fördert das Projekt

- **Annahme:** A42
- **Voraussetzung:** keine
- **Test:** Schriftliche Anfrage mit einer halben Seite Projektbeschreibung an zwei Stiftungen, die Projekte in Kiel bzw. Schleswig-Holstein fördern.
- **Mit wem:** 2 Stiftungen
- **Bis wann:** 2026-11-13
- **Messgröße:** Antworten; ob die Stiftung bestätigt, dass ein Projekt wie unseres gefördert werden kann, mit Betrag und Frist
- **Schwelle:** Mindestens eine von zwei Stiftungen bestätigt schriftlich, dass sie ein Projekt wie unseres fördern kann, und nennt einen Betrag und eine Frist.
- **Ergebnis:**
- **Status:** geplant
- **Ausgewertet:** nein
