# Referenzlauf „Mensa-Retter“ – Transkript

Fiktiver Beispielfall für den Selbstlernkurs. Lena (Studentin der Sozialen Arbeit, Team mit Ahmet und Jule) führt die Skills des Agentic Business Model Canvas in einem leeren, privaten Git-Repository aus. **Agent** = Claude Code, das die Skills liest und befolgt. Fragen des Agenten sind wörtlich wiedergegeben; Dateiinhalte stehen im Git-Verlauf.

**Zeitachse.** Die Commits tragen die Daten der Geschichte (Projektstart 2026-10-05, Interviews 14.–22. Oktober, Tests bis 18. Dezember, Retro am 2026-12-21). Die Schritte 8–13 sind ein zweiter Lauf ab Stand 07 mit den Skills vom 2026-11-23. Der Agent hat jeweils das Datum der Sitzung als „heute“ verwendet. Die gezeigten Ausgaben von `check_project.py` sind mit diesem Sitzungsdatum als „heute“ erzeugt, in den Schritten 8–13 mit dem echten Datum 2026-11-23 (sonst meldet der Check Karten mit *Bis wann* vor dem echten Ausführungsdatum als überfällig).

| Nr. | Datum | Befehl |
|---|---|---|
| 1 | 2026-10-05 | `/setup-model` |
| 2 | 2026-10-05 | `/show-canvas` |
| 3 | 2026-10-07 | `/grill-problem` |
| 4 | 2026-10-09 | `/to-interview-guide` |
| – | 2026-10-22 | Team führt Interviews, Lena trägt Notizen ein |
| 5 | 2026-10-23 | `/log-evidence` |
| 6 | 2026-10-23 | `/ask-model` |
| 7 | 2026-10-26 | `/map-solutions` |
| 8 | 2026-11-24 | `/grill-solution` |
| 9 | 2026-11-26 | `/to-model` |
| 10 | 2026-11-28 | `/to-tests` |
| – | bis 2026-12-18 | Team testet |
| 11 | 2026-12-19 | `/log-evidence` |
| 12 | 2026-12-20 | `/review-model` |
| 13 | 2026-12-21 | `/model-retro` |

---

## 1 · `/setup-model` (2026-10-05)

**Lena:** /setup-model

*Agent erkundet: `ls -A` (nur `.claude/` und `.git/`), `git remote -v` (kein Remote), kein `AGENTS.md`, kein `CANVAS.md`, keine weiteren Dateien.*

**Agent:**
> Hallo! Ich habe mir den Ordner angesehen:
>
> - Er ist ein Git-Repository ohne Remote, also bisher nur auf diesem Rechner.
> - Er enthält nur die installierten Skills unter `.claude/skills/` – noch kein Canvas, kein Annahmen-Register, kein `AGENTS.md`.
> - Bisherige Ergebnisse (Notizen, Exporte) liegen hier keine.
>
> Es fehlt also alles, was die anderen Skills lesen. Drei kurze Fragen, eine nach der anderen.
>
> **A. Ort.** Ist dieser Ordner der richtige für euer Projekt? Ich empfehle genau so etwas: einen eigenen, leeren Projektordner. Es gibt kein Remote – wenn ihr ihn später auf GitHub legt, dann bitte als **privates** Repository: Interview-Notizen und Ideen gehören nicht ins Netz.

**Lena:** Ja, der Ordner ist richtig. Jule hat ihn angelegt, der ist privat und noch nicht auf GitHub.

**Agent:**
> Gut, dann bleibt es hier.
>
> **B. Team und Idee.** Wie heißt euer Team (oder wer seid ihr), und was ist eure Idee in einem Satz? Mehr braucht es jetzt nicht – Problem und Lösung schärfen wir später mit `/grill-problem` und `/grill-solution`.

**Lena:** Mensa-Retter. Wir sind Lena, Ahmet und Jule. Idee: Übrig gebliebenes Mensa-Essen abends an soziale Einrichtungen bringen.

**Agent:**
> **C. Bisherige Ergebnisse.** Liegen schon Ergebnisse vor, z. B. aus Notion, einem Dokument oder Notizen? Wenn ja: Wo stehen sie, und welche Kapitel des Handbuchs habt ihr schon bearbeitet?

**Lena:** Ja, wir haben eine Notion-Seite. Ich kopier sie als notion-export.md in den Ordner. Welche Kapitel genau, weiß ich gerade nicht, die Problem-Hypothesen haben wir nach dem Handbuch gemacht.

*Lena legt `notion-export.md` ab. Agent liest sie.*

**Agent:**
> Danke, ich habe die Seite gelesen. Sie hat zwei Teile: *Problem* (zwei Sätze) und *Problem-Hypothesen* (drei Punkte). Daraus werden fünf Zeilen im Annahmen-Register, alle mit Status *Annahme*:
>
> | ID | Aussage | Kategorie (Vorschlag) | Quelle |
> |---|---|---|---|
> | A1 | Mensen werfen jeden Tag viel Essen weg. | Problem | Seite Problem + Problem-Hypothesen (fast gleiche Aussage, eine Zeile, Wortlaut der Hypothese) |
> | A2 | Menschen in sozialen Einrichtungen bekommen abends nichts Warmes. | Problem | Seite Problem |
> | A3 | Es fehlt eine App, die das verbindet. | Lösung | Seite Problem |
> | A4 | Soziale Einrichtungen würden das Essen gern nehmen. | Zielgruppe | Problem-Hypothesen |
> | A5 | Das Studierendenwerk würde für so einen Service bezahlen. | Zahlungsbereitschaft | Problem-Hypothesen |
>
> *Kritisch* und *Test* lasse ich leer, das entscheidet ihr später. Nichts davon ist *belegt* – das geht erst mit euren eigenen Interviews oder Tests (`/log-evidence`).
>
> Ich habe angelegt: `CANVAS.md` (Kopf mit Team, Idee, Version 2026-10-05; in Block 6 die IDs A1–A5), `ASSUMPTIONS.md`, `PROBLEM.md`, `INTERVIEWS.md`, `SOLUTIONS.md`, `MODEL.md`, `TESTS.md`, `DECISIONS.md`, `SIGNALS.md`, eine `.gitignore` mit `build/` und `CLAUDE.md` mit `@AGENTS.md`.
>
> In `AGENTS.md` steht jetzt dieser Abschnitt – hier steht, wo eure Dateien liegen und welche Regeln ich in jeder Sitzung befolge:
>
> ```
> ## Agentic Business Model Canvas
> - Canvas: CANVAS.md (vor jeder Arbeit lesen; aktualisieren, wenn etwas entschieden ist)
> - Annahmen-Register: ASSUMPTIONS.md. Jede Aussage … steht dort mit Status und Quelle …
> - Problem: PROBLEM.md; Interviews: INTERVIEWS.md; bestehende Lösungen: SOLUTIONS.md
> - Geschäftsmodell: MODEL.md …
> - Tests: TESTS.md; Entscheidungen: DECISIONS.md; Signale: SIGNALS.md …
> - Checks: python3 .claude/skills/evidence-checks/scripts/check_project.py
> - Sprache: Deutsch, du
> - Bisherige Ergebnisse: Notion-Export (notion-export.md, Seiten Problem und Problem-Hypothesen)
> ```
>
> Stimmt der Inhalt so – Orte der Dateien, Sprache, und dass der Notion-Export eure bisherige Quelle ist?

**Lena:** ok, passt.

**Agent:**
> Dann ist das Projekt angelegt. Ich schlage vor, jetzt zu committen – mit den installierten Skills unter `.claude/skills/`, damit Ahmet und Jule dieselbe Version nutzen (persönliche Einstellungen wie `.claude/settings.local.json` nicht). Danach geht es mit `/grill-problem` weiter.

**Lena:** Ja, mach.

*Commit `1 · setup-model · Projekt angelegt, Notion-Export ins Register übernommen`.*

**Check (`check_project.py`):** OK verweise, OK status (5 Einträge); OFFEN kritische (noch keine markiert), OFFEN interviews (0 von 3).

---

## 2 · `/show-canvas` (2026-10-05)

**Lena:** /show-canvas

*Agent sucht in `AGENTS.md` die Zeile `- Canvas:` (→ `CANVAS.md`). Eine Zeile `- Language:` gibt es nicht (der Abschnitt sagt `- Sprache: Deutsch, du`), also Standard `de`.*

```
python3 .claude/skills/show-canvas/scripts/render_canvas.py CANVAS.md --lang de --out build/canvas.html
Wrote build/canvas.html
```

**Agent:**
> Die Seite liegt unter `build/canvas.html` – öffne sie im Browser (`build/` steht schon in `.gitignore`; die Seite ist nur eine Ansicht, das Canvas bleibt die Quelle).
>
> Das Wichtigste:
> - **1 von 11 Blöcken ausgefüllt** – nur Block 6 (Annahmen A1–A5 aus dem Notion-Export). Leer sind die 👤-Blöcke 1, 2, 3, 4, 7, 11 („Noch nicht entschieden“) und die 🤖-Blöcke 5, 8, 9, 10 („Noch nicht entworfen“). Als Nächstes füllt `/grill-problem` die Blöcke 1 und 2.
> - Keine Entscheidungen im Log, keine offenen Fragen.

**Lena:** Ah, so sieht das aus. Ok, dann grill-problem.

*Keine Dateiänderung (die Seite liegt im ignorierten `build/`); leerer Commit `2 · show-canvas · …` als Markierung für die Übung.*

---

## 3 · `/grill-problem` (2026-10-07)

**Lena:** /grill-problem

*Agent liest `CANVAS.md`, `PROBLEM.md` (leer), `ASSUMPTIONS.md` (A1–A5), `DECISIONS.md` (leer) und lädt `assumptions`.*

**Agent:**
> Ich frage euch so lange, bis das Problem klar ist – bevor wir über eine Lösung sprechen. Es werden ungefähr fünf Runden, dazu eine kurze Warum-Kette. Was im Notion-Export steht, frage ich nicht noch einmal ab.
>
> **Runde 1 von etwa 5**
>
> ❓ **F1** – **Welches Problem steht im Kern?** Euer Notion-Export nennt zwei: (a) In Mensen wird jeden Tag Essen weggeworfen [A1]; (b) Menschen in sozialen Einrichtungen bekommen abends nichts Warmes [A2]. Der dritte Satz, „Es fehlt eine App, die das verbindet“ [A3], beschreibt eine fehlende Lösung, kein Problem – den heben wir für später auf. Welches von (a) und (b) ist euer Kernproblem, und welches ist eher Anlass oder Rahmen?
>
> ➡️ Ich empfehle (b): Eure Idee setzt bei den Menschen in den Einrichtungen an, und das Kernproblem beschreibt die Lage der Betroffenen. Entscheiden müsst ihr – beides ist möglich, führt aber zu anderen Interviews.
>
> ❓ **F2** – **Rahmen:** Gilt das Problem für Kiel, für Schleswig-Holstein oder allgemein?
>
> ➡️ Kiel – so steht es im Notion-Export, und dort könnt ihr Interviews führen.

**Lena:** F1: b. Das Wegwerfen hat uns auf die Idee gebracht, aber eigentlich geht's um die Leute. F2: Kiel, ja.

*Agent hält beide Entscheidungen in `DECISIONS.md` fest.*

**Agent:**
> Notiert: Kernproblem ist das fehlende warme Abendessen, die Verschwendung ist der Anlass. Rahmen Kiel.
>
> **Runde 2 von etwa 5** (danach noch drei)
>
> ❓ **F3** – **Kernproblem in euren Worten:** Beschreibt in ein bis drei Sätzen, was den Menschen passiert – aus ihrer Sicht, nicht aus Sicht der Mensa und nicht als fehlende App.
>
> ➡️ Hier zuerst eure Worte. Ich helfe danach beim Schärfen, falls nötig.

**Lena:** Menschen, die in Kiel auf soziale Einrichtungen angewiesen sind, bekommen abends oft nichts Warmes zu essen.

**Agent:**
> Das ist präzise und aus Sicht der Betroffenen – ich übernehme es wörtlich als [A6]. Es ersetzt A2 aus dem Notion-Export (A2 bleibt im Register stehen, mit „ersetzt durch A6“).
>
> Jetzt die Warum-Kette: eine Frage pro Nachricht.
>
> **Warum** bekommen Menschen, die auf soziale Einrichtungen angewiesen sind, abends oft nichts Warmes zu essen?

**Lena:** Die Einrichtungen haben abends kein Personal zum Kochen.

**Agent:**
> **Warum** haben die Einrichtungen abends kein Personal zum Kochen?

**Lena:** Weiß ich nicht.

**Agent:**
> Völlig in Ordnung – dann endet die Kette hier. „Warum gibt es abends kein Personal?“ kommt unter *Noch offen* in `PROBLEM.md`; genau das könnt ihr in den Interviews fragen.
>
> **Erkenntnis:** Wo ihr ansetzen könnt, wisst ihr noch nicht – fehlt abends Personal, Geld, eine Küche oder etwas anderes? Das ist die wichtigste offene Frage für die Interviews.
>
> Soll ich ein paar Fakten zu Problem und Ursachen recherchieren? Was ich finde, kommt mit Link als *recherchiert* ins Register – das zeigt, was es gibt, belegt aber kein Bedürfnis eurer Zielgruppe.

