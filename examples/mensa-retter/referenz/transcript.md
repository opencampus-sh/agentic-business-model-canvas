# Referenzlauf „Mensa-Retter“ – Transkript

Fiktiver Beispielfall für den Selbstlernkurs. Lena (Studentin der Sozialen Arbeit, Team mit Ahmet und Jule) führt die Skills des Agentic Business Model Canvas in einem leeren, privaten Git-Repository aus. **Agent** = Claude Code, das die Skills liest und befolgt. Fragen des Agenten sind wörtlich wiedergegeben; Dateiinhalte stehen im Git-Verlauf.

**Zeitachse.** Die Commits tragen die Daten der Geschichte (Projektstart 2026-10-05, Interviews 14.–22. Oktober, Tests bis 13. November, Retro am 2026-11-23). Der Agent hat jeweils das Datum der Sitzung als „heute“ verwendet. Die gezeigten Ausgaben von `check_project.py` sind mit diesem Sitzungsdatum als „heute“ erzeugt (sonst meldet der Check Karten mit *Bis wann* vor dem echten Ausführungsdatum als überfällig).

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
| 8 | 2026-10-28 | `/grill-solution` |
| 9 | 2026-10-30 | `/to-model` |
| 10 | 2026-11-02 | `/to-tests` |
| – | bis 2026-11-13 | Team testet |
| 11 | 2026-11-16 | `/log-evidence` |
| 12 | 2026-11-18 | `/review-model` |
| 13 | 2026-11-23 | `/model-retro` |

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
> Die SWOTs stehen in `SOLUTIONS.md`. Die Einschätzungen (E) sind mein Entwurf – bitte prüft sie, z. B. „foodsharing könnte eher Partner als Konkurrenz sein“ oder „das Mobil kocht vor Ort und braucht deshalb keine Kühlkette für fertige Speisen“.
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

## 8 · `/grill-solution` (2026-10-28)

**Lena:** /grill-solution

*Agent liest `CANVAS.md`, `PROBLEM.md`, `ASSUMPTIONS.md`, `INTERVIEWS.md`, `SOLUTIONS.md`, `DECISIONS.md`; lädt `assumptions`. Voraussetzungen erfüllt: vier Interviews ausgewertet, `SOLUTIONS.md` gefüllt. Schon entschieden und nicht mehr gefragt: keine eigene App, foodsharing als möglicher Partner.*

**Agent:**
> Jetzt geht es darum, was ihr anbietet, für wen, wer zahlt und woran ihr Erfolg erkennt – und welche Annahmen das alles tragen. Die Voraussetzungen aus dem Handbuch sind erfüllt (vier Interviews, bestehende Lösungen). Es werden etwa fünf Runden.
>
> **Runde 1 von etwa 5**
>
> ❓ **F1** – **Vision:** Welche Veränderung in der Gesellschaft wollt ihr erreichen? Höchstens zwei Sätze, ein Zielzustand, den ihr allein nicht erreichen könnt – keine Lösung, kein Produkt. Oft beginnt sie mit „Wir wollen, dass …“.
>
> ➡️ Hier zuerst eure Worte; ich helfe erst, wenn ihr keine findet.

**Lena:** Kannst du das Canvas nicht einfach für uns ausfüllen? Du weißt doch jetzt alles.

**Agent:**
> Das mache ich nicht, weil sonst lauter plausible Sätze im Canvas stünden, die wie euer Wissen aussehen, aber meine Vermutungen sind. Was ich anbiete: Ihr erzählt in euren eigenen Worten, auch unfertig, und ich ordne, frage nach und trage ein – das geht schneller, als es klingt. Also: Was soll in Kiel anders sein, wenn ihr Erfolg habt?

**Lena:** Ok. Dass niemand in Kiel abends hungrig bleiben muss.

**Agent:**
> Das ist eine gute Vision: ein gesellschaftlicher Zielzustand, keine Lösung, ein Satz. Ich übernehme sie wörtlich in Block 1.
>
> **Runde 2 von etwa 5** (danach noch drei)
>
> ❓ **F2** – **Lösung:** Beschreibt eure Idee in wenigen Sätzen: Was macht ihr, für wen? Und was macht ihr anders als Tafel, foodsharing und das Foodmobil (Fazit in `SOLUTIONS.md`)?
>
> ➡️ Eure Worte zuerst.

**Lena:** Wir holen nachmittags übrig gebliebenes Essen in der Mensa ab, kühlen es und bringen es abends zu Einrichtungen, die abends Gäste haben. Ohne App, erstmal mit einer Messenger-Gruppe.

**Agent:**
> Danke. Zwei Rückfragen, bevor ich es eintrage:
> 1. Ihr sagt „wir bringen es“. Die Tafel-Ausgabestelle hat in I1 gesagt, Abholen sei ihr Problem [A17]; und die Mensa ist um 15 Uhr fertig [A26]. Wer fährt bei euch – jeden Abend?
> 2. Ihr habt foodsharing als möglichen Partner genannt. Ist „nur bei foodsharing mitmachen“ eine Alternative, die ihr verworfen habt?

**Lena:** 1. Puh. Wir haben jede:r nur ein paar Stunden pro Woche. Dann: Die Einrichtungen holen ab, wenn sie können, sonst bringen wir es. 2. Mit foodsharing reden wir, aber erstmal probieren wir es selbst.

**Agent:**
> Notiert – Lösung mit „oder die Einrichtungen holen es selbst ab“, App und „nur foodsharing“ als verworfene Alternativen in `DECISIONS.md`. Dass die Einrichtungen meistens selbst abholen, ist damit eine wichtige Annahme; dazu gleich mehr.
>
> **Runde 3 von etwa 5** (danach noch zwei)
>
> ❓ **F3** – **Nutzer:innen und Kund:innen:** Wer nutzt euer Angebot? Wer zahlt oder ermöglicht es? Bei wem entsteht die Wirkung? Und welcher Fall des Handbuchs trifft zu: (a) dieselben, (b) verschieden – eine dritte Partei zahlt, (c) die Zielgruppe ist Teil der Wertschöpfungskette, (d) keins davon?
>
> ➡️ Ich vermute (b), aber sagt erst, wie ihr es seht.

**Lena:** Die Einrichtungen sind unsere Kunden.

**Agent:**
> Fast: Im Handbuch sind **Nutzer:innen** die, die euer Angebot nutzen – das sind die Einrichtungen, und die Wirkung entsteht bei ihren Gästen. **Kund:innen** sind die, die zahlen oder es möglich machen. Die Tagesstätte aus I2 hat gesagt: „Bezahlen können wir dafür nichts“ [A22]. Wer zahlt dann bei euch, wer ermöglicht es?

**Lena:** Ah. Dann das Studierendenwerk, das stand ja auch in Notion. Und die geben ja das Essen.

**Agent:**
> Dann ist es Fall (b): Nutzer:innen (Einrichtungen) und Kund:innen (Studierendenwerk) sind verschieden. Das Studierendenwerk hat dabei zwei Rollen: Es gibt das Essen frei – laut I3 braucht es dafür „eine Freigabe von oben und eine Haftungsregel“ [A25] –, und es soll zahlen [A5]. Beides sind bisher Annahmen.
>
> **Runde 4 von etwa 5** (danach noch eine)
>
> ❓ **F4** – **Wertangebot, je Gruppe:** Was verbessert sich für die Einrichtungen, für ihre Gäste und für das Studierendenwerk? Stützt euch auf die Interviews (z. B. I2: „abends gibt es nichts. Da kommen trotzdem Leute und fragen“). Für eine ausführliche Passung gibt es das Value Proposition Canvas von Strategyzer.com.
>
> ➡️ Eure Worte zuerst, ein Satz pro Gruppe reicht.
>
> ❓ **F5** – **Erfolgskriterien:** Woran merkt ihr, dass das Problem kleiner wird? Und was muss wahr sein, damit euer Modell trägt? Am besten mit Zahlen (wie viele Einrichtungen, wie oft) – und festgelegt, bevor ihr testet.
>
> ➡️ Wenn ihr Zahlen noch nicht zu dritt beschlossen habt, schreibe ich sie als offene Frage auf, nicht als Entscheidung.

