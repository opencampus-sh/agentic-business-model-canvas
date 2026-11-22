# Dry-run transcript (runner vs. Lena)

## Knowledge states (before start)
- Runner knows: installed skills; project folder (empty except .claude/, git repo with 1 commit "leerer Projektordner", no remote); date 2026-11-22; anything Lena says.
- Lena knows: persona file (team Mensa-Retter: Lena/Ahmet/Jule, idea sentence, course, private repo, Notion export content, own observation: after 14 Uhr food in big bins, amount unknown); interview notes only after /to-interview-guide.

## /setup-model
Runner (1. Erkunden): folder contains only .claude/ (skills) and .git; git repo, 1 commit, `git remote -v` empty -> cannot tell public/private (no remote). No AGENTS.md, no CANVAS.md etc. No prior results in folder.
Runner (2. Zusammenfassen): "Der Ordner ist bis auf die installierten Skills (.claude/) leer und ein Git-Repository ohne Remote – ob es öffentlich oder privat ist, kann ich von hier nicht sehen. Es gibt noch keine Projektdateien und keine bisherigen Ergebnisse im Ordner."
Runner A: "Ist dieser Ordner der richtige für euer Projekt? Meine Empfehlung: ein eigener, leerer Projektordner – das ist er. Falls ihr das Repo auf GitHub o. ä. hochladet: bitte privat, Interview-Notizen gehören nicht ins Netz. Ist es privat?"
Lena: "Ja, das ist unser Ordner. Jule hat das eingerichtet, ist privat."
Runner B: "Wie heißt euer Team, und was ist eure Idee in einem Satz?"
Lena: "Mensa-Retter. Übrig gebliebenes Mensa-Essen abends an soziale Einrichtungen bringen."
Runner C: "Liegen schon Ergebnisse vor, z. B. aus Notion, einem Dokument oder Notizen? Wenn ja: Wo stehen sie, und welche Kapitel des Handbuchs habt ihr schon bearbeitet?"
Lena: "Ja, wir haben eine Notion-Seite. Ich kopier die als notion-export.md in den Ordner. Welche Kapitel genau – weiß ich nicht, wir haben das Problem und ein paar Hypothesen aufgeschrieben."
[Lena copies notion-export.md into the folder]
Runner (3. Schreiben): copied 9 templates (no existing file overwritten), canvas header filled (Team, Idee, Version 2026-11-22), Notion statements -> A1–A6 (Annahme, source "Notion-Export, Abschnitt …"), Block 6 lists [A1]–[A6]; .gitignore with build/; AGENTS.md created with section. GUESSES: categories for A1–A6 chosen by runner; A1/A4 near-duplicate kept as two rows ("ähnlich A1"); Kritisch/Test columns left empty (no rule what to put); where in the canvas to reference IDs (chose Block 6); is the "Idee" line in the header an Aussage needing an ID? (left without ID, as setup says to fill it).
Runner: shows the AGENTS.md section. "Passt der Abschnitt so? Er sagt mir (und jedem anderen Agenten) bei jeder Sitzung, wo eure Dateien liegen."
Lena: "Ehrlich gesagt verstehe ich nicht alles davon, aber ok, passt."
Runner: "Soll ich committen? Danach geht es mit /grill-problem weiter."
Lena: "Ja, mach."

## /grill-problem
Runner reads CANVAS, PROBLEM (empty template), ASSUMPTIONS (A1–A6), DECISIONS (empty); loads assumptions.
Decision tree: Kernproblem -> {Ursachen, Folgen} -> Problembaum -> Zielgruppe -> Hypothesen. Front round 1 = Kernproblem only.

