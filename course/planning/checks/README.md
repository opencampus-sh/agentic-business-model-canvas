# Checks

Was gelten muss, bevor eine Einheit freigegeben wird (Katalog: Skill `course-checks` von Agentic Course Creation). Typ: automatisch, Walk-through oder manuell.

| Check | Typ | Befehl oder wer | Einheiten |
|---|---|---|---|
| Jedes Lernziel wird mindestens einmal geübt und geprüft | manuell | `/to-course-plan` | alle |
| Jeder Schritt liegt innerhalb der Grenze (Block 6) | Walk-through | `/walk-through` | alle |
| Jeder Befehl und jeder Pfad auf den Kursseiten stimmt mit dem Skillset überein (Skill-Namen, Dateien) | automatisch | `python3 ../../scripts/check_skillset.py` (Skill-Verweise) und Suche | alle |
| Übungs-Startzustände und Lösungen existieren und passen zur Seite | manuell | Kursleitung | 1–5 |
| Installationsbefehle auf der Seite von Einheit 0 stimmen mit dem README überein (`claude plugin …`, `npx skills@latest add -g …`) | automatisch (Suche) | `grep -F` jedes Befehls in `README.md` und `course/docs/0-einrichten.md` | 0 |
| Links funktionieren | manuell | Kursleitung, später Link-Check in der Seiten-Pipeline | alle |
| Einrichtung funktioniert von null an (Agent, Skills installieren) | Walk-through oder manuell | `/walk-through 0` | 0 |
| Alle Beispieldaten sind als fiktiv gekennzeichnet | manuell | Kursleitung | alle |