**Lena:** F4: Einrichtungen: Sie haben abends was Warmes für ihre Gäste, ohne selbst zu kochen. Gäste: ein warmes Abendessen. Studierendenwerk: weniger in die Biogasanlage und gutes Image. F5: Wenn die Einrichtungen regelmäßig abends was Warmes von uns bekommen. Und fürs Modell: Die Mensa macht mit, die Abholung klappt, und jemand bezahlt die Kosten. Wie viele genau, das müssen wir im Team besprechen.

**Agent:**
> Eingetragen, ohne Zahlen; „wie viele Einrichtungen, wie oft“ steht unter Offene Fragen – das ganze Team, vor `/to-tests`. Zum Wertangebot: „gutes Image“ für das Studierendenwerk ist bisher nur eine Vermutung des Küchenleiters [A29].
>
> **Runde 5 von 5** (die letzte)
>
> ❓ **F6** – **Lösungs-Hypothesen:** Aus Lösung, Gruppen und Wertangebot schlage ich diese prüfbaren Aussagen vor:
> - [A35] Soziale Einrichtungen in Kiel, die abends Gäste haben, nehmen übrig gebliebenes Mensa-Essen an mehreren Abenden pro Woche an.
> - [A36] Die Einrichtungen holen das Essen an den meisten Tagen selbst in der Mensa ab.
> - [A37] Das Studierendenwerk gibt übrig gebliebenes Mensa-Essen zur Abholung frei und klärt die Haftung.
> - [A5] Das Studierendenwerk würde für so einen Service bezahlen. (gibt es schon)
> - [A30] Das Essen muss zwischen 15 Uhr und Abend gekühlt gelagert und mit dokumentierter Kühlkette übergeben werden. (gibt es schon)
>
> ➡️ Übernehmen oder umformulieren.
>
> ❓ **F7** – **Kritische Annahmen:** Kritisch ist, worauf andere Annahmen aufbauen und was die Idee kippt, wenn es fällt. Mein Vorschlag:
> - **A35** – ohne Einrichtungen, die das Essen nehmen, gibt es keine Wirkung. Die Interviews stützen das nur schwach (I2 nach dem Pitch, I4 lehnt ab).
> - **A37** – ohne Freigabe gibt es kein Essen; laut I3 geht ohne Freigabe nichts.
> - **A36** – ihr habt nur wenige Stunden pro Woche; wenn ihr jeden Abend selbst fahren müsst, trägt die Lösung nicht.
> - **A5** – ohne jemanden, der zahlt, sind Kühlung, Verpackung und Fahrten nicht gedeckt; bisher gibt es dazu keinen einzigen Hinweis.
>
> A30 schlage ich nicht als kritisch vor: Es ist eine Bedingung, die ihr mit A36 und A37 mitprüft.
>
> ➡️ Diese vier als kritisch markieren. Ihr entscheidet.

**Lena:** F6: ok, passt. F7: Ja, die vier.

*Agent schreibt Register (A35–A37, Kritisch: ja bei A5, A35, A36, A37), Canvas Blöcke 1–4 und 6, Offene Fragen, sechs Einträge in `DECISIONS.md` (Vision, Lösung, Nutzer:innen/Kund:innen, Erfolgskriterien ohne Zahlen, Lösungs-Hypothesen – „Formulierung vom Agenten vorgeschlagen, vom Team übernommen“ –, kritische Annahmen).*

```
$ python3 .claude/skills/evidence-checks/scripts/check_project.py
OK      verweise      alle Verweise stehen im Register
OK      status        37 Einträge mit gültigem Status und Quelle
OFFEN   kritische     A5: keine Testkarte; A35: keine Testkarte; A36: keine Testkarte; A37: keine Testkarte
OK      schwellen     0 Testkarten geprüft
OK      eine-annahme  jede Karte prüft eine Annahme
OK      ergebnisse    alle Ergebnisse ausgewertet, keine Karte überfällig
OK      widerlegt     keine widerlegte Annahme in MODEL.md
OK      interviews    4 von mindestens 3 Interviews ausgewertet (4 notiert)
```

**Agent:**
> Keine Fehler; dass die kritischen Annahmen noch keine Testkarten haben, ist erwartet – das kommt mit `/to-tests`. Hier die Blöcke 1–4 und 6:
>
> - **1:** Kernproblem [A6] … **Vision:** Dass niemand in Kiel abends hungrig bleiben muss.
> - **2:** Nutzer:innen = Einrichtungen mit Abendgästen; Wirkung bei den Gästen; Kund:innen = Studierendenwerk (Freigabe [A37], zahlt vermutlich [A5]); Einrichtungen zahlen nicht ([A22] für I2). Fall: eine dritte Partei zahlt.
> - **3:** Lösung in euren Worten; Wertangebot je Gruppe; Lösungs-Hypothesen [A35] [A36] [A37] [A5] [A30].
> - **4:** Erfolg = regelmäßig abends Warmes; trägt, wenn Mensa mitmacht, Abholung klappt, jemand zahlt. Zahlen offen.
> - **6:** Kritisch: A35, A37, A36, A5.
>
> Passt das?

**Lena:** Ja.

**Agent:**
> Dann schlage ich vor zu committen, dann `/to-model`.

*Commit `8 · grill-solution · Vision, Lösung ohne App, Nutzer:innen/Kund:innen, vier kritische Annahmen`.*

---

## 9 · `/to-model` (2026-10-30)

**Lena:** /to-model

*Agent liest `CANVAS.md`, `ASSUMPTIONS.md`, `PROBLEM.md`, `SOLUTIONS.md`, `DECISIONS.md`; lädt `assumptions` und `evidence-checks`. Block 1–3 sind gefüllt.*

**Agent:**
> Ich mache aus Canvas und Register euer Social Business Model Canvas. Zuerst die Gliederung – was es schon gibt und wo Lücken sind:
>
> | Feld | Schon im Register | Lücke? |
> |---|---|---|
> | 1. Gesellschaftliche Herausforderung | A6 (Annahme), A7 (Annahme), A17, A18 (belegt) | – (aus Block 1) |
> | 2. Gesellschaftliche Veränderung | Vision (Entscheidung, ohne ID) | – (aus Block 1) |
> | 3. Lösung | A35 (Annahme), A24 (belegt), A29 (Annahme) | – (aus Block 3) |
> | 4. Schlüsselaktivitäten | A30, A36 (Annahme) | **ja** – was ihr konkret tut |
> | 5. Schlüsselpartner:innen | A37 (Annahme), A32 (recherchiert) | **ja** – wer außer dem Studierendenwerk |
> | 6. Kund:innengruppen | A35, A14, A13, A5, A37 | – (aus Block 2) |
> | 7. Kund:innenbeziehung | – (A21 als Hinweis) | **ja** |
> | 8. Kanäle | – | **ja** |
> | 9. Einnahmequellen | A5 (Annahme), A22 (belegt: I2 zahlt nicht) | **ja** – wofür, wie viel |
> | 10. Kostenstruktur | – | **ja** |
>
> Sechs Lücken, also zwei Runden.
>
> **Runde 1 von 2**
>
> ❓ **F1** – **Schlüsselaktivitäten:** Was müsst ihr tun, damit es funktioniert? *Beispiele für Arten: abholen, kühlen, dokumentieren, verteilen, koordinieren.*
>
> ❓ **F2** – **Schlüsselpartner:innen:** Mit wem arbeitet ihr zusammen, wer liefert euch etwas zu – außer dem Studierendenwerk? *Beispiele für Arten: andere Initiativen, Vereine, Einrichtungen.*
>
> ❓ **F3** – **Kund:innenbeziehung:** Wie haltet ihr den Kontakt zu den Einrichtungen, damit sie bleiben? (In I2 ist der Kontakt zum Hotel „eingeschlafen“ [A21].) *Beispiele: persönliche Ansprechperson, feste Zeiten, eine Gruppe.*
>
> ❓ **F4** – **Kanäle:** Wie erreicht ihr Einrichtungen und Studierendenwerk – wo begegnen sie euch? *Beispiele: Telefon, Besuch, E-Mail, über Bekannte.*