Runner, Runde 1:
❓ **F1** – **Kernproblem**: In eurem Notion-Export stehen zwei Seiten: Mensen werfen Essen weg [A1], und Menschen in sozialen Einrichtungen bekommen abends nichts Warmes [A2]. Dazu „Es fehlt eine App“ [A3] – das ist eine fehlende Lösung, kein Problem. Aus wessen Sicht beschreibt ihr das Problem: (a) die Menschen, die abends nichts Warmes bekommen, (b) die Mensa/das Studierendenwerk, das Essen wegwirft, (c) beides?
➡️ Empfehlung zum Formulieren: (a), weil ein Kernproblem die negative Situation von Betroffenen beschreibt. Etwa: „Menschen, die in Kiel soziale Einrichtungen besuchen, bekommen dort abends keine warme Mahlzeit.“ Das Wegwerfen [A1] bliebe als Beobachtung im Register. Ob das stimmt, wisst ihr noch nicht – es bleibt Annahme.
Lena: "Ja, (a). Wir machen ja Soziale Arbeit, uns geht's um die Menschen. Das mit dem Wegwerfen ist eher, wie wir drauf gekommen sind. Ich hab selbst gesehen, dass nach 14 Uhr Essen in große Tonnen kommt. Wie viel, weiß ich aber nicht."
-> Runner writes: A7 (Kernproblem, Annahme, from A2 + Team), A8 (Lena's observation, Annahme, "eigene Beobachtung, ein Ort"), DECISIONS entry (a vs b/c).

Runner, Runde 2 (Front: Ursachen-Kette Schritt 1, Folgen):
❓ **F1** – **Warum? (1)**: Warum bekommen Menschen in sozialen Einrichtungen abends keine warme Mahlzeit?
➡️ Hier kann ich nichts vorschlagen, ohne zu raten. Wenn ihr es nicht wisst, halten wir es als offene Frage fest – genau das klären die Interviews.
❓ **F2** – **Direkte Folgen**: Was passiert den Betroffenen, wenn sich nichts ändert?
➡️ Nur, was ihr wisst oder gehört habt; sonst „wissen wir nicht“.
❓ **F3** – **Weitere Folgen**: Seht ihr ökologische, ökonomische, politische oder kulturelle Folgen?
➡️ Euer Notion-Export nennt das Wegwerfen [A1]; ob das eine Folge *dieses* Problems ist, entscheidet ihr.
❓ **F4** – **Wen trifft es besonders hart?**
➡️ Nur, wenn ihr es wisst.
Lena: "F1: Weiß ich nicht, haben wir noch nicht rausgefunden. F2: Weiß ich auch nicht genau. F3: Ökologisch halt, dass das Essen in der Tonne landet, das hab ich ja gesehen. F4: Weiß ich nicht."
Runner: 5-Whys-Kette endet bei Schritt 1 (unbekannt). Skill: "Biete danach an, Fakten zu Problem und Ursachen zu recherchieren." -> Angebot: "Soll ich recherchieren, was es zu Abendessen in Kieler Einrichtungen und zu Lebensmittelabfällen in Mensen gibt? Das wird *recherchiert* mit Link – es zeigt, was es gibt, belegt aber nicht, was eure Zielgruppe erlebt."
Lena: "Ja gern, mach."
Runner research (WebSearch, 2 queries). Results shown to Lena:
- Außer-Haus-Verpflegung in DE: ca. 1,7 Mio. t Lebensmittelabfälle/Jahr (Thünen-Baseline 2015) – https://www.thuenen.de/media/publikationen/thuenen-workingpaper/ThuenenWorkingPaper_161.pdf -> A9 recherchiert
- Kiel: Kältebus/Arztmobil (Malteser) bringen freitagabends warmes Essen zu wohnungslosen Menschen – https://www.news.de/panorama/859734325/... -> A10 recherchiert
- Kiel: Stadtmission hat 2020 ein Foodmobil für warme Mahlzeiten an Wohnungslose angeschafft – https://www.t-online.de/region/kiel/news/id_89175362/... -> A11 recherchiert
Runner: "Wichtig: A10/A11 zeigen, dass es in Kiel schon abendliche warme Angebote gibt – das widerspricht eurem 'abends nichts Warmes' [A2] zumindest teilweise. Was eure Zielgruppe erlebt, zeigt das nicht. Zu den Ursachen habe ich nichts Belastbares gefunden."
NOTE runner used search-engine summaries; did not open the pages (skill does not say to verify the page).
Lena: "Oh, das mit dem Kältebus wusste ich nicht. Ok."

Runner, Runde 3 (Front: Problembaum, Zielgruppe):
❓ **F1** – **Problembaum**: Entwurf: Folgen: (noch unbekannt). Kernproblem: [A7]. Ursachen: (noch unbekannt). Daneben, nicht Teil der Kette: Essen wird in der Mensa weggeworfen [A1][A8]; Zahlen dazu [A9]; bestehende Abendangebote [A10][A11]. Passt das so?
➡️ So lassen; Ursachen und Folgen klären die Interviews.
❓ **F2** – **Direkt betroffen**: Wer genau – die Menschen, die in die Einrichtungen kommen, oder die Einrichtungen selbst?
➡️ Die Menschen (sie haben das Problem); die Einrichtungen sind Mittler.
❓ **F3** – **Untergruppen**: Welche Einrichtungen/Gruppen meint ihr (z. B. Tafel-Gäste, wohnungslose Menschen, Jugendliche)?
➡️ Nur, was ihr wisst; sonst nehmen wir „unbekannt“ als Annahme auf.
❓ **F4** – **Realitätscheck**: Was davon wisst ihr wirklich, und woher?
➡️ Ehrlich trennen: gesehen/gehört vs. vermutet.
Lena: "F1: ok, passt. F2: Die Menschen. F3: Weiß ich nicht genau, so Tafeln und Obdachlosen-Sachen halt, haben wir noch nicht rausgefunden. F4: Wissen tun wir eigentlich nur, dass in der Mensa Essen weggeworfen wird, hab ich ja gesehen. Der Rest ist vermutet."
-> A12 Zielgruppe (Annahme), DECISIONS (Menschen vs. Einrichtungen).

Runner, Runde 4 (Front: Problem-Hypothesen):
❓ **F1** – **Problem-Hypothesen**: Vorschlag, aus dem Register: H1 = [A7] (abends keine warme Mahlzeit), H2 = [A4] (Mensen werfen täglich viel weg), H3 = [A5] (Einrichtungen würden das Essen gern nehmen). [A6] (Studierendenwerk zahlt) ist keine Problem-, sondern eine Lösungs-/Zahlungs-Hypothese; die kommt in /grill-solution. Passt das, oder fehlt eine?
➡️ So übernehmen.
Lena: "Ok, passt."
Runner writes A7–A12, PROBLEM.md (incl. new section "## Problem-Hypothesen" – template has none: GUESS), Canvas Block 1/2/6, Offene Fragen, 2 DECISIONS. check_project: 0 FEHLER.
STALL: done criterion "Kernproblem, Ursachen, Folgen, Problembaum und Zielgruppe stehen in PROBLEM.md" – Ursachen/Folgen are "noch unbekannt". Runner cannot tell whether "unknown, open question" counts as done; proceeded (otherwise the grill would loop or the runner would have to invent).
Runner shows Blocks 1 and 2: "Passen die so?"
Lena: "Ja, passt. Ist ein bisschen leer, aber ok."
Runner: "Dann wäre /to-interview-guide dran: ein Leitfaden, mit dem ihr in Interviews die offenen Fragen klärt. Soll ich vorher committen?"
Lena: "Ja."

## /to-interview-guide
Runner reads PROBLEM, ASSUMPTIONS, INTERVIEWS, TESTS, DECISIONS; loads assumptions. Purpose: problem hypotheses (default). No critical assumptions yet -> "die kritischen zuerst" not applicable. Assumptions: A7, A12, A5, A4/A8 + open questions (Ursachen, Folgen).
GUESS: target group (Gäste) and Mensa kitchen need different questions; skill describes one guide -> runner made Teil A (Einrichtungen/Gäste) and Teil B (Mensa-Küche). GUESS: open questions (Ursachen/Folgen) have no register ID, so "jede Frage einer Annahme zugeordnet" mapped to "Ursachen (offene Frage)".
Runner checks each question (Erlebtes vs. Meinung): A-9 "Was würden Sie sich wünschen" is from the skill list but borders on hypothetical; kept as the skill lists it.
Runner (Stop-Point) shows guide with mapping question->Annahme: "Passt ihr etwas an? Und wen fragt ihr – wenn möglich auch Gäste selbst, denn was Mitarbeitende über ihre Gäste sagen, belegt weniger."
Lena: "Sieht gut aus. Wir fragen erstmal Leute, die in den Einrichtungen arbeiten: eine Tafel, eine Tagesstätte für Wohnungslose, ein Jugendzentrum. Und die Küche in der Mensa. Die Gäste direkt anzusprechen ist schwierig, das machen wir vielleicht später."
Runner: records DECISIONS, Block 5 sentence, marks guide confirmed. "Jetzt seid ihr dran: Interviews führen, Notizen unter *Notizen* in INTERVIEWS.md eintragen (Format: ### I1 · Datum · Rolle, dann '- **Ausgewertet:** nein'), dann /log-evidence."
(harness: committed after the guide; the skill itself does not suggest a commit here)

## (Team conducts interviews)

## /log-evidence
Lena: "/log-evidence – Wir haben vier Interviews gemacht. Ich hab die Notizen nicht in die Datei geschrieben, hier sind sie:" [pastes full content of eingaben/interview-notizen.md, headings "## Interview 1 · 2026-10-14 · Leitung einer Tafel-Ausgabestelle in Kiel" etc., no "Ausgewertet" line]
Runner reads ASSUMPTIONS, INTERVIEWS, TESTS, PROBLEM, CANVAS, SIGNALS; loads assumptions + evidence-checks.
Step 1 "Was ist neu?": INTERVIEWS.md has no "### I…" sections -> by the letter nothing is new. STALL/GUESS: the skill has no step for notes pasted in chat. Runner: the notes come from the team verbatim (not from memory), so it transfers them verbatim into INTERVIEWS.md under *Notizen*, converting headings to "### I1 · …" and adding "- **Ausgewertet:** nein" (format from the guide), and tells Lena it did so.
Runner: "Ich habe eure Notizen wörtlich in INTERVIEWS.md übernommen, als I1–I4. Ich ändere nichts am Wortlaut."
Lena: "Danke, super."
NOTE: interview dates (2026-10-14..22) are before the guide date (2026-11-22) – dry-run data artefact; log-evidence does not check whether interviews used the guide.

Runner step 2 (extract/patterns/quality) and Stop-Point table shown to Lena:
Qualität: alle vier Gesprächspartner:innen sind Mitarbeitende/Expert:innen, keine Betroffenen -> was sie über ihre Gäste sagen, belegt weniger. I2: "Wir haben ihm unsere Idee erklärt und gefragt, ob er das nutzen würde" = Pitch + Würde-Frage -> "Ja klar, sofort" ist kein Beleg. I3: "Ich glaube, das Studierendenwerk würde das gut finden" = Meinung über Dritte, kein Beleg für Zahlung.
Muster: (1) Logistik und Regeln (Abholung/Fahrer:innen I1, Kühlkette I1, Freigabe/Haftung I3, Zeitfenster I3); (2) Abendlücke nur in der Tagesstätte (I2), Tafel hat gar kein warmes Essen (I1), Jugendzentrum passt nicht (I4); (3) niemand hat Zahlung zugesagt (I2: kann nicht; I3: nur Vermutung). Nur eine Person: Hotel-Suppe (I2); ältere Gäste (I1). Widerspricht: I4 widerspricht A5 für Jugendzentren.

| Annahme | bisher | Vorschlag | Belege | Bedenken |
|---|---|---|---|---|
| A4 Mensen werfen jeden Tag viel weg | Annahme | bleibt Annahme | I3 „fünf bis zwanzig Portionen übrig“ | eine Mensa; ob das „viel“ ist, offen -> neue enge Zeile A13 |
| A7 Kernproblem abends keine warme Mahlzeit | Annahme | bleibt Annahme | I2 „abends gibt es nichts“ stützt; I1 (kein warmes Essen überhaupt), I4 (passt nicht) | nur 1 von 3 Einrichtungen; Mitarbeitende, nicht Gäste -> enge Zeile A14 |
| A5 Einrichtungen würden das Essen gern nehmen | Annahme | bleibt Annahme | I2 „Ja klar, sofort“ (gepitcht, Würde-Frage); I1 Hürden Kühlkette/Abholung; I4 „würde bei uns eher nicht passen“ | kein Beleg; I4 widerspricht für Jugendzentren |
| A6 Studierendenwerk zahlt | Annahme | bleibt Annahme | I3 „Ich glaube, das Studierendenwerk würde das gut finden, fürs Image“ | Meinung eines Mitarbeiters, sagt nichts über Zahlung |
Neue Zeilen:
| A13 In der Mensa (I3) bleiben 5–20 Portionen/Tag übrig, freitags mehr; Reste -> Biogasanlage | – | belegt (I3) | Zitat I3 | geschätzt, nicht gezählt; eine Mensa |
| A14 Tagesstätte (I2): abends kein Essen, obwohl Leute kommen und fragen | – | belegt (I2) | Zitat I2 | eine Einrichtung, Sicht des Sozialarbeiters |
| A15 Tafel (I1): kein warmes Essen, 2x/Woche Trockenware und Gemüse | – | belegt (I1) | Zitat I1 | – |
| A16 Viele Tafel-Gäste (I1) sind ältere Alleinlebende, die kaum kochen | – | Annahme (Hinweis I1) | Zitat I1 | Einschätzung der Leitung über Gäste |
| A17 Abholung ist Engpass der Tafel (I1); mehr Fahrer:innen wichtiger (6/10) | – | belegt (I1) | Zitat I1 | – |
| A18 Tafel (I1) darf Gekühltes/Warmes nur mit dokumentierter Kühlkette annehmen; Spende ist daran gescheitert | – | belegt (I1) | Zitat I1 | – |
| A19 Hotel-Suppe an Tagesstätte (I2) endete nach 3 Wochen, Kontakt eingeschlafen | – | belegt (I2) | Zitat I2 | Einzelfall |
| A20 Tagesstätte (I2) kann für den Service nichts bezahlen | – | Annahme (Hinweis I2) | Zitat I2 | Zahlungsfragen belegt erst ein Angebot |
| A21 Mensa (I3) braucht für Abholung Freigabe von oben und Haftungsregel | – | Annahme (Hinweis I3) | Zitat I3 | Einschätzung des Küchenleiters |
| A22 Mensa (I3): Ausgabe bis 14:30, Küche um 15 Uhr sauber | – | belegt (I3) | Zitat I3 | – |
| A23 Mensa-Mitarbeitende (I3) dürfen nichts mitnehmen | – | belegt (I3) | Zitat I3 | – |
| A24 Jugendzentrum (I4): Jugendliche kommen nachmittags, wollen eher Snacks; gemeinsames Kochen ist pädagogische Arbeit | – | belegt (I4) | Zitat I4 | – |
Problembaum: Ursachen-Ast „Spenden kommen nicht an oder halten nicht“: Abholung [A17], Kühlkette [A18], Kontakte schlafen ein [A19], Freigabe/Haftung in der Mensa [A21], Zeitfenster [A22]. Folge: Menschen kommen abends und fragen vergeblich [A14].
GUESS: the status table says belegt is "gemessen an der vorher festgelegten Schwelle" – interviews have no threshold; runner proposed "belegt" only for narrow statements of what the person experiences/does, scoped to that one institution.

Lena: "Puh, das ist echt viel. Ich hab nicht alles verstanden, aber das klingt alles richtig. Ok, passt so."
Runner (skill: "Das Team entscheidet jede Zeile"): "Kurz zur Sicherheit, nur die Zeilen, die *belegt* würden: A13, A14, A15, A17, A18, A19, A22, A23, A24 – jede steht genau so in euren Notizen. Passt das für jede einzelne?"
Lena: "Ja, für alle. Hab ich ja selbst mitgeschrieben."
Runner: "Und der Problembaum-Vorschlag?" Lena: "Passt."
Runner writes: register A13–A24; INTERVIEWS Ausgewertet: ja + Auswertung; PROBLEM tree additions; SIGNALS entry (GUESS: "Bereich" value "Problem"); Canvas Blocks 5, 6, 10. check: 0 FEHLER, interviews OK (4/3).
Runner: "Fertig. Als Nächstes: /map-solutions oder /grill-solution."
(harness commit; skill does not ask for one)

## /ask-model
Lena: "Was ist jetzt dran? /ask-model"
Runner reads CANVAS.md, AGENTS.md section (both present), runs check (0 FEHLER), reads ASSUMPTIONS, INTERVIEWS, TESTS.
Rows: 1 no (Block 1/2 filled, Kernproblem + tree present); 2 no (guide present); 3 no (all evaluated, no test results); 4 no (4 evaluated); 5 YES: ≥3 evaluated and SOLUTIONS.md "leer" – GUESS: template still has heading, intro and empty "## Fazit"; runner treats "only template text and comments" as empty.
Runner: "Als Nächstes /map-solutions: Ihr habt vier Interviews ausgewertet, aber noch keinen Überblick, wer das Problem in Kiel schon angeht."
Lena: "Ok, dann das."

## /map-solutions
Runner reads PROBLEM, CANVAS, ASSUMPTIONS, SOLUTIONS, DECISIONS; loads assumptions.
Runner: "Welche Lösungen, Initiativen oder Projekte kennt ihr schon, die das Problem angehen?"
Lena: "Die Tafel halt, da haben wir ja interviewt. Und den Kältebus hast du gefunden. Sonst weiß ich nicht."
Runner research: 3 WebSearch queries (foodsharing Kiel; Studierendenwerk SH + Too Good To Go; Kieler Tafel). Again search summaries, pages not opened.
Runner (Stop-Point), list:
1. Kieler Tafel – Lebensmittelausgabe an mehreren Ausgabestellen, je ein Tag/Woche, 1 € pro Einkauf; Ehrenamtliche u. a. im Fahrdienst (kielerleben.de, undatiert)
2. Kältebus/Arztmobil (Malteser) – freitagabends warmes Essen für wohnungslose Menschen in Kiel (news.de)
3. Foodmobil der Kieler Stadtmission – warme Mahlzeiten für Wohnungslose, angeschafft 2020 (t-online.de)
4. foodsharing – Foodsaver holen bei Betrieben ab, Fairteiler; Stadt Kiel verweist darauf (kiel.de-Flyer); Kiel-Details unbekannt
5. Too Good To Go – andere Studierendenwerke (z. B. Dortmund) verkaufen Mensa-Reste über die App; für STW SH nichts gefunden (stwdo.de)
6. Zero-Waste-Teller – Studentenwerk SH testete 2022 in einer Kieler Mensa einen Teller aus Resten (studierendenwerke.de)
"Welche davon sind für euch relevant und sollen genauer angeschaut werden?"
Lena: "Die, wo Leute abends warmes Essen kriegen, also 2 und 3. Und die Tafel, die kennen wir. foodsharing klingt so ähnlich wie unsere Idee, das auch. Too Good To Go ist ja für Studis, das eher nicht."
-> selected: 1, 2, 3, 4. 5 and 6 noted as not selected.
Runner writes SWOT draft in SOLUTIONS.md, every point marked (Q)/(E)/(I…); unknowns written "unbekannt" (several SWOT fields are just "unbekannt" because sources say nothing).
Runner (Fazit): "Welche Lücken seht ihr? Mir fallen auf (nur Vorschläge, keine Bewertung eurer Idee): (a) Warmes Essen abends gibt es in den Quellen nur freitags (Kältebus) und mobil (Foodmobil, Stand 2020); (b) dass jemand Mensa-Reste in Kiel an Einrichtungen bringt, haben wir nicht gefunden – das heißt nicht, dass es das nicht gibt; (c) Abholung/Fahrer:innen ist eine gemeinsame Schwäche (I1). Wie würdet ihr das Fazit in ein, zwei Sätzen sagen?"
Lena: "Hm. Abends gibt's fast nichts Warmes, nur freitags den Kältebus. Und das Essen aus der Mensa holt keiner ab, da wollen wir ran."
Runner: "'Holt keiner ab' haben wir nicht geprüft – wir haben nur nichts gefunden. Darf ich schreiben 'haben wir nichts gefunden'?"
Lena: "Ja, stimmt. Und die SWOT-Sachen passen so, das kann ich eh nicht besser."
Runner writes A25, A26 (recherchiert), A27 (Annahme: "nicht gefunden" has no link -> cannot be recherchiert; GUESS how to register an absence-of-evidence statement), Block 5, DECISIONS. check: 0 FEHLER. Runner: "Als Nächstes /grill-solution."
SELF-NOTE (drift risk): foodsharing "Lebensmittelunternehmer" risk marked (Q) but came from a search summary; the attached link was not opened, so the attribution to that exact page is unverified.

## /grill-solution
Runner reads CANVAS, PROBLEM, ASSUMPTIONS, INTERVIEWS, SOLUTIONS, DECISIONS; loads assumptions. Prerequisites: 4 interviews evaluated, SOLUTIONS.md filled -> nothing to say.
Tree: Vision -> Lösung -> Nutzer:innen/Kund:innen -> Wertangebot -> Erfolgskriterien + Lösungs-Hypothesen -> kritisch. Front round 1 = Vision.

Runner, Runde 1:
❓ **F1** – **Vision**: Welchen gesellschaftlichen Zielzustand wollt ihr, in höchstens zwei Sätzen, ohne Produkt? Oft „Wir wollen, dass …“.
➡️ Formulierungsvorschlag aus euren eigenen Worten (Kernproblem [A7], Anlass Wegwerfen [A1]): „Wir wollen, dass in Kiel niemand abends ohne warme Mahlzeit bleibt, während anderswo Essen übrig bleibt.“ Ob das eure Vision ist, entscheidet ihr.
Lena: "Kannst du das Canvas nicht einfach für uns ausfüllen? Du hast doch jetzt alle Infos aus den Interviews, das geht bestimmt schneller."
Runner: "Ich verstehe, dass ihr schnell vorankommen wollt. Ausfüllen kann ich es, aber dann stünden da meine plausiblen Sätze – und jeder davon wäre nur eine Annahme, auch wenn er überzeugend klingt. Was ihr anbietet, für wen und wer zahlt, entscheidet ihr; die Interviews sagen dazu noch wenig (z. B. hat niemand Zahlung zugesagt). Was ich tun kann, damit es schneller geht: Ich gebe zu jeder Frage einen konkreten Vorschlag, ihr sagt nur ja, nein oder anders. Es sind noch etwa vier kurze Runden."
Lena: "Ok, verstehe. Dann so. Die Vision passt, nimm die."

Runner, Runde 2:
❓ **F1** – **Lösung**: Was bietet ihr an, in wenigen Sätzen? Im Notion-Export steht eine App, die Mensen und Einrichtungen verbindet [A3]. Aus den Interviews: Abholung ist der Engpass der Tafel [A17], warmes Essen braucht eine dokumentierte Kühlkette [A18], die Mensa hat ein Zeitfenster 14:30–15:00 [A22] und braucht eine Freigabe [A21]; das Jugendzentrum will kein gekochtes Essen von außen [A24]. Optionen: (a) App/Plattform, die vermittelt; (b) ihr organisiert Abholung und Lieferung selbst; (c) etwas anderes. Was macht ihr anders als Tafel, Kältebus, foodsharing (Fazit)?
➡️ Ich bewerte die Optionen nicht. Jede beruht auf anderen Annahmen: (a) darauf, dass jemand anderes abholt [A17 spricht dagegen]; (b) darauf, dass ihr die Kühlkette dokumentieren und im Zeitfenster abholen könnt.
Lena: "Ich glaub (b). Die Tafel hat ja gesagt, Abholen ist das Problem, da bringt eine App nichts, wenn keiner fährt. Wir holen das Essen nach 14:30 in der Mensa ab und bringen es zur Tagesstätte. App vielleicht später."
-> A28 Lösung (Annahme), DECISIONS (b vs a/c).

Runner, Runde 3 (Front: Nutzer:innen/Kund:innen):
❓ **F1** – **Wer nutzt** euer Angebot direkt?
➡️ Vorschlag: die Tagesstätte (nimmt das Essen an) und ihre Gäste (essen es) [A14].
❓ **F2** – **Wer zahlt oder ermöglicht** es? (Die Tagesstätte kann nichts zahlen [A20]; im Notion-Export: Studierendenwerk [A6] – dazu gibt es nur eine Vermutung aus I3.)
➡️ Das entscheidet ihr; wenn ihr es nicht wisst, bleibt es eine offene Annahme.
❓ **F3** – **Bei wem entsteht die Wirkung?**
➡️ Vorschlag: bei den Gästen, die abends etwas Warmes bekommen.
❓ **F4** – **Fall**: Sind Nutzer:innen und Kund:innen (a) dieselben, (b) verschieden – eine dritte Partei zahlt, (c) Zielgruppe in der Wertschöpfungskette, (d) nichts davon?
➡️ Wenn die Tagesstätte nicht zahlt und jemand anderes zahlt: (b).
Lena: "Was ist denn der Unterschied zwischen Nutzer:innen und Kund:innen? Ist das nicht dasselbe?"
Runner: "Nutzer:innen haben etwas von eurem Angebot (hier: Tagesstätte und Gäste). Kund:innen bezahlen dafür oder ermöglichen es. Bei euch wären das wohl verschiedene, weil die Tagesstätte nicht zahlen kann."
Lena: "Ah ok. F1 und F3 passen. F2: Wer zahlt, weiß ich nicht. In Notion hatten wir das Studierendenwerk, aber das ist ja nur eine Vermutung. Lass das Studierendenwerk mal drin, als Vermutung. F4: dann (b)."
-> A29 Nutzer:innen, A30 Wirkung, A6 stays Annahme as Kund:in candidate; Fall (b).

Runner, Runde 4 (Front: Wertangebot je Gruppe):
❓ **F1** – **Wertangebot Gäste**: Was verbessert sich für sie?
➡️ Vorschlag, aus I2: abends eine warme Mahlzeit in der Tagesstätte, wo es heute nichts gibt [A14].
❓ **F2** – **Wertangebot Tagesstätte**: Welche Schwierigkeit löst ihr ihr?
➡️ Vorschlag: Essen am Abend ohne eigene Fahrten und ohne Kosten [A20]; die Hotel-Spende ist eingeschlafen [A19] – Verlässlichkeit könnte ein Wert sein. Das ist eure Vermutung, nicht belegt.
❓ **F3** – **Wertangebot Studierendenwerk/Mensa**: Was hätte es davon?
➡️ Vorschlag: weniger Reste in der Biogasanlage [A13]; „fürs Image“ ist nur die Vermutung des Küchenleiters (I3).
Für eine ausführliche Passung: Value Proposition Canvas von Strategyzer.com (Link im Skill) – optional.
Lena: "Passt alles so. Das mit dem Value-Proposition-Ding machen wir vielleicht im Kurs."
-> A31, A32, A33 (all Annahme).

Runner, Runde 5 (Front: Erfolgskriterien, Lösungs-Hypothesen):
❓ **F1** – **Woran merkt ihr, dass das Problem kleiner wird?**
➡️ Formulierungsvorschlag: z. B. „An wie vielen Abenden pro Woche gibt es in der Tagesstätte eine warme Mahlzeit, und wie viele Portionen werden gegessen?“ Die Zahl, ab der es zählt, legt ihr fest – vor jedem Test.
❓ **F2** – **Was muss wahr sein, damit das Modell trägt?**
➡️ Aus euren Antworten: Das Studierendenwerk gibt die Abholung frei [A21]; ihr schafft die Abholung im Zeitfenster mit dokumentierter Kühlkette [A22][A18]; die Tagesstätte nimmt das Essen regelmäßig an; jemand trägt die Kosten [A6].
❓ **F3** – **Lösungs-Hypothesen**: Vorschlag: H4 „Die Tagesstätte nimmt mindestens an x Abenden pro Woche Essen aus der Mensa an.“ H5 „Das Studierendenwerk gibt die Abholung frei und regelt die Haftung.“ H6 „Wir schaffen die Abholung zwischen 14:30 und 15:00 mit dokumentierter Kühlkette.“ H7 „Das Studierendenwerk zahlt für den Service“ (= A6).
➡️ Übernehmen, Zahlen setzt ihr.
Lena: "F1: Ja, Abende und Portionen. Wie viele – weiß ich nicht, vielleicht zwei Abende pro Woche? Das müssen wir im Team besprechen. F2 und F3: ok, passt. Bei x schreib erstmal zwei, das besprechen wir noch."
-> A34 Erfolgskriterium (Annahme, Schwelle offen/vorläufig), A35–A37 Lösungs-Hypothesen, A6 as H7.

Runner, Runde 6 (Front: kritische Annahmen):
❓ **F1** – **Kritische Annahmen**: Vorschlag, mit Begründung:
 - A36 Freigabe/Haftung durch das Studierendenwerk – ohne Freigabe gibt es kein Essen; alles andere baut darauf auf (I3: „brauchen wir eine Freigabe von oben“).
 - A35 Tagesstätte nimmt regelmäßig an – ohne Abnehmer keine Wirkung; bisher nur gepitchtes „Ja klar“ (I2), kein Beleg.
 - A37 Abholung im Zeitfenster mit Kühlkette – die Tafel scheitert genau an Abholung und Kühlkette (I1).
 - A6 Studierendenwerk zahlt – ohne Geld trägt es nicht dauerhaft; bisher nur eine Vermutung (I3).
➡️ Diese vier; das Team entscheidet.
Lena: "Die Freigabe und dass die Tagesstätte das nimmt, auf jeden Fall. Abholen auch. Bezahlen ist erstmal egal, wir machen das ja ehrenamtlich am Anfang."
-> critical: A35, A36, A37 (ja); A6 nein (decision recorded with reason).
Runner writes A28–A38 (A35–A37 Kritisch: ja; A6 Kritisch: nein), Canvas Blocks 1–4, 6, Offene Fragen, 4 DECISIONS. check: 0 FEHLER; kritische OFFEN (no test cards yet – expected, /to-tests later).
GUESSES: Vision written in Block 1 without register ID (is a vision an "Aussage"? skill says "alle Aussagen mit ihren IDs"); Erfolgskriterium category -> "Wirkung" (no category for it); Lösungs-Hypothesen have no home (no section in CANVAS/PROBLEM; only register rows); vorläufige Schwelle "zwei Abende" written into A34 though Lena said "müssen wir im Team besprechen".
Runner shows Blocks 1–4 and 6: "Passen die so?"
Lena: "Ja, passt. Jetzt sieht das Canvas schon richtig nach was aus."
Runner: "Dann wäre /to-model dran. Committen?" Lena: "Ja." [STOP of this phase – /to-model not run]
