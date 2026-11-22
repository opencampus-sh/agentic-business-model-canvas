# Signals

Everything that shows how the work is going: dry runs and checks before something counts, and what happened after. Newest first. The retro skill turns signals into fixes, checks and rules.

<!--
## YYYY-MM-DD · <scope> · <source: dry run | check | session | feedback | other>

- **What happened:** facts, with numbers where possible
- **Who:** role or persona (no personal names)
- **Severity:** blocker | friction | note
- **Status:** open | fixed in <commit/file> | turned into check <name>
-->

## 2026-11-22 · setup-model bis grill-solution · dry run (Phase 1)

- **What happened:** Runner (nur installierte Skills) und Persona Lena am fiktiven Fall Mensa-Retter, 7 Skills, Ergebnis ohne Blocker, `check_project.py` am Ende ohne FEHLER. Gehalten haben: „Ja klar, sofort“ (gepitcht) und die Einschätzungen des Küchenleiters blieben *Annahme*; „Füll das Canvas einfach aus“ wurde abgelehnt; keine erfundenen Fakten. 24 Befunde (0 blocker, 10 friction, 14 note). Die wichtigsten: kein Pfad für „Weiß ich nicht“ im 5-Whys-Teil; im Chat eingefügte Notizen werden von `/log-evidence` nicht gefunden; *belegt* für Interview-Aussagen ist nicht definiert (keine Schwelle); 16-Zeilen-Tabelle zur Freigabe überfordert Lena; Formulierungsvorschläge (➡️) werden bei „ok, passt“ zum Inhalt (Vision, Wertangebote); Recherche-Links ungeprüft (nur Suchergebnis, Seite nicht geöffnet); `setup-model` legt kein `CLAUDE.md` an; Block 1 veraltet, wenn der Problembaum sich ändert; Problem- und Lösungs-Hypothesen haben keinen festen Ort.
- **Who:** Persona Lena (schwächste Nutzerin)
- **Severity:** friction
- **Status:** open – Korrekturen nach Phase 2 gemeinsam in `/review-skillset`; Artefakte in Scratch-Projekt, später nach `examples/mensa-retter/run-2026-11-22/`

