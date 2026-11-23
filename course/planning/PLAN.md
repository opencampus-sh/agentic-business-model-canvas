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

Vorgabe: 6–8 Stunden gesamt (Block 2). Zielwerte pro Einheit, nachzurechnen, sobald die Seiten stehen (Lesezeit nach Wortzahl, Übung nach Schritten im Referenzlauf):

| Einheit | Lesen | Übung | Selbstcheck | Transfer | Summe (Ziel) |
|---|---|---|---|---|---|
| 0 | 10 | 40 (Installation) | 5 | – | 55 min |
| 1 | 10 | 30 | 5 | 30 | 75 min |
| 2 | 10 | 30 | 5 | 30 (+ eigene Interviews, außerhalb) | 75 min |
| 3 | 15 | 20 | 5 | 20 | 60 min |
| 4 | 10 | 35 | 5 | 30 | 80 min |
| 5 | 10 | 30 | 5 | 30 (+ eigene Tests, außerhalb) | 75 min |
| **Gesamt** | | | | | **7 h** |

Eigene Interviews und Tests gehören zum Changemaker-Kurs, nicht zu diesem Kurs, und sind nicht eingerechnet.