**Lena:** Ja, schau mal.

*Agent sucht im Web und öffnet zwei Seiten: Verbraucherzentrale, „Essen außer Haus: Was in Töpfen und auf den Tellern bleibt“ (Stand 03.08.2026), und Destatis, Themenseite Wohnungslosigkeit (Pressemitteilung vom 26.06.2026). Zur Frage, warum Einrichtungen abends kein Personal haben, findet er nichts Belastbares.*

**Agent:**
> Gefunden und auf den Seiten geprüft:
>
> - [A8] *recherchiert*: In der Außer-Haus-Verpflegung (dazu gehören Kantinen und Mensen) werden in Deutschland im Jahr rund 1,9 Mio. Tonnen Lebensmittel als Abfälle entsorgt, etwa 17 % aller Lebensmittelabfälle. (verbraucherzentrale.de)
> - [A9] *recherchiert*: In Gemeinschaftsverpflegung und Gastronomie werden aus Unsicherheit mit Hygieneregeln immer wieder noch verzehrfähige Speisen entsorgt. (dieselbe Seite)
> - [A10] *recherchiert*: Zum Stichtag 31.01.2026 waren in Deutschland rund 452.900 Personen wegen Wohnungslosigkeit untergebracht. (destatis.de)
>
> Zur Ursache „kein Personal am Abend“ habe ich nichts gefunden, was ich als Quelle eintragen würde – sie bleibt eure Annahme [A7]. Und Achtung: Keine dieser Zahlen sagt, dass Kieler Einrichtungen Mensa-Essen brauchen.
>
> **Runde 3 von etwa 5** (danach noch zwei)
>
> ❓ **F4** – **Direkte Folgen:** Was passiert den Menschen, wenn sich nichts ändert – heute Abend, diese Woche?
>
> ➡️ Sagt, was ihr vermutet; alles kommt als *Annahme* ins Register.
>
> ❓ **F5** – **Langfristige und gesellschaftliche Folgen:** Was passiert über Monate? Gibt es ökologische, ökonomische, politische oder kulturelle Folgen?
>
> ➡️ Nennt nur, was ihr wirklich vermutet; „weiß ich nicht“ ist eine gültige Antwort.
>
> ❓ **F6** – **Wen trifft es besonders hart?**
>
> ➡️ Eine Gruppe reicht, wenn ihr nur eine vermutet.

**Lena:** F4: Die gehen hungrig ins Bett oder essen was Kaltes, Billiges. Vermute ich. F5: Langfristig werden die vielleicht eher krank. Ökologisch… das Wegwerfen in der Mensa passiert ja so oder so, das ist keine Folge davon, oder? Politisch und kulturell weiß ich nicht. F6: Wohnungslose, vermute ich. Wer sonst, weiß ich nicht.

**Agent:**
> Genau: Die Verschwendung ist keine Folge eures Kernproblems, sie läuft parallel – sie bleibt als Anlass stehen [A1]. Eingetragen: [A11] hungrig schlafen oder nur Kaltes, Billiges; [A12] langfristig eher krank; [A13] besonders hart trifft es wohnungslose Menschen. Politische und kulturelle Folgen kommen unter *Noch offen*.
>
> **Runde 4 von etwa 5** (danach noch eine)
>
> ❓ **F7** – **Problembaum:** So sieht er jetzt aus. Stimmt das?
>
> ```
> Folgen
> ├── hungrig schlafen oder nur Kaltes, Billiges essen [A11]
> ├── langfristig eher krank [A12]
> └── trifft besonders wohnungslose Menschen [A13]
> Kernproblem: Menschen, die in Kiel auf soziale Einrichtungen angewiesen sind, bekommen abends oft nichts Warmes zu essen. [A6]
> Ursachen
> └── Einrichtungen haben abends kein Personal zum Kochen [A7]
>     └── warum? – noch offen
> ```
>
> ➡️ Bestätigen; die Wurzeln sind dünn, das ist ehrlich und wird nach den Interviews ergänzt.
>
> ❓ **F8** – **Zielgruppe:** Wer ist direkt betroffen, und welche Untergruppen gibt es? Nicht „alle Bedürftigen“, sondern möglichst konkret. Wichtig: Direkt betroffen sind die Menschen, nicht die Einrichtungen.
>
> ➡️ Nennt die Arten von Einrichtungen, an deren Gäste ihr denkt.
>
> ❓ **F9** – **Realitätscheck:** Was davon *wisst* ihr – und woher? Was nehmt ihr nur an?
>
> ➡️ Ehrlich trennen; eine eigene Beobachtung ist wertvoll, aber eine Beobachtung an einem Ort.

**Lena:** F7: ja, passt. F8: Leute in Tagesstätten für Wohnungslose, Leute bei der Tafel, vielleicht Jugendliche im Jugendzentrum. F9: Ich hab in der Mensa gesehen, dass nach 14 Uhr Essen in große Tonnen kommt. Wie viel, weiß ich nicht. Der Rest ist eher vermutet.

**Agent:**
> Eingetragen: [A14] vermutete Untergruppen (Tagesstätten für Wohnungslose, Tafel-Ausgabestellen, Jugendzentren); [A15] deine Beobachtung, als *Annahme* mit Quelle „eigene Beobachtung (Lena), eine Mensa, Menge unbekannt“. Sie ist ein guter Hinweis, aber noch kein Beleg für Kieler Mensen allgemein.
>
> **Runde 5 von 5** (die letzte)
>
> ❓ **F10** – **Problem-Hypothesen:** Welche Aussagen wollt ihr in den Interviews prüfen? Vorschlag aus dem Register:
> - [A6] Menschen, die in Kiel auf soziale Einrichtungen angewiesen sind, bekommen abends oft nichts Warmes.
> - [A7] Die Einrichtungen haben abends kein Personal zum Kochen.
> - [A11] Wer abends nichts Warmes bekommt, geht hungrig schlafen oder isst nur Kaltes, Billiges.
> - [A4] Soziale Einrichtungen würden das Essen gern nehmen.
> - [A1] Mensen werfen jeden Tag viel Essen weg.
>
> ➡️ Diese fünf: Sie decken Kernproblem, Ursache, Folge und beide Seiten (Einrichtungen, Mensa) ab.
>
> ❓ **F11** – **Offene Punkte:** Wer klärt die Punkte unter *Noch offen*, und bis wann?
>
> ➡️ Alle drei, in den Interviews, mit einem Datum.

**Lena:** F10: ok, passt. Und A5 mit dem Bezahlen auch? F11: Wir alle drei, in den Interviews, bis Ende Oktober.

**Agent:**
> A5 würde ich nicht dazunehmen: Ob das Studierendenwerk zahlt, ist keine Aussage über das Problem, und ein Interview kann es nicht belegen – „würden Sie zahlen?“ beantwortet jeder höflich. Das prüft ihr später mit einem Test (`/to-tests`). Einverstanden?

**Lena:** Ah ok, ja.

*Agent schreibt `PROBLEM.md`, Register A6–A15, Blöcke 1, 2 und Offene Fragen im Canvas, drei Einträge in `DECISIONS.md` (Kernproblem, Kiel, Problem-Hypothesen – Letztere als „Vorschlag des Agenten, vom Team übernommen“).*

```
$ python3 .claude/skills/evidence-checks/scripts/check_project.py
OK      verweise      alle Verweise stehen im Register
OK      status        15 Einträge mit gültigem Status und Quelle
OFFEN   kritische     noch keine Annahme als kritisch markiert
OK      schwellen     0 Testkarten geprüft
OK      eine-annahme  jede Karte prüft eine Annahme
OK      ergebnisse    alle Ergebnisse ausgewertet, keine Karte überfällig
OK      widerlegt     keine widerlegte Annahme in MODEL.md
OFFEN   interviews    0 von mindestens 3 Interviews ausgewertet (0 notiert)
```

**Agent:**
> Keine Fehler. Hier die Blöcke 1 und 2, wie sie jetzt im Canvas stehen:
>
> **1. Herausforderung & Vision** – Kernproblem [A6]; Ursache (vermutet) [A7], warum offen; Folgen (vermutet) [A11] [A12]. Vision folgt mit `/grill-solution`.
> **2. Nutzer:innen & Kund:innen** – Betroffen: Menschen, die abends in soziale Einrichtungen in Kiel kommen, vermutet [A14]; besonders hart wohnungslose Menschen [A13]. Nutzer:innen und Kund:innen folgen später.
>
> Passt das so?

**Lena:** Ja.

**Agent:**
> Dann schlage ich vor zu committen. Weiter geht es mit `/to-interview-guide`.

*Commit `3 · grill-problem · Kernproblem, Warum-Kette, Folgen, Zielgruppe und Problem-Hypothesen`.*

---

## 4 · `/to-interview-guide` (2026-10-09)

**Lena:** /to-interview-guide

*Agent liest `PROBLEM.md`, `ASSUMPTIONS.md`, `INTERVIEWS.md` (noch kein Leitfaden), `TESTS.md`, `DECISIONS.md`; lädt `assumptions`. Kein Zusatz beim Befehl → Leitfaden für die Problem-Hypothesen.*

**Agent:**
> Ich bereite einen Leitfaden für eure Problem-Hypothesen vor. Diese Annahmen sollen die Interviews prüfen, die wichtigsten zuerst:
>
> - [A6] Kernproblem: kein warmes Abendessen
> - [A7] Ursache: kein Personal zum Kochen
> - [A11] Folge: hungrig schlafen oder Kaltes essen
> - [A4] Einrichtungen würden das Essen gern nehmen
> - [A1] Mensen werfen jeden Tag viel Essen weg
> - dazu aus *Noch offen*: warum es abends kein Personal gibt, wie viel übrig bleibt, welche Einrichtungen abends überhaupt Gäste haben.
>
> Ihr fragt zwei Gruppen – Einrichtungen und Mensa –, also bekommt jede einen eigenen Teil. Ein Hinweis vorab: Wenn ihr Mitarbeitende der Einrichtungen fragt statt der Gäste selbst, belegt das, was sie über ihre Gäste sagen, weniger als das, was Gäste selbst erzählen würden. Was sie über ihre eigene Einrichtung sagen, zählt voll.
>
> *(Agent zeigt den Entwurf: Ziel, Einstieg, Teil A mit acht Fragen, Teil B mit sechs Fragen, jede mit der Annahme, die sie prüft – Wortlaut wie in `INTERVIEWS.md`. Auszug:)*
>
> | Nr. | Frage | prüft |
> |---|---|---|
> | A-1 | Erzähl mal von einem ganz normalen Abend bei euch: Wer kommt, was passiert? | [A6], offen: wer abends Gäste hat |
> | A-3 | Woran liegt es, dass es abends so ist, wie es ist? Was müsste da sein, damit es anders wäre? | [A7], offen: warum kein Personal |
> | A-7 | Wie wichtig ist das Thema Abendessen für euch, auf einer Skala von 1 bis 10 – und warum? Was wäre euch gerade wichtiger? | [A6] [A4] |
> | B-2 | Wie viel bleibt ungefähr übrig – an welchen Tagen mehr, an welchen weniger? | [A1], offen: Menge |
> | B-5 | Hat schon mal jemand gefragt, ob er übrig gebliebenes Essen bekommen kann? Was ist daraus geworden? | [A1] |
>
> **Nicht fragen:** Stellt eure Idee nicht vor und fragt nicht, ob sie gut ist; keine „Würdet ihr …?“-Fragen. Fragt die Person nach eurer Idee, erzählt erst ganz am Ende davon – und notiert, was sie dann sagt, getrennt als Feedback.
>
> **Notieren:** pro Interview `### I1 · Datum · Rolle`, darunter `- **Ausgewertet:** nein`, möglichst wörtliche Aussagen, keine Namen.
>
> Wollt ihr etwas anpassen? Und: Wen fragt ihr genau?

**Lena:** Frage 7 mit der Skala find ich gut. Können wir bei der Mensa nicht direkt fragen, ob die das Essen abgeben würden? Wir fragen die Tafel, eine Tagesstätte, ein Jugendzentrum und den Küchenleiter in der Mensa. Gäste direkt fragen wir erstmal nicht, das ist uns zu heikel.

**Agent:**
> „Würdet ihr das Essen abgeben?“ ist eine Frage nach der Zukunft – darauf sagen die meisten höflich Ja, und es belegt nichts. Was ihr wirklich wissen wollt, steckt schon in B-4 bis B-6: was sie bisher daran hindert, ob schon mal jemand gefragt hat und wer darüber entscheidet. Die Antworten zeigen viel besser, ob es geht. Lassen wir es so?

**Lena:** Ok, verstehe. Ja, so lassen.

**Agent:**
> Dann steht der Leitfaden in `INTERVIEWS.md` unter *Leitfaden*, jede Frage mit ihrer Annahme. In `DECISIONS.md` steht, wen ihr fragt und warum (Gäste noch nicht), in Block 5 des Canvas ein Satz zum Leitfaden.
>
> Ich schlage vor zu committen. Und jetzt seid ihr dran: Interviews führen, Notizen in `INTERVIEWS.md` unter *Notizen* eintragen (oder später in den Chat einfügen) – danach `/log-evidence`.

