# Signale

Alles, was zeigt, wie die Arbeit läuft: Prüfungen, bevor etwas zählt, und was danach passiert ist (Interviews, Tests, Feedback). Die neuesten oben. Der Retro-Skill macht aus Signalen Korrekturen, Checks und Regeln.

<!--
## JJJJ-MM-TT · <Bereich> · <Quelle: Interview | Test | Feedback | Check | Sonstiges>

- **Was passiert ist:** Fakten, wo möglich mit Zahlen
- **Wer:** Rolle oder Persona (keine Namen)
- **Schwere:** blockiert | bremst | Hinweis
- **Status:** offen | behoben in <Datei> | als Check <Name> aufgenommen
-->

## 2026-12-21 · Aktivitäten · Test

- **Was passiert ist:** In der Probewoche lieferte das Team an 3 von 5 Tagen selbst zur Tafel-Ausgabestelle (A46). Die Lösung setzte darauf, dass die Einrichtungen selbst abholen (A37), obwohl I1 Abholen als Problem nannte (A17). Die Zeit des Teams (A40) war auf Wunsch des Teams nicht kritisch und wurde nicht gemessen. Ursache: Ein Vorschlag des Agenten wurde abgelehnt, weil das Team die eigene Zeit für bekannt hielt. Warum kein Check: Es gibt keinen Check, der verlangt, die Arbeit des Teams selbst mitzuzählen.
- **Wer:** Team
- **Schwere:** bremst
- **Status:** als Check *Team-Zeit mitzählen* aufgenommen (Block 8)

## 2026-12-21 · Zahlungsbereitschaft · Test

- **Was passiert ist:** Das Studierendenwerk findet die Idee gut, zahlt aber nichts (T4, A5 widerlegt). A5 stammt aus dem Notion-Export und war bis zum Test ungeprüft. Warum kein Check: Der Test hat es gefunden – so soll es sein.
- **Wer:** Abteilungsleitung Hochschulgastronomie
- **Schwere:** blockiert
- **Status:** keine Änderung nötig; Weg in `DECISIONS.md` (2026-12-20)

## 2026-12-21 · Tests · Feedback

- **Was passiert ist:** Bei der Auswertung wollte das Team die Schwelle von T1 nachträglich auf „2 von 4“ senken („fühlte sich wie ein Erfolg an“). Nach Erklärung blieb es bei der vorher festgelegten Schwelle. Warum kein Check nötig: Regel „nie einen Check lockern“ und der Commit der Karten vor dem Test haben gegriffen.
- **Wer:** Team
- **Schwere:** Hinweis
- **Status:** keine Änderung (Regel hat gegriffen)

## 2026-12-21 · Tests · Test

- **Was passiert ist:** Das Jugendzentrum war in T1, obwohl es laut I4 nicht passt (A27) und das Team es zwei Tage vorher aus den Nutzer:innen genommen hatte. Es sagte ab („passt nicht zu uns“); dadurch brauchte T1 alle drei anderen Zusagen. Ursache: Der Agent hatte es bei `/to-tests` gemeldet; das Team entschied anders. Warum kein Check: Der Review-Check „Schwelle misst, was die Annahme sagt“ hat gegriffen, die Entscheidung lag beim Team.
- **Wer:** Team
- **Schwere:** bremst
- **Status:** bewusst kein Check (Entscheidung des Teams, `DECISIONS.md` 2026-12-21)

## 2026-12-21 · Tests · Test

- **Was passiert ist:** Für die Tagesstätte ist in T2 nicht notiert, an wie vielen Tagen sie selbst abholte. Ursache: Während der Probewoche gab es keine Liste für die Messgröße. Warum kein Check: Die Lücke fällt erst beim Auswerten auf.
- **Wer:** Team
- **Schwere:** Hinweis
- **Status:** als Check *Strichliste je Messgröße* aufgenommen (Block 8)

## 2026-12-21 · Tests · Sonstiges

- **Was passiert ist:** T6 wurde nicht durchgeführt. Die Testkarte hat dafür keinen Status; sie blieb *geplant* mit neuem Datum, der Grund steht nirgends. Warum kein Check: `check_project.py` meldet eine solche Karte erst, wenn sie überfällig ist.
- **Wer:** Team, Skill `/log-evidence`
- **Schwere:** Hinweis
- **Status:** Skill-Vorschlag 2 in `SKILL-PROPOSALS.md`

## 2026-12-21 · Checks · Check

- **Was passiert ist:** `check_project.py` meldet bei *reihenfolge* T4 (vor T3), obwohl im Feld *Voraussetzung* „keine (gleiches Gespräch wie T3)“ steht, und nennt T1 doppelt. Ursache: Das Skript liest jede T-Nummer im Feld als Voraussetzung.
- **Wer:** Skill `evidence-checks`
- **Schwere:** Hinweis
- **Status:** Skill-Vorschlag 1 in `SKILL-PROPOSALS.md`

