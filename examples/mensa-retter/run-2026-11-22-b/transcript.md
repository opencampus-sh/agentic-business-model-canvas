# Dry-Run 2 · Agentic Business Model Canvas · Mensa-Retter

Datum der Simulation: 2026-11-22. Runner = Agent in `dryrun2/mensa-retter` (liest nur `.claude/skills/…` und Projektdateien). Persona = Lena (`persona-lena.md`, Eingaben aus `eingaben/`). `[Runner-Notiz]` = Beobachtung für den Bericht, nicht Teil des Gesprächs.

---

## 1. /setup-model

**Lena:** /setup-model

**Agent:** *(liest `.claude/skills/setup-model/SKILL.md`, Templates; führt aus: `ls -A`, `git remote -v`)*

Hallo! Ich habe mir den Ordner angeschaut:

- Der Ordner ist bis auf die installierten Skills (`.claude/`) leer. Es ist ein Git-Repository mit einem ersten Commit, aber **ohne Remote** – ich kann also nicht prüfen, ob es irgendwo öffentlich liegt.
- Es gibt noch kein `AGENTS.md`, kein `CANVAS.md` und keine anderen Projektdateien.
- Bisherige Ergebnisse (Notion, Dokumente, Notizen) finde ich hier keine.

Ein paar Fragen, nacheinander:

**A. Ort.** Ist dieser Ordner der richtige für euer Projekt? Ich empfehle einen eigenen, leeren Projektordner – das ist er. Da es kein Remote gibt: Soll das Repository später irgendwo hochgeladen werden (z. B. GitHub), und wenn ja, privat oder öffentlich? Ich empfehle **privat**: Interview-Notizen und Ideen gehören nicht ins Netz.

**Lena:** Ja, der Ordner passt, den hat Jule angelegt. Hochgeladen ist noch nichts. Wenn, dann privat, das hat Jule auch so gesagt.

**Agent:** Super, dann bleibt es privat. **B. Team und Idee.** Wie heißt euer Team (oder eure Namen), und was ist eure Idee in einem Satz?

**Lena:** Wir sind die „Mensa-Retter“, also Ahmet, Jule und ich. Idee: Übrig gebliebenes Mensa-Essen abends an soziale Einrichtungen bringen.

**Agent:** Danke! **C. Bisherige Ergebnisse.** Liegen schon Ergebnisse vor, z. B. aus Notion, einem Dokument oder Notizen? Wenn ja: Wo stehen sie, und welche Kapitel des Handbuchs habt ihr schon bearbeitet?

**Lena:** Ja, wir haben eine Notion-Seite. Ich kopier sie als `notion-export.md` in den Ordner. Kapitel … das zum Problem, glaube ich, mehr nicht.

**Agent:** *(liest `notion-export.md`)* Danke, gelesen. Darin stehen ein Problem-Absatz und drei Problem-Hypothesen. Ich würde daraus diese Zeilen ins Annahmen-Register übernehmen – alle mit Status *Annahme*, Kategorie als Vorschlag, *Kritisch* und *Test* bleiben leer (das entscheidet ihr später):

| ID | Aussage | Kategorie (Vorschlag) | Quelle |
|---|---|---|---|
| A1 | In Kieler Mensen wird jeden Tag (viel, gutes) Essen weggeworfen. | Problem | Notion, Seite Problem + Seite Problem-Hypothesen |
| A2 | Menschen in sozialen Einrichtungen bekommen abends nichts Warmes zu essen. | Problem | Notion, Seite Problem |
| A3 | Es fehlt eine App, die Mensen und soziale Einrichtungen verbindet. | Lösung | Notion, Seite Problem |
| A4 | Soziale Einrichtungen würden das übrig gebliebene Mensa-Essen gern nehmen. | Zielgruppe | Notion, Seite Problem-Hypothesen |
| A5 | Das Studierendenwerk würde für so einen Service bezahlen. | Zahlungsbereitschaft | Notion, Seite Problem-Hypothesen |

„In Mensen wird jeden Tag gutes Essen weggeworfen“ (Seite Problem) und „Mensen werfen jeden Tag viel Essen weg“ (Hypothesen) sind fast gleich – daraus wird **eine** Zeile (A1) mit beiden Quellen. Nichts davon ist *belegt*; das entscheidet ihr erst mit `/log-evidence`, wenn ihr Interviews oder Tests habt. Passt das so?

**Lena:** Ok, passt.

**Agent:** *(schreibt: Templates kopiert, Canvas-Kopf, Register A1–A5, Block 6 mit IDs, `.gitignore` mit `build/`, `CLAUDE.md` mit `@AGENTS.md`, `AGENTS.md` mit dem Abschnitt)*

Ich habe angelegt: `CANVAS.md`, `ASSUMPTIONS.md`, `PROBLEM.md`, `INTERVIEWS.md`, `SOLUTIONS.md`, `MODEL.md`, `TESTS.md`, `DECISIONS.md`, `SIGNALS.md`, dazu `.gitignore` (Zeile `build/`) und `CLAUDE.md` mit der einen Zeile `@AGENTS.md`, damit Claude Code die Regeln in jeder Sitzung liest. Im Canvas stehen Team, Idee und Version (2026-11-22); in Block 6 die übernommenen IDs [A1]–[A5].

In `AGENTS.md` steht jetzt ein Abschnitt „Agentic Business Model Canvas“: Hier steht, wo eure Dateien liegen und welche Regeln ich in jeder Sitzung befolge – z. B. dass jede Aussage im Register steht, ich nichts erfinde, wo der Check liegt, dass wir Deutsch sprechen und eure Notion-Seite die Quelle der bisherigen Ergebnisse ist. Stimmt das inhaltlich so für euch?

**Lena:** Ja, passt.

**Agent:** *(führt `check_project.py` aus: verweise OK, status OK, kritische OFFEN, interviews OFFEN 0/3)* Alles angelegt, der Check meldet keine Fehler. Soll ich das jetzt committen? Danach geht es weiter mit `/grill-problem`.

**Lena:** Ja, mach.

**Agent:** *(git commit „Projekt angelegt (/setup-model)“ → 75a9c9a)*

`[Runner-Notiz]` Das Commit umfasst die Projektdateien, nicht `.claude/` – der Skill sagt nicht, ob installierte Skills mit ins Repo gehören. Beim Zusammenführen von A1 sagt der Skill nicht, welcher Wortlaut gilt; der Agent hat beide zu einer Formulierung kombiniert („viel, gutes“), was schon eine leichte Umformulierung ist.

---

## 2. /grill-problem

**Lena:** /grill-problem

**Agent:** *(liest `.claude/skills/grill-problem/SKILL.md`, lädt `assumptions`; liest `CANVAS.md`, `PROBLEM.md`, `ASSUMPTIONS.md`, `DECISIONS.md`)*

Jetzt schärfen wir euer Problem – noch ganz ohne Lösung. Ich frage in Runden; es werden **ungefähr vier Runden**, dazu eine kurze Warum-Kette (5 Whys), bei der ich eine Frage pro Nachricht stelle. „Weiß ich nicht“ ist jederzeit eine gültige Antwort.

**Runde 1 von ca. 4**

❓ **F1** – **Kernproblem in euren Worten**: Was passiert den betroffenen Menschen? Beschreibt die negative Situation aus ihrer Sicht, in ein bis drei Sätzen. (In Notion steht „Es fehlt eine App, die das verbindet“ – das ist eine fehlende Lösung; mich interessiert, was den Menschen passiert, solange es sie nicht gibt.)

➡️ Erst eure Worte – ich mache nur einen Vorschlag, wenn ihr keine findet.

❓ **F2** – **Woher wisst ihr von A1?** In Notion steht „Mensen werfen jeden Tag viel Essen weg“ [A1]. Habt ihr das gesehen, gelesen, gehört – oder vermutet ihr es?

➡️ Sag einfach, woher es kommt; dann trage ich die Quelle ein. Ohne Quelle bleibt es eine Annahme, das ist völlig ok.

**Lena:** F1: Menschen in Kiel, die wenig Geld haben, kriegen abends oft nichts Warmes zu essen, obwohl in der Mensa jeden Tag Essen übrig bleibt.
F2: Ich hab selbst gesehen, dass nach 14 Uhr Essen in große Tonnen kommt. Wie viel genau, weiß ich nicht.

**Agent:** Danke, das ist eine gute Beschreibung aus Sicht der Betroffenen. Ich trenne sie in zwei Aussagen: das Kernproblem („Menschen mit wenig Geld bekommen abends oft keine warme Mahlzeit“ → neu [A6]) und den Gegensatz „in der Mensa bleibt Essen übrig“ (das ist [A1]). Deine Beobachtung trage ich als eigene Zeile ein [A7] – Status *Annahme*, Quelle „eigene Beobachtung, eine Mensa“: Eine Beobachtung an einem Ort ist noch kein Beleg für alle Mensen. Wie viel übrig bleibt, kommt unter *Noch offen*.

