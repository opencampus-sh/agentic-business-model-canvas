# Ressourcen

Wo jede Ressource des Kurses liegt, wer sie sieht und welche Kopie die Quelle ist. Gepflegt von `/map-resources`; gelesen von allen anderen Skills.

## Orte

| Ort | Sichtbarkeit | Zielgruppe | Rolle |
|---|---|---|---|
| `course/docs/` in `opencampus-sh/agentic-business-model-canvas` | privat, öffentlich ab Release | Lernende | Kursseiten (später MkDocs auf GitHub Pages) |
| `course/planning/` im selben Repo | wie oben | Kursleitung | Planung (dieses Verzeichnis) |
| `examples/mensa-retter/` im selben Repo | wie oben | Lernende | Beispielfall, Startzustände und Lösungen der Übungen (Dry-Run-Artefakte) |
| `skills/`, `README.md`, `canvas/` im selben Repo | wie oben | Lernende | das Skillset selbst |
| https://opencampus.gitbook.io/changemaker/ | öffentlich | Lernende | Kurshandbuch „Become a Changemaker“ (Bezug, nicht Teil dieses Kurses) |

## Fakten und ihre Quelle

| Fakt | Quelle | Spiegel |
|---|---|---|
| Installationsbefehle der Skills (`npx skills …`, `claude plugin …`) | `README.md` (Abschnitt Installation) | Kursseite Einheit 0 |
| Installation der Agenten, Kosten, Konten | offizielle Seiten der Anbieter (Links mit Abrufdatum auf der Kursseite) | Kursseite Einheit 0 |
| Skill-Namen und was sie tun | `skills/*/SKILL.md` (Frontmatter) | README-Tabelle, `docs/process.md`, Kursseiten |
| Dateien im Projektordner | `skills/setup-model/templates/` | `docs/process.md`, Kursseiten |
| Status-Begriffe (Annahme, recherchiert, belegt, widerlegt) | `skills/assumptions/SKILL.md` | Vorlage `ASSUMPTIONS.md`, `canvas/README.md`, Kursseiten |
| Blöcke des Canvas | `skills/setup-model/templates/CANVAS.md` | `canvas/README.md`, gedrucktes Canvas, Kursseiten |
| Übungs-Startzustände und Lösungen | Referenzlauf in `examples/mensa-retter/` (Git-Bundle, ein Commit pro Skill) | Kursseiten |
| Methoden (5 Whys, Problembaum, SWOT, MVP …) | Kurshandbuch „Become a Changemaker“ | Kursseiten verlinken nur |

## Ressourcen pro Einheit

| Einheit | Planung | Kursseite | Übung (Start / Lösung) | Selbstcheck | Status |
|---|---|---|---|---|---|
| 0 | `PLAN.md` | `docs/0-einrichten.md` | eigener leerer Ordner | auf der Seite | überarbeitet nach Walk-through |
| 1 | `PLAN.md` | `docs/1-problem.md` | Referenzlauf: nach `/setup-model` → nach `/grill-problem` | auf der Seite | überarbeitet nach Walk-through |
| 2 | `PLAN.md` | `docs/2-interviews.md` | Referenzlauf: nach `/grill-problem` → nach `/log-evidence` (Interviews) | auf der Seite | überarbeitet nach Walk-through |
| 3 | `PLAN.md` | `docs/3-annahme-oder-beleg.md` | Referenzlauf: Register nach der Auswertung | auf der Seite | überarbeitet nach Walk-through |
| 4 | `PLAN.md` | `docs/4-loesung-und-modell.md` | Referenzlauf: nach `/map-solutions` → nach `/to-model` (zweiter Lauf) | auf der Seite | überarbeitet nach Walk-through |
| 5 | `PLAN.md` | `docs/5-testen-und-entscheiden.md` | Referenzlauf: nach `/to-model` → nach `/review-model`, optional `/model-retro` (zweiter Lauf) | auf der Seite | überarbeitet nach Walk-through |

**Konflikt:** Die beiden Dry-Runs vom 2026-11-22 taugen nur teilweise als Übungsmaterial: Lauf 1 entstand mit den Skills vor den Korrekturen, Lauf 2 hat `/to-interview-guide`, `/map-solutions` und `/model-retro` übersprungen und Lena alles in den Chat schreiben lassen. Entscheidung siehe `DECISIONS.md`.
