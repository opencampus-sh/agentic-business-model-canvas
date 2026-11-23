# AGENTS.md

Instructions for agents working on this repository (the skills themselves, not a project that uses them).

- Skill conventions: see [CONTRIBUTING.md](CONTRIBUTING.md).
- When a change affects users of the skills or the canvas (anything under `skills/`, `.claude-plugin/` or `canvas/`), add an entry under `## Unreleased` in `CHANGELOG.md`.
- Releases go through the `release-skillset` skill (`.claude/skills/release-skillset/`); leave `version` in `.claude-plugin/plugin.json` to it.
- New skills under `skills/` are also added to the `skills` list in `.claude-plugin/plugin.json`.
- The canvas template is the single source of the canvas; regenerate the printed canvas from it (command below) whenever it changes.
- Files listed in `.skillset-core.json` come from the core of the Agentic Skillset Builder; change verbatim ones there, then sync with `/sync-core`.
- This repository is public-facing material: never put content of a real team (ideas, interview notes, names, numbers) into it. Real projects live in the teams' own folders.

## Agentic skillset builder

- Canvas: `design/SKILLSET-CANVAS.md` (read before any work on this skillset; update when something is decided)
- Language: de
- Design files: `design/` (personas, sources, skill map, decisions, signals)
- Canvas template: `skills/setup-model/templates/CANVAS.md`
- Printed canvas: `canvas/agentic-business-model-canvas.svg` and `.pdf`, made with `python3 skills/show-canvas/scripts/render_canvas.py skills/setup-model/templates/CANVAS.md --print --lang de --out canvas/agentic-business-model-canvas.svg --pdf canvas/agentic-business-model-canvas.pdf --subtitle "Der Agent fragt und prüft, das Team entscheidet – getestet wird, bevor es zählt." --footer "Agentic Business Model Canvas v0.9 · CC BY 4.0 · github.com/opencampus-sh/agentic-business-model-canvas"`
- Example case: `examples/mensa-retter/`
- Checks: `python3 scripts/check_skillset.py`
- Other skillsets in: `course/planning/`
- Core: `.skillset-core.json`, synced with `/sync-core` from the Agentic Skillset Builder

## Agentic course creation

- Canvas: `course/planning/COURSE-CANVAS.md` (vor jeder Kursarbeit lesen; aktualisieren, wenn etwas entschieden ist)
- Personas: `course/planning/PERSONAS.md`; Ressourcen: `course/planning/RESOURCES.md`
- Entscheidungen: `course/planning/DECISIONS.md`; Signale: `course/planning/SIGNALS.md`; Plan: `course/planning/PLAN.md`
- Checks: `course/planning/checks/README.md`
- Andere Orte: Kurshandbuch „Become a Changemaker“ (GitBook, öffentlich, nur Bezug)
- Handbuch: Kursseiten in `course/docs/` (später MkDocs auf GitHub Pages); Übungsdateien in `examples/mensa-retter/`
- Quizzes: keine; Selbstcheck-Fragen mit aufklappbarer Lösung auf den Kursseiten
- Folien: keine (Selbstlernkurs ohne Sitzungen)
- Einheit: Einheit; 6 Einheiten, nummeriert 0–5. Die Skills sagen „unit“; hier heißt es „Einheit“.
- Sprache: Deutsch (Planung und Kurs)
- Lösungen zum Vergleich sind Teil des Kurses (Selbstlernkurs ohne Bewertung); es gibt keine Teilnehmendendaten.