*Commit `4 · to-interview-guide · Leitfaden für Einrichtungen und Mensa`.*

---

## Zwischen den Skills: Interviews (14.–22. Oktober)

Das Team führt vier Interviews. Lena trägt die Notizen selbst in `INTERVIEWS.md` ein, im Format des Leitfadens (`### I1 · 2026-10-14 · Leitung einer Tafel-Ausgabestelle in Kiel`, `- **Ausgewertet:** nein`, wörtliche Aussagen). In I2 hat das Team die Idee doch vorgestellt und gefragt, ob die Person sie nutzen würde – so steht es auch in der Notiz.

*Commit `Interviews notiert`.*

---

## 5 · `/log-evidence` (2026-10-23)

**Lena:** /log-evidence

*Agent liest `ASSUMPTIONS.md`, `INTERVIEWS.md`, `TESTS.md`, `PROBLEM.md`, `CANVAS.md`, `SIGNALS.md`; lädt `assumptions` und `evidence-checks`. Neu: I1–I4, alle „Ausgewertet: nein“. Keine Testkarten.*

**Agent:**
> Ich habe vier neue Interviews gefunden: I1 (Tafel-Ausgabestelle), I2 (Tagesstätte), I3 (Mensa-Küchenleiter), I4 (Jugendzentrum). Danke, dass ihr sie so ordentlich eingetragen habt.
>
> Eine Frage vorab: Frage A-3 aus dem Leitfaden („Woran liegt es, dass es abends so ist?“) finde ich in keiner Notiz. Habt ihr sie gestellt?

**Lena:** Weiß ich nicht mehr genau. Steht nicht in den Notizen, dann wohl nicht.

**Agent:**
> Ok – dann bleibt die Ursache „kein Personal“ [A7] ungeprüft, und ich schreibe es als Signal auf.
>
> **Was mir an den Notizen auffällt (Qualität):**
> - Alle vier sind Mitarbeitende, keine Gäste. Was sie über ihre Einrichtung sagen, zählt voll; was sie über ihre Gäste sagen, ist ein Hinweis.
> - In I2 habt ihr die Idee erklärt und gefragt, ob er sie nutzen würde. Sein „Ja klar, sofort, das wäre toll“ ist deshalb Feedback, kein Beleg.
>
> **Muster:**
> - Abends gibt es nichts Warmes – in Tafel und Tagesstätte (I1, I2).
> - Die Hürde ist Logistik, nicht Vermittlung: Abholen, Kühlkette, Fahrer:innen (I1). Eine App hat niemand vermisst.
> - Spenden versanden: Hotel-Suppe nach drei Wochen eingeschlafen (I2), Restaurant-Spende an der Kühlkette gescheitert (I1).
> - Die Mensa hat weniger übrig als gedacht: 5–20 Portionen, und es geht in die Biogasanlage (I3).
> - Nicht jede Einrichtung passt: Das Jugendzentrum will kein gekochtes Essen von außen (I4).
>
> Jetzt die vorgeschlagenen Änderungen, in Abschnitten von höchstens fünf Zeilen, die *belegt*-Vorschläge zuerst. Bei *belegt* brauche ich zu jeder Zeile ein ausdrückliches Ja – ein pauschales „passt“ reicht dafür nicht. Alle Vorschläge sind eng formuliert, auf die befragte Einrichtung bezogen, im Wortlaut der Notiz.
>
> **Abschnitt 1 von 6 – neue Zeilen, vorgeschlagen als *belegt***
>
> | ID | Aussage | bisher | Vorschlag | Beleg | Bedenken |
> |---|---|---|---|---|---|
> | A16 (neu) | In der Tafel-Ausgabestelle aus I1 gibt es gar kein warmes Essen; verteilt werden zweimal pro Woche fast nur Trockenware und Gemüse. | – | belegt | I1: „Warmes Essen haben wir gar nicht.“ | keine |
> | A17 (neu) | Für die Tafel-Ausgabestelle aus I1 ist das Abholen das Problem; sie hat einen Transporter und zwei Ehrenamtliche mit Führerschein. | – | belegt | I1: „Abholen ist unser Problem.“ | keine |
> | A18 (neu) | Die Tafel-Ausgabestelle aus I1 darf gekühltes oder warmes Essen nur annehmen, wenn die Kühlkette dokumentiert ist; daran ist schon eine Restaurant-Spende gescheitert. | – | belegt | I1: „… nur annehmen, wenn die Kühlkette dokumentiert ist.“ | keine |
> | A19 (neu) | Für die Tafel-Ausgabestelle aus I1 ist das Thema eine 6 von 10; wichtiger wären ihr mehr Fahrer:innen. | – | belegt | I1: „Eine 6. Wichtiger wäre uns mehr Fahrer:innen.“ | keine |
> | A20 (neu) | In der Tagesstätte aus I2 gibt es abends nichts zu essen; trotzdem kommen abends Leute und fragen. | – | belegt | I2: „… abends gibt es nichts. Da kommen trotzdem Leute und fragen.“ | gesagt vor dem Pitch, also unbeeinflusst |
>
> Welche davon setze ich auf *belegt*?

**Lena:** A16 ja, A17 ja, A18 ja, A19 ja, A20 ja.

**Agent:**
> **Abschnitt 2 von 6 – neue Zeilen, vorgeschlagen als *belegt***
>
> | ID | Aussage | bisher | Vorschlag | Beleg | Bedenken |
> |---|---|---|---|---|---|
> | A21 (neu) | Die Tagesstätte aus I2 bekam letzten Winter drei Wochen lang Suppe von einem Hotel; dann ist der Kontakt eingeschlafen. | – | belegt | I2 | keine |
> | A22 (neu) | Die Tagesstätte aus I2 kann für so einen Service nichts bezahlen; ihr Budget ist komplett verplant. | – | belegt | I2: „Bezahlen können wir dafür nichts …“ | eine Aussage über sich selbst – zählt, obwohl nach dem Pitch |
> | A23 (neu) | In der Mensa aus I3 bleiben am Ende des Tages je nach Tag fünf bis zwanzig Portionen übrig, freitags mehr. | – | belegt | I3 | ersetzt A1 („viel Essen“) |
> | A24 (neu) | In der Mensa aus I3 geht, was übrig ist, in die Biogasanlage; Mitarbeitende dürfen nichts mitnehmen. | – | belegt | I3 | ersetzt A1 („weggeworfen“) |
> | A25 (neu) | Damit jemand Essen aus der Mensa aus I3 abholen kann, braucht es eine Freigabe von oben und eine Haftungsregel. | – | belegt | I3: „… brauchen wir eine Freigabe von oben und eine Haftungsregel.“ | keine |

**Lena:** A21 bis A25 ja.

**Agent:**
> **Abschnitt 3 von 6 – neue Zeilen, vorgeschlagen als *belegt***
>
> | ID | Aussage | bisher | Vorschlag | Beleg | Bedenken |
> |---|---|---|---|---|---|
> | A26 (neu) | In der Mensa aus I3 ist um 14:30 Uhr Schluss mit der Ausgabe; um 15 Uhr muss die Küche sauber sein. | – | belegt | I3 | keine |
> | A27 (neu) | Für das Jugendzentrum aus I4 würde gekochtes Essen von außen eher nicht passen; zusammen kochen ist dort pädagogische Arbeit. | – | belegt | I4: „Gekochtes Essen von außen würde bei uns eher nicht passen.“ | eine Ablehnung für die eigene Organisation – sie widerlegt nicht A4 für alle Einrichtungen |
> | A28 (neu) | Die Jugendlichen im Jugendzentrum aus I4 kommen nachmittags und wollen eher Snacks als ein Mittagessen. | – | belegt | I4 | keine |

**Lena:** A26 ja, A27 ja. A28 nein – das mit den Snacks ist nicht unser Thema, uns geht's ums Abendessen. Dass gekochtes Essen dort nicht passt, steht ja schon in A27.

**Agent:**
> Verstanden, die Zeile lege ich nicht an; ich halte deine Begründung in `DECISIONS.md` fest. Die folgenden neuen Zeilen rücken in der Nummer nach.
>
> **Abschnitt 4 von 6 – bestehende Annahmen: Status bleibt, Quelle wird ergänzt**
>
> | ID | Aussage | bisher | Vorschlag | Belege | Bedenken |
> |---|---|---|---|---|---|
> | A1 | Mensen werfen jeden Tag viel Essen weg. | Annahme | bleibt, Quelle „ersetzt durch A23, A24“ | I3 | nur teilweise widersprochen: Reste gibt es, aber 5–20 Portionen und Biogas statt Müll. Ersetzen statt verbiegen; zitiert wird künftig A23/A24. |
> | A6 | Menschen, die in Kiel auf soziale Einrichtungen angewiesen sind, bekommen abends oft nichts Warmes. | Annahme | bleibt Annahme, „gestützt durch I1, I2“ | I1, I2 | allgemeine Aussage über die Zielgruppe – belegt erst ein Test mit Schwelle; I4 passt nicht (nachmittags) |
> | A4 | Soziale Einrichtungen würden das Essen gern nehmen. | Annahme | bleibt Annahme | I2 nur nach Pitch; I4 lehnt für sich ab | „Würdest du das nutzen?“ – „Ja“ ist kein Beleg |
> | A7 | Die Einrichtungen haben abends kein Personal zum Kochen. | Annahme | bleibt Annahme, „ohne Bezug“ | – | Frage A-3 nicht notiert |
> | A3 | Es fehlt eine App, die das verbindet. | Annahme | bleibt Annahme, Hinweis aus I1 | I1 nennt Fahrer:innen | niemand hat eine Vermittlung vermisst |
>
> Dazu bei A14 der Vermerk, dass das Jugendzentrum aus I4 nicht passt (A27). A5 (Studierendenwerk zahlt): kein Interview hat etwas dazu gesagt.

**Lena:** passt.

**Agent:**
> **Abschnitt 5 von 6 – neue Annahmen**
>
> | ID | Aussage | Status | Quelle |
> |---|---|---|---|
> | A28 | Viele Gäste der Tafel-Ausgabestelle aus I1 sind ältere, allein lebende Menschen, die kaum noch kochen. | Annahme | Hinweis aus I1 – eine Aussage über die Gäste, nicht über die Einrichtung |
> | A29 | Das Studierendenwerk würde eine Abholung gut finden, fürs Image. | Annahme | Hinweis aus I3 – eine Vermutung des Küchenleiters über seinen Arbeitgeber |
> | A30 | Essen aus der Mensa muss zwischen 15 Uhr und dem Abend gekühlt gelagert und mit dokumentierter Kühlkette übergeben werden. | Annahme | mein Schluss aus I1 (A18) und I3 (A26) – bitte prüfen, ob ihr das auch so seht |

**Lena:** Ja, A30 sehen wir auch so. passt.

**Agent:**
> **Abschnitt 6 von 6 – Ergänzung am Problembaum**
>
> ```
> Ursachen
> ├── Einrichtungen haben abends kein Personal zum Kochen [A7]
> │   └── warum? – noch offen (in den Interviews nicht beantwortet)
> └── Spenden mit warmem Essen kommen nicht an oder versanden
>     ├── Abholen ist schwierig: ein Transporter, zwei Fahrer:innen [A17]
>     ├── Annahme nur mit dokumentierter Kühlkette [A18]
>     └── Kontakte zu Spendern schlafen ein [A21]
> ```
>
> Soll das so in den Problembaum?

**Lena:** Ja.

*Agent schreibt: Register (A16–A30, Quellen bei A1, A3, A4, A6, A7, A14), `INTERVIEWS.md` (Auswertung mit Mustern und Zuordnungstabelle, I1–I4 „Ausgewertet: ja“), `PROBLEM.md` (Problembaum, Zielgruppe, Noch offen), zwei Einträge in `SIGNALS.md` (Auswertung; Pitch in I2 und fehlende Frage A-3), Canvas Blöcke 1, 5, 6, 10, `DECISIONS.md` (A28-Vorschlag abgelehnt).*

```
$ python3 .claude/skills/evidence-checks/scripts/check_project.py
OK      verweise      alle Verweise stehen im Register
OK      status        30 Einträge mit gültigem Status und Quelle
OFFEN   kritische     noch keine Annahme als kritisch markiert
OK      schwellen     0 Testkarten geprüft
OK      eine-annahme  jede Karte prüft eine Annahme
OK      ergebnisse    alle Ergebnisse ausgewertet, keine Karte überfällig
OK      widerlegt     keine widerlegte Annahme in MODEL.md
OK      interviews    4 von mindestens 3 Interviews ausgewertet (4 notiert)
```

**Agent:**
> Alles ausgewertet, keine Fehler. Zusammengefasst: 12 neue belegte Aussagen, jede über eine Einrichtung bzw. die Mensa aus I3; 3 neue Annahmen; A1 ersetzt; widerlegt ist nichts. Eure großen Annahmen (A6, A4, A5) sind weiter offen – das ist normal nach Interviews.
>
> Ich schlage vor zu committen. Als Nächstes `/map-solutions` – schauen, wer das Problem schon angeht – oder direkt `/grill-solution`.

