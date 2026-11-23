# Vorschläge für das Skillset

Aus `/model-retro` am 2026-12-21. Ohne Inhalte des Projekts; zum Einreichen als Issue unter https://github.com/opencampus-sh/agentic-business-model-canvas (macht Jule).

## 1. Der Check *reihenfolge* soll „keine (… wie T3)“ nicht als Voraussetzung lesen

Wenn im Feld *Voraussetzung* „keine“ steht und danach zur Erklärung eine andere Karte genannt wird, meldet `check_project.py` diese Karte trotzdem als Voraussetzung, und es nennt dieselbe Meldung mehrfach; das Skript soll ein Feld, das mit „keine“ beginnt, als „keine Voraussetzung“ lesen und jede Karte nur einmal nennen.

```diff
--- a/.claude/skills/evidence-checks/scripts/check_project.py
+++ b/.claude/skills/evidence-checks/scripts/check_project.py
@@ -133,14 +133,19 @@
     report("FEHLER" if multi else "OK", "eine-annahme",
            f"Karten mit mehr als einer Annahme (eine Schwelle pro Annahme): {', '.join(multi)}" if multi
            else "jede Karte prüft eine Annahme")
+    def prereqs(body):
+        value = field(body, "Voraussetzung")
+        if value.lower().startswith("keine"):       # „keine (gleiches Gespräch wie T3)“ nennt T3 nur zur Erklärung
+            return []
+        return sorted(set(re.findall(r"\bT\d+\b", value)))
     bad_pre = [f"{t}: {ref}" for t, body in tests.items()
-               for ref in re.findall(r"\bT\d+\b", field(body, "Voraussetzung")) if ref not in tests or ref == t]
+               for ref in prereqs(body) if ref not in tests or ref == t]
     if bad_pre:
         report("FEHLER", "voraussetzung", "Voraussetzung gibt es nicht: " + ", ".join(bad_pre))
     passed = {t for t, body in tests.items()
               if field(body, "Status").lower().startswith("abgeschlossen") and field(body, "Ausgewertet").lower().startswith("ja")}
     early = [f"{t} (vor {ref})" for t, body in tests.items() if field(body, "Ergebnis")
-             for ref in re.findall(r"\bT\d+\b", field(body, "Voraussetzung")) if ref in tests and ref != t and ref not in passed]
+             for ref in prereqs(body) if ref in tests and ref != t and ref not in passed]
     if early:
         report("OFFEN", "reihenfolge", "Ergebnis, obwohl die Voraussetzung noch nicht abgeschlossen ist: " + ", ".join(early)
                + " – Vorbehalt in der Quelle nennen (/log-evidence)")
```

## 2. Ein Test, der nicht gemacht wurde, bekommt einen eigenen Status

Sagt ein Team „Den Test haben wir nicht gemacht“, gibt es dafür in der Testkarte keinen Status, und der Grund geht verloren; die Vorlage soll den Status „nicht durchgeführt (mit Grund)“ kennen, und `/log-evidence` soll nach Grund und neuem Datum fragen, statt ein Ergebnis einzutragen.

```diff
--- a/.claude/skills/log-evidence/SKILL.md
+++ b/.claude/skills/log-evidence/SKILL.md
@@ -32,6 +32,7 @@
 - Vorschlag: *belegt*, wenn die Schwelle erreicht ist; *widerlegt*, wenn nicht; offen, wenn der Test zu klein war, abgebrochen wurde oder das Ergebnis an eine noch offene Bedingung geknüpft ist (dann bleibt die Karte auf *läuft*). Will das Team die Schwelle nach dem Ergebnis ändern, gilt: nie einen Check lockern, damit er besteht – mit geänderter Schwelle ist das Ergebnis nur noch ein Signal.
 - Beobachtungen aus dem Test, die nicht die Annahme der Karte betreffen, kommen als eigene Zeilen ins Register (siehe *Wann etwas belegt ist* in `assumptions`).
 - Bleibt eine Karte auf *läuft*, setz *Ausgewertet: teilweise*; ausgewertet ist sie erst, wenn die Bedingung erfüllt oder gefallen ist.
+- Sagt das Team, ein Test wurde nicht gemacht, schreib kein Ergebnis: Setz *Status: nicht durchgeführt*, frag nach dem Grund (in die Karte) und ob es ein neues *Bis wann* gibt oder die Annahme auf anderem Weg geklärt wird. Die Annahme bleibt, wie sie ist.
 
 ## 4. Stop-Point
 
--- a/.claude/skills/setup-model/templates/TESTS.md
+++ b/.claude/skills/setup-model/templates/TESTS.md
@@ -15,7 +15,7 @@
 - **Messgröße:** was ihr zählt oder beobachtet
 - **Schwelle:** ab wann die Annahme als belegt gilt (z. B. „mindestens 3 von 5 Einrichtungen sagen verbindlich zu“)
 - **Ergebnis:** (nach dem Test) was herauskam, gemessen an der Schwelle
-- **Status:** geplant | läuft | abgeschlossen
+- **Status:** geplant | läuft | abgeschlossen | nicht durchgeführt (mit Grund)
 - **Ausgewertet:** nein
 -->
 
```
