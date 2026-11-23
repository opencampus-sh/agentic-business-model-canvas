# Entscheidungen

Ein Eintrag pro Entscheidung, die neueste oben. Das Team entscheidet; der Agent schlägt vor und hält fest.

<!--
## JJJJ-MM-TT: <Entscheidung in einer Zeile>

- **Kontext:** was die Entscheidung nötig gemacht hat
- **Entscheidung:** was entschieden wurde
- **Begründung:** warum
- **Alternativen:** was sonst in Frage kam, und warum nicht
- **Canvas:** betroffene Blöcke
-->

## 2026-11-23: Werkzeuge, Aufwand und Abgleich mit den Skills

- **Kontext:** `/review-unit` nach den Walk-throughs aller Einheiten (R1–R4).
- **Entscheidung:** (R1) Einheit 0 prüft und installiert Python 3 und Git mit dem Agenten; die Skills haben einen Ausweg ohne Python (Canvas als Text, Handprüfung). (R2) Git ist Teil von Einheit 0; ohne Git hält der Agent das Datum der Schwelle in `DECISIONS.md` fest. (R3) Kürzen statt verlängern: `/map-solutions` (Einheit 4) und `/model-retro` (Einheit 5) optional, kürzere Vergleichslisten; neue Zeiten im Plan (gesamt etwa 7 h 20 min). (R4) Seiten an die aktuellen Skills angepasst, Referenzlauf ab Einheit 4 mit den aktuellen Skills neu, neuer Check vor jedem Release.
- **Begründung:** Python fehlt auf frischen Windows-Rechnern und blockiert Lena; ein 9-Stunden-Kurs sprengt die Vorgabe; Lösungen müssen zeigen, was Lernende erleben.
- **Alternativen:** Python nur im Kurs oder nur in den Skills; Rahmen auf 8–9 h anheben; nur Seiten anpassen.
- **Canvas:** 4, 5, 6, 8

## 2026-11-23: Keine Bewertungen realer Initiativen im Übungsmaterial

- **Kontext:** Im Referenzlauf hat `/map-solutions` echte Kieler Angebote recherchiert und SWOT-Einschätzungen entworfen (E1).
- **Entscheidung:** Namen, Links und Fakten aus den Quellen (Q) bleiben; die Einschätzungen (E) sind in allen Übungsständen und im Transkript entfernt und durch „vom Team einzuschätzen“ ersetzt.
- **Begründung:** Die Übung zeigt weiterhin Recherche mit Quellen; opencampus veröffentlicht keine ungeprüften Bewertungen realer Initiativen.
- **Alternativen:** Einschätzungen behalten und als fiktiv markieren; Organisationen durch fiktive ersetzen.
- **Canvas:** 7

## 2026-11-23: Übungsmaterial, Transfer, Installationswege

- **Kontext:** Stop-Points von `/map-resources` und `/to-course-plan` (D1–D4).
- **Entscheidung:** (D1) Ein dritter, vollständiger Referenzlauf mit den aktuellen Skills liefert Start- und Lösungszustände pro Einheit (ein Commit pro Skill). (D2) Eigene Interviews und Tests liegen außerhalb des Kurses; der Transfer umfasst Leitfaden und Testkarte, die Auswertung echter Belege folgt im Changemaker-Kurs. (D3) Quelle der Installationsbefehle ist das README; ein Check vergleicht die Kursseite damit. (D4) Für Claude Code ist der Plugin-Weg (ohne Node.js) der Hauptweg in Einheit 0; `npx skills` für OpenCode und Codex.
- **Begründung:** Übungen sollen das Verhalten der aktuellen Skills zeigen; ein 7-Stunden-Kurs darf nicht wochenlang auf Interviews warten; eine Quelle pro Fakt; eine Installation weniger für Lena.
- **Alternativen:** Material aus beiden Dry-Runs zusammensetzen; echte Interviews im Kurs; `npx skills` für alle.
- **Canvas:** 7, 9

## 2026-11-23: Lernende, Lernziele, Nachweis und Vorwissen

- **Kontext:** `/grill-course`, Runde 1 (F1–F5).
- **Entscheidung:** Personas Lena und Jonas, Gesamtzeit 6–8 Stunden; sechs Lernziele (Block 3), ohne die Methoden selbst; Nachweis über Selbstchecks, ein Ergebnis pro Einheit im eigenen Projekt und einen Abschluss-Check (Block 4); Claude Code ausführlich, OpenCode und Codex in je einem Kasten; vorausgesetzt werden Laptop mit Installationsrechten, Internet, Handbuch Kapitel 1 und ein Agent-Konto, nicht Terminal, Git oder Markdown. Alle Formulierungen vom Agenten vorgeschlagen, vom Autor übernommen.
- **Begründung:** Zuschnitt des Skillsets (schwächste Nutzerin); die Methoden stehen im Handbuch; ein Agent im Detail hält Einheit 0 kurz.
- **Alternativen:** alle drei Agenten gleich ausführlich; Installation nicht im Kurs.
- **Canvas:** 2, 3, 4, 6

## 2026-11-23: Setup des Selbstlernkurses

- **Kontext:** `/setup-course` (Agentic Course Creation), Abschnitte A–E.
- **Entscheidung:** Kurs in `course/` des Skillset-Repos, Planung in `course/planning/`, Seiten in `course/docs/`; Lösungen zum Vergleich sind Teil des Kurses. Sechs Einheiten (0–5), Selbstlernen ohne Sitzungen, je Lesen, Übung am Fall Mensa-Retter und Transfer, Dauer wird in `/to-course-plan` berechnet. Selbstcheck-Fragen auf den Seiten statt Quiz-Werkzeug, keine Folien. Planung und Kurs auf Deutsch.
- **Begründung:** öffentlicher Selbstlernkurs ohne Bewertung und ohne Teilnehmendendaten; wer den Changemaker-Kurs betreut, soll auch die Planung lesen können.
- **Alternativen:** Planung in eigenem privatem Repo; Quiz in Forms/Formbricks; Planung auf Englisch.
- **Canvas:** 5, 7