Jetzt die Warum-Kette, eine Frage nach der anderen.

**Warum 1:** Warum bekommen Menschen mit wenig Geld abends nichts Warmes?

**Lena:** Die Einrichtungen haben abends kein Personal zum Kochen.

**Agent:** Notiert [A8]. **Warum 2:** Warum haben die Einrichtungen abends kein Personal zum Kochen?

**Lena:** Weiß ich nicht.

**Agent:** Völlig ok – dann endet die Kette hier. Ich schreibe „Warum haben Einrichtungen abends kein Personal? – wissen wir noch nicht“ unter *Noch offen* in `PROBLEM.md`; das prüft ihr in den Interviews. Erkenntnis bisher: Ansetzen könnt ihr dort, wo abends Personal fehlt [A8].

Soll ich Fakten zu Problem und Ursachen recherchieren (z. B. Zahlen zu Lebensmittelabfällen in Mensen)? Was ich finde, käme mit Link als *recherchiert* ins Register.

**Lena:** Nee, erstmal nicht, wir wollen vorankommen.

**Agent:** Gut. **Runde 2 von ca. 4 (danach noch zwei)**

❓ **F1** – **Direkte Folgen**: Was passiert den Menschen direkt, wenn sie abends nichts Warmes bekommen?

➡️ Denkt an den Abend und die Nacht selbst.

❓ **F2** – **Langfristige und gesellschaftliche Folgen**: Was passiert, wenn sich nichts ändert – in einem Jahr, für die Stadt?

➡️ Wenn ihr es nicht wisst, ist „weiß ich nicht“ ok.

❓ **F3** – **Weitere Folgen**: Gibt es ökologische, politische, ökonomische oder kulturelle Folgen?

➡️ Ökologisch liegt bei weggeworfenem Essen nahe – aber nur, wenn ihr das so seht.

**Lena:** F1: Die Leute gehen hungrig schlafen. F2: Weiß ich nicht so genau, vielleicht werden die krank. F3: Ja, das Essen landet im Müll, das ist Verschwendung. Mehr weiß ich nicht.

**Agent:** Notiert: [A9] hungrig schlafen, [A10] eher krank (als unsicher markiert), [A11] Lebensmittelverschwendung. Politische, ökonomische, kulturelle Folgen kommen unter *Noch offen*.

**Runde 3 von ca. 4 (danach noch eine)**

Hier ist euer Problembaum:

```
Folgen
├── Menschen gehen hungrig schlafen [A9]
│   └── werden eher krank [A10]
└── Lebensmittelverschwendung [A11]
Kernproblem: Menschen mit wenig Geld bekommen abends keine warme Mahlzeit [A6]
Ursachen
├── Einrichtungen haben abends kein Personal zum Kochen [A8]
│   └── warum? – noch offen
└── (gleichzeitig) in Mensen bleibt täglich Essen übrig [A1], [A7]
```

❓ **F1** – **Problembaum**: Stimmt der Baum so?

➡️ Bestätigen, wenn er euch richtig wiedergibt.

❓ **F2** – **Zielgruppe**: Wer genau ist direkt betroffen? Gibt es Untergruppen? (Nicht „alle mit wenig Geld“, sondern so konkret wie möglich.)

➡️ Eure Worte zuerst.

❓ **F3** – **Realitätscheck**: Was davon nehmt ihr an, was wisst ihr wirklich – und woher?

➡️ Ehrlich sein lohnt sich: Was ihr noch nicht wisst, prüft ihr in Interviews.

**Lena:** F1: Ok, passt. F2: Wohnungslose, ältere Leute und Leute mit wenig Geld, die zu solchen Einrichtungen gehen. F3: Das vermuten wir alles, wir haben noch mit niemandem gesprochen.

**Agent:** Danke – [A12], Status *Annahme*, mit genau diesem Hinweis als Quelle.

**Runde 4 von ca. 4 (die letzte)**

❓ **F1** – **Problem-Hypothesen**: Diese Aussagen würde ich als Problem-Hypothesen für eure Interviews vorschlagen: [A1] Mensen werfen viel Essen weg · [A2] Menschen in Einrichtungen bekommen abends nichts Warmes · [A4] Einrichtungen würden das Essen nehmen · [A6] Menschen mit wenig Geld bekommen abends keine warme Mahlzeit · [A8] Einrichtungen haben abends kein Personal. Fehlt etwas, soll etwas raus?

➡️ So lassen: Sie decken Kernproblem, Ursache und Zielgruppe ab.

❓ **F2** – **Offene Fragen**: Wer klärt „Warum fehlt abends Personal?“ und „Wie viel bleibt übrig?“, und bis wann?

➡️ Am besten in den ersten Interviews, mit einem Datum.

**Lena:** F1: Ok, passt. F2: Ich kümmere mich, wir fragen in den Interviews. Bis Mitte Dezember, also 15.12.

**Agent:** *(schreibt `PROBLEM.md`, Register A6–A12, Canvas Block 1, 2 und Offene Fragen; führt `check_project.py` aus: keine FEHLER; kritische OFFEN, interviews OFFEN 0/3)*

Der Check meldet keine Fehler. Hier die Blöcke 1 und 2:

> **1. Kernproblem:** Menschen in Kiel mit wenig Geld bekommen abends oft keine warme Mahlzeit [A6], während in Mensen täglich Essen übrig bleibt [A1], [A7]. **Ursache:** Einrichtungen haben abends kein Personal zum Kochen [A8] (warum, ist offen). **Folgen:** hungrig schlafen gehen [A9], eher krank werden [A10], Lebensmittelverschwendung [A11].
> **2. Betroffene:** wohnungslose Menschen, ältere Menschen, Menschen mit wenig Geld, die soziale Einrichtungen besuchen [A12].

Passt das so?

**Lena:** Ja.

**Agent:** Soll ich committen? Als Nächstes käme `/to-interview-guide`, damit ihr einen Leitfaden für eure Interviews habt.

**Lena:** Ja, committen. Den Leitfaden brauchen wir nicht mehr – wir haben schon mit 4 Leuten gesprochen! Ich hab die Notizen hier.

**Agent:** *(git commit „Problem geschärft (/grill-problem)“ → 7551473)* Super! Dann ist `/log-evidence` der richtige Schritt – ruf ihn auf und füg die Notizen einfach in den Chat ein.

`[Runner-Notiz]` „Weiß ich nicht“ landet doppelt: unter *Noch offen* in `PROBLEM.md` (Regel aus „Wie du fragst“) und unter *Offene Fragen* im Canvas mit wer/bis wann („Schreib mit“). Der Skill sagt nicht, ob beides gewollt ist. Bei *Kernproblem* hat der Agent Lenas Satz in zwei Aussagen geteilt (A6 + Verweis auf A1) – unproblematisch, weil ihr Wortlaut blieb, aber der Skill sagt nicht, ob eine solche Aufteilung bestätigt werden muss. Der Leitfaden wurde übersprungen; die Interviews fanden also ohne den Leitfaden des Skills statt.

---

## 3. /log-evidence (Interviews)

**Lena:** /log-evidence
Hier sind unsere Notizen von den 4 Interviews: *(fügt den Inhalt von `eingaben/interview-notizen.md` in den Chat ein: Interview 1 · 2026-10-14 · Leitung einer Tafel-Ausgabestelle … bis Interview 4 · 2026-10-22 · Mitarbeiterin eines Jugendzentrums)*

**Agent:** *(liest `.claude/skills/log-evidence/SKILL.md`, lädt `assumptions` und `evidence-checks`; liest `ASSUMPTIONS.md`, `INTERVIEWS.md`, `TESTS.md`, `PROBLEM.md`, `CANVAS.md`, `SIGNALS.md`)*

Danke! Bevor ich auswerte, übertrage ich eure Notizen **wörtlich** in `INTERVIEWS.md` unter *Notizen*, jeweils mit *Ausgewertet: nein*:

- `### I1 · 2026-10-14 · Leitung einer Tafel-Ausgabestelle in Kiel` (5 Punkte)
- `### I2 · 2026-10-16 · Sozialarbeiter in einer Tagesstätte für wohnungslose Menschen` (4 Punkte)
- `### I3 · 2026-10-20 · Küchenleiter einer Mensa (Studierendenwerk)` (4 Punkte)
- `### I4 · 2026-10-22 · Mitarbeiterin eines Jugendzentrums` (3 Punkte)

Ich habe nur „Interview 1“ usw. zu „I1“ usw. gemacht, sonst nichts verändert; den Hinweis „Fiktiv“ oben aus eurer Datei habe ich weggelassen, weil er kein Teil der Interviews ist. Stimmt die Zuordnung (Nummer, Datum, Rolle)?

