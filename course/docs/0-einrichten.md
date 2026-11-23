# Einheit 0 · Einrichten und das Canvas lesen

**Ziel:** Der Agent läuft, die Skills sind installiert, euer Projektordner ist angelegt – und du weißt, welche Teile des Canvas ihr entscheidet und welche der Agent vorbereitet.
**Zeit:** ca. 55 Minuten, davon etwa 40 für die Installation.

## 1. Agent und Skill in einem Satz

Ein **Agent** ist ein KI-Programm, das in einem Ordner auf deinem Laptop arbeitet: Es liest und schreibt Dateien und führt Befehle aus. Ein **Skill** ist eine Anleitung für den Agenten, die er Schritt für Schritt befolgt. Wenn du `/setup-model` eingibst, liest der Agent die Anleitung „Projekt anlegen“ und richtet damit euren Ordner ein.

Das Skillset besteht aus zwölf solchen Anleitungen. Sie haben eine gemeinsame Regel: **Der Agent fragt, recherchiert und prüft – entscheiden tut ihr.**

## 2. Das Terminal öffnen

Das Terminal ist ein Fenster, in das du Befehle tippst statt zu klicken.

=== "macOS"
    Drücke ++cmd+space++, tippe `Terminal` und drücke ++enter++.

=== "Windows"
    Drücke die Windows-Taste, tippe `PowerShell` und drücke ++enter++.

=== "Linux"
    Öffne das Programm „Terminal“ aus dem Menü.

Du siehst eine Zeile, die auf deine Eingabe wartet. Einen Befehl kopierst du von dieser Seite, fügst ihn ein (macOS ++cmd+v++, Windows ++ctrl+v++ oder Rechtsklick) und drückst ++enter++.

## 3. Claude Code installieren

Wir zeigen hier **Claude Code**. OpenCode und Codex funktionieren auch – siehe die Kästen am Ende.