**Lena:** F1: Essen abholen, in Kühlboxen packen, Temperatur aufschreiben, abends verteilen, die Messenger-Gruppe organisieren. F2: Die Mensa halt, die Einrichtungen, vielleicht foodsharing, die könnten mit abholen oder uns Tipps geben. F3: Eine feste Ansprechperson pro Einrichtung, damit's nicht einschläft wie beim Hotel. F4: Einrichtungen anrufen und vorbeigehen. Studierendenwerk über den Küchenleiter.

**Agent:**
> Eingetragen als A38 (Aktivitäten), A39 (foodsharing als Partner), A40 (Ansprechperson), A41 (Kanäle) – alles *Annahme*. Die Einrichtungen sind eure Nutzer:innen, die stehen schon im Feld 6.
>
> **Runde 2 von 2**
>
> ❓ **F5** – **Einnahmequellen:** Wer zahlt wofür, und wie viel? *Beispiele für Arten: ein Auftrag oder eine Pauschale, eine Stiftung, Spenden, öffentliche Förderung.*
>
> ❓ **F6** – **Kostenstruktur:** Welche Kosten habt ihr – einmalig und laufend – und welche sind am größten?

**Lena:** F5: Das Studierendenwerk zahlt eine Pauschale für die Abholung. Wenn nicht, eine Stiftung. Wie viel, weiß ich nicht. F6: Kühlboxen, Verpackungen, Fahrtkosten. Ist ja nicht viel.

**Agent:**
> „Ist ja nicht viel“ schreibe ich nicht als Zahl auf, sondern als offene Frage: Was kosten Kühlboxen, Verpackungen und Fahrten im Monat – und wie hoch müsste eine Pauschale oder Förderung sein? Wer klärt das bis wann?

**Lena:** Ahmet, der kann das. Bis zum 13. November.

**Agent:**
> Notiert. Und die Stiftung: Was hätte sie davon, euch zu fördern? Das braucht ihr fürs Feld *Lösung*, weil sie dann eine eurer Kund:innen wäre.

**Lena:** Die wollen ja Projekte fördern, die was bewirken. Ein Ehrenamtsprojekt halt.

**Agent:**
> Dann steht die Gliederung. Passt sie so – kann ich `MODEL.md` schreiben?

**Lena:** Ja.

*Agent schreibt `MODEL.md` (alle zehn Felder mit IDs; Lösung und Kund:innengruppen für Nutzer:innen und Kund:innen getrennt; Quellenvermerk bleibt), Register A38–A43, Block 7 im Canvas, offene Fragen zu Beträgen. Dann prüft er.*

```
$ python3 .claude/skills/evidence-checks/scripts/check_project.py
OK      verweise      alle Verweise stehen im Register
OK      status        43 Einträge mit gültigem Status und Quelle
OFFEN   kritische     A5: keine Testkarte; A35: keine Testkarte; A36: keine Testkarte; A37: keine Testkarte
…
```

**Agent:**
> Keine Fehler. Drei Funde aus den Review-Checks, je mit Vorschlag:
>
> **1. Wer zahlt, steht nicht vollständig in Block 2.** *Was und wo:* Im Modell (Feld 9) zahlt notfalls eine Stiftung [A42]; in Block 2 des Canvas steht nur das Studierendenwerk. *Warum wichtig:* Canvas und Modell sollen sich nicht widersprechen. *Optionen:* (a) Stiftung in Block 2 als mögliche Kund:in ergänzen *(Empfehlung)* – dann passt beides zusammen; (b) Stiftung aus dem Modell nehmen – dann hängt alles am Studierendenwerk.
>
> **2. Eine Annahme, auf der viel aufbaut, ist nicht kritisch.** *Was und wo:* A42 (Stiftung fördert) trägt Feld 3, 6 und 9, sobald das Studierendenwerk nicht zahlt. *Warum wichtig:* Bisher gibt es keinen einzigen Hinweis, dass das Studierendenwerk zahlt [A5]. *Optionen:* (a) A42 als kritisch markieren *(Empfehlung)* – dann bekommt sie eine Testkarte; (b) nicht kritisch – dann gibt es keinen geprüften Plan B.
>
> **3. Ob die Einnahmen die Kosten decken, ist nicht zu sagen.** *Was und wo:* Feld 9 und 10 haben keine Beträge. *Warum wichtig:* Ein Modell ohne Zahlen kann tragen oder nicht – das weiß noch niemand. Ich rechne das nicht selbst. *Optionen:* (a) als offene Frage stehen lassen, Ahmet klärt bis 13.11. *(Empfehlung)*; (b) jetzt Schätzungen eintragen – die würden aussehen wie Wissen.

**Lena:** 1a, 2a – wenn das Studierendenwerk nicht zahlt, brauchen wir das. 3a.

*Agent markiert A42 als kritisch, ergänzt Block 2 und 6, hält drei Entscheidungen in `DECISIONS.md` fest (Gliederung, Beträge offen, Stiftung).*

**Agent:**
> Erledigt. Das Modell steht in `MODEL.md`; jede Aussage hat ihre ID, Beträge sind offene Fragen. Fünf kritische Annahmen brauchen jetzt Testkarten. Ich schlage vor zu committen, dann `/to-tests`.

**Lena:** Ok.

*Commit `9 · to-model · Social Business Model Canvas, Stiftung als Plan B, Beträge offen`.*

---

## 10 · `/to-tests` (2026-11-02)

**Lena:** /to-tests

*Agent liest `ASSUMPTIONS.md`, `CANVAS.md` (Block 4 und 6), `MODEL.md`, `TESTS.md` (leer), `DECISIONS.md`; lädt `assumptions` und `evidence-checks`. Kritisch und offen: A35, A36, A37, A5, A42.*

**Agent:**
> Ich entwerfe für jede eurer fünf kritischen Annahmen eine Testkarte – eine Karte pro Annahme, mit eigener Schwelle. Bevorzugt Tests, die Verhalten zeigen, nicht Meinungen. Zuerst eine Frage, damit ich den Plan nicht größer mache, als ihr schaffen könnt: **Wie viel Zeit habt ihr zusammen pro Woche, und bis wann soll die Testrunde fertig sein?**

**Lena:** Zusammen etwa zwölf Stunden pro Woche. Bis zum 13. November, da ist Ahmet auch mit den Kosten fertig.