`[Runner-Notiz]` Wortgleichheit per `diff` gegen die Eingabedatei geprüft: identisch.

**Lena:** Ja, stimmt.

**Agent:** Ich habe die Notizen ausgewertet. Zwei Dinge vorab, die die Belege schwächen:

- **Wen ihr befragt habt:** Alle vier sind Mitarbeitende von Einrichtungen bzw. der Mensa (der Küchenleiter in I3 ist Experte, nicht betroffen). Mit den Betroffenen selbst – Gästen der Tafel, wohnungslosen Menschen – habt ihr noch nicht gesprochen.
- **I2 wurde gepitcht:** „Wir haben ihm unsere Idee erklärt und gefragt, ob er das nutzen würde“ – das „Ja klar, sofort“ ist höflich, kein Beleg dafür, dass Einrichtungen das Essen nehmen.

Jetzt die vorgeschlagenen Änderungen, in Abschnitten von höchstens fünf Zeilen, die *belegt*-Vorschläge zuerst. *Belegt* kann nur werden, was eine Person über ihre **eigene** Organisation erlebt oder tut – dafür braucht es keine Schwelle. Allgemeine Aussagen über „die Einrichtungen“ oder „die Mensen“ bleiben *Annahme*, bis ein Test es zeigt.

**Abschnitt 1 von 4 – neue Zeilen, Vorschlag *belegt***

| Annahme | bisher | Vorschlag | Beleg | Bedenken |
|---|---|---|---|---|
| A13 Die Tafel aus I1 verteilt fast nur Trockenware und Gemüse, kein warmes Essen. | neu | belegt | I1: „Warmes Essen haben wir gar nicht.“ | – |
| A14 In der Tagesstätte aus I2 gibt es abends kein Essen; trotzdem kommen Leute und fragen. | neu | belegt | I2: „abends gibt es nichts. Da kommen trotzdem Leute und fragen.“ | – |
| A15 In der Mensa aus I3 bleiben 5–20 Portionen pro Tag übrig, freitags mehr. | neu | belegt | I3: „fünf bis zwanzig Portionen übrig, freitags mehr“ | eine Mensa |
| A16 In der Mensa aus I3 geht Übriges in die Biogasanlage; Mitarbeitende dürfen nichts mitnehmen. | neu | belegt | I3: „geht in die Biogasanlage“ | widerspricht „Müll“ in A11 |
| A17 Die Tagesstätte aus I2 kann für den Service nichts bezahlen. | neu | belegt | I2: „Bezahlen können wir dafür nichts“ | – |

Bestätigt ihr diesen Abschnitt?

**Lena:** Ok, passt alles.

**Agent:** Danke! Weil es um *belegt* geht, frage ich hier jede Zeile einzeln – ein pauschales „passt“ reicht mir dafür nicht, das entscheidet ihr Zeile für Zeile:
- A13 belegt mit I1?
- A14 belegt mit I2?
- A15 belegt mit I3?
- A16 belegt mit I3?
- A17 belegt mit I2?

**Lena:** A13 ja, A14 ja, A15 ja, A16 ja, A17 ja.

**Agent:** **Abschnitt 2 von 4 – neue Zeilen, Vorschlag *belegt*** (bitte wieder je Zeile ja/nein)

| Annahme | bisher | Vorschlag | Beleg | Bedenken |
|---|---|---|---|---|
| A18 Für die Tafel aus I1 ist Abholen das Problem: ein Transporter, zwei Ehrenamtliche mit Führerschein. | neu | belegt | I1: „Abholen ist unser Problem.“ | – |
| A19 Die Tafel aus I1 darf gekühltes/warmes Essen nur mit dokumentierter Kühlkette annehmen. | neu | belegt | I1: „nur annehmen, wenn die Kühlkette dokumentiert ist“ | – |
| A20 Die Mensa aus I3 braucht für eine Abholung eine Freigabe von oben und eine Haftungsregel. | neu | belegt | I3: „brauchen wir eine Freigabe von oben und eine Haftungsregel“ | – |
| A21 In der Mensa aus I3 endet die Ausgabe um 14:30, um 15 Uhr muss die Küche sauber sein. | neu | belegt | I3: „Um 14:30 ist Schluss …“ | – |
| A22 Ins Jugendzentrum aus I4 kommen Jugendliche nachmittags und wollen eher Snacks; dort wird zusammen gekocht (pädagogische Arbeit). | neu | belegt | I4 | – |

**Lena:** A18 ja, A19 ja, A20 ja, A21 ja, A22 ja.

**Agent:** **Abschnitt 3 von 4 – zwei weitere *belegt*, dann bestehende Zeilen**

| Annahme | bisher | Vorschlag | Beleg | Bedenken |
|---|---|---|---|---|
| A23 Die Tafel aus I1 bewertet das Problem mit 6/10; mehr Fahrer:innen wären ihr wichtiger. | neu | belegt | I1: „Eine 6. Wichtiger wäre uns mehr Fahrer:innen.“ | – |
| A24 Die Tagesstätte aus I2 bekam letzten Winter drei Wochen Suppe von einem Hotel; dann schlief der Kontakt ein. | neu | belegt | I2 | – |
| A25 Viele Gäste der Tafel aus I1 sind ältere Menschen, die allein leben. | neu | belegt | I1: „Viele unserer Gäste sind ältere Menschen, die allein leben.“ | „Die kochen kaum noch“ ist ihre Einschätzung → eigene Annahme A26 |
| A11 Übriges Mensa-Essen landet im Müll. | Annahme | bleibt Annahme, Bedenken ergänzen | I3 widerspricht für eine Mensa | Formulierung prüfen? |
| A1 Mensen werfen jeden Tag viel Essen weg. | Annahme | bleibt Annahme, Hinweis I3 | I3: 5–20 Portionen, Biogas | allgemeine Aussage, eine Mensa |

**Lena:** A23 ja, A24 ja, A25 ja. A11 und A1 so lassen, ok.

**Agent:** **Abschnitt 4 von 4 – bestehende Zeilen, Status bleibt, Quelle wird ergänzt**

| Annahme | bisher | Vorschlag | Beleg | Bedenken |
|---|---|---|---|---|
| A2 Einrichtungen bekommen abends nichts Warmes. | Annahme | bleibt, Hinweis I1, I2 | I1, I2 stützen | allgemeine Aussage; I4 kein Bezug |
| A4 Einrichtungen würden das Essen gern nehmen. | Annahme | bleibt, Hinweise | I2 (gepitcht), I4 widerspricht, I1 nennt Bedingungen | kein Beleg |
| A5 Studierendenwerk würde bezahlen. | Annahme | bleibt | I3: nur „gut fürs Image“ | zu Bezahlung nichts |
| A8 Einrichtungen haben abends kein Personal. | Annahme | bleibt | I2 nennt keinen Grund | weiter offen |
| A3 Es fehlt eine App. | Annahme | bleibt | niemand nennt eine App | – |

**Neue Annahmen (Status *Annahme*):**
- A26 Ältere, allein lebende Menschen kochen kaum noch. (Hinweis aus I1)
- A27 Einrichtungen mit eigener pädagogischer Küche wollen kein gekochtes Essen von außen. (Hinweis aus I4 – eine Aussage über eure Idee, darum kein *belegt*)
- A28 Das Studierendenwerk fände eine Abholung gut fürs Image. (Hinweis aus I3 – Vermutung über Dritte)

**Ergänzungen am Problembaum (Ursachen):** Abholen als Engpass [A18], [A23]; Regeln zu Kühlkette und Haftung [A19], [A20]; Zeitlücke Mensa 14:30 vs. abends [A21], [A14]. Bei den Folgen: „Lebensmittelverschwendung“ [A11] ist für die Mensa aus I3 fraglich, das Essen geht in die Biogasanlage [A16].

**Lena:** Ok, passt.

**Agent:** *(schreibt Register, `INTERVIEWS.md` Auswertung + Ausgewertet: ja, `PROBLEM.md` Baum und Noch offen, `SIGNALS.md`, Canvas Block 1 (Ursachen ergänzt, weil der Baum sich geändert hat), Block 5, Block 6 (alter Stand ersetzt), Block 10; führt `check_project.py` aus)*

```
OK      verweise      alle Verweise stehen im Register
OK      status        28 Einträge mit gültigem Status und Quelle
OFFEN   kritische     noch keine Annahme als kritisch markiert
OK      schwellen     0 Testkarten geprüft
OK      eine-annahme  jede Karte prüft eine Annahme
OK      ergebnisse    alle Ergebnisse ausgewertet, keine Karte überfällig
OK      widerlegt     keine widerlegte Annahme in MODEL.md
OK      interviews    4 von mindestens 3 Interviews ausgewertet (4 notiert)
```

