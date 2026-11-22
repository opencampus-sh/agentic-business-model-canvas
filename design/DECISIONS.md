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

## 2026-11-22: Das Agentic Business Model Canvas

- **Context:** `/design-canvas`, Entscheidungen C1–C2.
- **Decision:** 11 Blöcke in drei Spalten (Problem & Wirkung: Herausforderung & Vision, Nutzer:innen & Kund:innen, Lösung & Wertangebot, Erfolgskriterien; Geschäftsmodell: Wissen & Recherche 🤖, Annahmen 👤 als Grenze, Geschäftsmodell, Checks 🤖; Testen & Lernen: Tests & MVP 🤖, Ergebnisse & Signale 🤖, Lernen & Entscheiden). Das Social Business Model Canvas wird nicht nachgebaut, sondern liegt als Begleitdatei `MODEL.md` daneben; Block 7 verweist darauf. Weitere Begleitdateien (Richtung, endgültig in `/to-skill-map`): `PROBLEM.md`, `INTERVIEWS.md`, `ASSUMPTIONS.md`, `TESTS.md`, `DECISIONS.md`, `SIGNALS.md`. Block 11 heißt „Lernen & Entscheiden“ statt „Entscheidungen & nächste Schritte“ (passt ins gedruckte Canvas).
- **Reason:** Das agentische Canvas ordnet Entscheidungen, Belege und Tests; die Fachmethode bleibt unverändert neben ihm (Lizenz M3, Passung zum Kurs M4). Getrennte Dateien bleiben für die schwächste Nutzerin überschaubar.
- **Alternatives:** Die zehn SBMC-Felder als Blöcke des Canvas; weniger, größere Begleitdateien.
- **Canvas:** 7

## 2026-11-22: Quellen, Lizenzen und Fassung des Social Business Model Canvas

- **Context:** `/map-sources`, Entscheidungen M1–M8.
- **Decision:**
  - M1: Handbuch, Starterkitchen-Text und SEEd-Material gehören (sehr wahrscheinlich) dem Campus Business Box e.V.; der e.V. soll die Adaption im Skillset erlauben, idealerweise mit einer offenen Lizenz. Bis dahin: eigene Worte, Verweise.
  - M2: Value Proposition Canvas (Copyright Strategyzer AG) wird nur verlinkt, mit Quellenangabe; keine Vorlage im Skillset. Erlaubnis bei Strategyzer kann parallel angefragt werden.
  - M3: Agentisches Canvas unter CC BY 4.0; die Vorlage des Social Business Model Canvas als eigene Begleitdatei unter CC BY-SA 4.0, mit „SEEd / Campus Business Box e.V., nach dem Business Model Canvas von Strategyzer.com“. Strategyzer wird informiert.
  - M4: Aktuelle SEEd-Fassung (10 Felder, Leitfragen „Makeover 12.1.26“) plus Playbook-Regel: sind Kund:innen und Nutzer:innen verschieden, werden Wertversprechen und Zielgruppe für beide ausgefüllt.
  - M5: Business Model Canvas und Sustainable Business Model Canvas nur verlinkt.
  - M6: Jede kritische Annahme bekommt vor dem Test Messgröße und Schwelle; „mindestens 2 Personen“ aus dem Handbuch bleibt Untergrenze.
  - M7: Reihenfolge wie im Handbuch (Vision nach den Interviews).
  - M8: SWOT bestehender Lösungen dabei; USP und „Zielsetzung & KPIs“ nur verlinkt.
- **Reason:** Ein Träger für alle eigenen Quellen; Strategyzer-Bedingungen (VPC-Adaptionen und Software nur mit Erlaubnis, BMC-Varianten CC BY-SA mit Quellenangabe); Passung zum Kurs.
- **Alternatives:** siehe Stop-Point von `/map-sources` (Erlaubnis bei Strategyzer; alles CC BY-SA; Handbuch-Fassung mit „neun“ Bausteinen; klassisches Business Model Canvas; Vision nach vorn).
- **Canvas:** 5, 7

## 2026-11-21: Ergebnisse, Belege, Entscheidungsgrenze und schwächste Nutzerin

- **Context:** `/grill-practice`, Runde 2 (Q4–Q9).
- **Decision:** Name bleibt „Agentic Business Model Canvas“. Ergebnisse, Belege und Entscheidungsgrenze wie in Block 3, 4 und 6 des Skillset Canvas; zentraler Check „Annahme vs. Beleg“ mit drei Status (*Annahme*, *recherchiert*, *belegt*). Die schwächste Nutzerin hat keine BWL- und kaum Agent-Erfahrung; das Skillset setzt einen laufenden Agenten voraus, die Installation gehört in den Kurs. Personas werden mit einer Fragenliste von der Kursleitung bestätigt.
- **Reason:** Das Social Business Model Canvas ist das zentrale Ergebnis, die Problemanalyse speist seine ersten Blöcke. Ohne Status pro Eintrag sieht ein vom Agenten gefülltes Canvas fertig aus, obwohl es nur Annahmen enthält.
- **Alternatives:** Umbenennung (z. B. `agentic-impact-startup`); nur zwei Status (Annahme/belegt); Installation des Agenten im Skillset.
- **Canvas:** 2, 3, 4, 6

## 2026-11-21: Rechteinhaber und Sichtbarkeit

- **Context:** Repository unter `opencampus-sh`.
- **Decision:** Rechteinhaber ist Campus Business Box e.V. (opencampus.sh). Keine Inhalte echter Teams im Skillset-Repo.
- **Reason:** Träger von opencampus.sh; das Repo kann öffentlich werden.
- **Alternatives:** Steffen Brandt als Person.
- **Canvas:** 5

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
