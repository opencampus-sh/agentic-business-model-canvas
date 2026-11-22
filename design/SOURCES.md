# Sources

Woher die Fachlogik des Skillsets kommt. Eine Regel in einem Skill, die sich weder auf eine Quelle hier noch auf eine Entscheidung in `DECISIONS.md` zurückführen lässt, ist eine Erfindung des Agenten.

## Inventory

| # | Source | Kind | Location | License | Accessed | Used for |
|---|---|---|---|---|---|---|
| S1 | Kurshandbuch „Become a Changemaker“ (42 Seiten; Kapitel Einführung, Problemanalyse, Zielgruppe, Vision, Ideenfindung, Solution Design, Pitch, Bonus) | Handbuch | https://opencampus.gitbook.io/changemaker/ (Markdown über `llms.txt`); GitHub-Repo `opencampus-sh/become-a-changemake` ist noch leer | **unbekannt**: keine Lizenz-, Autoren- oder Copyright-Angabe auf irgendeiner Seite | 2026-11-22 | Prozess, Aufgaben, Methoden, Leitfragen, Beispiele |
| S2 | Value Proposition Canvas (Strategyzer AG) | Canvas | Abbildung in S1 ohne Quellenangabe; Nutzungsbedingungen: https://www.strategyzer.com/legal/usage-of-our-tools | **Copyright Strategyzer AG.** Nutzung in eigener Arbeit und Lehre erlaubt, mit Nennung „Strategyzer.com und Strategyzer AG“. Adaptionen und Aufnahme in Software nur mit ausdrücklicher Erlaubnis. | 2026-11-22 | Felder Aufgaben/Bedürfnisse, Pains, Gains, Produkte, Pain Relievers, Gain Creators |
| S3 | Social Business Model Canvas, Handout von SEEd (Social Entrepreneurship Education), c/o Campus Business Box e.V.; aktuelle Fassung „Makeover 12.1.26“ | Canvas | https://seed.schule/lehrmaterial/ → `SEEd-Handout-Social-Business-Model-Canvas-A3_Makeover-12.1.26.pdf`; ältere Fassung als Abbildung in S1 | **keine Lizenzangabe; Rechteinhaber Campus Business Box e.V.** (wie dieses Skillset). Kein Strategyzer-Vermerk, obwohl Variante des Business Model Canvas (S4, CC BY-SA). | 2026-11-22 | 10 Felder mit Leitfragen; Felder 3 „Lösung (Produkt/Dienstleistung)“ und 6 „Zielgruppe: Kund:innen und/oder Nutzer:innen“ |
| S4 | Business Model Canvas (Osterwalder, Pigneur; Strategyzer) | Canvas | Abbildung in S1; https://www.strategyzer.com/legal/usage-of-our-tools | **CC BY-SA 3.0** (Strategyzer). Varianten erlaubt; Quelle muss genannt werden, „Strategyzer.com“ sichtbar unter jedem Canvas; ShareAlike für Adaptionen; bei Software „gute Praxis“, Strategyzer vorher zu kontaktieren. | 2026-11-22 | Alternative zu S3 |
| S5 | Sustainable Business Model Canvas | Canvas | Abbildung in S1 („optional“), ohne Autor | **unbekannt**: mehrere Varianten mit verschiedenen Autoren und Lizenzen (z. B. Threebility, CC BY-SA 4.0); welche S1 zeigt, ist offen | 2026-11-22 | Alternative zu S3, je Baustein eine Nachhaltigkeitsfrage |
| S6 | Lean Startup (Eric Ries) | Methode | https://theleanstartup.com/ (in S1 verlinkt) | Methode, nur Verweis | – | Bauen–Messen–Lernen, MVP, Hypothesen |
| S7 | Lean Impact (Ann Mei Chang) | Methode | https://www.annmei.com/ (in S1 verlinkt) | Methode, nur Verweis | – | Wirkungsperspektive auf Lean Startup |
| S8 | Videos und Artikel (Y Combinator, Pebble, Doordash, Michael Seibel, Viva con Aqua, Guy Kawasaki) | Links | in S1 verlinkt | nur Verweis | – | Vertiefung, nicht übernommen |
| S10 | Starterkitchen „Basics: Social Business Model Canvas“ | Webseite | https://startup.starterkitchen.de/basics/social-business-model-canvas | **unbekannt**; Starterkitchen gehört zu opencampus | 2026-11-22 | gleicher Text wie S1 (Ursprung von S1?) |
| S11 | SEEd Playbook (47 Seiten, Methoden für Schulworkshops) | Handbuch | https://seed.schule/lehrmaterial/ → `SEEd-Playbook-240926.pdf` | keine Lizenzangabe; Campus Business Box e.V. | 2026-11-22 | Einführung des Social Business Model Canvas; Regel: sind Käufer:in und Nutzer:in verschieden, Wertversprechen und Zielgruppe jeweils für beide ausfüllen |
| S9 | Agentic Data Science, Agentic Course Creation, Agentic Skillset Builder | Skillsets | github.com/steffen74/… | MIT / CC BY 4.0 | 2026-11-21 | Rollen, Konventionen, Kern |