Keine Fehler. Eingetragen: 13 *belegte* Aussagen über die befragten Organisationen, 3 neue Annahmen, 5 ergänzte Quellen, 3 neue Ursachen im Problembaum. In Block 6 steht jetzt der neue Stand statt der Liste aus Notion. Soll ich committen? Als Nächstes: `/map-solutions` (bestehende Lösungen recherchieren) oder `/grill-solution`.

**Lena:** Ja, committen. Wir machen mit `/grill-solution` weiter.

**Agent:** *(git commit „Interviews I1–I4 ausgewertet (/log-evidence)“ → a9f5385)*

`[Runner-Notiz]` Der Stop-Point sagt „Tabelle der vorgeschlagenen Änderungen … Darunter neue Annahmen“. Ob neue Zeilen mit Vorschlag *belegt* in die Tabelle gehören (dann gelten Reihenfolge und Einzelbestätigung) oder „darunter“, ist nicht eindeutig; der Agent hat sie in die Tabelle genommen. Bei 13 *belegt*-Zeilen bedeutet die Einzelbestätigung 13 Einzelantworten – Lena hat brav „ja, ja, ja“ getippt, das ist Reibung, schützt aber die Regel. Unklar ist auch die Regel für I4: „Gekochtes Essen von außen würde bei uns eher nicht passen“ ist eine Aussage über die eigene Organisation **und** über die Idee; `assumptions` lässt Ablehnungen der Idee wie Zustimmungen als *Annahme* stehen. A11 („landet im Müll“) wird durch I3 für eine Mensa widersprochen; die Regeln kennen nur *widerlegt* oder *Annahme*, keinen Weg, die Formulierung einer Annahme zu korrigieren.

---

## 4. /grill-solution (verkürzt)

**Lena:** /grill-solution

**Agent:** *(liest `.claude/skills/grill-solution/SKILL.md`, lädt `assumptions`; liest `CANVAS.md`, `PROBLEM.md`, `ASSUMPTIONS.md`, `INTERVIEWS.md`, `SOLUTIONS.md`, `DECISIONS.md`)*

Bevor wir starten, ein Hinweis: Ihr habt 4 Interviews ausgewertet – gut. Aber `SOLUTIONS.md` ist leer: Ihr habt noch nicht recherchiert, was es schon gibt (z. B. andere Initiativen, die Essen retten). Das Handbuch sieht beides vor der Lösung vor; ohne diese Recherche wisst ihr nicht, was ihr anders macht als andere. Wollt ihr trotzdem weitermachen, oder zuerst `/map-solutions`?

**Lena:** Wir machen trotzdem weiter, wir wollen schnell vorankommen.

**Agent:** Ok, halte ich in `DECISIONS.md` fest. Es werden **ungefähr fünf bis sechs Runden**.

**Runde 1 von ca. 6**

❓ **F1** – **Vision**: Welche Veränderung in der Gesellschaft wollt ihr erreichen – ein Zielzustand, den ihr nicht allein schafft, kein Produkt? Höchstens zwei Sätze, gern „Wir wollen, dass …“. **Bitte in euren eigenen Worten.**

➡️ Eure Worte zuerst; wenn euch nichts einfällt, mache ich einen Vorschlag.

❓ **F2** – **Veränderung**: Was soll sich durch eure Idee konkret verändern?

➡️ Auch hier eure Worte.

**Lena:** F1: Dass niemand in Kiel abends hungrig bleiben muss. F2: Dass das Essen nicht weggeworfen wird, sondern bei Menschen landet.

**Agent:** Das ist eine Vision im Sinne des Handbuchs: ein Zielzustand, keine Lösung. Ich trage sie so in Block 1 ein, **ohne ID** – sie ist eure Entscheidung, keine Aussage über die Welt, und kommt deshalb nicht ins Register, sondern in `DECISIONS.md`. Bei der Veränderung schreibe ich „statt in der Biogasanlage“, weil I3 das so sagt [A16] – ok?

**Lena:** Ja.

**Agent:** **Runde 2 von ca. 6 (danach noch etwa vier)**

❓ **F1** – **Lösung**: Was bietet ihr an – in ein paar Sätzen, **in euren Worten**? Was macht ihr anders als das, was es gibt? (Was es gibt, wisst ihr noch nicht, weil `SOLUTIONS.md` leer ist.)

➡️ Erst eure Worte.

**Lena:** Kannst du das Canvas nicht einfach für uns ausfüllen?

**Agent:** Das mache ich lieber nicht: Es entstünden lauter plausible Sätze, die im Canvas wie Wissen aussehen, aber nur meine Annahmen sind. Mein Angebot: Du erzählst in deinen Worten, wie ihr euch das vorstellt – auch ungeordnet –, ich ordne es, frage nach und trage es ein.

**Lena:** Ok. Also: Wir holen das übrige Essen nach 14:30 in der Mensa ab und bringen es abends zu Einrichtungen wie der Tafel und der Tagesstätte. Erstmal von Hand, ohne App.

**Agent:** Danke, das trage ich so ein. Darauf beruht die Lösung (keine Bewertung, nur was trägt):
- dass die Mensa abgibt – I3 sagt, dafür braucht es eine Freigabe von oben und eine Haftungsregel [A20] → neue Annahme [A30];
- dass Einrichtungen das Essen annehmen – I1 und I2 stützen, I4 widerspricht → neue Annahme [A31];
- dass ihr Abholung und Lieferung selbst schafft – Abholen ist für die Tafel der Engpass [A18] → neue Annahme [A32];
- zwischen 14:30 und abends muss das Essen gekühlt werden; die Tafel braucht eine dokumentierte Kühlkette [A19].

Ihr habt die App aus Notion [A3] zurückgestellt – das halte ich als verworfene Alternative in `DECISIONS.md` fest. Ok?

**Lena:** Ok, passt.

**Agent:** **Runde 3 von ca. 6 (danach noch etwa drei)**

❓ **F1** – **Nutzer:innen und Kund:innen**: Wer nutzt euer Angebot, wer bezahlt oder ermöglicht es, bei wem entsteht die Wirkung? Das Handbuch kennt vier Fälle: (a) dieselben, (b) verschieden – eine dritte Partei zahlt, (c) die Zielgruppe ist Teil der Wertschöpfungskette, (d) nichts davon.

➡️ Ich vermute (b): Die Tagesstätte aus I2 sagt, sie kann nichts bezahlen [A17]. Wer stattdessen zahlt, wisst nur ihr – oder es ist noch offen.

**Lena:** Nutzen tun die Einrichtungen und ihre Gäste. Bezahlen … vielleicht das Studierendenwerk? Oder eine Stiftung. Wissen wir noch nicht. Dann ist es (b), oder?

**Agent:** Ja, (b). „Wer zahlt“ kommt unter Offene Fragen; als Annahmen stehen dann [A5] Studierendenwerk zahlt (schon im Register; aus I3 gibt es dazu nur „gut fürs Image“) und neu [A29] eine Stiftung fördert. Die Wirkung entsteht bei den Gästen [A12].

**Runde 4 von ca. 6 (danach noch etwa zwei)**

❓ **F1** – **Wertangebot für die Einrichtungen**: Was verbessert sich für sie? **In euren Worten.**

➡️ Erst eure Worte.

❓ **F2** – **Wertangebot für die Mensa / das Studierendenwerk**: Was haben sie davon? **In euren Worten.**

➡️ Erst eure Worte.

❓ **F3** – **Wertangebot für eine Stiftung**: Was hätte eine Stiftung davon?

➡️ Erst eure Worte; „weiß ich nicht“ ist ok.

(Für eine ausführliche Passung gibt es das Value Proposition Canvas von Strategyzer.com.)

**Lena:** F1: Die kriegen abends was Warmes für ihre Leute, ohne selbst zu kochen oder abzuholen. F2: Weniger wegwerfen und gut fürs Image. F3: Weiß ich nicht.

**Agent:** Danke. F1 stützt sich auf [A31] und den Engpass Abholen [A18]; F2 auf [A28] (Vermutung aus I3) und [A16]. F3 kommt unter Offene Fragen.

**Runde 5 von ca. 6 (danach noch eine)**

❓ **F1** – **Erfolgskriterien**: Woran merkt ihr, dass das Problem kleiner wird? Und was muss wahr sein, damit euer Modell trägt? Legt es fest, bevor ihr testet.

➡️ Eure Worte; ich helfe dann, es prüfbar zu machen.

❓ **F2** – **Lösungs-Hypothesen**: Ich schlage diese prüfbaren Aussagen vor: [A31] Einrichtungen nehmen regelmäßig Mensa-Essen an, wenn ihr es liefert · [A30] Die Mensa gibt ab, wenn Freigabe und Haftung geklärt sind · [A32] Ihr schafft Abholung und Lieferung selbst · [A5] Das Studierendenwerk zahlt · [A29] Eine Stiftung fördert. Fehlt etwas?

