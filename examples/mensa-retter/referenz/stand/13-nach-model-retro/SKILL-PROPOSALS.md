# Vorschläge für das Skillset

Aus `/model-retro` am 2026-11-23. Ohne Inhalte unseres Projekts formuliert, damit wir sie als Issue im Repository des Skillsets einreichen können: https://github.com/opencampus-sh/agentic-business-model-canvas

## 1. Check: Testergebnis vor bestandener Voraussetzung

Der Check soll melden, wenn eine Testkarte schon ein Ergebnis hat, obwohl der Test, der vorher bestanden sein muss, noch nicht abgeschlossen ist – bisher prüft er nur, ob es die Voraussetzung gibt, und so lief bei uns eine Probewoche, bevor die Freigabe da war, ohne dass ein Check es zeigte.

```diff
--- a/skills/evidence-checks/scripts/check_project.py
+++ b/skills/evidence-checks/scripts/check_project.py
@@ -134,6 +134,13 @@
                for ref in re.findall(r"\bT\d+\b", field(body, "Voraussetzung")) if ref not in tests or ref == t]
     if bad_pre:
         report("FEHLER", "voraussetzung", "Voraussetzung gibt es nicht: " + ", ".join(bad_pre))
+    passed = {t for t, body in tests.items()
+              if field(body, "Status").lower().startswith("abgeschlossen") and field(body, "Ausgewertet").lower().startswith("ja")}
+    early = [f"{t} (vor {ref})" for t, body in tests.items() if field(body, "Ergebnis")
+             for ref in re.findall(r"\bT\d+\b", field(body, "Voraussetzung")) if ref in tests and ref != t and ref not in passed]
+    if early:
+        report("OFFEN", "reihenfolge", "Ergebnis, obwohl die Voraussetzung noch nicht abgeschlossen ist: " + ", ".join(early)
+               + " – Vorbehalt in der Quelle nennen (/log-evidence)")
     unevaluated = [t for t, body in tests.items()
                    if field(body, "Ergebnis") and not field(body, "Ausgewertet").lower().startswith("ja")
                    and not field(body, "Status").lower().startswith("läuft")]
```

## 2. Regel in `to-tests`: kein Preisangebot ohne Preis

`/to-tests` soll prüfen, ob ein vorgeschlagenes Angebot mit Preis überhaupt machbar ist, solange Kosten oder Preis noch offene Fragen sind – sonst empfiehlt der Agent einen Test, den das Team nicht durchführen kann, und es weicht auf eine schwächere Frage aus.

```diff
--- a/skills/to-tests/SKILL.md
+++ b/skills/to-tests/SKILL.md
@@ -26,6 +26,7 @@
 - Tests, die eine Annahme nur mit einer Meinung prüfen, wo Verhalten möglich wäre;
 - Schwellen, die so niedrig sind, dass jedes Ergebnis sie erfüllt;
 - Tests, die auf einer anderen, ungetesteten kritischen Annahme aufbauen (Reihenfolge);
+- Tests, die ein Angebot mit Preis oder Betrag brauchen, obwohl Preis oder Kosten noch als offene Frage im Canvas stehen (dann zuerst die Zahl klären, oder eine Zusage ohne Preis testen und sagen, was sie nicht zeigt);
 - ein Plan, der für das Team in der verfügbaren Zeit nicht machbar ist (frag nach der Zeit, schätze nicht).
 
 ## 2. Stop-Point
```
