#!/usr/bin/env python3
"""Prüft ein Projekt des Agentic Business Model Canvas: Annahmen-Register, Verweise, Belege, Tests, Interviews.

  check_project.py            # im Projektordner
  check_project.py <ordner>

Ausgabe je Prüfung: OK, OFFEN (noch nicht so weit) oder FEHLER (Regel verletzt). Exit-Code 1 bei einem FEHLER.
Nur Standardbibliothek.
"""
import datetime
import pathlib
import re
import sys

STATUS = {"annahme", "recherchiert", "belegt", "widerlegt"}
ID = re.compile(r"\[(A\d+)\]")
results = []


def report(level, check, message):
    results.append((level, check, message))


def read(root, name):
    path = root / name
    if not path.exists():
        return None
    return re.sub(r"<!--.*?-->", "", path.read_text(encoding="utf-8"), flags=re.S)


def register(text):
    """Rows of the first table whose header starts with 'ID'."""
    rows, header = [], None
    for line in text.splitlines():
        if not line.strip().startswith("|"):
            if header and rows:
                break
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if header is None:
            if cells and cells[0].lower() == "id":
                header = [c.lower() for c in cells]
            continue
        if set("".join(cells)) <= set("-: "):
            continue
        rows.append(dict(zip(header, cells)))
    return header, rows


def sections(text, prefix):
    """'### I1 · …' or '### T1: …' sections -> {id: body}."""
    found = {}
    for m in re.finditer(rf"^###\s+({prefix}\d+)\b.*?$(.*?)(?=^###\s|^##\s|\Z)", text, re.M | re.S):
        found[m.group(1)] = m.group(2)
    return found


def field(body, name):
    m = re.search(rf"^[ \t]*-[ \t]*\*\*{name}:\*\*[ \t]*(.*)$", body, re.M)
    return m.group(1).strip() if m else ""