**Agent:**
> Danke. Hier zuerst die **Probleme**, die ich im Plan sehe, jeweils mit Empfehlung – danach die Karten.
>
> 1. **Reihenfolge.** Die Probewoche (T2, T3) braucht Essen aus der Mensa – und laut I3 geht ohne „Freigabe von oben und eine Haftungsregel“ nichts [A25]. ➡️ Das Gespräch mit dem Studierendenwerk (T1) zuerst; T1 ist *Voraussetzung* von T2 und T3.
> 2. **T4 (Studierendenwerk zahlt) nur mit einer Meinung prüfen.** Die Frage „Würden Sie dafür zahlen?“ beantwortet man höflich. ➡️ Ein schriftliches Angebot mit Preis schicken und schauen, ob es angenommen wird – das zeigt Verhalten.
> 3. **Die Schwelle für T2 übernimmt eine offene Zahl.** „Wie viele Einrichtungen“ steht noch als offene Frage im Canvas. Ich schlage vor: *mindestens 3 von 4 Einrichtungen nehmen an mindestens 3 von 5 Tagen an* – niedriger (z. B. 2 von 4) würde fast jedes Ergebnis erfüllen. ➡️ Bitte bestätigt ausdrücklich, ob ihr **zu dritt** diese Zahl beschlossen habt; sonst bleibt die Karte offen.
> 4. **Zeit.** Wenn die Einrichtungen nicht selbst abholen (T3), fahrt ihr eine Woche lang jeden Abend. ➡️ Plant dafür Stunden ein, bevor ihr startet.
> 5. **T5 (Stiftung) hat eine eher niedrige Schwelle** (1 von 2). ➡️ Ok für einen ersten Schritt, aber eine Bestätigung der Förderbarkeit ist noch keine Zusage.
>
> *(Agent zeigt die fünf Karten T1–T5 – Wortlaut wie in `TESTS.md`.)*
>
> | Karte | Annahme | Test | Schwelle |
> |---|---|---|---|
> | T1 | A37 Freigabe | Gespräch mit Abteilungsleitung Hochschulgastronomie + Küchenleiter | Freigabe zugesagt, ohne offene Bedingung (Haftung geregelt) |
> | T2 | A35 Einrichtungen nehmen an | Probewoche mit 4 Einrichtungen | mind. 3 von 4 nehmen an mind. 3 von 5 Tagen an |
> | T3 | A36 selbst abholen | dieselbe Probewoche, pro Tag notieren, wer abholt | jede annehmende Einrichtung holt an mind. 4 von 5 Tagen selbst ab |
> | T4 | A5 Studierendenwerk zahlt | schriftliches Angebot mit Preis | Angebot angenommen |
> | T5 | A42 Stiftung | Anfrage an 2 Stiftungen | mind. 1 von 2 bestätigt schriftlich Förderbarkeit mit Betrag und Frist |
>
> Ihr entscheidet: welche Tests, welche Reihenfolge, welche Schwellen.

**Lena:** 1: ok, passt. 2: Nee, das Angebot mit Preis machen wir nicht. Wir haben noch keinen Preis, Ahmet rechnet erst. Und der Küchenleiter hat gesagt, ohne Freigabe von oben läuft gar nichts – da wollen wir nicht gleich mit einer Rechnung kommen. Wir fragen im Gespräch einfach, ob die was übernehmen. 3: Moment, ich frag Ahmet und Jule im Chat. … Beide sagen ja, 3 von 4. 4: Ok. 5: Lassen wir so. Bei T2: Wir fragen auch das Jugendzentrum, vielleicht ja doch.

**Agent:**
> Verstanden, ich halte die Ablehnung mit eurer Begründung in `DECISIONS.md` fest. Damit T4 trotzdem möglichst viel zeigt, formuliere ich die Karte so: Ihr fragt im Gespräch **konkret**, ob das Studierendenwerk einen Teil der Kosten übernimmt (Pauschale, Material oder Fahrten), und schreibt die Antwort wörtlich auf. Schwelle: *Das Studierendenwerk sagt eine konkrete Geldleistung zu und nennt Art und Größenordnung.* Der Haken: Ein „Ja“ im Gespräch ist noch keine Zahlung. Ein „Nein, dafür haben wir kein Geld“ zählt dagegen voll, weil die Organisation das über sich selbst sagt. Ok so?

**Lena:** Ja, ok.

**Agent:**
> Und die Zahl „3 von 4“ halte ich als Beschluss von euch dreien fest (Lena, Ahmet, Jule, 2026-11-02); in Block 4 steht sie als Kriterium für die Probewoche.

*Agent schreibt `TESTS.md` (T1–T5, Status geplant, Ausgewertet nein), Spalte *Test* im Register, Block 9 (Liste der Tests mit Annahme und Schwelle), Block 4, Offene Fragen, drei Einträge in `DECISIONS.md` (Testplan und Reihenfolge; Schwelle T2 vom ganzen Team; kein Preisangebot – Empfehlung des Agenten abgelehnt).*

```
$ python3 .claude/skills/evidence-checks/scripts/check_project.py
OK      verweise      alle Verweise stehen im Register
OK      status        43 Einträge mit gültigem Status und Quelle
OK      kritische     5 offene kritische Annahmen haben eine Testkarte mit Schwelle
OK      schwellen     5 Testkarten geprüft
OK      eine-annahme  jede Karte prüft eine Annahme
OK      ergebnisse    alle Ergebnisse ausgewertet, keine Karte überfällig
OK      widerlegt     keine widerlegte Annahme in MODEL.md
OK      interviews    4 von mindestens 3 Interviews ausgewertet (4 notiert)
```

**Agent:**
> *kritische* und *eine-annahme* sind OK. Bitte committet die Karten **jetzt**, bevor ihr testet: So bleibt im Git-Verlauf sichtbar, dass die Schwellen vor den Ergebnissen feststanden.
>
> Dann seid ihr dran: zuerst das Gespräch mit dem Studierendenwerk (T1, T4), dann die Probewoche (T2, T3), parallel die Stiftungen (T5). Ergebnisse tragt ihr in `TESTS.md` ein oder fügt sie in den Chat ein – danach `/log-evidence`.

**Lena:** Mach den Commit.

*Commit `10 · to-tests · Testkarten T1–T5 mit Schwellen, vor dem Testen committet`.*

---

## Zwischen den Skills: Testrunde (2.–13. November)

Das Team führt das Gespräch mit dem Studierendenwerk, die Probewoche und die Anfragen an zwei Stiftungen durch. Die Ergebnisse schreibt Lena nicht in die Datei, sondern fügt sie beim nächsten Befehl in den Chat ein.

---

## 11 · `/log-evidence` (2026-11-16)

**Lena:** /log-evidence – hier unsere Ergebnisse:

> **Gespräch mit dem Studierendenwerk (Abteilungsleitung Hochschulgastronomie):** „Finden wir gut, machen wir gern mit, wenn die Haftung geklärt ist. Bezahlen können wir dafür aber nichts, höchstens Verpackungen stellen.“
>
> **Probewoche:** Vier Einrichtungen wurde angeboten, eine Woche lang abends übrig gebliebenes Mensa-Essen zu bringen. Zwei haben zugesagt und es an mindestens drei Tagen angenommen (Tafel-Ausgabestelle, Tagesstätte). Eine hat abgelehnt (Jugendzentrum: „passt nicht zu uns“), eine hat nicht geantwortet. Die Tafel konnte nur zwei von fünf Tagen selbst abholen; an den anderen Tagen hat das Team geliefert.
>
> **Stiftungen:** Eine hat geantwortet: Förderung für Ehrenamtsprojekte bis 5.000 € möglich, Antrag bis März. Die andere hat nicht geantwortet.

