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
| Installation | `curl -fsSL https://opencode.ai/v2/install \| bash`; `brew install anomalyco/tap/opencode-v2`; Desktop-App (Beta) für macOS, Windows, Linux | https://github.com/sst/opencode |
| Konto, Modelle, Kosten, Start, Skills | **nicht geprüft** – opencode.ai war nicht erreichbar | – |
| Skills (laut `npx skills`) | Projekt: `.agents/skills/` | https://raw.githubusercontent.com/vercel-labs/skills/main/docs/agents.md |

## Codex CLI (Kasten)

| Thema | Fakt | Quelle |
|---|---|---|
| Installation | `curl -fsSL https://chatgpt.com/codex/install.sh \| sh`; Windows: `powershell -ExecutionPolicy ByPass -c "irm https://chatgpt.com/codex/install.ps1 \| iex"`; `brew install --cask codex` | https://github.com/openai/codex |
| Windows | **widersprüchlich**: `docs/install.md` nennt nur WSL2, das README einen nativen PowerShell-Installer | ebd. |
| Konto | „Sign in with ChatGPT“; Plus, Pro, Business, Edu oder Enterprise; Preise **nicht geprüft** (openai.com nicht erreichbar) | ebd. |
| Start | `codex` im Projektordner | ebd. |
| Skills (laut `npx skills`) | Projekt: `.agents/skills/`; Aufruf **nicht geprüft** | vercel-labs/skills |

## Skills installieren mit `npx skills`

| Thema | Fakt | Quelle |
|---|---|---|
| Voraussetzung | „Requires Node.js 22.20 or later.“ | https://github.com/vercel-labs/skills |
| Was `add` tut | fragt nach Skills und Agenten; installiert ins aktuelle Projekt (mit `-g` global) | ebd. |
| Pfade | Claude Code `.claude/skills/`; OpenCode und Codex `.agents/skills/` | `docs/agents.md` ebd. |

## Folgen für den Kurs

- Claude Code braucht ein **bezahltes** Konto (ab Pro); das ist die Frage 17 an die Kursleitung.
- `npx skills` braucht **Node.js 22.20+** – eine zusätzliche Installation für Lena. Für Claude Code ist der Plugin-Weg ohne Node.js möglich; Einheit 0 sollte ihn als Hauptweg zeigen.
- OpenCode- und Codex-Kästen erst schreiben, wenn `opencode.ai`, `developers.openai.com` und `openai.com` erreichbar sind.