*Commit `5 · log-evidence · Interviews I1–I4 ausgewertet, A1 ersetzt, 12 Aussagen belegt`.*

---

## 6 · `/ask-model` (2026-10-23)

**Lena:** /ask-model – was ist jetzt dran? Ahmet meint, wir sollten gleich mit der Lösung anfangen.

*Agent liest `CANVAS.md` und den Abschnitt in `AGENTS.md`, führt `check_project.py` aus (keine Fehler, 4 Interviews ausgewertet), liest `ASSUMPTIONS.md`, `INTERVIEWS.md`, `TESTS.md` und geht die Tabelle des Wegweisers von oben durch: Block 1 und 2 gefüllt, Leitfaden vorhanden, nichts Unausgewertetes, mindestens drei Interviews ausgewertet – aber `SOLUTIONS.md` enthält nur die Vorlage.*

**Agent:**
> Als Nächstes: **`/map-solutions`**. Ihr habt vier Interviews ausgewertet, aber noch nicht geschaut, wer das Problem in Kiel schon angeht – das Handbuch sieht das vor der Lösung vor, damit ihr nichts erfindet, das es schon gibt, und die Lücke seht, an der ihr ansetzen könnt.

**Lena:** Ok, dann das zuerst.

*Keine Dateiänderung; leerer Commit `6 · ask-model · …` als Markierung für die Übung.*

---

## 7 · `/map-solutions` (2026-10-26)

**Lena:** /map-solutions

*Agent liest `PROBLEM.md`, `CANVAS.md`, `ASSUMPTIONS.md`, `SOLUTIONS.md`, `DECISIONS.md`; lädt `assumptions`.*

**Agent:**
> Bevor ich suche: Welche Lösungen, Initiativen oder Projekte kennt ihr schon, die Essen an Menschen in Kiel bringen oder Reste retten?

**Lena:** Weiß ich nicht so richtig. Die Tafel halt, die wir interviewt haben. Und foodsharing hab ich mal gehört.

*Agent sucht im Web mit Begriffen aus Kernproblem, Zielgruppe und Ursachen (u. a. „Studentenwerk Schleswig-Holstein Mensa Too Good To Go Kiel“, „foodsharing Kiel Fairteiler“, „Kieler Tafel Ausgabestellen“, „Stadtmission Kiel warme Mahlzeiten“) und öffnet die Treffer: kielerleben.de (Kieler Tafel, 2025), foodsharing-kiel.org und kielerleben.de (foodsharing, 2023), t-online.de (Foodmobil, 2020), de.wikipedia.org (Too Good To Go). Zwei Seiten ließen sich nicht öffnen (studierendenwerke.de – Zugriffsschutz; ein Flyer auf kiel.de); deren Angaben nimmt er nicht auf.*

**Agent:**
> Das habe ich gefunden – jeweils nur, was auf der geöffneten Seite steht:
>
> | Lösung | Was sie macht | Quelle |
> |---|---|---|
> | **Kieler Tafel e.V.** | seit 1995; fünf Kühlfahrzeuge, bis zu 3 t Lebensmittel am Tag; Ehrenamtliche von über 250 auf knapp 120 gesunken, sucht Leute für den Fahrdienst | kielerleben.de, Artikel vom 07.01.2025 |
> | **foodsharing Kiel e.V.** | kooperiert mit ca. 75 Betrieben, 500 aktive Foodsaver:innen; gibt u. a. an Obdachlosenhilfen und die Bahnhofsmission weiter | foodsharing-kiel.org; kielerleben.de (2023) |
> | **SattMissions-Mobil** (stadt.mission.mensch) | mobile Küche, Ehrenamtliche kochen warme Mahlzeiten für Wohnungslose in Kiel; geplant mind. zweimal pro Woche, wenn Spenden reichen | t-online.de, 23.12.2020 – ob es heute noch fährt: unbekannt |
> | **Too Good To Go** | App, über die Betriebe überschüssige Lebensmittel günstig an Selbstabholer:innen verkaufen | de.wikipedia.org – ob Kieler Mensen dabei sind: unbekannt |
>
> Nicht gefunden habe ich ein Angebot, das Mensa-Reste abends zu Einrichtungen bringt. Das ist kein Beweis, dass es keins gibt – ich trage es als *Annahme* mit Datum und Suchbegriffen ein.
>
> Welche davon sind für euch relevant und sollen eine SWOT bekommen?

**Lena:** Tafel, foodsharing und das Mobil. Too Good To Go nicht, das verkauft an Leute mit App und Geld, das ist was anderes.

*Agent entwirft die drei SWOTs in `SOLUTIONS.md`, jeden Punkt markiert mit (Q) = aus der Quelle oder (E) = Einschätzung.*

**Agent:**
> Die SWOTs stehen in `SOLUTIONS.md`. Die Einschätzungen (E) sind mein Entwurf – bitte prüft sie. *(Im veröffentlichten Übungsmaterial sind die Einschätzungen zu realen Initiativen entfernt.)*
>
> Jetzt zum Fazit, und zuerst eure Sicht: **Welche Lücke seht ihr** – Gruppen, die niemand erreicht, Orte, Zeiten, Schwächen, die alle teilen? Und was heißt das für eure Idee?

**Lena:** Keiner bringt abends warmes Essen aus der Mensa zu den Einrichtungen. Die Tafel hat zu wenig Fahrer, foodsharing rettet viel, aber ob auch gekochtes Essen, wissen wir nicht. Wir brauchen keine eigene App – vielleicht können wir mit foodsharing zusammenarbeiten.

**Agent:**
> Das übernehme ich als euer Fazit. Eine Ergänzung, die ich sehe: Alle drei haben dieselbe Schwäche – zu wenige Ehrenamtliche oder unsichere Finanzierung. Das passt zu dem, was die Tafel-Ausgabestelle in I1 gesagt hat (Fahrer:innen fehlen). Wer bei euch abends fährt, wird also eine wichtige Frage. Soll das mit ins Fazit?

**Lena:** Ja, gut.

*Agent schreibt `SOLUTIONS.md` (drei Lösungen mit SWOT, Fazit), Register A31–A33 (*recherchiert*, mit Link) und A34 (*Annahme*: nichts gefunden, mit Suchbegriffen), Block 5 im Canvas, zwei Einträge in `DECISIONS.md` (Auswahl; Fazit – keine eigene App, foodsharing als möglicher Partner).*

```
$ python3 .claude/skills/evidence-checks/scripts/check_project.py
OK      verweise      alle Verweise stehen im Register
OK      status        34 Einträge mit gültigem Status und Quelle
OFFEN   kritische     noch keine Annahme als kritisch markiert
…
OK      interviews    4 von mindestens 3 Interviews ausgewertet (4 notiert)
```

**Agent:**
> Keine Fehler. Ich schlage vor zu committen, dann `/grill-solution`.

*Commit `7 · map-solutions · Tafel, foodsharing und SattMissions-Mobil mit SWOT, Fazit des Teams`.*

---

## Zwischen den Läufen

Vor Schritt 8 wurden die Skills auf den Stand vom 2026-11-23 gebracht und die Einschätzungen (E) zu realen Initiativen aus `SOLUTIONS.md` entfernt (nicht Teil der Übung).

> **Hinweis zum Check *reihenfolge*.** In den Ausgaben unten meldet er für T4 und doppelt für T1 einen Fehlalarm: Das Skript las jede T-Nummer im Feld *Voraussetzung*, auch hinter „keine (…)“. Das Team hat es in der Retro als Vorschlag fürs Skillset notiert; seitdem gilt ein Feld, das mit „keine“ beginnt, als ohne Voraussetzung, und mit dem aktuellen Skript erscheint die Zeile nicht mehr.

---

## 8 · `/grill-solution` (2026-11-24)

**Lena:** `/grill-solution`

**Agent:** *(liest `CANVAS.md`, `PROBLEM.md`, `ASSUMPTIONS.md`, `INTERVIEWS.md`, `SOLUTIONS.md`, `DECISIONS.md`; lädt `assumptions`)*
Voraussetzungen erfüllt: vier Interviews ausgewertet (I1–I4), `SOLUTIONS.md` hat drei Lösungen und euer Fazit. Ich frage in Runden – Vision → Lösung → Nutzer:innen und Kund:innen → Wertangebot → Erfolgskriterien und Lösungs-Hypothesen → kritische Annahmen. Das werden **etwa sechs Runden**, je höchstens fünf Fragen.

### Runde 1 von 6

> ❓ **F1** – **Vision**: Welchen Zustand in der Gesellschaft wollt ihr erreichen – auch wenn ihr ihn allein nie schafft? Höchstens zwei Sätze, in euren Worten. Keine Lösung und kein Produkt.
> ➡️ Erst eure Worte; einen Vorschlag mache ich nur, wenn ihr keine findet.
>
> ❓ **F2** – **Gewünschte Veränderung**: Was ist für die Betroffenen anders, wenn eure Idee wirkt? In euren Worten.
> ➡️ Wie bei F1: erst eure Worte.

**Lena:** F1: Dass niemand in Kiel abends hungrig bleiben muss. F2: Dass die Leute in den Einrichtungen abends was Warmes kriegen. Und dass gutes Essen nicht in der Biogasanlage landet.

**Agent:** Die Vision passt: ein Zielzustand, kein Produkt, ein Satz. Zu F2: Am 2026-10-07 habt ihr entschieden, dass die Verschwendung der *Anlass* ist, nicht das Kernproblem. Soll die Biogasanlage als Nebenwirkung in die Veränderung oder ganz raus?

**Lena:** Als Nebenwirkung, ja.

*(eingetragen: Block 1 Vision und Veränderung, `DECISIONS.md`)*

### Runde 2 von 6

> ❓ **F3** – **Lösung**: Was macht ihr, in zwei, drei Sätzen? Euer Fazit in `SOLUTIONS.md`: Lücke ist warmes Essen am Abend aus der Mensa zu Einrichtungen mit Abendgästen; eigene App verfolgt ihr nicht. Was macht ihr anders als Tafel, foodsharing und SattMissions-Mobil?
> ➡️ Erst eure Worte.
>
> ❓ **F4** – **Verworfene Alternativen**: Habt ihr außer der App noch andere Lösungen verworfen?
> ➡️ Wenn ja, halte ich sie mit Grund fest; sonst bleibt es bei der App (`DECISIONS.md`, 2026-10-26).

**Lena:** Kannst du das Canvas nicht einfach für uns ausfüllen?

**Agent:** Das mache ich nicht: Es entstünden lauter Sätze, die wie Wissen aussehen, aber nur meine Annahmen über eure Idee sind. Erzähl mir in zwei, drei Sätzen, was ihr vorhabt – ich ordne, frage nach und trage ein.

**Lena:** Ok. Wir bringen die Mensa und die Einrichtungen zusammen. Die Einrichtungen holen nach der Ausgabe die Reste in der Mensa ab und machen sie abends bei sich warm. Wir machen die Absprachen und springen ein, wenn mal keiner fahren kann. Jeden Abend selbst fahren schaffen wir nicht. – F4: Nur die App.

**Agent:** Ich trage das so ein. Darauf beruht die Lösung (ohne Bewertung): Die Einrichtungen holen ab – I1 sagt allerdings „Abholen ist unser Problem“ [A17]. Das Essen muss von 15 Uhr bis abends gekühlt werden [A30]. Und die Mensa braucht eine Freigabe und eine Haftungsregel [A25]. Daraus mache ich in Runde 5 Lösungs-Hypothesen.

### Runde 3 von 6

> ❓ **F5** – **Nutzer:innen**: Wer nutzt euer Angebot direkt – wer nimmt das Essen an, holt es ab, gibt es aus? Und bei wem entsteht die Wirkung?
> ➡️ Nutzer:innen sind die Mitarbeitenden der Einrichtungen; die Wirkung entsteht bei ihren Gästen. So steht es in euren Notizen (I1, I2).
>
> ❓ **F6** – **Wer zahlt oder ermöglicht?** Beispiele für Arten: der Lieferant selbst, eine Stiftung, Spenden, ein Auftrag einer Einrichtung. Was ihr wisst: Die Tagesstätte aus I2 kann nichts zahlen [A22]; ob das Studierendenwerk zahlt [A5], ist ungeprüft.
> ➡️ Nennt, wen ihr euch vorstellt; es bleibt eine Annahme, bis ein Test es zeigt.
>
> ❓ **F7** – **Kühlung**: Wo wird das Essen zwischen 15 Uhr und abends gekühlt – in der Mensa, in den Einrichtungen, woanders?
> ➡️ Wenn ihr es nicht wisst, kommt es unter *Offene Fragen*.

**Lena:** F5: Ja, die Einrichtungen. Aber eigentlich geht's ja um die Gäste. F6: Die Einrichtungen sicher nicht, die haben nichts. Das Studierendenwerk gibt das Essen, vielleicht zahlt es auch was. Sonst eine Stiftung. F7: Weiß ich nicht. Jule fragt das bis zum 11. Dezember.

### Runde 4 von 6

