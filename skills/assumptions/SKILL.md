---
name: assumptions
description: Regeln für die Grenze zwischen Annahme und Beleg im Agentic Business Model Canvas – welcher Status eine Aussage hat, wie sich ungeprüfte Annahmen einschleichen und wie man sie erkennt. Verwenden beim Schreiben ins Canvas, ins Annahmen-Register, in PROBLEM.md oder MODEL.md, beim Auswerten von Interviews und Tests und wenn ein Ergebnis zu gut klingt.
---

# Annahmen

Die **Grenze** des Canvas (Block 6) trennt, was das Team weiß, von dem, was es vermutet. Jede Aussage über Problem, Zielgruppe, Lösung, Zahlungsbereitschaft, Kanäle, Partner, Kosten oder Wirkung steht im Annahmen-Register (`ASSUMPTIONS.md`) mit Status und Quelle. Eine Aussage, die als Wissen auftritt, aber nicht belegt ist, ist eine **Grenzüberschreitung**: Das Canvas sieht fertig aus, und das Team baut auf Sand.

## Status

| Status | Bedeutung | Quelle |
|---|---|---|
| Annahme | Das Team vermutet es. | keine nötig; woher die Vermutung kommt, wenn bekannt |
| recherchiert | Steht so in einer Recherche (Statistik, Studie, Website eines Anbieters). Zeigt, was es gibt; belegt kein Bedürfnis der Zielgruppe. | Link, Abrufdatum |
| belegt | Ein eigenes Interview oder ein eigener Test des Teams stützt es, gemessen an der vorher festgelegten Schwelle. | Interview-ID (`I2`) oder Test-ID (`T1`) |
| widerlegt | Ein eigenes Interview oder ein eigener Test hat es nicht bestätigt. | Interview- oder Test-ID |

## Regeln

- **Nur das Team belegt.** *Belegt* und *widerlegt* setzt der Agent nur mit Zustimmung des Teams und nur mit Verweis auf ein Interview oder einen Test des Teams.
- **Der Agent erfindet nichts.** Keine Interview-Aussagen, Zitate, Zahlungsbereitschaften, Nutzerzahlen oder Marktgrößen ohne Quelle. Wo eine Zahl fehlt, schreibe die Lücke als Annahme ins Register und frage.
- **Recherche ist kein Beleg für ein Bedürfnis.** Die Zahl der Tafeln in Deutschland, mit Quelle, kann *recherchiert* sein; „Tafeln wollen Mensa-Essen“ bleibt *Annahme*, bis Tafeln es sagen oder tun.
- **Ein Interview belegt, was die Person erlebt und tut, nicht, was sie in Zukunft tun würde.** „Würdet ihr das nutzen?“ – „Ja“ ist kein Beleg für Nutzung oder Zahlungsbereitschaft. Das belegt erst ein Test (Zusage, Vorbestellung, Bezahlung).
- **Kein Text ohne ID.** Im Canvas, in `PROBLEM.md` und `MODEL.md` steht jede Aussage mit ihrer ID, z. B. `[A4]`. Neue Aussagen kommen zuerst ins Register.
- **Kritisch entscheidet das Team.** Der Agent schlägt vor, welche Annahmen kritisch sind (andere bauen darauf auf; wenn sie fällt, fällt die Idee), das Team entscheidet.
- **Widerlegt bleibt sichtbar.** Eine widerlegte Annahme wird nicht gelöscht; sie ist ein Ergebnis.

## Wie sich ungeprüfte Annahmen einschleichen

- **Der Agent füllt aus.** Das Team bittet „Füll das Modell aus“, und plausible Sätze erscheinen. Jeder davon ist eine Annahme – auch wenn er überzeugend klingt.
- **Recherche wird zum Beleg.** Eine Statistik über das Problem wird als Beweis für das Bedürfnis nach genau dieser Lösung gelesen.
- **Suggestive Interviews.** Das Team pitcht die Idee und fragt, ob sie gut ist. Die Antworten sind höflich, nicht belastbar.
- **Höfliche Umfragen.** „Würdet ihr 50 € zahlen?“ – Zustimmung kostet nichts.
- **Die eigene Erfahrung.** „Bei uns in der Mensa ist das so“ ist eine Beobachtung an einem Ort, kein Beleg für alle.
- **Schwelle nach dem Test.** Das Kriterium wird erst festgelegt, wenn das Ergebnis da ist, und passt dann zufällig.
- **Nutzer:innen gleich Kund:innen.** Eine Zahlungsbereitschaft der Nutzer:innen wird angenommen, obwohl eine dritte Partei zahlen müsste – oder umgekehrt.

## Prüfen

- Bei jeder neuen Aussage: Steht sie im Register? Welcher Status, welche Quelle?
- Bei *belegt*: Verweist die Quelle auf ein eigenes Interview oder einen eigenen Test? Stimmt der Wortlaut der Notiz mit der Aussage überein? Wurde die Schwelle vorher festgelegt?
- Bei einem Ergebnis, das zu gut klingt: Wer hat gefragt, wie, wen? Lade `evidence-checks`.
- Der Check `check_project.py` (Skill `evidence-checks`) findet fehlende IDs, ungültige Status und *belegt* ohne Interview oder Test automatisch.