def main():
    root = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    reg_text = read(root, "ASSUMPTIONS.md")
    if reg_text is None:
        print("FEHLER  ASSUMPTIONS.md fehlt: zuerst /setup-model ausführen.")
        sys.exit(1)
    header, rows = register(reg_text)
    if header is None or "status" not in header:
        report("FEHLER", "register", "keine Tabelle mit den Spalten ID | Aussage | Kategorie | Status | Quelle | Kritisch | Test")
        rows = []
    ids = {r.get("id", "") for r in rows}

    interviews = sections(read(root, "INTERVIEWS.md") or "", "I")
    tests = sections(read(root, "TESTS.md") or "", "T")

    # 1. Every [A#] in the texts exists in the register.
    missing = {}
    for name in ("CANVAS.md", "PROBLEM.md", "MODEL.md"):
        text = re.sub(r"`[^`]*`", "", read(root, name) or "")      # examples in inline code are not references
        for ref in ID.findall(text):
            if ref not in ids:
                missing.setdefault(ref, set()).add(name)
    report("FEHLER" if missing else "OK", "verweise",
           "; ".join(f"[{r}] in {', '.join(sorted(f))} steht nicht im Register" for r, f in sorted(missing.items()))
           or "alle Verweise stehen im Register")

    # 2. Status and sources.
    bad = []
    for r in rows:
        rid, status, source = r.get("id", "?"), r.get("status", "").lower(), r.get("quelle", "")
        if status not in STATUS:
            bad.append(f"{rid}: Status „{r.get('status', '')}“ ist ungültig")
        elif status == "recherchiert" and not re.search(r"https?://|www\.", source):
            bad.append(f"{rid}: recherchiert ohne Link als Quelle")
        elif status in ("belegt", "widerlegt"):
            own = re.findall(r"\b([IT]\d+)\b", source)
            if not own:
                bad.append(f"{rid}: {status} ohne eigenes Interview (I…) oder eigenen Test (T…) als Quelle")
            for ref in own:
                if ref not in (interviews if ref.startswith("I") else tests):
                    bad.append(f"{rid}: Quelle {ref} gibt es nicht")
    report("FEHLER" if bad else "OK", "status", "; ".join(bad) or f"{len(rows)} Einträge mit gültigem Status und Quelle")

    # 3. Critical open assumptions have a test card with a threshold.
    critical = [r for r in rows if r.get("kritisch", "").lower() in ("ja", "x", "yes")]
    open_critical = [r for r in critical if r.get("status", "").lower() == "annahme"]
    untested = []
    for r in open_critical:
        cards = [t for t, body in tests.items() if re.search(rf"\b{r['id']}\b", field(body, "Annahme"))]
        skipped = [t for t in cards if field(tests[t], "Status").lower().startswith("nicht durchgeführt")]
        open_cards = [t for t in cards if t not in skipped and not field(tests[t], "Ausgewertet").lower().startswith("ja")]
        if not cards:
            untested.append(f"{r['id']}: keine Testkarte")
        elif not any(field(tests[t], "Schwelle") for t in cards):
            untested.append(f"{r['id']}: Testkarte ohne Schwelle")
        elif not open_cards and skipped:
            untested.append(f"{r['id']}: Test nicht durchgeführt ({', '.join(skipped)}) – neuer Test oder Entscheidung")
        elif not open_cards:
            untested.append(f"{r['id']}: Test ausgewertet, Annahme weiter offen – neuer Test oder Entscheidung")
    if not critical:
        report("OFFEN", "kritische", "noch keine Annahme als kritisch markiert")
    elif untested:
        report("OFFEN", "kritische", "; ".join(untested))
    else:
        report("OK", "kritische", f"{len(open_critical)} offene kritische Annahmen haben eine Testkarte mit Schwelle")

    # 4. Tests with a result had a threshold.
    no_threshold = [t for t, body in tests.items() if field(body, "Ergebnis") and not field(body, "Schwelle")]
    report("FEHLER" if no_threshold else "OK", "schwellen",
           f"Ergebnis ohne Schwelle: {', '.join(no_threshold)}" if no_threshold else f"{len(tests)} Testkarten geprüft")

    # 5. One assumption per card; prerequisites exist; results evaluated; overdue cards.
    multi = [t for t, body in tests.items() if len(re.findall(r"\bA\d+\b", field(body, "Annahme"))) > 1]
    report("FEHLER" if multi else "OK", "eine-annahme",
           f"Karten mit mehr als einer Annahme (eine Schwelle pro Annahme): {', '.join(multi)}" if multi
           else "jede Karte prüft eine Annahme")
    def prereqs(body):
        """T-numbers a card waits for; a field starting with „keine“ names none (it may still mention cards)."""
        text = field(body, "Voraussetzung")
        if text.lower().startswith("keine"):
            return []
        return list(dict.fromkeys(re.findall(r"\bT\d+\b", text)))
    bad_pre = [f"{t}: {ref}" for t, body in tests.items()
               for ref in prereqs(body) if ref not in tests or ref == t]
    if bad_pre:
        report("FEHLER", "voraussetzung", "Voraussetzung gibt es nicht: " + ", ".join(bad_pre))
    passed = {t for t, body in tests.items()
              if field(body, "Status").lower().startswith("abgeschlossen") and field(body, "Ausgewertet").lower().startswith("ja")}
    early = [f"{t} (vor {ref})" for t, body in tests.items() if field(body, "Ergebnis")
             for ref in prereqs(body) if ref in tests and ref != t and ref not in passed]
    if early:
        report("OFFEN", "reihenfolge", "Ergebnis, obwohl die Voraussetzung noch nicht abgeschlossen ist: " + ", ".join(early)
               + " – Vorbehalt in der Quelle nennen (/log-evidence)")
    unevaluated = [t for t, body in tests.items()
                   if field(body, "Ergebnis") and not field(body, "Ausgewertet").lower().startswith("ja")
                   and not field(body, "Status").lower().startswith("läuft")]
    running = [t for t, body in tests.items() if field(body, "Status").lower().startswith("läuft")]
    today = datetime.date.today().isoformat()
    overdue = [t for t, body in tests.items()
               if not field(body, "Ergebnis") and not field(body, "Status").lower().startswith("nicht durchgeführt")
               and (d := re.search(r"\d{4}-\d{2}-\d{2}", field(body, "Bis wann")))
               and d.group(0) < today]
    if unevaluated or overdue or running:
        report("OFFEN", "ergebnisse", "; ".join(
            ([f"noch nicht ausgewertet: {', '.join(unevaluated)} (/log-evidence)"] if unevaluated else []) +
            ([f"läuft (Bedingung offen): {', '.join(running)}"] if running else []) +
            ([f"überfällig ohne Ergebnis: {', '.join(overdue)}"] if overdue else [])))
    else:
        report("OK", "ergebnisse", "alle Ergebnisse ausgewertet, keine Karte überfällig")

    # 6. Refuted assumptions still used in MODEL.md.
    refuted = {r.get("id", "") for r in rows if r.get("status", "").lower() == "widerlegt"
               or "ersetzt durch" in r.get("quelle", "").lower()}
    replaced = {r.get("id", "") for r in rows if "ersetzt durch" in r.get("quelle", "").lower()}
    used = sorted(set(ID.findall(re.sub(r"`[^`]*`", "", read(root, "MODEL.md") or ""))) & refuted)
    in_problem = sorted(set(ID.findall(re.sub(r"`[^`]*`", "", read(root, "PROBLEM.md") or ""))) & replaced)
    found = ([f"widerlegte oder ersetzte Annahmen in MODEL.md: {', '.join(used)} – prüfen, ob das Feld noch darauf aufbaut"] if used else []) + \
            ([f"ersetzte Annahmen in PROBLEM.md: {', '.join(in_problem)} – durch die neue ID ersetzen"] if in_problem else [])
    report("OFFEN" if found else "OK", "widerlegt", "; ".join(found) or "keine widerlegte Annahme in MODEL.md, keine ersetzte in PROBLEM.md")

    # 7. At least three evaluated interviews (handbook).
    done = [i for i, body in interviews.items() if field(body, "Ausgewertet").lower().startswith("ja")]
    report("OK" if len(done) >= 3 else "OFFEN", "interviews",
           f"{len(done)} von mindestens 3 Interviews ausgewertet ({len(interviews)} notiert)")

    width = max(len(c) for _, c, _ in results)
    for level, check, message in results:
        print(f"{level:6}  {check.ljust(width)}  {message}")
    sys.exit(1 if any(level == "FEHLER" for level, _, _ in results) else 0)


if __name__ == "__main__":
    main()
