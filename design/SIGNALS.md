# Signals

Everything that shows how the work is going: dry runs and checks before something counts, and what happened after. Newest first. The retro skill turns signals into fixes, checks and rules.

<!--
## YYYY-MM-DD · <scope> · <source: dry run | check | session | feedback | other>

- **What happened:** facts, with numbers where possible
- **Who:** role or persona (no personal names)
- **Severity:** blocker | friction | note
- **Status:** open | fixed in <commit/file> | turned into check <name>
-->

## 2026-11-23 · grill-solution bis model-retro · Referenzlauf 2 für den Kurs (ab Stand 07)

- **What happened:** Läuft mit den aktuellen Skills durch, ohne FEHLER; drei echte Ablehnungen (A40 nicht kritisch, Jugendzentrum behalten, Probewoche parallel zur Freigabe), deren Folgen im Ergebnis sichtbar werden; Schwelle nicht gesenkt; Pivot nur bei „Wer zahlt?“. Funde: (1) Check *reihenfolge* liest T-Nummern hinter „keine (…)“ (Fehlalarm T4, T1 doppelt); (2) kein Status für einen nicht durchgeführten Test (T6); (3) `/to-tests` gibt bei sechs kritischen Annahmen und rund 4 Stunden pro Person und Woche keine Hilfe beim Priorisieren; (4) `/grill-solution` trägt die Ersetzung A4 → A36 nicht in `PROBLEM.md` nach; (5) `/review-model` ändert *Kritisch* im Register, Block 6 steht nicht in seiner Schreibliste; (6) keine Regel, wie Teilnehmende außerhalb der Gruppe der Annahme in der Schwelle zählen (vom Team abgelehnt: eigener Fehler).
- **Who:** Runner-Agent mit Persona Lena
- **Severity:** friction
- **Status:** (1) fixed in `skills/evidence-checks/scripts/check_project.py`; (2)–(5) open; (6) bewusst kein Check (Entscheidung des fiktiven Teams, vom Maintainer zu bestätigen)

## 2026-11-23 · alle Skills · Referenzlauf für den Kurs

- **What happened:** vollständiger Lauf aller zwölf Skills mit den aktuellen Skills am Fall Mensa-Retter, Lena als gute Beispielnutzerin (eigene Worte, drei begründete Ablehnungen von Agent-Empfehlungen). Alle Stolperfallen abgefangen. Befunde: `Sprache:` statt `Language:` in `AGENTS.md`; ⚠️ auch in Block 10; Probewoche vor bestandener Voraussetzung ohne Check; Preisangebot empfohlen, obwohl die Kosten offen waren; „kritische OK“, obwohl der Test einer kritischen Annahme schon ausgewertet war; Review prüfte nicht, ob die Schwelle misst, was die Annahme sagt; lange Folge von Bestätigungsabschnitten. Zwei Vorschläge kamen vom fiktiven Team selbst über `/model-retro` (`SKILL-PROPOSALS.md`).
- **Who:** Persona Lena (Referenzlauf)
- **Severity:** friction
- **Status:** fixed (siehe CHANGELOG); Lauf in `examples/mensa-retter/referenz/`

## 2026-11-23 · alle Skills · Recherche für den Kurs

- **What happened:** Skills werden je nach Agent anders aufgerufen: Claude Code mit `/name` (als Plugin `/agentic-business-model-canvas:name`), OpenCode automatisch oder mit `@name` (kein Slash-Befehl), Codex mit `$name` oder `/skills`. README, Skills und `ask-model` schreiben überall `/name`. `disable-model-invocation: true` ist ein Claude-Code-Feld; OpenCode bewirbt Skills nur mit `description` und lädt sie dann ggf. automatisch.
- **Who:** Recherche (Agent), für Persona Lena mit OpenCode oder Codex
- **Severity:** friction
- **Status:** open – README und Kurs zeigen die drei Aufrufformen; prüfen, ob OpenCode/Codex die Skills ungewollt automatisch laden (Dry-Run mit OpenCode)

## 2026-11-22 · Korrekturen · dry run (gezielt, zweiter Lauf)