> ❓ **F8** – **Fall**: Nutzer:innen (Einrichtungen) und Kund:innen (Studierendenwerk, Stiftung) sind verschieden. Optionen des Handbuchs: dieselben · verschieden (eine dritte Partei zahlt) · Zielgruppe in der Wertschöpfungskette · keins davon.
> ➡️ **verschieden** – die Einrichtungen zahlen nicht, eine dritte Partei soll zahlen.
>
> ❓ **F9** – **Wertangebot je Gruppe**: Was verbessert sich – für die Einrichtungen, die Gäste, die Mensa bzw. das Studierendenwerk, eine Stiftung? In euren Worten. Für eine ausführliche Passung gibt es das Value Proposition Canvas von Strategyzer.com.
> ➡️ Erst eure Worte.

**Lena:** F8: ok, passt. F9: Für die Einrichtungen: abends was Warmes für die Gäste, ohne selbst zu kochen. Für die Gäste: abends satt. Für die Mensa: weniger wegwerfen, und es sieht gut aus. Für die Stiftung … weiß ich nicht.

**Agent:** „Es sieht gut aus“ verweise ich auf [A29] (Vermutung des Küchenleiters aus I3). Stiftung kommt unter *Offene Fragen* – wer klärt es?

**Lena:** Ich, bis 11. Dezember.

### Runde 5 von 6

> ❓ **F10** – **Erfolgskriterien**: Woran merkt ihr, dass das Problem kleiner wird? Und was muss wahr sein, damit euer Modell trägt? Beispiele für Arten: Zahl der Einrichtungen und Abende, gerettete Portionen, wer zahlt. Legt es fest, bevor ihr testet.
> ➡️ Etwas Zählbares, das bei den Gästen ankommt (Einrichtungen × Abende), nicht bei der Mensa.
>
> ❓ **F11** – **Lösungs-Hypothesen**: Aus eurer Lösung werden prüfbare Aussagen. Mein Vorschlag fürs Register:
> – A35 Das Studierendenwerk gibt die Abholung frei und regelt die Haftung.
> – A36 Einrichtungen in Kiel, die abends Gäste haben, nehmen übrig gebliebenes Mensa-Essen regelmäßig an. *(ersetzt A4, enger)*
> – A37 Die Einrichtungen holen das Essen nach der Ausgabe selbst in der Mensa ab.
> – A38 Die Einrichtungen können das Essen bis zum Abend kühlen und dann aufwärmen.
> – A39 Eine Stiftung fördert das Projekt.
> – dazu das bestehende A5 (Studierendenwerk zahlt).
> ➡️ Übernehmen; A4 bekommt „ersetzt durch A36“.

**Lena:** F10: Wenn in zwei Einrichtungen abends regelmäßig was Warmes auf dem Tisch steht. Regelmäßig heißt … dreimal die Woche? Das muss ich noch mit Ahmet und Jule klären. Und tragen tut es, wenn die Mensa mitmacht und jemand anders als die Einrichtungen Verpackung und Fahrten bezahlt. Portionen zählen ist uns nicht so wichtig, uns geht's um die Leute, nicht um die Portionen. F11: Passt. A4 ersetzen ist ok.

**Agent:** Die „drei Abende“ sind noch nicht vom ganzen Team beschlossen – ich schreibe sie als Vorschlag in Block 4 und als offene Frage, nicht als Kriterium.

### Runde 6 von 6

> ❓ **F12** – **Kritische Annahmen**: Welche fallen, und mit ihnen die Idee? Mein Vorschlag:
> – **A36** – alles baut darauf, dass Einrichtungen das Essen regelmäßig nehmen; bisher nur „Ja klar, sofort“ nach dem Pitch (I2), kein Beleg.
> – **A35** – ohne Freigabe gibt es kein Essen (I3: A25).
> – **A37** – eure Lösung setzt darauf, dass ihr nur einspringt; I1 nennt Abholen das Problem (A17).
> – **A5** – sonst zahlt niemand, was ihr für „trägt“ festgelegt habt.
> ➡️ Diese vier. A38 und A39 bleiben vorerst offen, nicht kritisch.

**Lena:** ok, passt, die vier.

**Agent:** *(trägt ein: Register A35–A39, A4 ersetzt, *Kritisch: ja* bei A5, A35, A36, A37; Blöcke 1–4, 6, *Offene Fragen*; fünf Einträge in `DECISIONS.md`)*

```
$ python3 .claude/skills/evidence-checks/scripts/check_project.py
OK      verweise      alle Verweise stehen im Register
OK      status        39 Einträge mit gültigem Status und Quelle
OFFEN   kritische     A5: keine Testkarte; A35: keine Testkarte; A36: keine Testkarte; A37: keine Testkarte
OK      schwellen     0 Testkarten geprüft
OK      eine-annahme  jede Karte prüft eine Annahme
OK      ergebnisse    alle Ergebnisse ausgewertet, keine Karte überfällig
OK      widerlegt     keine widerlegte Annahme in MODEL.md
OK      interviews    4 von mindestens 3 Interviews ausgewertet (4 notiert)
```

Keine FEHLER. *OFFEN* bei *kritische* ist erwartet: Testkarten kommen mit `/to-tests`. *(zeigt Blöcke 1–4 und 6)* Passt das so?

**Lena:** Ja, passt.

**Agent:** Dann schlage ich vor zu committen, danach `/to-model`.

→ Commit `8 · grill-solution · Vision, Lösung, Nutzer:innen und Kund:innen, Wertangebot, Erfolgskriterien, vier kritische Annahmen`

---

## 9 · `/to-model` (2026-11-26)

**Lena:** `/to-model`

**Agent:** *(liest `CANVAS.md`, `ASSUMPTIONS.md`, `PROBLEM.md`, `SOLUTIONS.md`, `DECISIONS.md`; lädt `assumptions` und `evidence-checks`; Block 1–3 sind gefüllt)*

### 1. Gliederung

| Feld | Was schon im Register steht | Lücke |
|---|---|---|
| 1 Gesellschaftliche Herausforderung | A6, A7 (Annahme); A16, A17, A18, A20, A21 (belegt) | – |
| 2 Gesellschaftliche Veränderung | Vision aus Block 1 (Entscheidung, ohne ID); A24 (belegt) | – |
| 3 Lösung | Lösung aus Block 3 (Entscheidung); A36, A37, A38 (Annahme); Studierendenwerk: A24 (belegt), A29 (Annahme) | Wertangebot Stiftung (steht als offene Frage) |
| 4 Schlüsselaktivitäten | A37, A38, A30 (Annahme); A18, A26 (belegt) | Was tut ihr selbst? |
| 5 Schlüsselpartner:innen | A35 (Annahme), A25 (belegt), A32 (recherchiert) | Wer noch? |
| 6 Kund:innengruppen | Nutzer:innen A36; Kund:innen A5, A39; Betroffene A13, A14 | – |
| 7 Kund:innenbeziehung | A21 (belegt: Kontakt eingeschlafen) | Wie haltet ihr den Kontakt? |
| 8 Kanäle | – | Lücke |
| 9 Einnahmequellen | A5, A39 (Annahme); A22 (belegt) | wofür, wie viel? |
| 10 Kostenstruktur | – | Lücke |

Sechs Lücken, also **zwei Runden** (4 + 2 Fragen).

### Runde 1 von 2

> ❓ **F1** – **Schlüsselaktivitäten**: Was müsst ihr selbst regelmäßig tun, damit es läuft? In euren Worten.
> ❓ **F2** – **Kund:innenbeziehung**: Bei der Tagesstätte ist der Kontakt zum Hotel nach drei Wochen eingeschlafen [A21]. Wie haltet ihr den Kontakt zu Einrichtungen und Mensa? Beispiele für Arten: feste Ansprechperson, regelmäßiges Treffen, Gruppe im Messenger.
> ❓ **F3** – **Kanäle**: Wie erreicht ihr Einrichtungen, Studierendenwerk und Stiftung? Beispiele für Arten: persönlich, über Kontakte, per Mail, über eine Webseite.
> ❓ **F4** – **Kostenstruktur**: Was kostet Geld? Wenn ihr Beträge kennt, nennt sie; sonst wird es eine offene Frage.
> ➡️ Bei allen vier: eure Worte; ich ergänze nichts.

**Lena:** F1: Jeden Tag mit der Mensa klären, wie viel übrig ist, und den Einrichtungen Bescheid sagen. Die Kühlkette aufschreiben. Und einspringen, wenn keiner abholen kann. F2: Eine feste Ansprechperson bei uns für jede Einrichtung, und eine Messenger-Gruppe. F3: Die Einrichtungen kennen wir aus den Interviews, die sprechen wir direkt an. Das Studierendenwerk über den Küchenleiter. Stiftungen per Mail. F4: Verpackungen, Fahrten, vielleicht Kühltaschen. Wie viel, weiß ich nicht.

### Runde 2 von 2

> ❓ **F5** – **Einnahmequellen**: Wer zahlt wofür, und wie viel? Bisher: Studierendenwerk [A5] oder Stiftung [A39], nicht die Einrichtungen [A22].
> ➡️ Wenn ihr keine Beträge habt: offene Frage mit wer und bis wann.
> ❓ **F6** – **Schlüsselpartner:innen**: Mit wem arbeitet ihr außer dem Studierendenwerk zusammen, wer liefert euch etwas zu? Beispiele für Arten: Lieferant, eine Initiative mit Fahrer:innen, eine Einrichtung als Pilot.
> ➡️ Eure Worte.

**Lena:** F5: Die Stiftung oder das Studierendenwerk für Verpackungen und Fahrten. Wie viel – weiß ich nicht, Ahmet rechnet das bis 11. Dezember. F6: Die Mensa halt, und vielleicht foodsharing, wenn wir nicht fahren können.

**Agent:** Dann schreibe ich daraus neue Zeilen fürs Register (alle *Annahme*): A40 Team schafft Absprachen, Kühlkette und Einspringen neben dem Studium · A41 feste Ansprechperson und Messenger-Gruppe halten den Kontakt · A42 Kanäle · A43 größte Kosten · A44 foodsharing fährt, wenn ihr nicht könnt. Beträge kommen als offene Frage ins Canvas (Ahmet, bis 2026-12-11). Gliederung so bestätigt?

**Lena:** Ja.

### 2. Schreiben

*(füllt `MODEL.md` Feld für Feld mit IDs; Lösung und Kund:innengruppen getrennt für Nutzer:innen und Kund:innen; Quellenvermerk bleibt; Block 7 mit Wer zahlt / größte Kosten)*

### 3. Prüfen

```
$ python3 .claude/skills/evidence-checks/scripts/check_project.py
OK      verweise      alle Verweise stehen im Register
OK      status        44 Einträge mit gültigem Status und Quelle
OFFEN   kritische     A5: keine Testkarte; A35: keine Testkarte; A36: keine Testkarte; A37: keine Testkarte
…
```

Drei Funde:

> ❓ **P1** – **Canvas und Modell widersprechen sich (Block 2 ↔ Kund:innengruppen)**: Block 2 nennt Jugendliche in Jugendzentren als Betroffene [A14]. Eure Lösung richtet sich an Einrichtungen mit Abendgästen [A36], und das Jugendzentrum aus I4 sagt, gekochtes Essen von außen passt nicht [A27].
> – **(Empfehlung)** Im Modell nur Einrichtungen mit Abendgästen; in Block 2 ein Hinweis, dass Jugendzentren nicht dazugehören. Folge: Canvas und Modell passen zusammen.
> – Block 2 unverändert. Folge: Der Widerspruch bleibt, `/review-model` meldet ihn wieder.
>
> ❓ **P2** – **Tragen die Einnahmen die Kosten?** Kosten (Verpackungen, Fahrten, Kühltaschen [A43]) und Einnahmen haben noch keine Beträge. Ich rechne nicht – steht als offene Frage (Ahmet, 2026-12-11). Passt das?
>
> ❓ **P3** – **Nicht markierte Annahmen, auf denen mehrere Felder stehen**:
> – **A38** Einrichtungen kühlen und wärmen auf – trägt Lösung, Aktivitäten, Kosten (Kühltaschen). **(Empfehlung: kritisch)**
> – **A39** Stiftung fördert – fällt A5, zahlt sonst niemand (Einnahmen). **(Empfehlung: kritisch)**
> – **A40** Ihr schafft Absprachen, Kühlkette und Einspringen neben dem Studium – trägt Lösung („springen ein“), Aktivitäten, Beziehung (Ansprechperson) und, unbezahlt, die Kosten. **(Empfehlung: kritisch; in der Probewoche mitzählen, wie oft ihr einspringt und wie viele Stunden es kostet.)**
> Das Team entscheidet.

**Lena:** P1: ok, passt. P2: Ja. P3: A38 und A39 ja. A40 nicht – ob wir Zeit haben, wissen wir doch selbst. Das müssen wir nicht testen.

**Agent:** Verstanden – A40 bleibt eine Annahme, aber nicht kritisch; ich halte die Entscheidung mit eurem Grund und meinem Vorschlag als Alternative in `DECISIONS.md` fest. *(trägt ein: A38, A39 *Kritisch: ja*; Block 2 Hinweis; Block 6 neuer Stand; drei Einträge in `DECISIONS.md`)*