*Agent liest `ASSUMPTIONS.md`, `INTERVIEWS.md`, `TESTS.md`, `PROBLEM.md`, `CANVAS.md`, `SIGNALS.md`; lädt `assumptions` und `evidence-checks`. Karten T1–T5 haben noch kein Ergebnis.*

**Agent:**
> Danke! Ich übertrage die Ergebnisse zuerst wörtlich in `TESTS.md`, ins Feld *Ergebnis* der passenden Karte. So würde ich zuordnen:
>
> | Ergebnis | Karte(n) |
> |---|---|
> | Gespräch Studierendenwerk | **T1** (Freigabe) und **T4** (zahlt) – derselbe Wortlaut in beiden Karten |
> | Probewoche | **T2** (nehmen an) und **T3** (holen selbst ab) – derselbe Wortlaut in beiden Karten |
> | Stiftungen | **T5** |
>
> Stimmt die Zuordnung? Und zwei Rückfragen zu Messgrößen, die im Ergebnis fehlen:
> 1. **T3** zählt pro Einrichtung, an wie vielen Tagen sie selbst abgeholt hat. Für die Tafel steht es da (2 von 5). Wie oft hat die **Tagesstätte** selbst abgeholt?
> 2. **T5** verlangt eine **schriftliche** Bestätigung. Kam die Antwort der Stiftung schriftlich, und als Antwort auf eure Anfrage zu eurem Projekt?

**Lena:** Zuordnung stimmt. 1: Haben wir nicht aufgeschrieben. Weiß ich nicht genau. 2: Ja, per Mail, als Antwort auf unsere Anfrage.

**Agent:**
> Ok. Bei T3 ändert die fehlende Zahl nichts am Ergebnis, weil die Schwelle für *jede* annehmende Einrichtung gilt und die Tafel sie schon verfehlt – ich notiere aber, dass sie fehlt.
>
> Zwei Dinge, bevor ich Status vorschlage:
>
> - **Voraussetzung nicht bestanden.** T2 und T3 hatten T1 (Freigabe) als Voraussetzung. T1 ist nicht bestanden: „machen wir gern mit, **wenn die Haftung geklärt ist**“ ist eine Zusage unter Bedingung – T1 bleibt auf *läuft*. Kann das Ergebnis der Probewoche an der fehlenden Freigabe liegen? Die Absage („passt nicht zu uns“) und die fehlende Antwort hängen nicht daran, und die Tafel konnte aus eigenen Gründen nicht abholen. Ich schlage deshalb trotzdem einen Status vor und schreibe den Vorbehalt in die Quelle.
> - **Schwellen wörtlich:** Ich vergleiche jedes Ergebnis mit der Schwelle, die ihr am 02.11. committet habt (der Git-Verlauf zeigt: Karten vor den Ergebnissen).
>
> **Abschnitt 1 von 4 – vorgeschlagen als *widerlegt***
>
> | ID | Aussage | bisher | Vorschlag | Ergebnis gegen Schwelle | Bedenken |
> |---|---|---|---|---|---|
> | A35 | Soziale Einrichtungen in Kiel, die abends Gäste haben, nehmen übrig gebliebenes Mensa-Essen an mehreren Abenden pro Woche an. | Annahme | **widerlegt** | T2: 2 von 4 Einrichtungen; Schwelle „mindestens 3 von 4“ → nicht erreicht | Voraussetzung T1 offen (s. o.) |
> | A36 | Die Einrichtungen holen das Essen an den meisten Tagen selbst ab. | Annahme | **widerlegt** | T3: Tafel 2 von 5 Tagen; Schwelle „jede an mind. 4 von 5“ → nicht erreicht | Tagesstätte nicht notiert; Voraussetzung T1 offen |
> | A5 | Das Studierendenwerk würde für so einen Service bezahlen. | Annahme | **widerlegt** | T4: „Bezahlen können wir dafür aber nichts, höchstens Verpackungen stellen.“ Schwelle: konkrete Geldleistung → nicht erreicht | eine Aussage der Organisation über sich selbst – zählt |
>
> Bitte entscheidet jede Zeile einzeln.

**Lena:** Hm. 2 von 4 ist doch auch gut, können wir das nicht als belegt nehmen?

**Agent:**
> Ich verstehe den Wunsch – zwei Einrichtungen haben wirklich mitgemacht, das ist ein Ergebnis. Aber die Schwelle „3 von 4“ habt ihr zu dritt **vor** dem Test beschlossen und committet. Wenn wir sie jetzt senken, passt sie zufällig genau zum Ergebnis – dann ist das Ergebnis nur noch ein Signal, kein Beleg. Eine Schwelle wird nie gelockert, damit sie besteht.
>
> Was ihr stattdessen festhalten könnt: Die zwei, die angenommen haben, haben etwas gemeinsam – beide haben abends Gäste und kochen abends selbst nicht. Das schlage ich unten als neue, engere Annahme vor (A49). Die könnt ihr in der nächsten Runde mit eigener Schwelle testen.

**Lena:** Ok, verstehe. Dann widerlegt, aber die zwei, die mitgemacht haben, sind ja auch was. A35 widerlegt ja, A36 widerlegt ja, A5 widerlegt ja.

**Agent:**
> **Abschnitt 2 von 4 – vorgeschlagen als *belegt***
>
> | ID | Aussage | bisher | Vorschlag | Beleg | Bedenken |
> |---|---|---|---|---|---|
> | A42 | Eine Stiftung fördert das Projekt, wenn das Studierendenwerk nicht zahlt. | Annahme | **belegt** | T5: 1 von 2 bestätigt schriftlich, mit Betrag (bis 5.000 €) und Frist (März); Schwelle erreicht | Die Schwelle misst Förderbarkeit, keine Zusage – der Antrag ist nicht gestellt. Vorbehalt kommt in die Quelle. |
> | A44 (neu) | Die Tafel-Ausgabestelle aus I1 und die Tagesstätte aus I2 haben in der Probewoche an mindestens drei von fünf Tagen abends Mensa-Essen angenommen. | – | **belegt** | T2 (Beobachtung) | – |
> | A45 (neu) | Das Jugendzentrum aus I4 hat das Essen in der Probewoche abgelehnt: „passt nicht zu uns“. | – | **belegt** | T2 | – |
> | A46 (neu) | Die Tafel-Ausgabestelle aus I1 konnte in der Probewoche nur an zwei von fünf Tagen selbst abholen; an den anderen Tagen hat das Team geliefert. | – | **belegt** | T3 | – |
> | A47 (neu) | Das Studierendenwerk kann für den Service nichts bezahlen, höchstens Verpackungen stellen. | – | **belegt** | T4 | Aussage über sich selbst |

**Lena:** A42 ja, mit dem Vorbehalt. A44 ja, A45 ja, A46 ja, A47 ja.

**Agent:**
> **Abschnitt 3 von 4 – vorgeschlagen als *belegt***
>
> | ID | Aussage | bisher | Vorschlag | Beleg | Bedenken |
> |---|---|---|---|---|---|
> | A48 (neu) | Eine der zwei angefragten Stiftungen fördert Ehrenamtsprojekte mit bis zu 5.000 €; Antrag bis März. | – | **belegt** | T5 | Aussage der Stiftung über sich selbst |

**Lena:** A48 ja.

