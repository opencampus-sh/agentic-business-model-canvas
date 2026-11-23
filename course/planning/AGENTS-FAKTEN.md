# Fakten zu den Agenten (für Einheit 0)

Recherche vom 2026-11-23, nur aus offiziellen Quellen (Herstellerdokumentation, offizielle Repositories). Quelle für Einheit 0; vor jeder Freigabe neu prüfen, weil sich Preise und Befehle ändern.

## Claude Code (ausführlich in Einheit 0)

| Thema | Fakt | Quelle |
|---|---|---|
| Systeme | macOS 13+, Windows 10 (1809+), Ubuntu 20.04+, Debian 10+; 4 GB RAM; Internet nötig | https://code.claude.com/docs/en/setup |
| Windows | läuft nativ in PowerShell oder CMD, WSL nicht nötig; Git for Windows empfohlen | ebd. |
| Installation macOS/Linux | `curl -fsSL https://claude.ai/install.sh \| bash` | ebd. |
| Installation Windows (PowerShell) | `irm https://claude.ai/install.ps1 \| iex` | ebd. |
| Alternativen | `brew install --cask claude-code`; `winget install Anthropic.ClaudeCode` | ebd. |
| Konto | „The free claude.ai plan does not include Claude Code access.“ Nötig: Pro, Max, Ultra, Team, Enterprise oder Console (API-Guthaben) | ebd. |
| Günstigster Plan | Pro: 20 $ monatlich (17 $ bei jährlicher Zahlung); Preise „subject to change“ | https://claude.com/pricing |
| Start | im Projektordner `claude`; beim ersten Start Anmeldung im Browser; `claude doctor` prüft die Installation | https://code.claude.com/docs/en/quickstart |
| Skills | Projekt: `.claude/skills/<name>/SKILL.md`; Aufruf mit `/name`; Plugin-Skills als `/plugin:skill` | https://code.claude.com/docs/en/skills |
| Plugin | `claude plugin marketplace add owner/repo`, dann `claude plugin install <plugin>@<marketplace>`; in einer offenen Sitzung danach `/reload-plugins` | https://code.claude.com/docs/en/discover-plugins |
| Ohne Terminal | Desktop-App (macOS, Windows, Linux), Web (claude.ai/code), VS Code, JetBrains | Setup und Quickstart |

## OpenCode (Kasten)

| Thema | Fakt | Quelle |
|---|---|---|
| Version | OpenCode 2 ist aktuell (Docs unter /docs/); OpenCode 1 archiviert; beide nicht parallel installierbar | https://opencode.ai/docs/ |
| Installation | `curl -fsSL https://opencode.ai/v2/install \| bash`; `brew install anomalyco/tap/opencode-v2`; `npm install -g @opencode/cli`; Windows: ZIP-Download (Paketmanager nicht unterstützt); Desktop-App | https://opencode.ai/docs/ |
| Windows | V2: nativ, keine WSL-Empfehlung; V1 empfahl WSL (veraltet) | ebd., https://opencode.ai/v1/docs/ |
| Konto | für OpenCode selbst keins; Modelle über einen Anbieter (`/connect`) | https://opencode.ai/docs/providers |
| Kostenlos | mehrere **kostenlose Modelle** im OpenCode-Zen-Katalog (0 $, teils „for a limited time“) | https://opencode.ai/docs/zen |
| Günstigster Plan | OpenCode Go 10 $/Monat | https://opencode.ai/docs/console/go |
| Start | `opencode` im Projektordner; dann `/connect`, Anbieter wählen, `/models` | https://opencode.ai/docs/cli, /docs/providers |
| Skills | Projekt: `.opencode/skills`, auch `.claude/skills` und `.agents/skills`; Aufruf **automatisch** oder mit **`@skill-id`** im Prompt – **kein Slash-Befehl** | https://opencode.ai/docs/skills |

## Codex CLI (Kasten)

| Thema | Fakt | Quelle |
|---|---|---|
| Installation | macOS/Linux: `curl -fsSL https://chatgpt.com/codex/install.sh \| sh`; Windows: `powershell -ExecutionPolicy ByPass -c "irm https://chatgpt.com/codex/install.ps1 \| iex"`; `npm install -g @openai/codex`; `brew install --cask codex` | https://developers.openai.com/codex/cli, README |
| Windows | **nativ** (Standard, Windows 11 empfohlen); WSL nur bei Bedarf – „nur WSL2“ in `docs/install.md` ist veraltet | https://developers.openai.com/codex/windows |
| Konto | Anmeldung mit ChatGPT-Konto; Plus 20 $/Monat schließt die CLI ein; Free und Go: „Limited Codex access“, ob die **CLI** dazugehört, ist **unklar** | https://developers.openai.com/codex/pricing |
| Start | `codex` im Projektordner, „Sign in with ChatGPT“ | README |
| Skills | Projekt: `.agents/skills`; Aufruf mit **`$skill-name`** oder `/skills`; auch automatisch | https://developers.openai.com/codex/skills |

## Skills installieren mit `npx skills`

| Thema | Fakt | Quelle |
|---|---|---|
| Voraussetzung | „Requires Node.js 22.20 or later.“ | https://github.com/vercel-labs/skills |
| Was `add` tut | fragt nach Skills und Agenten; installiert ins aktuelle Projekt (mit `-g` global) | ebd. |
| Pfade | Claude Code `.claude/skills/`; OpenCode und Codex `.agents/skills/` | `docs/agents.md` ebd. |
| Symlink oder Kopie | Standard Symlink auf eine gemeinsame Kopie; `--copy` für Kopien; `-y` überspringt Rückfragen | https://raw.githubusercontent.com/vercel-labs/skills/main/docs/commands.md |

## Folgen für den Kurs

- Claude Code braucht ein **bezahltes** Konto (ab Pro); das ist die Frage 17 an die Kursleitung.
- `npx skills` braucht **Node.js 22.20+** – eine zusätzliche Installation für Lena. Für Claude Code ist der Plugin-Weg ohne Node.js möglich; Einheit 0 sollte ihn als Hauptweg zeigen.
- **Kostenloser Weg:** OpenCode mit kostenlosen Zen-Modellen (teils befristet). Für die Kursleitung (Frage 17) die einzige Option ohne Bezahlung.
- **Aufruf der Skills unterscheidet sich:** Claude Code `/setup-model` (als Plugin `/agentic-business-model-canvas:setup-model`), OpenCode `@setup-model`, Codex `$setup-model`. Kursseiten und README müssen das zeigen.