```
$ python3 .claude/skills/evidence-checks/scripts/check_project.py
OK      verweise      alle Verweise stehen im Register
OK      status        44 Einträge mit gültigem Status und Quelle
OFFEN   kritische     A5: keine Testkarte; A35: keine Testkarte; A36: keine Testkarte; A37: keine Testkarte; A38: keine Testkarte; A39: keine Testkarte
OK      schwellen     0 Testkarten geprüft
OK      eine-annahme  jede Karte prüft eine Annahme
OK      ergebnisse    alle Ergebnisse ausgewertet, keine Karte überfällig
OK      widerlegt     keine widerlegte Annahme in MODEL.md
OK      interviews    4 von mindestens 3 Interviews ausgewertet (4 notiert)
```

Keine FEHLER; alle zehn Felder gefüllt, Beträge als offene Frage. *(zeigt `MODEL.md`)* Bestätigt ihr das Modell?

**Lena:** Ja, passt.

**Agent:** Dann committen, danach `/to-tests`.

→ Commit `9 · to-model · Social Business Model Canvas in zehn Feldern, A38 und A39 kritisch, A40 vom Team nicht`

---

## 10 · `/to-tests` (2026-11-28)

**Lena:** `/to-tests`

**Agent:** *(liest `ASSUMPTIONS.md`, `CANVAS.md` Block 4 und 6, `MODEL.md`, `TESTS.md`, `DECISIONS.md`; lädt `assumptions` und `evidence-checks`)*
Sechs kritische Annahmen mit Status *Annahme*: A36, A37, A35, A5, A39, A38. Ich entwerfe sechs Karten, eine pro Annahme: T1 Probewoche (A36), T2 Selbst abholen in derselben Woche (A37), T3 Freigabe (A35) und T4 Bezahlen (A5) im selben Gespräch mit dem Studierendenwerk, T5 Anfrage bei zwei Stiftungen (A39), T6 Besuch vor Ort: Kühlen und Aufwärmen (A38). Bevor ich die Karten zeige, die Probleme im Plan – jeweils mit Empfehlung:

> ❓ **P1** – **Reihenfolge**: Die Probewoche (T1, T2) setzt voraus, dass die Mensa abgeben darf [A35] und die Einrichtungen kühlen können [A38] – beides ungetestet und kritisch.
> – **(Empfehlung)** Erst T3 und T6, dann die Probewoche (Voraussetzung T3, T6 in T1 und T2). Folge: sauberer Beleg, aber die Probewoche rückt nach hinten.
> – Parallel. Folge: T1 zeigt, ob Einrichtungen annehmen, aber nicht, dass die Mensa dauerhaft abgeben darf.
>
> ❓ **P2** – **Mit wem in T1**: Ihr nennt vier Einrichtungen, darunter das Jugendzentrum aus I4. Am 2026-11-26 habt ihr entschieden, dass Jugendzentren nicht zu euren Nutzer:innen gehören: Die Jugendlichen kommen nachmittags, gekochtes Essen von außen passt nicht [A27]. Mit ihm misst T1 etwas anderes als A36 (Einrichtungen *mit Abendgästen*).
> – **(Empfehlung)** Statt des Jugendzentrums eine weitere Einrichtung mit Abendgästen.
> – Jugendzentrum bleibt. Folge: Bei einer Schwelle „3 von 4“ müssen alle drei anderen zusagen, wenn es absagt.
>
> ❓ **P3** – **Bezahlen ohne Betrag (T4)**: Kosten und Beträge sind offen (Ahmet, 2026-12-11).
> – **(Empfehlung)** Im Gespräch eine Zusage ohne Betrag erfragen; die Karte sagt, was sie nicht zeigt (ob der Betrag die Kosten deckt).
> – Bis 2026-12-11 warten und mit Betrag fragen.
>
> ❓ **P4** – **Was T5 misst**: „Die Stiftung hält uns für förderfähig“ wäre schwächer als A39 („fördert“). Wisst ihr, wann Stiftungen entscheiden?
> ➡️ Schwelle: Förderzusage, nicht „förderfähig“. Wenn bis 2026-12-18 nur eine Auskunft kommt, bleibt die Karte offen.
>
> ❓ **P5** – **Machbarkeit**: Wie viel Zeit habt ihr in den nächsten drei Wochen? Ich schätze das nicht.
>
> ❓ **P6** – **Zahl aus Block 4**: Meine Schwelle für T1 übernimmt die „drei Abende“, die in Block 4 nur als Vorschlag von Lena stehen. Hat das ganze Team das beschlossen?

**Lena:** P1: Nein, parallel. Die Freigabe dauert bestimmt Wochen, dann sind wir im Januar noch nicht weiter. Wir machen die Probewoche gleichzeitig.
P2: Das Jugendzentrum fragen wir trotzdem. Die kennen uns schon, und vielleicht sagen sie ja doch ja, wenn sie es mal probieren können.
P3: Ohne Betrag, ok.
P4: Weiß ich nicht. Förderzusage zählt, ok.
P5: Ich hab so 4 Stunden die Woche. Ahmet und Jule ähnlich, glaub ich. Die Probewoche schaffen wir, wenn die Einrichtungen selbst abholen.
P6: Ich frag kurz in der Gruppe. … Ahmet und Jule sagen ja: drei Abende.

**Agent:** Ich halte fest: P1 und P2 entscheidet ihr anders als empfohlen – beides mit eurem Grund und meiner Empfehlung als Alternative in `DECISIONS.md`. Zu P5: Die Probewoche ist nur machbar, wenn A37 stimmt; T2 zählt deshalb auch die Tage, an denen ihr selbst liefert. Die drei Abende stehen jetzt als Beschluss in Block 4 (bestätigt von euch dreien, laut Lena).

**Karten (Entwurf, Schwellen vorgeschlagen):**

| Karte | Annahme | Test | Mit wem | Schwelle (Vorschlag) | Begründung |
|---|---|---|---|---|---|
| T1 | A36 | Probe-Lieferung, eine Woche Mo–Fr | 4 Einrichtungen (Tafel-Ausgabestelle I1, Tagesstätte I2, Jugendzentrum I4, eine weitere mit Abendgästen) | mindestens **3 von 4** sagen zu und nehmen an mindestens 3 von 5 Tagen an | A36 spricht von Einrichtungen allgemein: eine Mehrheit der Angefragten; „3 Tage“ = euer Kriterium „regelmäßig“ |
| T2 | A37 | Selbst abholen in derselben Woche | die Zusagenden (mind. 2) | mindestens 2 holen an mindestens 4 von 5 Tagen selbst ab | eure Lösung: ihr „springt nur ein“ |
| T3 | A35 | Gespräch Studierendenwerk | Abteilungsleitung + Küchenleiter I3 | schriftliche Freigabe mit Haftungsregel | I3 nennt genau das als Bedingung (A25) |
| T4 | A5 | dasselbe Gespräch, ohne Betrag | dieselben | Zusage, Geld zu zahlen (Betrag offen) | Meinung („fänden wir gut“) zählt nicht |
| T5 | A39 | Mail-Anfrage | 2 Stiftungen | mindestens 1 von 2 sagt Förderung zu | „förderfähig“ zählt nicht |
| T6 | A38 | Besuch vor Ort | Tafel-Ausgabestelle, Tagesstätte | mindestens 2 zeigen Kühlplatz und Aufwärmmöglichkeit | Lösung setzt Kühlen und Aufwärmen dort voraus |

Alle bis **2026-12-18**. Sagt das Jugendzentrum ab wie in I4, braucht T1 alle drei anderen. Festlegen tut ihr – passen die Schwellen?

**Lena:** Ok, 3 von 4. Die anderen passen auch.

*(trägt ein: sechs Karten in `TESTS.md`, Status *geplant*, *Ausgewertet: nein*; Test-IDs in der Spalte *Test* des Registers; Block 9 Liste, Block 4 „drei Abende“; vier Einträge in `DECISIONS.md`)*

```
$ python3 .claude/skills/evidence-checks/scripts/check_project.py
OK      verweise      alle Verweise stehen im Register
OK      status        44 Einträge mit gültigem Status und Quelle
OK      kritische     6 offene kritische Annahmen haben eine Testkarte mit Schwelle
OK      schwellen     6 Testkarten geprüft
OK      eine-annahme  jede Karte prüft eine Annahme
OK      ergebnisse    alle Ergebnisse ausgewertet, keine Karte überfällig
OK      widerlegt     keine widerlegte Annahme in MODEL.md
OK      interviews    4 von mindestens 3 Interviews ausgewertet (4 notiert)
```

*kritische* und *eine-annahme* sind OK. **Bitte committet die Karten jetzt**, bevor ihr testet: So bleibt sichtbar, dass die Schwellen vor den Ergebnissen feststanden. Dann seid ihr dran: testen, Ergebnisse in `TESTS.md` notieren oder hier einfügen, dann `/log-evidence`.

→ Commit `10 · to-tests · Testkarten T1–T6 mit Schwellen, vor dem Testen committet`

*(Das Team testet bis 2026-12-18.)*

---

## 11 · `/log-evidence` (2026-12-19)

**Lena:** `/log-evidence` – Hier unsere Ergebnisse:
- T1 und T2: Probe-Abholung bei Einrichtungen: Vier Einrichtungen wurde angeboten, eine Woche lang abends übrig gebliebenes Mensa-Essen zu bringen. Zwei haben zugesagt und es an mindestens drei Tagen angenommen (Tafel-Ausgabestelle, Tagesstätte). Eine hat abgelehnt (Jugendzentrum: „passt nicht zu uns“), eine hat nicht geantwortet. Die Tafel konnte nur zwei von fünf Tagen selbst abholen; an den anderen Tagen hat das Team geliefert.
- T3 und T4: Gespräch mit dem Studierendenwerk (Abteilungsleitung Hochschulgastronomie): „Finden wir gut, machen wir gern mit, wenn die Haftung geklärt ist. Bezahlen können wir dafür aber nichts, höchstens Verpackungen stellen.“
- T5: Anfrage bei zwei Stiftungen: Eine hat geantwortet: Förderung für Ehrenamtsprojekte bis 5.000 € möglich, Antrag bis März. Die andere hat nicht geantwortet.
- T6: Den Test haben wir nicht gemacht.

**Agent:** *(liest `ASSUMPTIONS.md`, `INTERVIEWS.md`, `TESTS.md`, `PROBLEM.md`, `CANVAS.md`, `SIGNALS.md`; lädt `assumptions` und `evidence-checks`)*
Ich übertrage eure Ergebnisse wörtlich in das Feld *Ergebnis*: Probe-Abholung → T1 und T2, Gespräch → T3 und T4, Stiftungen → T5. T6 bleibt ohne Ergebnis. Stimmt die Zuordnung?

**Lena:** Ja.

**Agent:** Zwei Rückfragen:
1. **T2** zählt pro Einrichtung, an wie vielen Tagen sie selbst abgeholt hat. Für die Tafel steht es da (2 von 5). Und für die Tagesstätte?
2. **T6** ist bis 2026-12-18 angesetzt und hat kein Ergebnis. Bleibt der Test geplant – bis wann?

**Lena:** 1: Weiß ich nicht, haben wir nicht aufgeschrieben. 2: Machen wir im Januar, bis 15. Januar.

**Agent:** Reihenfolge der Schwellen: Laut Git-Verlauf stehen alle sechs Schwellen seit dem Commit vom 2026-11-28 in `TESTS.md`, vor den Ergebnissen. ✔
Voraussetzungen: T1–T5 hatten keine; die Probewoche lief auf eure Entscheidung vor der Freigabe (T3) und ohne Kühl-Check (T6). Das hat das Ergebnis von T1 nicht verursacht, steht aber als Vorbehalt in der Quelle.

### Abschnitt 1 von 3 – vorgeschlagen *widerlegt* (einzeln zu bestätigen)

| Annahme | bisher | Vorschlag | Beleg (Ergebnis gegen Schwelle) | Bedenken |
|---|---|---|---|---|
| A36 Einrichtungen mit Abendgästen nehmen regelmäßig an | Annahme | **widerlegt** | T1: 2 von 4 an ≥ 3 von 5 Tagen; Schwelle 3 von 4 | Das Jugendzentrum hat keine Abendgäste (A27) und war auf euren Wunsch dabei; „keine Antwort“ ist kein Nein; Probewoche vor der Freigabe |
| A37 Einrichtungen holen selbst ab | Annahme | **widerlegt** | T2: Tafel 2 von 5 Tagen; Schwelle 2 Einrichtungen an 4 von 5 Tagen – mit nur zwei Zusagenden nicht mehr erreichbar | Tagesstätte nicht notiert (ändert das Ergebnis nicht) |
| A5 Studierendenwerk zahlt | Annahme | **widerlegt** | T4: „Bezahlen können wir dafür aber nichts“ – Aussage der Organisation über sich selbst | ohne Betrag gefragt; ein Nein gilt trotzdem |

**Lena:** 2 von 4 ist doch auch gut, können wir das nicht als belegt nehmen?

