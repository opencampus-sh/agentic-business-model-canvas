# Decisions

One entry per decision, newest first. People decide; the agent proposes and records.

<!--
## YYYY-MM-DD: <decision in one line>

- **Context:** what made the decision necessary
- **Decision:** what was decided
- **Reason:** why
- **Alternatives:** what else was considered, and why not
- **Canvas:** block(s) affected
-->

## 2026-11-21: Zuschnitt, Nutzende und Arbeitsumgebung

- **Context:** `/grill-practice`, Runde 1 (Q1–Q3).
- **Decision:** Das Skillset begleitet Problemanalyse, Zielgruppe und Interviews, Lösungshypothesen, Solution Design (Nutzer:innen/Kund:innen, Value Proposition Canvas, Social Business Model Canvas) und die Lean-Schleife mit MVP-Tests. Finanzierung, Rechtsform und Pitch werden nur verlinkt. Die Teams führen die Skills selbst aus. Arbeitsablage ist ein Ordner mit Markdown-Dateien, mit Claude Code, OpenCode oder Codex; Notion bleibt optionaler Export.
- **Reason:** Das Canvas ist ohne Problemanalyse und Tests nur eine Sammlung von Annahmen; die Entscheidungen gehören dem Team; Markdown-Ordner funktionieren mit allen drei Agenten ohne Git.
- **Alternatives:** Nur die Canvases; das ganze Kapitel Solution Design; der ganze Kurs inkl. Pitch; Coaches als Nutzende; Notion über Connector; ein GitHub-Repo pro Team.
- **Canvas:** 1, 2, 7

## 2026-11-21: Name, Sprache und Ziel des Skillsets

- **Context:** `/setup-skillset`, Abschnitte A–C.
- **Decision:** „Agentic Business Model Canvas“, Repo und Plugin `agentic-business-model-canvas`, Setup-Skill `setup-model`; Inhalte und Gespräch auf Deutsch (du), Bezeichner englisch; lokal gebaut, privates GitHub-Repo `opencampus-sh/agentic-business-model-canvas`, vom Maintainer leer angelegt, Push auf `main`.
- **Reason:** Zuschnitt auf das Solution Design statt auf den ganzen Kurs; die Session kann keine Repos anlegen.
- **Alternatives:** `agentic-changemaker` für den ganzen Gründungsweg.
- **Canvas:** 1, 7