- **What happened:** frisches Projekt, Lena fügt alles in den Chat ein, gibt eigene Worte, sagt „Weiß ich nicht“ und pauschal „passt“. Alle neun Korrekturen bestanden (CLAUDE.md und Import; Runden und eigene Worte; Chat-Notizen wörtlich übertragen, Freigabe in Abschnitten, pauschales „passt“ setzt nichts; Ziele ohne ID, vorläufige Zahl als offene Frage; `/to-model` in Runden, nur Arten als Optionen; eine Annahme pro Karte, Commit vor dem Test; Schwellensenkung abgelehnt, bedingte Ergebnisse offen, Widerlegtes markiert statt editiert; Review ohne freies „Weiter testen“; Commit-Angebote). 13 neue Befunde (0 blocker, 6 mittel, 7 niedrig): Status bei fehlender Voraussetzung; Karten auf *läuft* gehen verloren; teilweise widersprochene Annahmen lassen sich nicht ersetzen; neue *belegt*-Zeilen und Einzelbestätigung; Anpassen vs. Pivot bei kritischer Annahme; wo markieren; u. a.
- **Who:** Persona Lena
- **Severity:** note
- **Status:** fixed (Ausgewertet *teilweise* und *läuft* in `log-evidence` und `check_project.py`; „ersetzt durch“; Bestätigung mit ausdrücklichen IDs; Pivot-Regel; ⚠️-Zeile im Canvas; *Noch offen* als Quelle; Lösungstext ohne ID; Ablehnung für die eigene Organisation; Dubletten im Original-Wortlaut; installierte Skills committen; IDs einzeln; wer die Schwelle bestätigt hat). Artefakte in `examples/mensa-retter/run-2026-11-22-b/`.

## 2026-11-22 · to-model bis model-retro · dry run (Phase 2)

- **What happened:** gleiche Persona, gleicher Projektstand, 6 Skills plus `/ask-model`, kein Blocker, `check_project.py` am Ende grün. Gehalten haben: Lenas Vorschlag, die Schwelle nach dem Ergebnis von „3 von 4“ auf „2 von 4“ zu senken, wurde abgefangen (A5 *widerlegt*, positive Teile als *belegt* A48 erhalten); „Bezahlen können wir nichts“ machte A6 *widerlegt*, Verpackungen blieben Sachleistung; Stiftungsauskunft zählte nicht als Zahlung; keine eigenen Geldrechnungen; `/review-model` ließ den Weg (Anpassen) dem Team; `/model-retro` lieferte Skill-Regeln als Diffs. 27 Befunde (0 blocker, 10 friction, 17 note). Die wichtigsten: widerlegte Annahme blieb in `MODEL.md` und Block 2/7 stehen, `check_project.py` merkte es nicht (erst das Review); `/log-evidence` übernimmt im Chat eingefügte Ergebnisse nicht (zum zweiten Mal); keine Testkarte hat *Ausgewertet*; eine Karte prüft zwei Annahmen mit einer Schwelle; vorläufige Zahl (A34) wird nicht verpflichtend neu bestätigt; kein Skill bittet ums Committen, obwohl `/log-evidence` den Git-Verlauf prüft; `/to-model` stellt zehn Fragen auf einmal; Antwort ohne Zahl wird Register-Zeile statt offener Frage; Kategorien fehlen für Beziehung und Aktivitäten; keine Regel für Antworten Dritter auf eigene Anfragen; Diffs der Retro ohne Ablageort und für Lena unverständlich.
- **Who:** Persona Lena
- **Severity:** friction
- **Status:** open – Korrekturen in `/review-skillset`; Artefakte in `examples/mensa-retter/run-2026-11-22/`

## 2026-11-22 · setup-model bis grill-solution · dry run (Phase 1)

- **What happened:** Runner (nur installierte Skills) und Persona Lena am fiktiven Fall Mensa-Retter, 7 Skills, Ergebnis ohne Blocker, `check_project.py` am Ende ohne FEHLER. Gehalten haben: „Ja klar, sofort“ (gepitcht) und die Einschätzungen des Küchenleiters blieben *Annahme*; „Füll das Canvas einfach aus“ wurde abgelehnt; keine erfundenen Fakten. 24 Befunde (0 blocker, 10 friction, 14 note). Die wichtigsten: kein Pfad für „Weiß ich nicht“ im 5-Whys-Teil; im Chat eingefügte Notizen werden von `/log-evidence` nicht gefunden; *belegt* für Interview-Aussagen ist nicht definiert (keine Schwelle); 16-Zeilen-Tabelle zur Freigabe überfordert Lena; Formulierungsvorschläge (➡️) werden bei „ok, passt“ zum Inhalt (Vision, Wertangebote); Recherche-Links ungeprüft (nur Suchergebnis, Seite nicht geöffnet); `setup-model` legt kein `CLAUDE.md` an; Block 1 veraltet, wenn der Problembaum sich ändert; Problem- und Lösungs-Hypothesen haben keinen festen Ort.
- **Who:** Persona Lena (schwächste Nutzerin)
- **Severity:** friction
- **Status:** open – Korrekturen nach Phase 2 gemeinsam in `/review-skillset`; Artefakte in Scratch-Projekt, später nach `examples/mensa-retter/run-2026-11-22/`