**Agent:** Ich verstehe, dass es sich nach Erfolg anfühlt – zwei Einrichtungen haben wirklich angenommen. Aber die Schwelle „3 von 4“ habt ihr am 2026-11-28 festgelegt, *bevor* ihr getestet habt; genau dafür habt ihr die Karten committet. Senkt ihr sie jetzt, passt sie zufällig zum Ergebnis, und das Ergebnis ist nur noch ein Signal, kein Beleg. Was die zwei Zusagen zeigen, verliert ihr nicht: Es kommt als eigene, belegte Zeile ins Register (A45, Abschnitt 2). Ihr habt drei Möglichkeiten:
- A36 *widerlegt* (Vorschlag, nach eurer Schwelle);
- A36 bleibt *Annahme* und ihr testet neu, z. B. nur mit Einrichtungen mit Abendgästen – das wäre ein neuer Test mit neuer Schwelle, vorher festgelegt;
- A36 *belegt* mit „2 von 4“ – das geht nicht, weil die Schwelle erst nach dem Ergebnis käme.

**Lena:** Ok, verstehe. Die Schwelle haben wir ja selbst vorher festgelegt. Dann widerlegt. A36 widerlegt, A37 widerlegt, A5 widerlegt.

### Abschnitt 2 von 3 – neue Zeilen, vorgeschlagen *belegt* (ohne Bedenken, kompakt)

- **A45** In der Probewoche haben die Tafel-Ausgabestelle aus I1 und die Tagesstätte aus I2 an mindestens drei von fünf Tagen Mensa-Essen angenommen. (T1)
- **A46** Die Tafel-Ausgabestelle aus I1 konnte nur an zwei von fünf Tagen selbst abholen; an den anderen Tagen hat das Team geliefert. (T2)
- **A47** Eine der zwei angefragten Stiftungen fördert Ehrenamtsprojekte mit bis zu 5.000 €; Antrag bis März. (T5, Auskunft der Stiftung über sich selbst)

**Lena:** A45, A46, A47 ja.

### Abschnitt 3 von 3 – ohne Statusänderung

| Was | Vorschlag |
|---|---|
| A35 Freigabe und Haftung | bleibt *Annahme*: „machen wir gern mit, wenn die Haftung geklärt ist“ ist eine Absicht unter Bedingung. T3 bleibt *läuft*, *Ausgewertet: teilweise*. |
| A39 Stiftung fördert | bleibt *Annahme*: „förderfähig“ ist keine Zusage. T5 *läuft* (Antrag), *teilweise*. |
| A48 neu: Studierendenwerk würde höchstens Verpackungen stellen | *Annahme* (Hinweis aus T4, keine Zusage) |
| A27 Jugendzentrum | Quelle ergänzt: „T1: Probewoche abgelehnt („passt nicht zu uns“)“ |
| A40 Team schafft Absprachen und Einspringen (nicht kritisch) | Quelle ergänzt: Hinweis aus T2 – das Team lieferte an 3 von 5 Tagen (A46). Kein Status. |
| T6 | ohne Ergebnis, *geplant*, neu bis 2027-01-15 |
| Problembaum | unter „Abholen ist schwierig [A17]“: „in der Probewoche nur an 2 von 5 Tagen selbst abgeholt [A46]“ |

**Lena:** Passt.

*(schreibt: Register, `TESTS.md` (Ergebnis, Status, Ausgewertet), Problembaum, `SIGNALS.md` (Test), Canvas Block 5, 6 (neuer Stand), 10; ⚠️-Zeilen für A36, A37, A5 in Block 2, 3, 6, 7, 9; `MODEL.md` bleibt unverändert; Entscheidung in `DECISIONS.md`)*

```
$ python3 .claude/skills/evidence-checks/scripts/check_project.py
OK      verweise      alle Verweise stehen im Register
OK      status        48 Einträge mit gültigem Status und Quelle
OK      kritische     3 offene kritische Annahmen haben eine Testkarte mit Schwelle
OK      schwellen     6 Testkarten geprüft
OK      eine-annahme  jede Karte prüft eine Annahme
OFFEN   reihenfolge   Ergebnis, obwohl die Voraussetzung noch nicht abgeschlossen ist: T1 (vor T3), T1 (vor T6), T1 (vor T3), T1 (vor T6), T4 (vor T3) – Vorbehalt in der Quelle nennen (/log-evidence)
OFFEN   ergebnisse    läuft (Bedingung offen): T3, T5
OFFEN   widerlegt     widerlegte oder ersetzte Annahmen in MODEL.md: A36, A37, A5 – prüfen, ob das Feld noch darauf aufbaut
OK      interviews    4 von mindestens 3 Interviews ausgewertet (4 notiert)
```

**Agent:** Keine FEHLER.
- *reihenfolge*: Für T1 stimmt der Hinweis – die Probewoche lief vor T3 und T6; der Vorbehalt steht in der Quelle von A36. Für T4 ist es ein Fehlalarm: Im Feld *Voraussetzung* steht „keine (gleiches Gespräch wie T3)“, und das Skript liest jede T-Nummer im Feld als Voraussetzung. T1 erscheint doppelt aus demselben Grund. Ich ändere die Karten nach dem Test nicht; das notiere ich für die Retro.
- *widerlegt*: `MODEL.md` baut noch auf A36, A37, A5 – das klärt `/review-model` mit euch.
- *ergebnisse*: T3 und T5 laufen. (Mit dem heutigen Datum des Projekts wäre T6 ohne neues Datum überfällig gewesen; es steht jetzt auf 2027-01-15.)

Schlage vor zu committen, dann `/review-model`.

→ Commit `11 · log-evidence · Testergebnisse T1–T5 ausgewertet, A36 A37 A5 widerlegt, Schwelle nicht nachträglich gesenkt`

---

## 12 · `/review-model` (2026-12-20)

**Lena:** `/review-model`

**Agent:** *(liest alle Projektdateien und die letzten Einträge in `SIGNALS.md`; lädt `evidence-checks` und `assumptions`; führt die zwei Achsen nacheinander aus, nicht als eigene Sub-Agenten)*
Blockierend heißt: Das solltet ihr klären, bevor ihr darauf weiterbaut – es heißt nicht, dass ihr aufhören müsst.

### Achse 1: Beleg

`check_project.py`: keine FEHLER (OFFEN: *reihenfolge*, *ergebnisse*, *widerlegt*).

| # | Befund | Beleg | Vorschlag |
|---|---|---|---|
| B1 | **blockierend** – `MODEL.md` baut auf drei widerlegten kritischen Annahmen: Lösung und Aktivitäten auf A37, Lösung und Kund:innengruppen auf A36, Kund:innengruppen und Einnahmen auf A5. | Register; Check *widerlegt*; Block 2, 3, 7 mit ⚠️ | Weg wählen (unten), dann `/to-model` |
| B2 | **blockierend** – Freigabe [A35] offen: „machen wir gern mit, wenn die Haftung geklärt ist“ ist eine Absicht unter Bedingung. Ohne sie gibt es kein Essen. | T3 *läuft* | Haftungsfrage aktiv klären (F2) |
| B3 | Hinweis – Die Probewoche lief vor T3 und ohne T6, auf eure Entscheidung; Vorbehalt steht in A36. Der Check meldet zusätzlich T4 – ein Fehlalarm (T-Nummer im Text von *Voraussetzung*). | Check *reihenfolge*; `DECISIONS.md` 2026-11-28 | für die Retro |
| B4 | Hinweis – Messlücke in T2: Abholtage der Tagesstätte nicht notiert. | `TESTS.md` T2 | für die Retro |
| B5 | Hinweis – [A38] kritisch, T6 nicht gemacht (neu bis 2027-01-15). | `TESTS.md` T6 | so lassen |

Stand: kritisch **belegt** – keine; **widerlegt** – A36, A37, A5; **offen** – A35, A38, A39. Die meisten Felder von `MODEL.md` beruhen auf A36, A37 und A40.

### Achse 2: Wirkung

| # | Befund | Beleg | Vorschlag |
|---|---|---|---|
| W1 | **blockierend** – Trägt es sich? Niemand zahlt belegt: A5 widerlegt; A39 offen (A47: förderfähig bis 5.000 €, Antrag bis März). Ob das die Kosten deckt, kann ich nicht sagen: Es fehlen die Kosten pro Woche (offene Frage, Ahmet, war bis 2026-12-11) und ein Förderbetrag. | Register, Block 7, *Offene Fragen* | Weg wählen (F4) |
| W2 | **blockierend** – Wer fährt? A37 widerlegt; das Team lieferte an 3 von 5 Tagen [A46]. [A40] (schafft das Team das) ist nicht kritisch und wurde nicht gemessen, [A44] (foodsharing fährt) ist ungetestet. | `DECISIONS.md` 2026-11-26, Register | F3 |
| W3 | Hinweis – Wirkung bei den Gästen ist nicht gemessen: T1 zählt „angenommen“, nicht, ob abends etwas Warmes gegessen wurde. Block 4 („an drei Abenden etwas Warmes auf dem Tisch“) ist damit für eine Woche vielleicht erfüllt – wissen könnt ihr es nicht. | Block 4, T1 | beim nächsten Test mitzählen |
| W4 | Hinweis – Ob die Tafel-Ausgabestelle abends Gäste hat, wisst ihr nicht; ihr bekannt ist eine Ausgabe zweimal pro Woche [A16]. A45 ist deshalb nur bedingt die Gruppe aus A36. | A16, A45 | F1 |
| W5 | Hinweis – Vision und Zielgruppe passen noch zu Block 1 und `PROBLEM.md`; Nutzer:innen, Kund:innen und Fall in Block 2 stimmen mit `MODEL.md` überein, außer dass A5 widerlegt ist. | Block 1, 2, `MODEL.md` | – |

### Drei Wege

- **Weiter testen** – steht nicht zur Wahl: Drei Annahmen sind widerlegt, und ihr müsstet erklären, warum das nichts ändert.
- **Anpassen** – für A36 gibt es eine engere, gestützte Ersatz-Annahme (A45: Tafel-Ausgabestelle und Tagesstätte nahmen an), für das Fahren eine Beobachtung (A46). Für A5 (wer zahlt) **nicht**: A47 zeigt nur, dass eine Stiftung fördern *kann*. Damit ist „Anpassen“ nach der Regel des Reviews kein Weg, solange „wer zahlt“ offen ist.
- **Neu ansetzen (Pivot)** – bei „wer zahlt“: Problem, Vision und die zwei Einrichtungen bleiben; mit `/grill-solution` klärt ihr Kund:innen und Einnahmen neu (z. B. Förderung, Sachleistungen wie Verpackungen [A48], Ehrenamt). Dagegen: noch eine Runde, bevor wieder getestet wird.

### Entscheidungen

> ❓ **F1** – **Zielgruppe nach T1** (A36 widerlegt, A45 belegt; W4)
> – **(Empfehlung)** Mit Tafel-Ausgabestelle und Tagesstätte weiter; klären, ob die Tafel abends Gäste hat. Folge: kleine, gestützte Gruppe.
> – Neue Einrichtungen mit Abendgästen suchen, T1 wiederholen. Folge: mehr Aufwand, vielleicht breitere Gruppe.
> – Beides.
>
> ❓ **F2** – **Freigabe** (B2)
> – **(Empfehlung)** Beim Studierendenwerk nachfragen, welche Haftungsregel es braucht; T3 läuft weiter. Wer, bis wann?
> – Abwarten.
>
> ❓ **F3** – **Wer fährt?** (W2; A40 hattet ihr am 2026-11-26 nicht als kritisch markiert)
> – **(Empfehlung)** A40 jetzt als kritisch markieren und im nächsten Test messen (Stunden, Fahrten); foodsharing als Fahrer:innen [A44] mit testen.
> – Das Team fährt weiter, ohne Test.
> – Die Einrichtungen bitten, öfter selbst abzuholen.
>
> ❓ **F4** – **Weg**
> – **(Empfehlung)** Neu ansetzen bei „wer zahlt“ → `/grill-solution`, dann `/to-model`, `/to-tests`.
> – Anpassen – nur, wenn ihr eine gestützte Ersatz-Annahme für A5 nennt.
> – Ganz neu beim Problem → `/grill-problem` (das Problem selbst ist nicht widerlegt).

**Lena:** F1: Mit den beiden weiter. F2: Ahmet fragt nach, was die genau brauchen, bis Mitte Januar. F3: Ok, das mit der Zeit hätten wir doch testen sollen. Wir sind dreimal gefahren, das war echt viel. Also ja, A40 kritisch. F4: Ok, dann neu ansetzen bei der Frage, wer zahlt. Die Einrichtungen bleiben.

**Agent:** *(trägt ein: vier Einträge in `DECISIONS.md`; A40 *Kritisch: ja*; Block 6 aktualisiert; Block 8 Stand der Checks; Block 11 Weg und nächste Schritte; `SIGNALS.md` Eintrag *Review*; `MODEL.md` bleibt unverändert)*

