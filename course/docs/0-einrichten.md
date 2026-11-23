# Einheit 0 · Einrichten und das Canvas lesen

**Ziel:** Der Agent läuft, die Skills sind installiert, euer Projektordner ist angelegt – und du weißt, welche Teile des Canvas ihr entscheidet und welche der Agent vorbereitet.
**Zeit:** ca. 65 Minuten, davon etwa 45 für die Installation und die Werkzeuge.

## 1. Agent und Skill in einem Satz

Ein **Agent** ist ein KI-Programm, das in einem Ordner auf deinem Laptop arbeitet: Es liest und schreibt Dateien und führt Befehle aus. Ein **Skill** ist eine Anleitung für den Agenten, die er Schritt für Schritt befolgt. Wenn du `/setup-model` eingibst, liest der Agent die Anleitung „Projekt anlegen“ und richtet damit euren Ordner ein.

Das Skillset hat 14 Skills. **Zwölf** davon rufst du selbst auf, zum Beispiel `/setup-model`. Zwei sind Nachschlage-Regeln, die der Agent von selbst lädt: `assumptions` und `evidence-checks`. Sie stehen auch in der Liste, aber du brauchst sie nicht aufzurufen.

Alle Skills haben eine gemeinsame Regel: **Der Agent fragt, recherchiert und prüft – entscheiden tut ihr.**

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

Die Eingabezeile zeigt jetzt den Ordnernamen. Der Ordner liegt in deinem Benutzerordner – dort, wo das Terminal beim Öffnen startet. Für die Übungen nutzt du diesen Übungsordner; für euer echtes Projekt legst du später einen zweiten an.

## 5. Claude Code starten und anmelden

Starte Claude Code immer **in einem Projektordner**, nicht direkt im Benutzerordner:

```bash
claude
```

Danach begrüßt dich Claude Code im Ordner. Du kannst jetzt auf Deutsch mit ihm schreiben.