**Agent:**
> **Abschnitt 4 von 4 – Status bleibt, neue Annahme**
>
> | ID | Aussage | Status | Begründung |
> |---|---|---|---|
> | A37 | Das Studierendenwerk gibt das Essen frei und klärt die Haftung. | bleibt *Annahme*; T1 bleibt *läuft*, *Ausgewertet: teilweise* | „machen wir gern mit, wenn …“ ist eine Absicht unter Bedingung |
> | A49 (neu) | Einrichtungen, die abends Gäste haben und abends selbst nicht kochen (wie Tafel-Ausgabestelle und Tagesstätte), nehmen übrig gebliebenes Mensa-Essen an mehreren Abenden pro Woche an. | *Annahme*, „gestützt durch T2“ | zwei von zwei Einrichtungen dieser Art haben angenommen – das ist ein starker Hinweis, aber ohne eigene Schwelle kein Beleg |

**Lena:** passt.

*Agent schreibt: Ergebnisse wörtlich mit Vergleich gegen die Schwelle in T1–T5 (T1: Status läuft, Ausgewertet teilweise; T2–T5: abgeschlossen, ja); Register (A35, A36, A5 widerlegt; A42 belegt mit Vorbehalt; A44–A48 belegt; A49 Annahme; Quelle von A37); `SIGNALS.md` (Testrunde; Wunsch, die Schwelle zu senken); `DECISIONS.md` (Schwelle T2 bleibt); Canvas Block 5, 6 (Stand ersetzt), 10 und je eine Zeile `⚠️ [A…] widerlegt (T…) – prüfen` in den Blöcken 2, 3, 6, 7 und 9. `MODEL.md` bleibt unverändert.*

```
$ python3 .claude/skills/evidence-checks/scripts/check_project.py
OK      verweise      alle Verweise stehen im Register
OK      status        49 Einträge mit gültigem Status und Quelle
OK      kritische     1 offene kritische Annahmen haben eine Testkarte mit Schwelle
OK      schwellen     5 Testkarten geprüft
OK      eine-annahme  jede Karte prüft eine Annahme
OFFEN   ergebnisse    läuft (Bedingung offen): T1
OFFEN   widerlegt     widerlegte oder ersetzte Annahmen in MODEL.md: A35, A36, A5 – prüfen, ob das Feld noch darauf aufbaut
OK      interviews    4 von mindestens 3 Interviews ausgewertet (4 notiert)
```

**Agent:**
> Keine Fehler. Die zwei OFFEN sind gewollt: T1 wartet auf die Haftungsregel, und drei Felder in `MODEL.md` bauen auf widerlegten Annahmen auf – das ändere ich hier nicht, das klärt ihr im Review.
>
> Ich schlage vor zu committen, dann `/review-model`.

*Commit `11 · log-evidence · Testrunde ausgewertet: A35, A36, A5 widerlegt, A42 belegt, T1 läuft`.*

---

## 12 · `/review-model` (2026-11-18)

**Lena:** /review-model

*Agent liest alle Projektdateien und die letzten Einträge in `SIGNALS.md`, führt `check_project.py` aus, lädt `evidence-checks` und `assumptions`. Sub-Agenten stehen in dieser Umgebung nicht zur Verfügung; der Agent prüft die zwei Achsen nacheinander. Für die Reihenfolge von Schwelle und Ergebnis liest er den Git-Verlauf: `git log -- TESTS.md` zeigt die Karten im Commit vom 02.11., die Ergebnisse im Commit vom 16.11.*

**Agent:**
> Bevor ich den Bericht schreibe, eine Frage zu Achse 2: Ahmet wollte bis 13.11. die Kosten schätzen (Kühlboxen, Verpackungen, Fahrten) und wie hoch eine Förderung sein müsste. Gibt es die Zahlen?

**Lena:** Haben wir noch nicht rausgefunden. Ahmet hatte keine Zeit.

**Agent:**
> Ok, dann ist das ein Befund, keine Rechnung von mir. Hier der Bericht. *Blockierend heißt: Das solltet ihr klären, bevor ihr darauf weiterbaut – es heißt nicht, dass ihr aufhören müsst.*
>
> **Achse 1: Beleg**
>
> | # | Befund | Art | Beleg | Vorschlag |
> |---|---|---|---|---|
> | 1 | Drei kritische Annahmen sind widerlegt und tragen noch Felder in `MODEL.md` (Lösung, Aktivitäten, Kund:innengruppen, Einnahmen). | **blockierend** | A35 (T2), A36 (T3), A5 (T4); Check *widerlegt* | Modell mit `/to-model` anpassen |
> | 2 | Die Freigabe ist offen, und die Probewoche lief, obwohl ihre Voraussetzung T1 nicht bestanden war. | **blockierend** | A37, T1 „wenn die Haftung geklärt ist“ | Haftungsregel klären, bevor ihr regelmäßig abholt |
> | 3 | A42 ist belegt, aber die Schwelle von T5 maß nur Förderbarkeit – kein Euro ist zugesagt. | Hinweis | T5, A48 | Nächste Karte: Antrag bewilligt |
> | 4 | Zahlungsbereitschaft wurde im Gespräch erfragt, nicht durch ein Angebot geprüft. Für die Widerlegung reicht das (Aussage über sich selbst), für ein Ja hätte es nicht gereicht. | Hinweis | T4, `DECISIONS.md` 2026-11-02 | – |
> | 5 | In T3 fehlt die Messgröße für die Tagesstätte. | Hinweis | T3 | Bei der nächsten Probe pro Tag und Einrichtung notieren |
> | 6 | Canvas und Modell sagen „Studierendenwerk zahlt“, das ist widerlegt. | **blockierend** | Block 2, Block 7, `MODEL.md` Feld 6 und 9; A5 | mit `/to-model` auflösen |
> | 7 | Das Kernproblem [A6] und die Ursache [A7] sind weiter nur Annahmen; Gäste hat niemand befragt. | Hinweis | `PROBLEM.md`, *Noch offen* | Gäste über die Einrichtungen befragen |
>
> Schwellen standen vor den Ergebnissen (Git-Verlauf). Belegte Aussagen stimmen mit Notizen und Ergebnissen überein. Die meisten Felder von `MODEL.md` beruhen jetzt auf A37 (Freigabe, offen) und A42 (Geld, nur förderbar).
>
> **Achse 2: Wirkung**
>
> | # | Befund | Art | Beleg | Vorschlag |
> |---|---|---|---|---|
> | 8 | Das Modell dient der Vision: Zwei Einrichtungen ohne eigenes Abendessen haben an mindestens drei Abenden Essen angenommen. Ob es bei den Gästen ankommt, wisst ihr nicht. | Hinweis | A44; keine Daten zu Gästen | Gäste fragen oder Portionen zählen |
> | 9 | Trägt es sich? Es fehlen: Kosten pro Monat, Höhe der nötigen Förderung, ob 5.000 € reichen. Wer zahlt, ist nicht belegt (Studierendenwerk widerlegt, Stiftung nur förderbar). | **blockierend** | A5, A42, A43, A48; offene Frage überfällig | Kosten schätzen, bevor ihr einen Antrag schreibt |
> | 10 | Wer fährt? Die Tafel holt an 3 von 5 Tagen nicht selbst ab; ihr habt zusammen etwa 12 Stunden pro Woche. | **blockierend** | A36, A46; `DECISIONS.md` 2026-11-02 | Liefern als eigene Aktivität planen und testen, wer fährt |
> | 11 | Das Kriterium für die Probewoche (3 von 4) ist nicht erfüllt. | Hinweis | Block 4, T2 | – |
> | 12 | Nutzer:innen/Kund:innen: Das Studierendenwerk ist jetzt eher Partner (Freigabe, Verpackungen) als Kund:in; Kund:in wäre die Stiftung. Fall (b) bleibt. | Hinweis | A47, A48 | in `/to-model` in Block 2 und Feld 6 umstellen |
>
> **Drei Wege**
>
> - **Weiter testen** – steht nicht zur Wahl, ohne dass ihr erklärt, warum drei Widerlegungen nichts ändern.
> - **Anpassen** – geht hier, weil es für jede widerlegte kritische Annahme eine engere Ersatz-Annahme gibt, die eure eigenen Tests stützen: A49 statt A35 (T2: beide Einrichtungen ohne Abendessen nahmen an); die Stiftung statt des Studierendenwerks als Geldgeber (T5); Liefern durch das Team an Tagen ohne Abholung (T3, so ist es in der Probewoche gelaufen). *Dafür:* Die Richtung trägt. *Dagegen:* Geld und Fahrten sind nicht gelöst, nur verschoben. → danach `/to-model`, dann `/to-tests`.
> - **Neu ansetzen (Pivot)** – *Dafür:* Drei von fünf kritischen Annahmen sind gefallen. *Dagegen:* Für jede gibt es eine gestützte Ersatz-Annahme. → `/grill-solution`.
>
> **Entscheidungen** (der Weg zuletzt)
>
> **E1 – Stiftung (A42).** *Was und wo:* A42 ist belegt, aber T5 maß nur Förderbarkeit. *Warum wichtig:* Euer Modell hängt jetzt am Geld der Stiftung. *Einschränkung:* Antrag bis März. *Optionen:* (a) als Nächstes testen, ob der Antrag bewilligt wird *(Empfehlung)* – dann wisst ihr, ob Geld kommt; (b) A42 als ausreichend belegt ansehen – dann plant ihr mit Geld, das niemand zugesagt hat.
>
> **E2 – Fahrten (A36 widerlegt).** *Was und wo:* Die Tafel holt nur an 2 von 5 Tagen selbst ab. *Warum wichtig:* Ohne Fahrten keine Wirkung; eure Zeit ist begrenzt. *Optionen:* (a) Ihr liefert an Tagen ohne Abholung und testet in der nächsten Runde, wer diese Fahrten dauerhaft übernimmt *(Empfehlung)*; (b) nur Einrichtungen beliefern, die selbst abholen – dann fällt die Tafel weg; (c) nur an Abholtagen – die Tafel bekäme an 3 von 5 Tagen nichts.
>
> **E3 – Nutzer:innen.** *Was und wo:* Angenommen haben nur Einrichtungen ohne eigenes Abendessen (A44); abgelehnt hat das Jugendzentrum, das selbst kocht (A45). *Optionen:* (a) nächste Runde nur Einrichtungen wie in A49 *(Empfehlung)*; (b) weiter alle sozialen Einrichtungen.
>
> **E4 – Weg.** (a) **Anpassen** *(Empfehlung)*; (b) Neu ansetzen; (c) Weiter testen – nur mit Begründung, warum die Widerlegungen nichts ändern.