## Was S1 für die Blöcke und Schritte hergibt

| Schritt (S1-Kapitel) | Methode und Vorlage | Aufgaben in S1 | Kriterien in S1 |
|---|---|---|---|
| Kernproblem (Problemanalyse) | präzise, aus Sicht der Zielgruppe | Kernproblem benennen | negative Situation der Zielgruppe, nicht fehlende Lösung |
| Ursachen (5 Whys) | Warum-Kette bis zu einem Ansatzpunkt, dann „Erkenntnis“; danach Recherche | 5 Whys durchführen | etwa fünfmal, keine feste Regel; Wurzeln statt Symptome |
| Folgen | direkte, indirekte, gesellschaftliche Folgen, Betroffene; „Was passiert, wenn sich nichts ändert?“ | Folgen ergründen (sechs Ebenen) | die Schwächsten besonders betrachten |
| Problembaum | Stamm = Kernproblem, Wurzeln = Ursachen, Äste = Folgen | Ergebnisse zusammenfassen | nach Interviews überarbeiten |
| Zielgruppe | direkt Betroffene, Untergruppen; Realitätscheck „Was nehmen wir an, was wissen wir?“ | Zielgruppe definieren; Problem-Hypothesen formulieren | konkret, nicht „die breite Masse“ |
| Problem-Interviews | Leitfaden, 10 Beispielfragen, offen fragen, nicht pitchen; Aussagen clustern | Leitfaden, idealerweise 3 Interviews; auswerten, Problembaum ergänzen | 3 Personen; sonst Expert:innen/Stakeholder |
| Vision | höchstens zwei Sätze, gesellschaftlicher Zielzustand, keine Lösung | Vision formulieren | „Wir wollen, dass …“; nicht erreichbar |
| Bestehende Lösungen (SWOT) | Recherche; SWOT je bestehendem Projekt; Fazit | Überblick verschaffen; SWOT | Lücken als Chance |
| Lösungs-Hypothesen | Lösung in wenigen Sätzen; Hypothesen; kritische markieren | drei Aufgaben (Notion) | wenige kritische, zuerst zu beweisen |
| Nutzer:innen vs. Kund:innen | vier Fälle (identisch, verschieden, Wertschöpfungskette, Umsatzspende/NGO) | wer ist wer, wo entsteht Wirkung | beide Perspektiven zusammendenken |
| Value Proposition Canvas | Zielgruppe (Aufgaben, Pains, Gains) vs. Angebot (Produkte, Pain Relievers, Gain Creators) | ausfüllen mit Ergebnissen aus Kap. 2–3 | Passung sichtbar machen |
| Social Business Model Canvas | 10 Bausteine mit Leitfragen; Beispiel Mentoring | „euer Business Model Canvas“ ausfüllen | so einfach wie möglich |
| MVP | stark abgespeckt, in Stunden bis Wochen; auf kritischen Hypothesen; idealerweise gegen Geld | MVP starten; mindestens 2 Personen/Unternehmen vorstellen | Umfragen liefern höfliche Antworten |
| Weiter (Abschluss) | Feedback einarbeiten | verbessertes MVP wieder vorstellen | – |