## 2026-12-21 · Wirkung · Sonstiges

- **Was passiert ist:** Die Probewoche zählte, ob Einrichtungen Essen annahmen, nicht, ob die Gäste abends etwas Warmes gegessen haben. Ob das Erfolgskriterium aus Block 4 erfüllt war, lässt sich nicht sagen. Warum kein Check: Kein Check fragt bei einem Test nach der Wirkung bei den Betroffenen.
- **Wer:** Team
- **Schwere:** bremst
- **Status:** als Check *Wirkung mitzählen* aufgenommen (Block 8)

## 2026-12-21 · Tests · Feedback

- **Was passiert ist:** Sechs Testkarten auf einmal waren für das Team „viel“, bei etwa 4 Stunden pro Person und Woche.
- **Wer:** Team
- **Schwere:** Hinweis
- **Status:** bewusst kein Check („Das war ok, nur viel.“, Lena)

## 2026-12-20 · Modell · Review

- **Was passiert ist:** `/review-model` nach Runde 1: 6 Befunde, davon 4 blockierend (MODEL.md baut auf drei widerlegten kritischen Annahmen; niemand zahlt belegt; Freigabe offen; Fahren ungeklärt) und 5 Hinweise (Reihenfolge der Tests, Messlücke T2, T6 nicht gemacht, Wirkung bei Gästen nicht gemessen, Fehlalarm *reihenfolge* bei T4). Weg: neu ansetzen bei „Wer zahlt?“. A40 vom Team nachträglich als kritisch markiert.
- **Wer:** Team
- **Schwere:** blockiert
- **Status:** behoben: Weg entschieden (`DECISIONS.md` 2026-12-20)

## 2026-12-19 · Tests · Test

- **Was passiert ist:** Testergebnisse zu T1–T5 ausgewertet (T6 nicht durchgeführt, neues Datum 2027-01-15). 3 kritische Annahmen widerlegt (A36, A37, A5), 3 neue *belegte* Zeilen (A45–A47), 1 neue Annahme (A48), Quellen von A27, A35, A39, A40 ergänzt; T3 und T5 laufen weiter (Bedingung offen). Die Schwellen standen vor den Ergebnissen fest (Commit vom 2026-11-28). Das Team schlug vor, T1 nachträglich mit „2 von 4“ als belegt zu zählen; nach Erklärung blieb es bei der Schwelle. Überraschungen: Das Studierendenwerk findet die Idee gut, zahlt aber nichts; die Tafel konnte nur an 2 von 5 Tagen abholen, das Team lieferte an 3 Tagen. Messlücke: Abholtage der Tagesstätte (T2) nicht notiert.
- **Wer:** Leitung Tafel-Ausgabestelle, Sozialarbeiter Tagesstätte, Mitarbeiterin Jugendzentrum, eine weitere Einrichtung (ohne Antwort), Abteilungsleitung Hochschulgastronomie, zwei Stiftungen
- **Schwere:** bremst
- **Status:** erklärt in den Signalen vom 2026-12-21

## 2026-10-23 · Problem · Interview

- **Was passiert ist:** Vier Interviews (I1–I4) ausgewertet: 12 neue *belegte* Zeilen (A16–A27, je zu einer Einrichtung bzw. der Mensa), 3 neue Annahmen (A28–A30), A1 ersetzt durch A23 und A24. Kein Status einer bestehenden Annahme auf *belegt* oder *widerlegt*. Ein vorgeschlagener Eintrag (Jugendliche wollen eher Snacks, I4) vom Team abgelehnt. Überraschungen: In der Mensa bleiben nur 5–20 Portionen übrig, und sie gehen in die Biogasanlage, nicht in den Müll; die Tafel nennt Fahrer:innen wichtiger als Essen; die Ursache „kein Personal“ [A7] wurde in keinem Interview beantwortet.
- **Wer:** Leitung Tafel-Ausgabestelle, Sozialarbeiter Tagesstätte, Küchenleiter Mensa, Mitarbeiterin Jugendzentrum
- **Schwere:** Hinweis
- **Status:** behoben in `ASSUMPTIONS.md` (A16–A30)

## 2026-10-23 · Interviews · Interview

- **Was passiert ist:** In I2 wurde die Idee vorgestellt und gefragt, ob er sie nutzen würde – gegen den Leitfaden („Nicht fragen“). Frage A-3 (warum es abends so ist) steht in keiner Notiz.
- **Wer:** Team (Interview I2), Leitfaden Teil A
- **Schwere:** bremst
- **Status:** als Check *Interviews fragen nach Erlebtem* erfasst (`evidence-checks`, beim Auswerten); die Ursache „kein Personal“ bleibt unter *Noch offen* in `PROBLEM.md`