**Lena:** E1 a. E2 a. E3 a. E4: Anpassen. Die Richtung stimmt, zwei Einrichtungen wollen es ja. Nur das Geld und das Fahren müssen anders.

*Agent trägt ein: vier Entscheidungen in `DECISIONS.md`, Block 11 (Weg, was sich ändert, was als Nächstes getestet wird), Block 8 (Stand der Checks), Offene Fragen (Kosten überfällig, neuer Termin), einen Eintrag in `SIGNALS.md` (Quelle *Review*). `MODEL.md` bleibt unverändert – das macht `/to-model`.*

```
$ python3 .claude/skills/evidence-checks/scripts/check_project.py
OK      verweise      alle Verweise stehen im Register
OK      status        49 Einträge mit gültigem Status und Quelle
OK      kritische     1 offene kritische Annahmen haben eine Testkarte mit Schwelle
OK      schwellen     5 Testkarten geprüft
OK      eine-annahme  jede Karte prüft eine Annahme
OFFEN   ergebnisse    läuft (Bedingung offen): T1
OFFEN   widerlegt     widerlegte oder ersetzte Annahmen in MODEL.md: A35, A36, A5 – prüfen, ob das Feld noch darauf aufbaut
OK      interviews    4 von mindestens 3 Interviews ausgewertet (4 notiert)
```

**Agent:**
> Der Weg steht. Ich schlage vor zu committen, dann `/model-retro` – und danach `/to-model`, das zum Weg „Anpassen“ gehört.

*Commit `12 · review-model · Zwei-Achsen-Review, Weg: Anpassen`.*

---

## 13 · `/model-retro` (2026-11-23)

**Lena:** /model-retro

*Agent liest `SIGNALS.md`, `DECISIONS.md`, `CANVAS.md`, `ASSUMPTIONS.md`, `TESTS.md` und die Einträge des Reviews; lädt `assumptions` und `evidence-checks`; sieht sich `git log` und die Check-Ausgabe an.*

**Agent:**
> Wir machen aus dem, was passiert ist, die nächste Runde besser – für euer Projekt und für das Skillset. Eine Runde Fragen:
>
> 1. Was lief anders als geplant?
> 2. Was hat euch überrascht?
> 3. Wo habt ihr festgesteckt?
> 4. Welche Entscheidung hat sich im Nachhinein als voreilig erwiesen?
> 5. Wo habe ich etwas getan oder vorgeschlagen, das nicht gepasst hat?

**Lena:** 1. Die Tafel konnte nicht abholen, wir sind dreimal gefahren, das hat viel Zeit gekostet. 2. Dass das Studierendenwerk nichts zahlt, obwohl die das gut finden. 3. Bei den Kosten, Ahmet kam nicht dazu. 4. Dass wir der Tagesstätte die Idee erzählt haben. Und die Probewoche vor der Haftung. 5. Das Angebot mit Preis ging nicht, wir hatten ja keinen Preis. Und die Tabellen bei log-evidence waren ganz schön lang.