!!! warning "Zugang"
    Claude Code braucht ein **bezahltes** Konto bei Anthropic (ab dem Pro-Plan, laut [Anthropic](https://claude.com/pricing) 20 $ im Monat, Stand 2026-11-23). Im kostenlosen Plan ist es nicht enthalten. Fragt eure Kursleitung, ob der Kurs Zugänge stellt – oder nutzt OpenCode mit einem kostenlosen Modell (Kasten unten).

=== "macOS / Linux"
    ```bash
    curl -fsSL https://claude.ai/install.sh | bash
    ```

=== "Windows (PowerShell)"
    ```powershell
    irm https://claude.ai/install.ps1 | iex
    ```

Prüfe danach:

```bash
claude --version
```

Du siehst eine Versionsnummer. Wenn nicht: Schließe das Terminal, öffne es neu und versuche es noch einmal. Hilft das nicht, zeigt `claude doctor`, was fehlt.

Quelle: [Claude Code Setup](https://code.claude.com/docs/en/setup), abgerufen am 2026-11-23.

## 4. Einen Projektordner anlegen

Euer Projekt bekommt einen eigenen Ordner. `mkdir` legt ihn an, `cd` wechselt hinein:

```bash
mkdir mensa-retter-uebung
cd mensa-retter-uebung
```

Die Eingabezeile zeigt jetzt den Ordnernamen. Für die Übungen nutzt du diesen Übungsordner; für euer echtes Projekt legst du später einen zweiten an.

## 5. Claude Code starten und anmelden

```bash
claude
```

Beim ersten Start öffnet sich der Browser zur Anmeldung. Danach begrüßt dich Claude Code im Ordner. Du kannst jetzt auf Deutsch mit ihm schreiben.

## 6. Das Skillset hinzufügen

Beende Claude Code mit ++ctrl+c++ (zweimal) und gib im Terminal diese zwei Befehle ein:

```bash
claude plugin marketplace add opencampus-sh/agentic-business-model-canvas
claude plugin install agentic-business-model-canvas@agentic-business-model-canvas
```

Starte Claude Code wieder mit `claude`. Tippst du `/`, erscheinen die Befehle des Skillsets, zum Beispiel `/agentic-business-model-canvas:setup-model`.

!!! note "Kurze und lange Form"
    Im Kurs schreiben wir die kurze Form, zum Beispiel `/setup-model`. Als Plugin heißt derselbe Befehl `/agentic-business-model-canvas:setup-model`. Tippe einen Schrägstrich und die ersten Buchstaben, dann wählst du aus der Liste.

## 7. Das Projekt anlegen

Gib ein:

```text
/setup-model
```

Der Agent schaut sich den Ordner an und stellt drei Fragen – eine nach der anderen, jeweils mit seiner Empfehlung:

- **Ort:** Ist dieser Ordner der richtige? (Ja, der Übungsordner.)
- **Team und Idee:** Für die Übung: „Mensa-Retter“ – „Übrig gebliebenes Mensa-Essen abends an soziale Einrichtungen bringen.“
- **Bisherige Ergebnisse:** Für die Übung: keine.

Danach legt er die Dateien an und zeigt dir einen Abschnitt für `AGENTS.md`: Dort steht, wo eure Dateien liegen und welche Regeln er in jeder Sitzung befolgt. Du bestätigst den Inhalt.

**Ergebnis:** Im Ordner liegen jetzt unter anderem `CANVAS.md` (das Canvas), `ASSUMPTIONS.md` (das Annahmen-Register), `PROBLEM.md`, `INTERVIEWS.md`, `MODEL.md`, `TESTS.md`, `DECISIONS.md` und `SIGNALS.md`.

## 8. Das Canvas ansehen

```text
/show-canvas
```

Der Agent erzeugt eine Seite und nennt dir den Pfad (`build/canvas.html`). Öffne sie im Browser. Alle Blöcke sind gestrichelt: noch leer.

## 9. Das Canvas lesen

Das Canvas hat drei Spalten – **Problem & Wirkung**, **Geschäftsmodell**, **Testen & Lernen** – und elf Blöcke. Achte auf die Farben:

- **Lila – „Team entscheidet“:** Problem, Zielgruppe, Lösung, Erfolgskriterien, Annahmen, Geschäftsmodell, Lernen & Entscheiden. Der Agent darf vorschlagen, entscheiden tut ihr.
- **Grün – „Agent entwirft, Team bestätigt“:** Wissen & Recherche, Checks, Tests, Ergebnisse. Hier macht der Agent die Fleißarbeit, ihr prüft sie.

Block 6, **Annahmen**, ist die Grenze: Alles, was ihr über Problem, Zielgruppe oder Zahlungsbereitschaft sagt, steht dort mit einem Status – *Annahme*, *recherchiert*, *belegt* oder *widerlegt*. Ein Canvas kann voll aussehen und trotzdem nur Annahmen enthalten. Darum geht es in [Einheit 3](3-annahme-oder-beleg.md).

Mehr zu jedem Block: [Canvas-Leitfaden](https://github.com/opencampus-sh/agentic-business-model-canvas/blob/main/canvas/README.md).

## Selbstcheck

??? question "1. Was passiert, wenn du `/setup-model` eingibst?"
    Der Agent liest die Anleitung „Projekt anlegen“, schaut sich den Ordner an, stellt drei Fragen und legt erst nach deiner Bestätigung die Dateien an.

??? question "2. Wer entscheidet, was in Block 3 „Lösung & Wertangebot“ steht?"
    Das Team (lila Block). Der Agent darf Vorschläge machen und nachfragen.

??? question "3. Das Canvas ist komplett ausgefüllt. Wisst ihr damit, dass euer Geschäftsmodell funktioniert?"
    Nein. Erst das Annahmen-Register zeigt, was davon belegt ist – durch eure Interviews und Tests – und was nur vermutet.

??? question "4. Du startest Claude Code und siehst die Befehle des Skillsets nicht. Was prüfst du?"
    Ob du im richtigen Ordner bist, ob die zwei Plugin-Befehle ohne Fehler durchgelaufen sind, und ob du Claude Code danach neu gestartet hast.

## Übertragen auf euer Projekt

Leg einen zweiten Ordner für euer echtes Projekt an, wechsle hinein, starte den Agenten und ruf `/setup-model` auf. Habt ihr schon Ergebnisse in Notion, exportiert die Seite als Markdown und legt die Datei in den Ordner: Der Agent übernimmt jede Aussage daraus als *Annahme* ins Register.

---

??? info "OpenCode statt Claude Code"
    OpenCode lässt sich auch mit **kostenlosen Modellen** nutzen (laut [OpenCode Zen](https://opencode.ai/docs/zen) teils nur für begrenzte Zeit). Installation (macOS/Linux): `curl -fsSL https://opencode.ai/v2/install | bash` – für Windows gibt es einen Download auf [opencode.ai](https://opencode.ai/docs/). Start im Projektordner mit `opencode`, dann `/connect`, einen Anbieter wählen und mit `/models` ein Modell aussuchen.

    Die Skills installierst du mit `npx skills@latest add -g opencampus-sh/agentic-business-model-canvas` (braucht [Node.js](https://nodejs.org) 22.20 oder neuer); `-g` macht sie in allen Ordnern verfügbar, auch in den Übungsordnern. **Aufruf in OpenCode:** mit `@` statt `/`, zum Beispiel `@setup-model`.

    Quellen: [opencode.ai/docs](https://opencode.ai/docs/), [Skills](https://opencode.ai/docs/skills), abgerufen am 2026-11-23.

??? info "Codex statt Claude Code"
    Codex braucht ein ChatGPT-Konto; die Kommandozeile ist laut [OpenAI](https://developers.openai.com/codex/pricing) sicher ab ChatGPT Plus enthalten. Installation macOS/Linux: `curl -fsSL https://chatgpt.com/codex/install.sh | sh`; Windows (PowerShell): `powershell -ExecutionPolicy ByPass -c "irm https://chatgpt.com/codex/install.ps1 | iex"`. Start mit `codex`, dann „Sign in with ChatGPT“.

    Die Skills installierst du mit `npx skills@latest add -g opencampus-sh/agentic-business-model-canvas` (Node.js 22.20 oder neuer; `-g` für alle Ordner). **Aufruf in Codex:** mit `$` statt `/`, zum Beispiel `$setup-model`.

    Quellen: [Codex CLI](https://developers.openai.com/codex/cli), [Skills](https://developers.openai.com/codex/skills), abgerufen am 2026-11-23.

??? info "Optional: Was ist ein Commit?"
    Die Skills fragen am Ende oft: „Committen?“ Ein Commit ist ein gespeicherter Zwischenstand eures Ordners mit Git – wie ein Foto, zu dem ihr zurückkehren könnt. Das ist nützlich, aber nicht nötig. Wollt ihr es nutzen, sagt dem Agenten einfach „Ja, bitte committen“; er erledigt das.