➡️ So übernehmen; sie decken Lösung, Partner und „wer zahlt“ ab.

**Lena:** F1: Wenn jeden Abend Essen bei den Einrichtungen ankommt. Und dass so 3 von 4 Einrichtungen mitmachen? Schreib erstmal 3 von 4, das muss ich noch mit Ahmet und Jule absprechen. F2: Ok, passt.

**Agent:** „Jeden Abend kommt Essen an“ und „mehrere Einrichtungen machen mit“ trage ich als Erfolgskriterien in Block 4 ein (ohne ID, es sind eure Entscheidungen). Die Zahl „3 von 4“ habt ihr aber noch nicht gemeinsam beschlossen – sie kommt deshalb als **offene Frage** ins Canvas („vorläufig 3 von 4, Lena klärt mit Ahmet und Jule“), nicht als Entscheidung. Bis wann?

**Lena:** Bis nächsten Sonntag, 29.11.

**Agent:** **Runde 6 von ca. 6 (die letzte)**

❓ **F1** – **Kritische Annahmen**: Ich schlage als kritisch vor:
- [A31] Einrichtungen nehmen an – ohne sie gibt es keine Wirkung;
- [A30] Mensa gibt ab – ohne Essen kein Angebot;
- [A5] Studierendenwerk zahlt **oder** [A29] Stiftung fördert – ohne Geld trägt sich der Lieferdienst nicht; ich würde beide markieren, weil noch offen ist, wer zahlt.
[A32] würde ich nicht kritisch machen: Das könnt ihr selbst beeinflussen.

➡️ Diese vier.

**Lena:** Ok, passt, alle vier.

**Agent:** *(schreibt Register A29–A32, *Kritisch: ja* bei A5, A29, A30, A31; Canvas Block 1–4, 6, Offene Fragen; `DECISIONS.md` (Weitermachen ohne SOLUTIONS, Vision, Lösung ohne App, Erfolgskriterien); führt `check_project.py` aus)*

```
OK      verweise      alle Verweise stehen im Register
OK      status        32 Einträge mit gültigem Status und Quelle
OFFEN   kritische     A5: keine Testkarte; A29: keine Testkarte; A30: keine Testkarte; A31: keine Testkarte
…
OK      interviews    4 von mindestens 3 Interviews ausgewertet (4 notiert)
```

Keine Fehler; die kritischen Annahmen brauchen noch Testkarten (das kommt mit `/to-tests`). Hier die Blöcke 1–4 und 6 *(zeigt sie)*. Passt das so?

**Lena:** Ja.

**Agent:** Soll ich committen? Dann weiter mit `/to-model`.

**Lena:** Ja.

**Agent:** *(git commit „Lösung geschärft (/grill-solution)“ → a03a52e)*

`[Runner-Notiz]` Unklar, ob der Lösungstext in Block 3 („Wir holen … ab und bringen …“) eine ID braucht: `assumptions` nimmt nur Vision, Erfolgskriterien und Schwellen aus, der Skill verlangt „alle Aussagen über die Welt mit ihren IDs“. Der Agent hat die Lösung als Entscheidung ohne ID eingetragen und die tragenden Hypothesen mit IDs daneben. Ebenso bei der Wertangebots-Formulierung (Lenas Wortlaut mit IDs dahinter). Der Bezug auf die „Lücken aus dem Fazit in `SOLUTIONS.md`“ ging nicht, weil die Datei leer ist – der Agent hat das in der Frage gesagt.

---

## 5. /to-model (verkürzt)

**Lena:** /to-model

**Agent:** *(liest `.claude/skills/to-model/SKILL.md`, lädt `assumptions` und `evidence-checks`; liest `CANVAS.md`, `ASSUMPTIONS.md`, `PROBLEM.md`, `SOLUTIONS.md`, `DECISIONS.md`)*

Block 1–3 sind gefüllt, wir können loslegen. Zuerst die Gliederung eures Social Business Model Canvas:

| Feld | Was es im Register schon gibt | Lücke |
|---|---|---|
| 1. Gesellschaftliche Herausforderung | A6, A1, A15 (belegt) | – |
| 2. Gesellschaftliche Veränderung | Vision, Block 1 (ohne ID) | – |
| 3. Lösung | A31, A18 (belegt), A28, A16 (belegt) | Wertangebot Stiftung offen |
| 4. Schlüsselaktivitäten | A32 | was genau ihr tun müsst |
| 5. Schlüsselpartner:innen | A30, A20 (belegt) | weitere? |
| 6. Kund:innengruppen | A31, A12, A5, A29 | – |
| 7. Kund:innenbeziehung | – | ja |
| 8. Kanäle | – | ja |
| 9. Einnahmequellen | A5, A29, A17 (belegt) | wie viel |
| 10. Kostenstruktur | – | ja |

Für die Lücken habe ich Fragen, in **zwei Runden** mit höchstens vier Fragen. Die Optionen sind nur Beispiele für *Arten*, keine Vorschläge für bestimmte Organisationen oder Beträge.

**Runde 1 von 2**

❓ **F1** – **Schlüsselaktivitäten**: Was müsst ihr regelmäßig tun, damit es funktioniert? In euren Worten. (Beispiele für Arten: abholen, transportieren, Absprachen treffen, dokumentieren.)

➡️ Eure Worte zuerst.

❓ **F2** – **Schlüsselpartner:innen**: Mit wem arbeitet ihr zusammen, wer liefert euch etwas? (Beispiele für Arten: eine Mensa oder Küche, eine Organisation, die Fahrzeuge verleiht, Ehrenamtliche.)

➡️ Eure Worte zuerst.

❓ **F3** – **Kund:innenbeziehung**: Wie haltet ihr den Kontakt zu den Einrichtungen, damit sie dabeibleiben? (Beispiele für Arten: feste Ansprechperson, Gruppe in einem Messenger, regelmäßige Treffen.)

➡️ Eure Worte zuerst.

❓ **F4** – **Kanäle**: Wie erreicht ihr die Einrichtungen und die Mensa? (Beispiele für Arten: persönlich vorbeigehen, über bestehende Kontakte, ein Netzwerk von Einrichtungen.)

➡️ Eure Worte zuerst.

**Lena:** F1: Essen abholen, ausliefern, mit den Einrichtungen absprechen, wann wir kommen. F2: Die Mensa bzw. das Studierendenwerk. F3: Eine WhatsApp-Gruppe mit den Einrichtungen, damit die wissen, was kommt. F4: Wir gehen persönlich hin und stellen uns vor. Beim Studierendenwerk über den Küchenleiter.

**Agent:** Danke, notiert als Annahmen [A33] (Aktivitäten), [A34] (Beziehung), [A35] und [A36] (Kanal); Partner ist [A30].

**Runde 2 von 2 (die letzte)**

❓ **F1** – **Einnahmequellen**: Ihr habt Studierendenwerk [A5] oder Stiftung [A29] genannt. Wie viel braucht ihr bzw. erwartet ihr von wem? (Beispiele für Arten von Einnahmen: eine Stiftung, Spenden, ein Auftrag einer Einrichtung, ein Förderprogramm.)

➡️ Wenn ihr keine Zahl habt, ist das ok – dann wird es eine offene Frage.

❓ **F2** – **Kostenstruktur**: Welche Kosten habt ihr, und was ist am teuersten?

➡️ Eure Worte; Beträge nur, wenn ihr sie wisst.

**Lena:** F1: Studierendenwerk oder Stiftung, wie besprochen. Wie viel, wissen wir nicht. F2: Transport, also Auto oder Lastenrad, und Verpackungen. Ist ja nicht viel.

**Agent:** Die Kostenarten trage ich als Annahme ein [A37]. „Ist ja nicht viel“ ist aber keine Zahl – daraus mache ich keine Register-Zeile, sondern eine **offene Frage** im Canvas: „Wie hoch sind die Kosten für Transport und Verpackungen?“ Ebenso „Wie viel Geld braucht ihr, wie viel könnte wer geben?“. Wer klärt das, bis wann?

**Lena:** Ahmet, der studiert Wirtschaft. Bis 15.12.

**Agent:** Bestätigt ihr die Gliederung so?

**Lena:** Ja.

**Agent:** *(schreibt `MODEL.md` Feld für Feld; neue Zeilen A33–A37 mit Kategorien Aktivitäten, Beziehung, Kanal, Kanal, Kosten; Lösung und Kund:innengruppen getrennt für Nutzer:innen und Kund:innen; Quellenvermerk bleibt; Block 7; führt `check_project.py` aus: keine FEHLER)*

Beim Prüfen ist mir aufgefallen:

1. **Niemand zahlt bisher sicher** (`MODEL.md` Feld 9, Block 7): Studierendenwerk [A5] und Stiftung [A29] sind Annahmen, die Tagesstätte kann nicht zahlen [A17]. Das ist wichtig, weil ohne Geld Transport und Verpackungen nicht gedeckt sind. Optionen: (a) *(Empfehlung)* so lassen – A5 und A29 sind schon kritisch und werden getestet; (b) eine weitere Einnahmeart aufnehmen. Ob die Einnahmen die Kosten decken, kann ich nicht sagen: Es fehlen beide Zahlen.
2. **Auf [A32] bauen Aktivitäten und Kosten auf** (Feld 4 und 10), A32 ist aber nicht kritisch. Optionen: (a) *(Empfehlung)* A32 kritisch markieren, weil die Tafel genau beim Abholen ein Problem hat [A18]; (b) nicht kritisch lassen, weil ihr es selbst in der Hand habt.

**Lena:** 1: a. 2: b, das schaffen wir schon, wir sind zu dritt.

**Agent:** *(schreibt `DECISIONS.md`)* Ist das Modell so für euch bestätigt?

**Lena:** Ja.

**Agent:** Soll ich committen? Dann weiter mit `/to-tests`.

**Lena:** Ja.

**Agent:** *(git commit „Geschäftsmodell (/to-model)“ → c93e6b1)*

`[Runner-Notiz]` Bei F1 Runde 2 sind die Arten-Beispiele etwas redundant mit dem, was das Team schon gesagt hat; unkritisch. Die Prüfung „Einnahmen decken die Kosten?“ läuft ins Leere, wenn beide Zahlen offen sind – der Skill sagt richtig „nicht rechnen, nachfragen“, das Ergebnis ist eine offene Frage. Kein Problem gefunden.

---

## 6. /to-tests

*(Simulation: Zeit ist gerafft; alle Dateidaten bleiben 2026-11-22.)*

**Lena:** /to-tests

**Agent:** *(liest `.claude/skills/to-tests/SKILL.md`, lädt `assumptions` und `evidence-checks`; liest `ASSUMPTIONS.md`, `CANVAS.md` Block 4 und 6, `MODEL.md`, `TESTS.md`, `DECISIONS.md`)*

Ihr habt vier kritische Annahmen mit Status *Annahme*: [A30] Mensa gibt ab, [A5] Studierendenwerk zahlt, [A31] Einrichtungen nehmen an, [A29] Stiftung fördert. Ich habe für jede **eine eigene Karte mit eigener Schwelle** entworfen; T1 und T2 nutzen dasselbe Gespräch, haben aber getrennte Karten. Eine Frage vorab, weil ich den Aufwand nicht schätzen will: **Wie viel Zeit habt ihr in den nächsten Wochen?**

**Lena:** Jeder so 4 Stunden pro Woche. Eine Woche Probe-Lieferung schaffen wir, dann machen wir halt mal mehr.

**Agent:** Danke. Zuerst die Probleme, die ich im Plan sehe, jeweils mit Empfehlung:

1. **Reihenfolge:** Die Probe-Lieferung (T3, [A31]) braucht Essen aus der Mensa – sie baut also auf [A30] auf, das selbst noch ungetestet ist. ➡️ *Empfehlung:* T3 bekommt *Voraussetzung: T1*; erst das Gespräch mit dem Studierendenwerk.
2. **Meinung statt Verhalten bei T2 ([A5]):** „Würden Sie dafür bezahlen?“ ist eine Meinung. Verhalten zeigt erst ein konkretes Angebot mit Preis. Einen Preis habt ihr aber noch nicht (offene Frage). ➡️ *Empfehlung:* entweder bis zum Gespräch einen Preis festlegen, oder die Schwelle streng halten: Nur eine **verbindliche** Zahlungszusage zählt, „finden wir gut“ nicht.
3. **Schwelle von T3 übernimmt eine offene Zahl:** „3 von 4“ steht im Canvas noch als offene Frage („vorläufig, Lena klärt mit Ahmet und Jule“). **Habt ihr die Zahl inzwischen als ganzes Team beschlossen?** Wenn nicht, bleibt die Karte offen, bis es so weit ist.
4. **Jugendzentrum in T3:** I4 hat gesagt, gekochtes Essen von außen passe eher nicht [A27]. Ist es eine der vier, braucht ihr praktisch alle anderen drei. ➡️ *Empfehlung:* durch eine andere Einrichtung mit Abendbetrieb ersetzen – oder bewusst drinlassen.
5. **Schwellen zu niedrig?** T4 „mindestens eine von zwei Stiftungen sagt zu“ ist niedrig, aber eine echte Zusage ist ein starkes Signal. ➡️ *Empfehlung:* so lassen.

Dann die Karten *(zeigt T1–T4 wie in `TESTS.md`, je mit Annahme, Voraussetzung, Test, Mit wem, Bis wann, Messgröße, Schwelle, Status: geplant, Ausgewertet: nein)*.

**Lena:** 1: Ok, dann zuerst das Gespräch. 2: Wir haben keinen Preis, wir fragen einfach, ob sie zahlen. Streng ist ok. 3: Ja, haben wir am Donnerstag zu dritt besprochen, 3 von 4 passt für alle. 4: Wir fragen das Jugendzentrum trotzdem, wir kennen nicht so viele Einrichtungen. 5: Ok.

**Agent:** Danke – ich nehme „3 von 4“ als **gemeinsam beschlossene** Schwelle auf, streiche die offene Frage und halte das in `DECISIONS.md` fest; Block 4 bekommt die Zahl jetzt als Erfolgskriterium. Die Karten sind bestätigt?

**Lena:** Ja.

**Agent:** *(schreibt `TESTS.md`, Test-IDs in die Spalte *Test* des Registers, Block 9 und Block 4, `DECISIONS.md`; führt `check_project.py` aus)*

```
OK      verweise      alle Verweise stehen im Register
OK      status        37 Einträge mit gültigem Status und Quelle
OK      kritische     4 offene kritische Annahmen haben eine Testkarte mit Schwelle
OK      schwellen     4 Testkarten geprüft
OK      eine-annahme  jede Karte prüft eine Annahme
OK      ergebnisse    alle Ergebnisse ausgewertet, keine Karte überfällig
OK      widerlegt     keine widerlegte Annahme in MODEL.md
OK      interviews    4 von mindestens 3 Interviews ausgewertet (4 notiert)
```

*kritische* und *eine-annahme* sind OK. **Bitte committet die Karten jetzt, bevor ihr testet** – so bleibt im Git-Verlauf sichtbar, dass die Schwellen vor den Ergebnissen feststanden. Soll ich das machen?

**Lena:** Ja, mach.

**Agent:** *(git commit „Testkarten T1–T4 vor dem Testen (/to-tests)“ → 58fa83c)* Jetzt seid ihr dran: testen, und die Ergebnisse in `TESTS.md` notieren oder einfach in den Chat einfügen – dann `/log-evidence`.

`[Runner-Notiz]` Der Agent kann nicht prüfen, ob „3 von 4“ wirklich vom ganzen Team beschlossen wurde; er übernimmt Lenas Aussage und vermerkt sie als ihre Aussage in `DECISIONS.md`. Das ist vermutlich das Maximum. Der Skill sagt nicht, ob das Jugendzentrum-Risiko (Problem 4) in der Schwelle berücksichtigt werden muss; Lena hat es bewusst drin gelassen.

---

## 7. /log-evidence (Tests)

**Lena:** /log-evidence
Wir haben getestet! Hier die Ergebnisse: *(fügt den Inhalt von `eingaben/test-ergebnisse.md` in den Chat ein – Probe-Abholung bei Einrichtungen; Gespräch mit dem Studierendenwerk; Anfrage bei zwei Stiftungen – ohne die Zeile zum Verhalten der Persona)*

**Agent:** *(liest `.claude/skills/log-evidence/SKILL.md`, lädt `assumptions` und `evidence-checks`; liest Projektdateien; führt `git log -- TESTS.md` und `git show 58fa83c -- TESTS.md` aus)*

Danke! Zuerst übertrage ich eure Ergebnisse **wörtlich** in das Feld *Ergebnis* der passenden Karten. So würde ich zuordnen:

| Euer Ergebnis | Karte |
|---|---|
| Probe-Abholung bei Einrichtungen | **T3** Probe-Lieferung ([A31]) |
| Gespräch mit dem Studierendenwerk | **T1** Essen abgeben ([A30]) **und T2** bezahlen ([A5]) – dasselbe Zitat in beiden Karten |
| Anfrage bei zwei Stiftungen | **T4** ([A29]) |

Stimmt diese Zuordnung?

**Lena:** Ja, genau.

**Agent:** Zu T3 fehlt mir eine Messgröße der Karte: **Wie viele Portionen wurden pro Abend angenommen?** Und eine Frage zur Reihenfolge: T3 hatte *Voraussetzung: T1* (Freigabe der Mensa). Das Studierendenwerk hat aber nur unter Bedingung zugesagt. Woher kam das Essen in der Probewoche?

