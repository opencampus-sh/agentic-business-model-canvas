# Changelog

## Unreleased

- Korrekturen aus dem Dry-Run vom 2026-11-22 (Fall Mensa-Retter):
  - Eigene Worte zuerst: Bei Problem, Vision, Lösung, Wertangebot und Fazit fragen die Skills zuerst nach den Worten des Teams; übernommene Agent-Formulierungen werden in `DECISIONS.md` vermerkt.
  - `assumptions` definiert, wann Interview-Aussagen, beobachtetes Verhalten und Antworten Dritter *belegt* sind; Ziele (Vision, Erfolgskriterien, Schwellen) sind keine Aussagen; Quellen müssen geöffnet werden; „nichts gefunden“ bleibt Annahme; Antwort auf „Füll es einfach aus“.
  - Im Chat eingefügte Notizen und Ergebnisse überträgt `/log-evidence` zuerst wörtlich in die Dateien.
  - Freigaben in Abschnitten von höchstens fünf Zeilen; ein pauschales „passt“ setzt nie *belegt*. `/to-model` fragt in Runden von höchstens vier Fragen; Grill-Skills nennen die verbleibenden Runden; „Weiß ich nicht“ wird zur offenen Frage.
  - Testkarten: eine Annahme pro Karte, neue Felder *Voraussetzung* und *Ausgewertet*, vorläufige Zahlen müssen vom Team beschlossen sein, Karten vor dem Testen committen.
  - `check_project.py`: neue Prüfungen *eine-annahme*, *voraussetzung*, *ergebnisse* (nicht ausgewertet, überfällig), *widerlegt* (widerlegte Annahme in `MODEL.md`).
  - `/setup-model` legt `CLAUDE.md` an, erfragt die Sichtbarkeit ohne Remote, führt Dubletten zusammen; neue Abschnitte *Problem-Hypothesen* und *Noch offen* in `PROBLEM.md`; Kategorien *Beziehung* und *Aktivitäten*.
  - `/review-model`: klare Abgrenzung zwischen „weiter testen“ und „anpassen“, Folgeskill je Weg, Erklärung von „blockierend“. `/model-retro` schreibt Skill-Vorschläge in `SKILL-PROPOSALS.md`.
  - Jeder schreibende Skill bietet am Ende einen Commit an.
- Korrekturen aus dem zweiten, gezielten Dry-Run: Testkarten auf *läuft* (*Ausgewertet: teilweise*) werden weiter verfolgt und von `check_project.py` gemeldet; teilweise widersprochene Annahmen werden ersetzt („ersetzt durch A…“); Pivot-Regel bei widerlegter kritischer Annahme; ⚠️-Zeile im Canvas für widerlegte Annahmen; IDs einzeln statt als Bereich.
- `/model-retro`: aus Signalen werden Korrekturen, Checks, Canvas-Änderungen und Vorschläge für das Skillset.
- Skills für Interviews, Belege, bestehende Lösungen und Review: `/to-interview-guide`, `/log-evidence`, `/map-solutions`, `/review-model`.
- Skills für Problem, Lösung, Modell und Tests: `/grill-problem`, `/grill-solution`, `/to-model` (Social Business Model Canvas mit Verweisen ins Register), `/to-tests` (Testkarten mit Schwelle vor dem Test).
- Erste Skills: `/setup-model` (Projektordner mit Canvas, Annahmen-Register, Problem, Interviews, bestehenden Lösungen, Social Business Model Canvas, Tests), `/ask-model` (Wegweiser), Referenz-Skills `assumptions` (Grenze Annahme vs. Beleg) und `evidence-checks` mit `check_project.py`.
- First draft: canvas (guide, printed SVG and PDF, template), process, principles, 12 user-invoked skills and 2 reference skills. Designed with the Agentic Skillset Builder; design files in `design/`.
