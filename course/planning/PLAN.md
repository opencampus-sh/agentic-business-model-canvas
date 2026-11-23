# Kursplan

Entwurf aus `/to-course-plan`, 2026-11-23. Grundlage: `COURSE-CANVAS.md` (Blöcke 1–4, 6), `PERSONAS.md`, `RESOURCES.md`.

## Einheiten

Jede Einheit: **Ziel**, **Lesen** (kurz, mit Verweis aufs Handbuch für die Methode), **Übung** am Fall Mensa-Retter in einem Übungsordner (Startzustand und Lösung zum Vergleich), **Selbstcheck** (3–5 Fragen, Lösung aufklappbar), **Transfer** aufs eigene Projekt.

| Einheit | Thema | Leitfrage | Ziele | Ergebnis im eigenen Projekt | Vorher nötig |
|---|---|---|---|---|---|
| 0 | Einrichten und das Canvas lesen | Wie bekomme ich den Agenten und die Skills zum Laufen? | 1 | Projektordner mit allen Dateien nach `/setup-model`, `/show-canvas` geöffnet | Laptop, Agent-Konto |
| 1 | Das Problem schärfen | Wie bleibt das Problem meins, wenn der Agent mitformuliert? | 3, 6 | Kernproblem, Problembaum, Problem-Hypothesen im Register | Einheit 0; Handbuch Kap. 2 |
| 2 | Interviews | Wie wird aus Gesprächen ein Beleg – und wann nicht? | 4 | Leitfaden; nach eigenen Interviews: Auswertung, Status-Änderungen begründet entschieden | Einheit 1; Handbuch Kap. 3 |
| 3 | Annahme oder Beleg? | Woran erkenne ich, was wir wirklich wissen? | 2, 6 | Register durchgesehen; eine Aussage herabgestuft oder ersetzt; `check_project.py` gelesen | Einheit 2 |
| 4 | Von der Lösung zum Modell | Wie entsteht ein Geschäftsmodell, ohne dass der Agent es erfindet? | 3, 6 | Vision, Lösung, kritische Annahmen; `MODEL.md` mit IDs | Einheit 3; Handbuch Kap. 4–5 |
| 5 | Testen und entscheiden | Wie teste ich, ohne mir die Ergebnisse schönzureden? | 5, 6 | Testkarte mit Schwelle, committed; nach dem Test: Auswertung und Review | Einheit 4; Handbuch MVP |

## Ausrichtung (Ziele × Einheiten)

E = eingeführt, Ü = geübt, N = nachgewiesen (Selbstcheck oder Ergebnis im eigenen Projekt)

| Ziel | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| 1 Einrichten und `/setup-model` | E Ü N | | | | | |
| 2 Status unterscheiden, Canvas ≠ Wissen | E | Ü | Ü | N | Ü | Ü |
| 3 Grill-Skill mit eigenen Worten, „Weiß ich nicht“ | | E Ü N | | | Ü N | |
| 4 Belege auswerten, Status-Änderungen begründen | | | E Ü N | Ü | | Ü |
| 5 Testkarte mit Schwelle vor dem Test | | | | | E | Ü N |
| 6 Vorweggenommene Entscheidungen erkennen und zurückweisen | | E | Ü | Ü | Ü | N |

Jedes Ziel wird nachgewiesen; jedes Ergebnis dient einem Ziel.

## Wachstum der Grenze

| Einheit | Kommt neu hinzu (wo) |
|---|---|
| 0 | Terminal öffnen, Ordner wechseln; Agent starten und anmelden; Skills installieren; ein Skill-Befehl (`/setup-model`); Projektdateien und `AGENTS.md`; Canvas-Seite mit `/show-canvas`; was ein Commit ist (Kasten, optional) |
| 1 | Runden mit ❓ und ➡️; eigene Worte statt Vorschlag; „Weiß ich nicht“ → *Noch offen*; Register-ID im Text |
| 2 | Leitfaden lesen und anpassen; Notizen eintragen oder in den Chat einfügen; Freigabe in Abschnitten |
| 3 | die vier Status; Quelle; `check_project.py` ausführen und lesen (OK, OFFEN, FEHLER); ersetzen statt verbiegen |
| 4 | Vision ohne ID; kritische Annahmen; `MODEL.md` und Kategorien |
| 5 | Testkarte (Schwelle, Voraussetzung), Commit vor dem Test; Ergebnis gegen Schwelle; Review-Wege |

## Aufwand

Vorgabe: 6–8 Stunden gesamt (Block 2). Nachgerechnet am 2026-11-23 aus den Walk-throughs (Lesezeit nach Wortzahl bei 200 Wörtern/min, Übung nach Schritten und Fragerunden im Referenzlauf) und nach den Kürzungen aus R3:

| Einheit | Lesen | Übung | Selbstcheck | Transfer | Summe | vorher geplant |
|---|---|---|---|---|---|---|
| 0 | 6 | 45 (Installation, Werkzeuge prüfen) | 5 | 10 | 65 min | 55 |
| 1 | 6 | 30 | 5 | 30 | 70 min | 75 |
| 2 | 5 | 45 (zwei Teile) | 5 | 20 (nur Leitfaden) | 75 min | 75 |
| 3 | 6 | 25 | 5 | 20 | 55 min | 60 |
| 4 | 6 | 40 (`/map-solutions` optional) | 5 | 30 | 80 min | 80 |
| 5 | 6 | 45 (`/model-retro` optional) | 5 | 20 (nur Testkarte) | 75 min | 75 |
| **Gesamt** | | | | | **7 h 20 min** | 7 h |

Nicht eingerechnet: Handbuch-Kapitel 2–5 (gehören zum Changemaker-Kurs), eigene Interviews und Tests, optionale Schritte (`/map-solutions` etwa 20 min, `/model-retro` etwa 15 min).