**Lena:** Portionen haben wir nicht gezählt. Woher genau das Essen kam, weiß ich nicht, das hat Jule organisiert.

**Agent:** Ok, ich notiere „Portionen pro Abend: nicht gezählt“ im Ergebnis. Weil die Voraussetzung T1 noch nicht bestanden ist, gilt das Ergebnis von T3 **nur unter Vorbehalt** – das schreibe ich dazu. Die Schwellen standen laut Git-Verlauf seit dem Commit „Testkarten T1–T4 vor dem Testen“ fest, also vor den Ergebnissen. Gut so.

Jetzt die vorgeschlagenen Änderungen, *belegt*/*widerlegt* zuerst, je Zeile einzeln zu bestätigen.

**Abschnitt 1 von 2**

| Annahme | bisher | Vorschlag | Beleg (Ergebnis gegen Schwelle) | Bedenken |
|---|---|---|---|---|
| A31 Einrichtungen nehmen regelmäßig an, wenn geliefert wird | Annahme, kritisch | **widerlegt** | T3: 2 von 4 nahmen an mind. 3 Abenden an; Schwelle „mind. 3 von 4“ nicht erreicht | Vorbehalt: T1 nicht bestanden – die Absagen kamen aber von den Einrichtungen, nicht von der Mensa |
| A5 Studierendenwerk würde bezahlen | Annahme, kritisch | **widerlegt** | T2: „Bezahlen können wir dafür aber nichts“ – Aussage über sich selbst | – |
| A38 Tafel und Tagesstätte nahmen in der Probewoche an mind. 3 Tagen an | neu | belegt | T3 (Beobachtung) | – |
| A39 Jugendzentrum lehnte ab („passt nicht zu uns“) | neu | belegt | T3 | – |
| A40 Tafel konnte nur an 2 von 5 Tagen selbst abholen, sonst lieferte das Team | neu | belegt | T3 | – |

**Lena:** Bei A31 … 2 von 4 ist doch auch gut, können wir das nicht als belegt nehmen?

**Agent:** Ich verstehe den Wunsch – zwei Einrichtungen haben wirklich mitgemacht, und das steht als *belegt* in A38. Aber die Schwelle „3 von 4“ habt ihr **vor** dem Test gemeinsam festgelegt und committet. Wenn wir sie jetzt senken, damit das Ergebnis passt, ist das genau die Falle „Schwelle nach dem Test“: Mit geänderter Schwelle wäre das Ergebnis nur noch ein **Signal**, kein Beleg. Mein Vorschlag: A31 *widerlegt*, und wenn ihr glaubt, dass zwei feste Einrichtungen reichen, formuliert ihr das als neue Annahme mit neuer Schwelle für den nächsten Test (z. B. über `/review-model` und `/to-tests`).

**Lena:** Ok, verstehe. Dann widerlegt. A5 ja, widerlegt. A38 ja, A39 ja, A40 ja.

**Agent:** **Abschnitt 2 von 2**

| Annahme | bisher | Vorschlag | Beleg | Bedenken |
|---|---|---|---|---|
| A42 Eine Stiftung fördert Ehrenamtsprojekte bis 5.000 €, Antrag bis März | neu | belegt | T4: Aussage der Stiftung über sich selbst | sagt nichts über *euren* Antrag |
| A30 Mensa gibt ab, wenn Freigabe und Haftung geklärt sind | Annahme, kritisch | bleibt Annahme, **offen**; T1 bleibt *läuft* | T1: „machen wir gern mit, wenn die Haftung geklärt ist“ – Zusage unter Bedingung, Schwelle (verbindliche Zusage) nicht erreicht | – |
| A29 Eine Stiftung fördert den Lieferdienst | Annahme, kritisch | bleibt Annahme, **offen**; T4 bleibt *läuft* | T4: Förderung möglich, Antrag bis März – noch keine Zusage; die zweite Stiftung hat nicht geantwortet | Ergebnis hängt am Antrag |

**Neue Annahme:** A41 Das Studierendenwerk würde Verpackungen stellen (Hinweis aus T2: „höchstens Verpackungen stellen“ – eine Absicht, keine Zusage).
**Quellen ergänzt:** A27 (Jugendzentrum lehnte in T3 ab), A32 (Team lieferte an 3 von 5 Tagen).

**Lena:** A42 ja. A30 und A29 offen lassen, ok. A41 ok.

**Agent:** *(schreibt Register, `TESTS.md` – Ergebnis, Ausgewertet: ja bei allen vier, Status: T2 und T3 abgeschlossen, T1 und T4 läuft –, `SIGNALS.md`, Canvas Block 5, 6 (Stand ersetzt), 10; führt `check_project.py` aus)*

```
OK      verweise      alle Verweise stehen im Register
OK      status        42 Einträge mit gültigem Status und Quelle
OK      kritische     2 offene kritische Annahmen haben eine Testkarte mit Schwelle
OK      schwellen     4 Testkarten geprüft
OK      eine-annahme  jede Karte prüft eine Annahme
OK      ergebnisse    alle Ergebnisse ausgewertet, keine Karte überfällig
OFFEN   widerlegt     widerlegte Annahmen in MODEL.md: A31, A5 – prüfen, ob das Feld noch darauf aufbaut
OK      interviews    4 von mindestens 3 Interviews ausgewertet (4 notiert)
```

Keine Fehler. Wichtig: **[A31] und [A5] sind widerlegt, stehen aber noch in `MODEL.md`** (Lösung, Kund:innengruppen, Einnahmequellen) **und in Block 2 und 7** des Canvas. Diese Stellen ändere ich nicht selbst – ich habe sie in Block 2 und 7 mit ⚠️ für euch und `/review-model` markiert; `MODEL.md` bleibt unverändert, der Check meldet sie unter *widerlegt*. Soll ich committen? Als Nächstes: `/review-model`.

**Lena:** Ja.

**Agent:** *(git commit „Testergebnisse T1–T4 ausgewertet (/log-evidence)“ → ab2730b)*

`[Runner-Notiz]` (1) Der Skill sagt, das Ergebnis einer Karte mit nicht bestandener Voraussetzung gelte „nur unter Vorbehalt“, aber nicht, welcher Status dann vorzuschlagen ist (*widerlegt* unter Vorbehalt? offen?). Der Agent hat *widerlegt* mit Vorbehalt vorgeschlagen, weil die Absagen nicht an der Mensa lagen – das ist eine Ermessensentscheidung. (2) T1 und T4 stehen auf *läuft* mit *Ausgewertet: ja*; Schritt 1 findet beim nächsten Mal nur Karten mit *Ausgewertet: nein*, also wird ein späteres Ergebnis (Haftung geklärt, Antrag bewilligt) leicht übersehen, und `check_project.py` meldet laufende Karten ohne neues Datum nicht. (3) „Markiere sie für das Team“ sagt nicht, wo: Der Agent hat Block 2/7 markiert, aber `MODEL.md` nicht angefasst – ob dort eine Markierung erlaubt ist, bleibt offen. Block 3 (Wertangebot, Lösungs-Hypothesen mit [A31]) und Block 4 (Erfolgskriterium „3 von 4“, jetzt verfehlt) nennt der Skill nicht, obwohl sie ebenfalls betroffen sind. (4) Dasselbe Zitat steht in T1 und T2 – richtig nach „eine Karte pro Annahme“, aber doppelt.

---

## 8. /review-model

**Lena:** /review-model

**Agent:** *(liest `.claude/skills/review-model/SKILL.md`, lädt `evidence-checks` und `assumptions`; liest alle Projektdateien und die letzten Einträge in `SIGNALS.md`; führt `check_project.py` aus. Die beiden Achsen laufen nacheinander, weil in dieser Simulation keine Sub-Agenten genutzt werden.)*

Ich habe euer Modell auf zwei Achsen geprüft: **Beleg** (was trägt, was ist nur Annahme) und **Wirkung** (dient es den Betroffenen, trägt es sich). Vorweg: Manche Befunde sind als **blockierend** markiert. *Blockierend heißt: Das solltet ihr klären, bevor ihr darauf weiterbaut – es heißt nicht, dass ihr aufhören müsst.*

**Achse 1: Beleg**

| # | Befund | Art | Beleg | Vorschlag |
|---|---|---|---|---|
| 1 | [A31] „Einrichtungen nehmen regelmäßig an“ ist widerlegt, trägt aber noch *Lösung* und *Kund:innengruppen* in `MODEL.md` sowie Block 2 und 3. | **blockierend** | `ASSUMPTIONS.md` A31, T3; `MODEL.md` Feld 3, 6 | engere Annahme auf Basis von [A38] formulieren und neu testen |
| 2 | [A5] „Studierendenwerk zahlt“ ist widerlegt; damit ist niemand belegt, der zahlt. *Einnahmequellen* und Block 7 bauen darauf auf. | **blockierend** | A5, T2; `MODEL.md` Feld 9 | Finanzierung über [A29]/[A42] (Stiftung) oder andere Art prüfen |
| 3 | [A30] „Mensa gibt ab“ ist offen (Zusage nur bei geklärter Haftung); ohne sie gibt es kein Essen. | **blockierend** | A30, T1 (läuft) | Haftung zuerst klären |
| 4 | T3 lief, obwohl die Voraussetzung T1 nicht bestanden war; das Ergebnis gilt nur unter Vorbehalt; Portionen nicht gezählt. | Hinweis | `TESTS.md` T3 | beim nächsten Test Reihenfolge einhalten, Portionen zählen |
| 5 | Die Problem-Hypothesen [A1], [A2], [A6], [A8] sind weiter *Annahme*; [A11] „landet im Müll“ widerspricht I3 (Biogasanlage). | Hinweis | Register, I3 | A11 im nächsten Schritt umformulieren oder als widerlegt prüfen |
| 6 | Alle Interviews mit Mitarbeitenden, keines mit Betroffenen; I2 wurde gepitcht. | Hinweis | `INTERVIEWS.md` Auswertung | Gäste der Tafel/Tagesstätte befragen |

Die Schwellen standen vor den Ergebnissen (Commit 58fa83c); belegte Aussagen stimmen mit dem Wortlaut der Notizen und Ergebnisse überein. Die meisten Felder von `MODEL.md` beruhen auf [A30] und [A29], die beide noch offen sind.

**Achse 2: Wirkung**

| # | Befund | Art | Beleg | Vorschlag |
|---|---|---|---|---|
| 7 | Das Modell dient der Vision („niemand bleibt abends hungrig“), und die Wirkung entsteht bei den Gästen der Einrichtungen [A12] – aber zu den Gästen selbst gibt es keinen Beleg. | Hinweis | Block 1, 2; `PROBLEM.md` | siehe 6 |
| 8 | Trägt es sich? Niemand zahlt belegt; es fehlen die Zahlen zu Kosten (Transport, Verpackung [A37]) und zum Geldbedarf. Ob 5.000 € [A42] reichen würden, kann ich nicht sagen – die Kosten fehlen. | Hinweis | Feld 9, 10; Offene Fragen | Ahmet klärt Kosten (steht schon unter Offene Fragen) |
| 9 | Das Erfolgskriterium „mind. 3 von 4 Einrichtungen machen mit“ (Block 4) ist mit 2 von 4 nicht erfüllt. | Hinweis | Block 4, T3 | Kriterium bei der Anpassung neu entscheiden |
| 10 | Die Tafel holt nur an 2 von 5 Tagen selbst ab [A40]; das Team hat den Rest geliefert. [A32] (ihr schafft das selbst) ist nicht kritisch, trägt aber Aktivitäten und Kosten. | Hinweis | A32, A40 | A32 bei der Anpassung erneut als kritisch erwägen |

Zu den Befunden ein paar Entscheidungen, dann der Weg (zuletzt):

**E1 – Wie geht ihr mit der Widerlegung von [A31] um?** (Was/wo: `MODEL.md` Feld 3, 6; Block 2/3. Warum wichtig: Ohne Einrichtungen keine Wirkung. Einschränkung: Zwei Einrichtungen haben angenommen [A38], eine abgelehnt [A39].)
- (a) *(Empfehlung)* Fokus auf Einrichtungen mit Abendbetrieb wie Tafel und Tagesstätte: neue, engere Annahme mit neuer Schwelle, im nächsten Test geprüft. Folge: kleineres, aber belastbareres Angebot.
- (b) Mehr Einrichtungen suchen und dieselbe Annahme noch einmal testen. Folge: mehr Aufwand, gleiche Frage.
- (c) Die Idee bei den Einrichtungen aufgeben (→ Neu ansetzen).

**E2 – Wer zahlt jetzt?** (Feld 9, Block 7; A5 widerlegt, A29 offen, A42 belegt: Förderung bis 5.000 €, Antrag bis März.)
- (a) *(Empfehlung)* Stiftungsantrag bis März vorbereiten; A29 bleibt kritisch.
- (b) Eine andere Art Einnahme suchen (z. B. Spenden).
- (c) Offen lassen, bis die Kosten bekannt sind.

**E3 – Haftung [A30]?**
- (a) *(Empfehlung)* Zuerst mit dem Studierendenwerk die Haftung klären, bevor weiter geliefert wird.
- (b) Parallel weiter liefern. Folge: T3-Problem wiederholt sich (Ergebnis unter Vorbehalt).

**E4 – Welchen Weg geht ihr?** Weil [A31] und [A5] widerlegt sind, stelle ich „Weiter testen“ nicht zur Wahl – außer ihr erklärt, warum die Widerlegungen nichts ändern.
- **Anpassen** *(Empfehlung)*: Einzelne Annahmen sind widerlegt, aber die Richtung trägt (zwei Einrichtungen haben angenommen, das Studierendenwerk will mitmachen). *Dafür:* ihr baut auf echtem Verhalten auf. *Dagegen:* [A31] war kritisch – wenn auch die engere Annahme fällt, steht die Idee. → danach `/to-model`, dann `/to-tests`.
- **Neu ansetzen (Pivot):** [A31] ist widerlegt, und auf ihr steht die Idee. *Dafür:* ehrlicher, falls Einrichtungen grundsätzlich wenig Interesse haben. *Dagegen:* zwei haben ja angenommen. → danach `/grill-solution` (Lösung, Zielgruppe, wer zahlt) oder `/grill-problem` (das Problem selbst).

**Lena:** E1: a. E2: a. E3: a. Weg: Anpassen – zwei haben ja mitgemacht, die Richtung stimmt. Das Studierendenwerk will mitmachen, nur nicht zahlen.

**Agent:** *(schreibt `DECISIONS.md` (Weg und Entscheidungen), Canvas Block 11 und Block 8, `SIGNALS.md` (Quelle Review); `MODEL.md` bleibt unverändert – `md5sum -c` bestätigt; führt `check_project.py` aus: keine FEHLER, *widerlegt* OFFEN A31, A5)*

Eingetragen. `MODEL.md` habe ich bewusst nicht geändert – das macht `/to-model` im nächsten Schritt. Soll ich committen? Danach empfehle ich `/model-retro` (was ihr aus dieser Runde fürs Vorgehen lernt), dann `/to-model` und `/to-tests`, wie es zum Weg „Anpassen“ gehört.

**Lena:** Ja, committen. Die Retro lassen wir erstmal weg.

**Agent:** *(git commit „Review nach T1–T4: Anpassen (/review-model)“ → 0554cfb)* Ok. Dann als Nächstes `/to-model`.

`[Runner-Notiz]` Die Abgrenzung „Anpassen“ vs. „Neu ansetzen“ ist für A31 schwierig: A31 war **kritisch** (die Idee steht auf ihr), und genau das definiert der Skill als Pivot-Fall. Der Agent hat beide Wege mit dafür/dagegen gezeigt und „Anpassen“ empfohlen, weil eine engere Annahme durch [A38] gestützt ist – das ist Ermessen, das der Skill nicht anleitet. Zu Befund 5 (A11 durch I3 fraglich) fehlt ein Weg im Gesamtprozess, eine Annahme umzuformulieren.

---

## Abschluss

Commits (Autor Lena <lena@example.org>):

```
0554cfb Review nach T1–T4: Anpassen (/review-model)
ab2730b Testergebnisse T1–T4 ausgewertet (/log-evidence)
58fa83c Testkarten T1–T4 vor dem Testen (/to-tests)
c93e6b1 Geschäftsmodell (/to-model)
a03a52e Lösung geschärft (/grill-solution)
a9f5385 Interviews I1–I4 ausgewertet (/log-evidence)
7551473 Problem geschärft (/grill-problem)
75a9c9a Projekt angelegt (/setup-model)
f9779b9 leerer Projektordner
```

Letzter Lauf von `check_project.py` (Exit-Code 0):

```
OK      verweise      alle Verweise stehen im Register
OK      status        42 Einträge mit gültigem Status und Quelle
OK      kritische     2 offene kritische Annahmen haben eine Testkarte mit Schwelle
OK      schwellen     4 Testkarten geprüft
OK      eine-annahme  jede Karte prüft eine Annahme
OK      ergebnisse    alle Ergebnisse ausgewertet, keine Karte überfällig
OFFEN   widerlegt     widerlegte Annahmen in MODEL.md: A31, A5 – prüfen, ob das Feld noch darauf aufbaut
OK      interviews    4 von mindestens 3 Interviews ausgewertet (4 notiert)
```