```
$ python3 .claude/skills/evidence-checks/scripts/check_project.py
OK      verweise      alle Verweise stehen im Register
OK      status        48 Einträge mit gültigem Status und Quelle
OFFEN   kritische     A40: keine Testkarte
OK      schwellen     6 Testkarten geprüft
OK      eine-annahme  jede Karte prüft eine Annahme
OFFEN   reihenfolge   Ergebnis, obwohl die Voraussetzung noch nicht abgeschlossen ist: T1 (vor T3), T1 (vor T6), T1 (vor T3), T1 (vor T6), T4 (vor T3) – Vorbehalt in der Quelle nennen (/log-evidence)
OFFEN   ergebnisse    läuft (Bedingung offen): T3, T5
OFFEN   widerlegt     widerlegte oder ersetzte Annahmen in MODEL.md: A36, A37, A5 – prüfen, ob das Feld noch darauf aufbaut
OK      interviews    4 von mindestens 3 Interviews ausgewertet (4 notiert)
```

Der Weg ist entschieden. Schlage vor zu committen, dann `/model-retro`, danach `/grill-solution`.

→ Commit `12 · review-model · Zwei-Achsen-Review, Weg: neu ansetzen bei „Wer zahlt?“, A40 jetzt kritisch`

---

## 13 · `/model-retro` (2026-12-21)

**Lena:** `/model-retro`

**Agent:** *(liest `SIGNALS.md`, `DECISIONS.md`, `CANVAS.md`, `ASSUMPTIONS.md`, `TESTS.md` und die Einträge von `/review-model`; lädt `assumptions` und `evidence-checks`)*

### 1. Signale sammeln – eine Runde

> 1. Was lief anders als geplant?
> 2. Was hat euch überrascht?
> 3. Wo habt ihr festgesteckt?
> 4. Welche Entscheidung war im Nachhinein voreilig?
> 5. Wo hat der Agent etwas getan oder vorgeschlagen, das nicht gepasst hat?

**Lena:** 1: Wir mussten dreimal zur Tafel fahren. Das war echt viel. 2: Dass das Studierendenwerk die Idee gut findet, aber nichts zahlt. 3: Bei der Schwelle. 2 von 4 hat sich wie ein Erfolg angefühlt. 4: Das Jugendzentrum zu fragen. Die hatten im Interview ja schon gesagt, dass es nicht passt. 5: Eigentlich nichts. Die sechs Testkarten waren viel auf einmal.

**Agent:** Dazu ergänze ich, was ich selbst sehe: die Messlücke in T2 (Tagesstätte), T6 ohne Platz für „nicht gemacht“, den Fehlalarm des Checks *reihenfolge* bei T4, und dass die Wirkung bei den Gästen nicht gemessen wurde.

### 2. Jedes Signal erklärt

| Signal | Ursache | Warum hat kein Check es gefunden? |
|---|---|---|
| Team fuhr an 3 von 5 Tagen [A46] | A37 trug die Lösung, obwohl I1 Abholen als Problem nannte [A17]; A40 (eure Zeit) habt ihr nicht als kritisch markiert. | Kein Check verlangt, die Arbeit des Teams mitzuzählen. |
| Studierendenwerk zahlt nicht [A5] | A5 kam aus dem Notion-Export und war bis zum Test ungeprüft. | Der Test hat es gefunden – so soll es sein. |
| Schwelle senken wollen | Zwei Zusagen fühlten sich nach Erfolg an. | Die Regel hat gegriffen (Karten vorher committet). |
| Jugendzentrum in T1 | Ich hatte es gemeldet; ihr habt anders entschieden. | Der Review-Check hat gegriffen; die Entscheidung lag bei euch. |
| T2: Tagesstätte nicht notiert | Keine Liste für die Messgröße während der Woche. | Fällt erst beim Auswerten auf. |
| T6 nicht gemacht | Die Karte kennt keinen solchen Status. | Das Skript meldet sie erst, wenn sie überfällig ist. |
| Fehlalarm *reihenfolge* (T4, T1 doppelt) | Das Skript liest jede T-Nummer im Feld *Voraussetzung*. | – (der Check selbst ist ungenau) |
| Wirkung bei Gästen nicht gemessen | T1 zählt „angenommen“, nicht „abends gegessen“. | Kein Check fragt nach der Wirkung bei den Betroffenen. |
| Sechs Karten auf einmal | sechs kritische Annahmen | – |

### 3. Vorschläge

1. **Jetzt korrigieren:** Status der alten Signale setzen (2026-10-23 ×2, 2026-12-19, 2026-12-20); Kostenfrage in *Offene Fragen* ist seit 2026-12-11 überfällig – neues Datum? *(Empfehlung: übernehmen)*
2. **Check (durch das Team, Block 8):** *Team-Zeit mitzählen* – in jedem Probelauf zählt ihr, wie oft ihr fahrt und wie viele Stunden es braucht. *(Empfehlung)*
3. **Check (durch das Team, Block 8):** *Strichliste je Messgröße* – vor dem Test steht in der Karte eine leere Liste je Messgröße und Einrichtung. *(Empfehlung)*
4. **Check (durch das Team, Block 8):** *Wirkung mitzählen* – jeder Probelauf zählt, an wie vielen Abenden das Essen bei den Gästen ankam. *(Empfehlung)*
5. **Canvas und Modell:** Block 2, 3, 7 und `MODEL.md` bauen auf A36, A37, A5 – das ändert die nächste Runde (`/grill-solution`, `/to-model`), nicht die Retro.
6. **Skill-Regel 1 (`check_project.py`):** Ein Feld *Voraussetzung*, das mit „keine“ beginnt, ist keine Voraussetzung; jede Karte nur einmal melden. *(Empfehlung)*
7. **Skill-Regel 2 (Vorlage `TESTS.md`, `/log-evidence`):** Status „nicht durchgeführt (mit Grund)“; `/log-evidence` fragt nach Grund und neuem Datum. *(Empfehlung)*
8. **Skill-Regel 3 (`/to-tests`):** Behält das Team Teilnehmende, die nicht zur Gruppe der Annahme gehören, zählt die Schwelle nur die passenden. *(Vorschlag; die Entscheidung von 2026-11-28 bleibt eure.)*

Jede Skill-Regel kommt mit einem Satz in einfacher Sprache und dem Diff in `SKILL-PROPOSALS.md`; ihr könnt sie als Issue im Repository des Skillsets einreichen, ohne Inhalte eures Projekts. Das Diff müsst ihr nicht verstehen – der Satz reicht.

**Lena:** 1 ja, Kosten macht Ahmet bis 15. Januar. 2, 3, 4 ja – die Liste hätte uns echt geholfen. 5 ok. 6 und 7 ja, Jule reicht das ein. 8 nicht – das war unser Fehler, nicht der vom Skill. Du hattest es ja gesagt.

### 4. Anwenden

*(schreibt: neun Signale vom 2026-12-21 und den Status aller Signale in `SIGNALS.md`; Block 8 drei Projekt-Checks; Block 11 Retro und nächste Runde; Kostenfrage neu bis 2027-01-15; `SKILL-PROPOSALS.md` mit Vorschlägen 1 und 2 (Diffs mit `git apply --check` geprüft); Entscheidung in `DECISIONS.md`)*

```
$ python3 .claude/skills/evidence-checks/scripts/check_project.py
OK      verweise      alle Verweise stehen im Register
OK      status        48 Einträge mit gültigem Status und Quelle
OFFEN   kritische     A40: keine Testkarte
OK      schwellen     6 Testkarten geprüft
OK      eine-annahme  jede Karte prüft eine Annahme
OFFEN   reihenfolge   Ergebnis, obwohl die Voraussetzung noch nicht abgeschlossen ist: T1 (vor T3), T1 (vor T6), T1 (vor T3), T1 (vor T6), T4 (vor T3) – Vorbehalt in der Quelle nennen (/log-evidence)
OFFEN   ergebnisse    läuft (Bedingung offen): T3, T5
OFFEN   widerlegt     widerlegte oder ersetzte Annahmen in MODEL.md: A36, A37, A5 – prüfen, ob das Feld noch darauf aufbaut
OK      interviews    4 von mindestens 3 Interviews ausgewertet (4 notiert)
```

Keine FEHLER; jedes Signal hat einen Status. Schlage vor zu committen. Nächster Schritt, wie `/ask-model` ihn empfehlen würde: Block 11 nennt „neu ansetzen bei *Wer zahlt?*“ → **`/grill-solution`**.

→ Commit `13 · model-retro · Signale erklärt, drei Checks für das Projekt, zwei Vorschläge für das Skillset`

---

## Entscheidungen im Überblick (Lenas Ablehnungen und Lehrmomente, Schritte 8–13)

| # | Skill | Zitat | Warum es zählt |
|---|---|---|---|
| 1 | /grill-solution | Lena: „Kannst du das Canvas nicht einfach für uns ausfüllen?“ – Agent: „Das mache ich nicht: Es entstünden lauter Sätze, die wie Wissen aussehen, aber nur meine Annahmen über eure Idee sind.“ | Der häufigste Weg, wie ungeprüfte Annahmen ins Canvas kommen. Das Team schreibt danach die Lösung in eigenen Worten. |
| 2 | /grill-solution | Lena: „Regelmäßig heißt … dreimal die Woche? Das muss ich noch mit Ahmet und Jule klären.“ – Agent schreibt die Zahl als Vorschlag und offene Frage, nicht als Kriterium. | Erfolgskriterien sind Entscheidungen des ganzen Teams; eine halb gesagte Zahl ist noch keine. In /to-tests wird sie ausdrücklich bestätigt. |
| 3 | /grill-solution | Agent: „Die Einrichtungen holen ab – I1 sagt allerdings ‚Abholen ist unser Problem‘ [A17].“ | Der Agent bewertet die Idee nicht, zeigt aber, worauf sie beruht. Genau diese Annahme (A37) wird später widerlegt. |
| 4 | /to-model | Lena: „A40 nicht – ob wir Zeit haben, wissen wir doch selbst. Das müssen wir nicht testen.“ | **Abgelehnte Empfehlung.** Das Team entscheidet, was kritisch ist – auch gegen den Agenten. Nach der Probewoche (Team fuhr 3 von 5 Tagen) markiert das Team A40 selbst als kritisch. |
| 5 | /to-tests | Lena: „Das Jugendzentrum fragen wir trotzdem. Die kennen uns schon, und vielleicht sagen sie ja doch ja, wenn sie es mal probieren können.“ | **Abgelehnte Empfehlung**, mit einem Grund, der für Einsteiger:innen natürlich klingt. Die Folge ist vorher benannt („dann müssen alle drei anderen zusagen“) und tritt ein. In der Retro: „Das war unser Fehler, nicht der vom Skill.“ |
| 6 | /to-tests | Lena: „Die Freigabe dauert bestimmt Wochen, dann sind wir im Januar noch nicht weiter. Wir machen die Probewoche gleichzeitig.“ | **Abgelehnte Empfehlung** (Reihenfolge). Der Agent hält fest, was das Ergebnis dann *nicht* zeigt; der Vorbehalt landet in der Quelle von A36. |
| 7 | /to-tests | Agent: „Bitte committet die Karten jetzt, bevor ihr testet.“ | Der Git-Verlauf beweist später, dass die Schwelle vor dem Ergebnis feststand. |
| 8 | /log-evidence | Lena: „2 von 4 ist doch auch gut, können wir das nicht als belegt nehmen?“ – Agent: „Senkt ihr sie jetzt, passt sie zufällig zum Ergebnis, und das Ergebnis ist nur noch ein Signal, kein Beleg.“ | Kern von Einheit 5: nie einen Check lockern, damit er besteht. Was die zwei Zusagen zeigen, geht nicht verloren (A45). |
| 9 | /log-evidence | T4: „Bezahlen können wir dafür aber nichts“ → A5 *widerlegt*, obwohl ohne Betrag gefragt; „machen wir gern mit, wenn …“ → A35 bleibt *Annahme*. | Aussagen über sich selbst zählen; Absichten unter Bedingungen nicht. Asymmetrie: Ein Nein gilt auch ohne Preis. |
| 10 | /log-evidence | Lena: „Weiß ich nicht, haben wir nicht aufgeschrieben.“ (Abholtage der Tagesstätte) | Ehrliche Lücke statt nachträglicher Schätzung; wird in der Retro zum Check *Strichliste je Messgröße*. |
| 11 | /review-model | Agent: „Für A5 gibt es keine gestützte Ersatz-Annahme – A47 zeigt nur, dass eine Stiftung fördern *kann*. Damit ist ‚Anpassen‘ kein Weg.“ | Pivot heißt nicht alles wegwerfen: neu ansetzen nur bei „Wer zahlt?“, Problem und Einrichtungen bleiben. |
| 12 | /review-model | Lena: „Ok, das mit der Zeit hätten wir doch testen sollen. Wir sind dreimal gefahren, das war echt viel.“ | Die abgelehnte Empfehlung aus /to-model kommt zurück – nicht als Vorwurf, sondern als Entscheidung des Teams mit neuem Wissen. |
| 13 | /model-retro | Agent: „Warum hat kein Check es gefunden?“ – drei Projekt-Checks (Team-Zeit, Strichliste, Wirkung) und zwei Skill-Vorschläge. | Aus Überraschungen werden Checks; aus einer Ungenauigkeit des Skripts ein Vorschlag fürs Skillset. |