Übergabepunkte außerhalb des Zuschnitts: Elevator Pitch und Startup Pitch nutzen Problem, Lösung, Zielgruppe, Geschäftsmodell und USP; Finanzierung und Rechtsform hängen am MVP-Feedback. Keine Seite erwähnt KI.

## What is adopted

*Vorschläge, bis die Entscheidungen von `/map-sources` getroffen sind.*

| Element | From | How | Note |
|---|---|---|---|
| Prozessschritte und Reihenfolge | S1 | übernommen als Ablauf, eigene Worte | Lizenz von S1 klären |
| Leitfragen der Canvas-Felder | S1, S2–S5 | in eigenen Worten | keine Abbildungen übernehmen |
| Problembaum, 5 Whys, Folgen, SWOT | S1 | adaptiert | allgemeine Methoden |
| Bauen–Messen–Lernen, MVP, kritische Annahmen | S1, S6, S7 | adaptiert | |
| Status Annahme/recherchiert/belegt | Entscheidung 2026-11-21 | eigene Regel | Lücke in S1 |

## Conflicts between sources

| # | Wo | Konflikt |
|---|---|---|
| K1 | S1, Social Business Model Canvas | Text nennt „neun Bausteine“, listet zehn; Aufgabe sagt „Business Model Canvas“. |
| K2 | S1, S3 vs. S4 | Das Social Business Model Canvas in S1 hat keine Schlüsselressourcen und kein Leistungsversprechen; dafür Herausforderung, Veränderung, Lösung. |
| K3 | S1 (gelöst durch S11) | Die Kapitelseite trennt Nutzer:innen und Kund:innen; im Social Business Model Canvas fasst „Kund:innengruppen“ beide zusammen, und „Lösung“ fragt nach Verbesserung für Kund:innen statt Nutzer:innen. |
| K4 | S1 | Die Abkürzung „SBMC“ steht für Social und für Sustainable Business Model Canvas. |
| K5 | S1, MVP | MVP sei „kein Prototyp, schon ein fertiges Produkt“, die Beispiele sind manuelle Attrappen; Prüfkriterium nur „mindestens 2 Personen“, kein Erfolgskriterium. |
| K6 | S1 | Vision soll „sehr früh“ entstehen, steht aber nach Zielgruppe und Interviews; Problem-Hypothesen und Interviews stehen unter „Zielgruppe“, die Übersicht ordnet sie der Problemanalyse zu. |
| K7 | S1 | Mehrere Seiten sprechen von „letzter/nächster Woche“ (Wochenkurs), der Kurs ist laut Startseite im eigenen Tempo. |
| K8 | S1 | Wechsel zwischen „du“ und „ihr“; Dateinamen und Titel vertauscht (SWOT ↔ Lösungs-Hypothesen). |

## Gaps: outcomes no source covers

| Outcome (Block 3) | Lücke |
|---|---|
| (6) Status pro Canvas-Eintrag | S1 sagt „alles sind Annahmen“, hat aber kein Kennzeichnungssystem. |
| (7) Testplan mit Erfolgskriterium | S1 verlangt Feedback von 2 Personen, aber keine vorab festgelegten Kriterien. |
| (2) Interview-Auswertung | Clustering nur in einem Satz; keine Vorlage für Notizen und Zuordnung zu Hypothesen. |
| (6) Wirkung | S3 soll Wirkung „messbar“ machen, hat aber kein Feld dafür. |
| (6) Konsistenz Value Proposition Canvas ↔ Social Business Model Canvas | in S1 nicht beschrieben. |

## Left out

Finanzierung, Rechtsform, Pitch (nur verlinkt); Bonus „Zielsetzung & KPIs“; Notion-Anbindung (optionaler Export).