**Agent:**
> Danke. Dazu kommt, was ich selbst nachsehen kann: die Check-Ausgabe (T1 läuft, widerlegte Annahmen im Modell), der Git-Verlauf (Karten am 02.11. vor den Ergebnissen am 16.11. – das hat funktioniert) und die Signale aus `SIGNALS.md`. Zu jedem Signal zuerst die Ursache – und die Frage, **warum kein Check es gefunden hat**:
>
> | Signal | Ursache | Warum hat kein Check es gefunden? |
> |---|---|---|
> | Probewoche vor der Freigabe (T2/T3 vor T1) | Ein „gern, wenn …“ wurde als Startsignal gelesen | `check_project.py` prüft nur, ob es die Voraussetzung **gibt**, nicht, ob sie **bestanden** ist, bevor ein Ergebnis kommt |
> | A42 „Stiftung fördert“ belegt, obwohl nichts zugesagt ist | Die Schwelle von T5 maß Förderbarkeit, nicht das, was A42 sagt | `/to-tests` hat die niedrige Schwelle genannt, aber kein Check vergleicht Schwelle und Wortlaut der Annahme – das kann nur ein Mensch |
> | Pitch in I2 | Gegen den Leitfaden; die Begeisterung im Gespräch | Gefunden – aber erst beim Auswerten, also nachdem die Antwort schon verbraucht war |
> | Frage A-3 (warum es abends so ist) nie beantwortet | Nicht gestellt oder nicht notiert | Kein Check vergleicht Leitfragen und Notizen; `/log-evidence` hat es nur zufällig bemerkt |
> | Tagesstätte in T3 ohne Zahl | Keine Liste pro Tag und Einrichtung | Die Messgröße steht auf der Karte, aber niemand hatte ein Blatt dafür |
> | Kosten fehlen (fällig 13.11.) | Keine Zeit; niemand hat nachgehalten | `check_project.py` liest die Offenen Fragen nicht |
> | Mein Vorschlag „Angebot mit Preis“ | Ich habe einen Test vorgeschlagen, für den eine Zahl fehlte, die selbst noch offene Frage war | `/to-tests` hat keine Prüfung dafür |
> | Wunsch, die Schwelle zu senken | Ihr wolltet ein Erfolgserlebnis – verständlich | Die Regel „nie einen Check lockern“ hat gegriffen – hier ist nichts zu tun |
>
> **Vorschläge** (nummeriert, mit Beleg und Empfehlung):
>
> *Jetzt korrigieren*
> 1. **A42** sagt „Eine Stiftung fördert das Projekt“, T5 zeigt nur, dass sie fördern **kann**. ➡️ A42 zurück auf *Annahme*, Quelle „ersetzt durch A48; Bewilligung offen“. (Beleg: T5, A48.) Das weicht vom Review ab, wo A42 mit Vorbehalt belegt blieb.
>
> *Checks für euer Projekt (Block 8, durch das Team)*
> 2. Vor jedem Interview *Nicht fragen* vorlesen; danach jede Leitfrage abhaken oder als „nicht gestellt“ notieren. (I2, A-3)
> 3. Strichliste pro Tag und Einrichtung bei jeder Probe. (T3)
> 4. Ein Test startet erst, wenn seine Voraussetzung abgeschlossen ist – sonst bewusst entscheiden und festhalten. (T1/T2)
> 5. Eine Schwelle misst, was die Annahme sagt. (T5)
> 6. Offene Fragen mit Termin bei jedem `/ask-model` durchgehen. (Kosten)
>
> *Canvas und Modell*
> 7. Block 2, Block 7 und `MODEL.md` (Felder 3, 4, 6, 9) bauen auf widerlegten Annahmen – das ist schon als nächster Schritt `/to-model` entschieden; hier keine zusätzliche Änderung.
>
> *Skill-Regeln* (in `SKILL-PROPOSALS.md`, jeweils ein Satz und das Diff)
> 8. **Check `reihenfolge` in `check_project.py`:** meldet ein Ergebnis auf einer Karte, deren Voraussetzung noch nicht abgeschlossen ist. Hätte die Probewoche am 16.11. automatisch markiert. *(Lieber ein Check als eine Regel.)*
> 9. **`to-tests`:** Ein Angebot mit Preis nur vorschlagen, wenn Preis oder Kosten keine offene Frage mehr sind.
> 10. **`to-interview-guide`:** In der Notizvorlage eine eigene Zeile „nach Vorstellung der Idee: …“, damit Feedback getrennt bleibt.
>
> Ihr müsst die Diffs nicht verstehen; der Satz reicht für die Entscheidung. Welche übernehmt ihr?

**Lena:** 1 ja – stimmt, die haben ja noch nichts zugesagt. 2 bis 6 ja. 7 ok. 8 und 9 ja. 10 nein: Das mit dem Pitch war unser Fehler, nicht der vom Skill. Im Leitfaden stand ja, dass wir die Idee nicht erzählen sollen.

**Agent:**
> Verstanden – Nummer 10 lasse ich weg; dafür steht euer eigener Check (Nr. 2) in Block 8. Ich habe den Check aus Nr. 8 an einer Kopie des Skripts gegen euer Projekt laufen lassen; er meldet:
>
> ```
> OFFEN   reihenfolge   Ergebnis, obwohl die Voraussetzung noch nicht abgeschlossen ist: T2 (vor T1), T3 (vor T1) – Vorbehalt in der Quelle nennen (/log-evidence)
> ```
>
> Die installierten Skills ändere ich nicht; die Vorschläge stehen in `SKILL-PROPOSALS.md`. Wenn ihr wollt, reicht die Datei als Issue im Repository des Skillsets ein (https://github.com/opencampus-sh/agentic-business-model-canvas) – sie enthält nichts aus eurem Projekt.

**Lena:** Ok, das macht Jule später.

*Agent wendet an: A42 im Register; Block 8 (fünf eigene Checks), Block 11 (Retro-Ergebnis, nächste Runde) und Block 6 im Canvas; Status bei jedem Signal in `SIGNALS.md` plus vier neue Signale; `SKILL-PROPOSALS.md`; Entscheidung in `DECISIONS.md` (inkl. abgelehntem Vorschlag Nr. 10).*

```
$ python3 .claude/skills/evidence-checks/scripts/check_project.py
OK      verweise      alle Verweise stehen im Register
OK      status        49 Einträge mit gültigem Status und Quelle
OK      kritische     2 offene kritische Annahmen haben eine Testkarte mit Schwelle
OK      schwellen     5 Testkarten geprüft
OK      eine-annahme  jede Karte prüft eine Annahme
OFFEN   ergebnisse    läuft (Bedingung offen): T1
OFFEN   widerlegt     widerlegte oder ersetzte Annahmen in MODEL.md: A35, A36, A42, A5 – prüfen, ob das Feld noch darauf aufbaut
OK      interviews    4 von mindestens 3 Interviews ausgewertet (4 notiert)
```

**Agent:**
> Keine Fehler. Ich schlage vor zu committen. Als Nächstes – wie `/ask-model` es täte: zuerst die Kosten (Ahmet, bis 27.11.), dann `/to-model`, um das Modell an den Weg „Anpassen“ anzupassen, danach `/to-tests` für die nächste Runde.

*Commit `13 · model-retro · A42 korrigiert, fünf eigene Checks, zwei Vorschläge fürs Skillset`.*

---

## Entscheidungen im Überblick (Lenas Ablehnungen und Lehrmomente)

| Wo | Moment |
|---|---|
| `/setup-model` | Bisherige Ergebnisse werden nur als *Annahme* übernommen; fast gleiche Aussagen werden eine Zeile. |
| `/grill-problem` | Kernproblem: das fehlende warme Abendessen, nicht die Verschwendung. Warum-Kette endet nach einem Schritt mit „Weiß ich nicht“ → *Noch offen*. |
| `/to-interview-guide` | „Würdet ihr das Essen abgeben?“ wird zu „Hat schon mal jemand gefragt …?“ umformuliert. |
| `/log-evidence` (1) | Pitch in I2 erkannt: „Ja klar, sofort“ ist Feedback, kein Beleg. A1 („viel weggeworfen“) wird ersetzt statt verbogen. **Lena lehnt** einen *belegt*-Vorschlag (Snacks im Jugendzentrum) ab. |
| `/grill-solution` | „Kannst du das Canvas nicht einfach für uns ausfüllen?“ – Agent lehnt in einem Satz ab und bietet Ordnen an. Nutzer:innen vs. Kund:innen geklärt. |
| `/to-model` | „Ist ja nicht viel“ wird offene Frage, keine Zahl. |
| `/to-tests` | Schwelle „3 von 4“ vom ganzen Team bestätigt. **Lena lehnt** das empfohlene Preisangebot ab (kein Preis, keine Freigabe). |
| `/log-evidence` (2) | „2 von 4 ist doch auch gut …?“ – die Schwelle bleibt; daraus wird die engere Annahme A49. |
| `/review-model` | Anpassen nur, weil jede widerlegte kritische Annahme eine durch eigene Tests gestützte Ersatz-Annahme hat. |
| `/model-retro` | A42 wird zurückgestuft. **Lena lehnt** Skill-Vorschlag Nr. 10 ab („unser Fehler, nicht der vom Skill“). |