!!! tip "Der erste Start: drei Fragen auf Englisch"
    Claude Code fragt auf Englisch. Du wählst mit den Pfeiltasten und bestätigst mit ++enter++.

    - **Anmelden.** Beim ersten Start fragt Claude Code nach der Anmeldung. Wähle das Konto mit deinem Claude-Abo (zum Beispiel Pro). Dann öffnet sich der Browser; melde dich dort an und kehre ins Terminal zurück. Claude Code merkt sich die Anmeldung.
    - **Vertraust du diesem Ordner?** In jedem neuen Ordner fragt Claude Code, ob du den Dateien darin vertraust („trust“). Für deinen eigenen Projektordner und die Übungsordner antwortest du mit Ja. In einem Ordner, den du nicht kennst, antwortest du mit Nein.
    - **Darf ich das tun?** Bevor der Agent eine Datei schreibt oder einen Befehl ausführt, kann er um Erlaubnis fragen: „Do you want to proceed?“ Lies kurz, was er tun will. Betrifft es deinen Projektordner, wähle **Yes**. Bei Dateien gilt „Yes, and don't ask again …“ bis zum Ende der Sitzung – danach fragt er bei Dateiänderungen nicht mehr. Bei Befehlen gilt diese Wahl dauerhaft; wähle dort im Zweifel einfach **Yes**. Kommt dir etwas falsch vor, zum Beispiel ein Ordner außerhalb deines Projekts, wähle **No**.

    Wie oft Claude Code fragt, hängt von der Einstellung ab. Manchmal fragt es kaum. Quellen: [Quickstart](https://code.claude.com/docs/en/quickstart), [Sicherheit](https://code.claude.com/docs/en/security), [Berechtigungen](https://code.claude.com/docs/en/permissions), abgerufen am 2026-11-23.

## 6. Werkzeuge prüfen: Python 3 und Git

Zwei Programme brauchen die Skills außerdem:

- **Python 3** baut die Canvas-Seite (`/show-canvas`) und führt den Check aus, der eure Dateien prüft (ab Einheit 1).
- **Git** speichert Zwischenstände eures Ordners. In Einheit 5 zeigt so ein Zwischenstand, dass ihr eine Schwelle festgelegt habt, *bevor* ihr testet.

Am einfachsten fragst du den Agenten. Schreib ihm:

```text
Prüf bitte, ob Python 3 und Git installiert sind, und hilf mir, fehlende zu installieren.
```

Er prüft das und schlägt dir die Befehle vor. Bestätige sie mit **Yes**. Fragt dein Rechner nach deinem Passwort oder einer Bestätigung, gib sie.

Lieber selbst? Beende Claude Code mit ++ctrl+c++ (zweimal) und tippe im Terminal:

=== "Windows"
    ```powershell
    winget install Python.Python.3.12
    winget install Git.Git
    ```

    `winget` gehört zu Windows 11 und aktuellen Versionen von Windows 10 (als Teil des „App Installer“). Schließe danach das Terminal, öffne es neu und prüfe mit `python --version` und `git --version`.

    Quellen: [WinGet](https://learn.microsoft.com/en-us/windows/package-manager/winget/), [Git für Windows](https://git-scm.com/install/windows), abgerufen am 2026-11-23.

=== "macOS"
    ```bash
    python3 --version
    git --version
    ```

    Fehlen die Werkzeuge, öffnet sich ein Fenster, das die „Command Line Tools“ von Apple installieren will. Bestätige die Installation und warte, bis sie fertig ist. Danach sind Python 3 und Git da; tippe die zwei Befehle noch einmal.

    Quellen: [Apple](https://developer.apple.com/documentation/xcode/installing-the-command-line-tools), [Python unter macOS](https://docs.python.org/3/using/mac.html), [Git für macOS](https://git-scm.com/install/mac), abgerufen am 2026-11-23.

=== "Linux"
    Installiere beides mit dem Paketmanager deines Systems, zum Beispiel unter Ubuntu oder Debian:

    ```bash
    sudo apt install python3 git
    ```

Klappt die Installation nicht, geht es trotzdem weiter: Ohne Python zeigt der Agent das Canvas als Text und macht den Check von Hand.

## 7. Das Skillset hinzufügen

Beende Claude Code mit ++ctrl+c++ (zweimal), falls er noch läuft, und gib im Terminal diese zwei Befehle ein:

```bash
claude plugin marketplace add opencampus-sh/agentic-business-model-canvas
claude plugin install agentic-business-model-canvas@agentic-business-model-canvas
```

Das Skillset gilt jetzt für **alle** deine Ordner, auch für die Übungsordner der nächsten Einheiten.

Starte Claude Code wieder mit `claude`. Tippst du `/`, erscheinen die Befehle des Skillsets, zum Beispiel `/agentic-business-model-canvas:setup-model`.

!!! note "Kurze und lange Form"
    Im Kurs schreiben wir die kurze Form, zum Beispiel `/setup-model`. Als Plugin heißt derselbe Befehl `/agentic-business-model-canvas:setup-model`. Tippe einen Schrägstrich und die ersten Buchstaben, dann wählst du aus der Liste.

## 8. Das Projekt anlegen

Gib ein:

```text
/setup-model
```

Der Agent schaut sich den Ordner an und stellt drei Fragen – eine nach der anderen, jeweils mit seiner Empfehlung:

- **Ort:** Ist dieser Ordner der richtige? (Ja, der Übungsordner.) Fragt er nach Git oder GitHub: „Kein Git, nur lokal.“
- **Team und Idee:** Für die Übung: „Mensa-Retter“ – „Übrig gebliebenes Mensa-Essen abends an soziale Einrichtungen bringen.“
- **Bisherige Ergebnisse:** Für die Übung: keine.

Dann legt er die Dateien an. Zum Schluss zeigt er dir einen Abschnitt in `AGENTS.md`: Dort steht, wo eure Dateien liegen und welche Regeln er in jeder Sitzung befolgt. Du bestätigst den Inhalt.

**Ergebnis:** Im Ordner liegen jetzt unter anderem `CANVAS.md` (das Canvas), `ASSUMPTIONS.md` (das Annahmen-Register), `PROBLEM.md`, `INTERVIEWS.md`, `MODEL.md`, `TESTS.md`, `DECISIONS.md` und `SIGNALS.md`.

## 9. Das Canvas ansehen

```text
/show-canvas
```

Der Agent erzeugt eine Seite und nennt dir den Pfad: `build/canvas.html`. So öffnest du sie:

- **Am einfachsten:** Schreib dem Agenten „Öffne die Canvas-Seite im Browser.“
- **Mit der Maus:** Öffne den Projektordner im Finder (macOS) oder Explorer (Windows), dann den Ordner `build`, und doppelklicke `canvas.html`.

Alle Blöcke sind gestrichelt: noch leer. Fehlt Python, zeigt dir der Agent das Canvas stattdessen als Text im Terminal.

### Dateien öffnen

Diese Handgriffe brauchst du in allen Einheiten.

- **Den Projektordner finden.** Schreib dem Agenten: „Öffne den Projektordner im Finder.“ (Windows: „im Explorer“.) Oder such ihn selbst: Er liegt in deinem Benutzerordner. Im Finder öffnet ++cmd+shift+h++ den Benutzerordner.
- **Eine `.md`-Datei lesen.** Die Projektdateien sind Markdown-Dateien: einfacher Text, in dem `#` eine Überschrift markiert und `|` eine Tabelle baut. Am einfachsten schreibst du dem Agenten: „Zeig mir `PROBLEM.md`.“ Oder du öffnest die Datei mit einem Texteditor: Rechtsklick auf die Datei → „Öffnen mit“ → TextEdit (macOS) oder Editor (Windows). Ein Doppelklick öffnet sie manchmal in einem Programm, das du nicht kennst.

## 10. Das Canvas lesen

Das Canvas hat drei Spalten – **Problem & Wirkung**, **Geschäftsmodell**, **Testen & Lernen** – und elf Blöcke. Achte auf die Farben:

- **Lila – „Team entscheidet“:** Herausforderung & Vision, Nutzer:innen & Kund:innen, Lösung & Wertangebot, Erfolgskriterien, Annahmen, Geschäftsmodell, Lernen & Entscheiden. Der Agent darf vorschlagen, entscheiden tut ihr.
- **Grün – „Agent entwirft, Team bestätigt“:** Wissen & Recherche, Checks, Tests & MVP, Ergebnisse & Signale. Hier macht der Agent die Fleißarbeit, ihr prüft sie.

Block 6, **Annahmen**, ist die Grenze: Alles, was ihr über Problem, Zielgruppe oder Zahlungsbereitschaft sagt, steht dort mit einem Status – *Annahme*, *recherchiert*, *belegt* oder *widerlegt*. Ein Canvas kann voll aussehen und trotzdem nur Annahmen enthalten. Darum geht es in [Einheit 3](3-annahme-oder-beleg.md).

Mehr zu jedem Block: [Canvas-Leitfaden](https://github.com/opencampus-sh/agentic-business-model-canvas/blob/main/canvas/README.md).

## Selbstcheck

??? question "1. Was passiert, wenn du `/setup-model` eingibst?"
    Der Agent liest die Anleitung „Projekt anlegen“, schaut sich den Ordner an und stellt drei Fragen. Dann legt er die Dateien an. Zum Schluss zeigt er dir den Abschnitt in `AGENTS.md`, und du bestätigst ihn.

??? question "2. Wer entscheidet, was in Block 3 „Lösung & Wertangebot“ steht?"
    Das Team (lila Block). Der Agent darf Vorschläge machen und nachfragen.

??? question "3. Das Canvas ist komplett ausgefüllt. Wisst ihr damit, dass euer Geschäftsmodell funktioniert?"
    Nein. Erst das Annahmen-Register zeigt, was davon belegt ist – durch eure Interviews und Tests – und was nur vermutet.

??? question "4. Du startest Claude Code und siehst die Befehle des Skillsets nicht. Was prüfst du?"
    Am Ordner liegt es nicht: Das Skillset gilt für alle deine Ordner. Prüfe:

    - Sind die zwei Plugin-Befehle ohne Fehlermeldung durchgelaufen? Sonst gib sie noch einmal ein.
    - Hast du Claude Code danach neu gestartet?
    - Ist das Plugin installiert? `claude plugin list` im Terminal zeigt es, ebenso `/plugin` in Claude Code (Reiter „Installed“).
    - Nutzt du OpenCode oder Codex? Dort rufst du die Skills mit `@` oder `$` auf, nicht mit `/`.

## Übertragen auf euer Projekt

Leg einen zweiten Ordner für euer echtes Projekt an, wechsle hinein, starte den Agenten und ruf `/setup-model` auf. Der Agent übernimmt jede Aussage aus euren bisherigen Ergebnissen als *Annahme* ins Register.

Habt ihr schon Ergebnisse in Notion? Klicke auf der Notion-Seite oben rechts auf **•••**, dann auf **Export**. Wähle das Format **Markdown & CSV** und klicke auf **Export**. Du bekommst eine ZIP-Datei. Entpacke sie (Doppelklick; Windows: Rechtsklick → „Alle extrahieren“) und leg die `.md`-Datei in euren Projektordner. Quelle: [Notion-Hilfe](https://www.notion.com/help/export-your-content), abgerufen am 2026-11-23.

---

??? info "OpenCode statt Claude Code"
    OpenCode lässt sich auch mit **kostenlosen Modellen** nutzen (laut [OpenCode Zen](https://opencode.ai/docs/zen) teils nur für begrenzte Zeit). Installation (macOS/Linux): `curl -fsSL https://opencode.ai/v2/install | bash` – für Windows gibt es einen Download auf [opencode.ai](https://opencode.ai/docs/). Start im Projektordner mit `opencode`, dann `/connect`, einen Anbieter wählen und mit `/models` ein Modell aussuchen.

    Die Skills installierst du mit `npx skills@latest add -g opencampus-sh/agentic-business-model-canvas` (braucht [Node.js](https://nodejs.org) 22.20 oder neuer); `-g` macht sie in allen Ordnern verfügbar, auch in den Übungsordnern. **Aufruf in OpenCode:** mit `@` statt `/`, zum Beispiel `@setup-model`.

    Quellen: [opencode.ai/docs](https://opencode.ai/docs/), [Skills](https://opencode.ai/docs/skills), abgerufen am 2026-11-23.

??? info "Codex statt Claude Code"
    Codex braucht ein ChatGPT-Konto; die Kommandozeile ist laut [OpenAI](https://developers.openai.com/codex/pricing) sicher ab ChatGPT Plus enthalten. Installation macOS/Linux: `curl -fsSL https://chatgpt.com/codex/install.sh | sh`; Windows (PowerShell): `powershell -ExecutionPolicy ByPass -c "irm https://chatgpt.com/codex/install.ps1 | iex"`. Start mit `codex`, dann „Sign in with ChatGPT“.

    Die Skills installierst du mit `npx skills@latest add -g opencampus-sh/agentic-business-model-canvas` (Node.js 22.20 oder neuer; `-g` für alle Ordner). **Aufruf in Codex:** mit `$` statt `/`, zum Beispiel `$setup-model`.

    Quellen: [Codex CLI](https://developers.openai.com/codex/cli), [Skills](https://developers.openai.com/codex/skills), abgerufen am 2026-11-23.

??? info "Was ist ein Commit?"
    Ein Commit ist ein gespeicherter Zwischenstand eures Ordners mit Git – wie ein Foto, zu dem ihr zurückkehren könnt. Die Skills schlagen am Ende einen Commit vor, wenn euer Ordner Git nutzt.

    **In den Übungsordnern gibt es kein Git.** Fragt der Agent dort nach einem Commit, antworte „Nein“.

    **In eurem eigenen Projekt** lohnt sich Git: In Einheit 5 zeigt ein Commit, dass die Schwelle vor dem Test feststand. Sag dem Agenten dann „Richte bitte Git in diesem Ordner ein“ und später „Ja, bitte committen“; er erledigt das.
