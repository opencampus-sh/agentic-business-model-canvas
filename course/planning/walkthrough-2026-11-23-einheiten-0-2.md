# Walk-through units 0–2 (Agentic Business Model Canvas, self-study course): Lena and Jonas, 2026-11-23

Skill: `/walk-through` (Agentic Course Creation), with `assumed-knowledge` loaded. Material walked: `course/docs/index.md`, `0-einrichten.md`, `1-problem.md`, `2-interviews.md`, `README.md`, ZIPs and `stand/` folders under `examples/mensa-retter/referenz/`, and the SKILL.md files of `setup-model`, `show-canvas`, `grill-problem`, `to-interview-guide` and `log-evidence` (read as "what the tool will do"). `transcript.md` was read only to check what the pages quote. Planning files were read only to build the knowledge states and the scope. Scratch: `/tmp/claude-0/-home-user/e7968edf-8442-5ce4-910f-3b54a64f6b1c/scratchpad/walk/`.

## Knowledge states

**Lena, unit 0 start.** Block 6 filtered to Lena:
- She has a laptop with install rights, internet, chapter 1 of the handbook, an idea and notes in Notion.
- She has an agent account. How she gets it is an open question.
- She does not know what a terminal, a path, Git, Markdown or a skill is.

**Lena, after unit 0.** She can open a terminal, use `mkdir`/`cd`, paste commands, install and start Claude Code and log in, add the plugin, type `/setup-model` and `/show-canvas`, and read the canvas colours. She has the folder `mensa-retter-uebung`.

**Lena, after unit 1.** She can also download and unzip a ZIP (by command or by mouse), use `cd` with drag and drop, and work in rounds (❓/➡️). She knows to use her own words, to say "Weiß ich nicht", and what a register ID is.

**Jonas, unit 0 start.**
- Claude Code runs on a paid plan, he has used skills, and he knows Git, BMC and Lean Startup.
- He does not know the impact perspective or why interviews come before the solution.
- He skips units.
- Assumed, not in his persona: Node.js and Python are installed.

**Jonas, later units.** Same as Lena's additions.

---

## Unit 0 · Einrichten und das Canvas lesen

### Lena

| # | Step (where) | Finding | Severity | Missing knowledge or info | Suggested fix |
|---|---|---|---|---|---|
| 1 | §6 marketplace add (0-einrichten.md:78) | The GitHub repo is still private: `github.com/opencampus-sh/agentic-business-model-canvas` returns 404 (curl), so `claude plugin marketplace add opencampus-sh/...` cannot work for learners. The same goes for the canvas guide link (line 122). | blocker (release condition) | Access to the repo | Release the repo publicly before the course, or tell learners the access route |
| 2 | §3 account warning (31–32) and OpenCode box (145–147) | Without a paid plan or a course account, the only route is OpenCode, which needs Node.js ≥ 22.20 for `npx skills`. Node is only linked, with no install steps. Block 6 leaves the account question open. | blocker (if no course account) | Paid account, or how to install Node.js | Settle the open question in block 6. If OpenCode is the free route, add Node install steps or a skills install without Node. |
| 3 | §8 `/show-canvas` (107–111) | The skill runs `python3 …/render_canvas.py` (show-canvas SKILL.md:16). Python is not in block 6 and not mentioned on any course page. On Windows `python3` is usually missing (Store stub). On a fresh Mac it triggers the Xcode command-line tools install. The same applies to `check_project.py`, which grill-problem and log-evidence run (units 1–2). | blocker on Windows, friction on macOS (not executed) | Python 3 installed | Add a Python step to §3 with a check command (`python3 --version`), or add it to block 6 |
| 4 | §5 first start (67–71) | The page only says "öffnet sich der Browser zur Anmeldung". Claude Code first asks for a theme and a login method, then a folder-trust question, then permission prompts for every file write or command ("Do you want to …? 1. Yes 2. Yes, and don't ask again …"). All of this is in English and not explained. It recurs in every unit. | friction | How to answer trust and permission prompts | Add a box: "Claude Code fragt vor dem Schreiben um Erlaubnis – so antwortest du", with a screenshot |
| 5 | §8 open the page (111) | „Öffne sie im Browser“: Lena does not know paths and does not know where `mensa-retter-uebung` lives (created with `mkdir` in her home folder). | friction | Opening a local file | „Sag dem Agenten: ‚Öffne die Seite im Browser‘“, or `open build/canvas.html` / `start build\canvas.html` |
| 6 | §9 colours (117) | The lila list uses „Problem, Zielgruppe“, but the blocks are called „Herausforderung & Vision“ and „Nutzer:innen & Kund:innen“ (template CANVAS.md:14,18; rendered HTML). Lena cannot match two of seven names. | friction | Block names | Use the block names as printed |
| 7 | Transfer (140) | „exportiert die Seite als Markdown und legt die Datei in den Ordner“: Notion exports a ZIP with hashed file names. How to export, unzip and find the folder in Finder or Explorer is not explained. Notion is Lena's persona situation. | friction | Notion export, finding the folder | Three steps (Notion → ••• → Export → Markdown; unzip; drag into the folder), or „schreib dem Agenten, wo die Datei liegt“. This transfer is also not in the plan's minutes (PLAN: Transfer „–“). |
| 8 | Self-check 1 (126–127) vs. §7 (101) and setup-model SKILL.md §3 | The self-check says the agent creates the files „erst nach deiner Bestätigung“. The page and the skill (and the transcript) have it write the files first and then confirm the AGENTS.md section. | note | – | Align the self-check: „legt die Dateien an und lässt dich den Abschnitt in AGENTS.md bestätigen“ |
| 9 | Self-check 4 (135–136) | „Ob du im richtigen Ordner bist“: the plugin installs with user scope by default (`claude plugin install --help`: default "user"), so the folder does not matter for the menu. This sends Lena looking in the wrong place. | note | – | Replace with „ob du Claude Code nach der Installation neu gestartet hast; `/plugin` zeigt installierte Plugins“ |
| 10 | §1 „zwölf solchen Anleitungen“ (10) vs. the `/` menu (82) | The plugin ships 14 skills (plugin.json). `assumptions` and `evidence-checks` have no `disable-model-invocation` and will also appear in the `/` list. | note | – | „zwölf, dazu zwei Nachschlage-Skills, die du nicht selbst aufrufst“ |
| 11 | Commit box (158–159) | „Die Skills fragen am Ende oft: ‚Committen?‘“: every skill says „falls Git“, and the exercise folders have no Git, so the question never comes. „Ja, bitte committen“ would also need Git, which Lena does not have. | note | Git | „In den Übungsordnern fragt der Agent nicht; für euer Projekt …“ |
| 12 | §7 question A (97) | In a folder without Git or a remote, the skill tells the agent to raise repository visibility in A („ohne Remote frag in Abschnitt A“). The agent may talk about Git or GitHub. The page's answer still works. | note | – | Optional: „Fragt er nach Git oder GitHub: ‚Kein Git, nur lokal‘“ |

### Jonas

| # | Step (where) | Finding | Severity | Missing knowledge or info | Suggested fix |
|---|---|---|---|---|---|
| 1 | §6 (78) | Repo private, 404 (as Lena 1). | blocker (release condition) | – | as above |
| 2 | Skipping unit 0, README install (README:69) | Jonas skips units and knows the README. The README's first install option is project-local `npx skills add` without `-g`. The unit-1 ZIP folders contain no skills („ohne installierte Skills“, referenz/README.md), so `/grill-problem` will be missing there. | friction | Skills must be global for the exercise folders | Unit 1 „Startzustand“: one line „Die Skills müssen global installiert sein (Plugin oder `-g`)“ |
| 3 | §9 (117) | Block names differ from the canvas (as Lena 6). | note | – | as above |
| 4 | Self-check 1 and 4, „zwölf“, commit box | As Lena 8–11. | note | – | as above |

---

## Unit 1 · Das Problem schärfen

### Lena

| # | Step (where) | Finding | Severity | Missing knowledge or info | Suggested fix |
|---|---|---|---|---|---|
| 1 | Startzustand ZIP links (1-problem.md:32,40,49) and solution link (98) | All github.com links return 404 while the repo is private. Locally, every path exists, `main` is the branch, and the ZIPs are tracked. | blocker (release condition) | – | Release, or host the ZIPs elsewhere |
| 2 | End of `/grill-problem` (grill-problem SKILL.md:47) | The skill runs `check_project.py` (python3). Same Python gap as unit 0 #3. | blocker on Windows / friction (not executed) | Python | as unit 0 #3 |
| 3 | Aufgabe 5 „Öffne `PROBLEM.md`“ (71) | Opening a .md file is never taught. Double-click opens Xcode or TextEdit, or asks for an app on Windows. Markdown is outside Lena's state. | friction | Opening and reading a Markdown file | „Öffne den Ordner im Finder/Explorer und dann PROBLEM.md mit einem Texteditor“, or „Sag dem Agenten: ‚Zeig mir PROBLEM.md‘“ |
| 4 | Recherche „Ja, schau mal“ (64) | Web search triggers permission prompts (see unit 0 #4). With OpenCode or a free model, web search may be missing. | friction | Permission prompts | Covered by the box from unit 0 #4 |
| 5 | Lesen point 1 (18) vs. grill-problem SKILL.md:25 | The page says the agent asks for own words first for „Problem, Ursachen und Zielgruppe“. The skill says „Problem, Vision, Lösung, Wertangebot“. | note | – | Align with the skill |
| 6 | Aufgabe 4 commit (70) | No Git in the ZIP folder, so the agent will not ask. | note | – | Drop the sentence, or say „falls er fragt“ |
| 7 | Checklist „jede Aussage … eine ID“ (103) | The *Noch offen* items in the solution have no IDs. That is correct (open questions are not statements), but a learner may count them as missing. | note | – | „jede Aussage (nicht die Punkte unter *Noch offen*)“ |

### Jonas

| # | Step (where) | Finding | Severity | Missing knowledge or info | Suggested fix |
|---|---|---|---|---|---|
| 1 | ZIP and solution links | 404 while private (as Lena 1). | blocker (release condition) | – | as above |
| 2 | Startzustand (34–42) | Skills missing in the new folder if installed project-local (unit 0 Jonas 2). | friction | – | as above |
| 3 | Lesen / Aufgabe (8–24) | Persona gap: the impact perspective. The page frames the problem „aus Sicht der Betroffenen“ but does not say why this matters for an impact startup, compared with a classic BMC customer problem. The handbook link covers it, but Jonas skips it. | note | Impact perspective | One sentence in Lesen: why the problem belongs to the affected people, not to the customer |
| 4 | Lesen point 1 (18) | As Lena 5. | note | – | – |

---

## Unit 2 · Interviews vorbereiten und auswerten

### Lena

| # | Step (where) | Finding | Severity | Missing knowledge or info | Suggested fix |
|---|---|---|---|---|---|
| 1 | ZIP and solution links (2-interviews.md:26–27, 69–70) | 404 while private. | blocker (release condition) | – | – |
| 2 | Teil B steps 3–5 (44–46) | The order does not work. In the reference run the *belegt* sections are 1–3, and the snacks row sits in section 3. After step 4 no *belegt* section is left, so step 5 („Schreib bei einem *belegt*-Abschnitt nur ‚passt‘“) cannot be done. log-evidence SKILL.md:38 shows *belegt* rows first. | friction | – | Move „Probier es aus: ‚passt‘“ before step 3 (first section), then the ID answers |
| 3 | Teil A step 2 (36) | The scripted answer „Frage 7 mit der Skala find ich gut“ refers to the reference draft (A-7). Lena's draft will be numbered differently, possibly without a scale question. Unit 1 warns about this; unit 2 Teil A does not. | friction | – | Repeat „Bei dir können Fragen anders nummeriert sein“, or „die Frage mit der Skala von 1 bis 10 (falls es eine gibt)“ |
| 4 | Teil B step 1 „Öffne `INTERVIEWS.md`“ (42) | As unit 1 #3. The file is 992 words with wide Markdown tables. | friction | Reading Markdown | as unit 1 #3, or read it in the GitHub `stand/04b-…` folder (rendered) |
| 5 | `/log-evidence` end (log-evidence SKILL.md:50) | Runs `check_project.py`, so Python again. | blocker on Windows / friction (not executed) | Python | – |
| 6 | Self-check 2 (86) | „mit dem Hinweis ‚gepitcht‘“: the solution says „nur nach Vorstellung der Idee“ / „nur nach Pitch“. „Pitch“ is never explained on the pages. | note | The word „Pitch“ | „mit dem Hinweis ‚nur nach Vorstellung der Idee‘“ |
| 7 | Startzustand (29) „öffne dort das Terminal“ | Unit 1 taught `cd` with drag and drop into an already open terminal, not opening a terminal in a folder. Following the unit-1 recipe works. | note | – | „wechsle mit `cd` hinein (wie in Einheit 1)“ |

### Jonas

| # | Step (where) | Finding | Severity | Missing knowledge or info | Suggested fix |
|---|---|---|---|---|---|
| 1 | Links | 404 while private. | blocker (release condition) | – | – |
| 2 | Teil B steps 3–5 | Order problem (as Lena 2). | friction | – | as above |
| 3 | Lesen (8–18) | Persona gap: why interviews come before the solution. The page explains why „Würdet ihr …?“ proves nothing, but not why interviews come before any solution work. Jonas tends to jump to the solution. | note | Problem before solution | One sentence: „Erst wenn ihr wisst, wie das Problem erlebt wird, lohnt sich eine Lösung – sonst testet ihr eure Idee statt das Problem“ |
| 4 | Teil A step 2 | The scripted „Frage 7“ answer (as Lena 3). | note (Jonas adapts) | – | – |

---

## Across personas (fix first)

| Finding | Units | Highest severity |
|---|---|---|
| The GitHub repo is private: marketplace add, all ZIP downloads, solution and canvas-guide links return 404 | 0, 1, 2 | blocker (release condition) |
| `/show-canvas`, `grill-problem` and `log-evidence` need `python3`, which is not on the boundary and not mentioned on any page (Lena surely; Jonas only by assumption) | 0, 1, 2 | blocker (Windows) |
| Unit 2 Teil B: step 5 („passt“) comes after the last *belegt* section | 2 | friction |
| Scripted answer „Frage 7 mit der Skala“ assumes the reference numbering | 2 | friction |
| Skills must be installed globally for the ZIP folders (README default is project-local) | 1, 2 | friction |
| Block names in unit 0 §9 („Problem, Zielgruppe“) do not match the canvas | 0 | friction |
| Commit prompts promised (unit 0 box, unit 1 step 4) but the exercise folders have no Git | 0, 1 | note |
| Unit 0 self-checks 1 and 4 and the count „zwölf“ vs. 14 menu entries | 0 | note |
| Where learners read the course: README links `course/docs/` on GitHub, where `=== tabs`, `!!!` and `??? question` (MkDocs Material) show as raw text or code blocks and the self-check solutions are not folded. The Pages site is not linked yet (`pages.yml` runs only once the repo is public). | all | friction |

## Walked without finding

- **ZIPs vs. pages.** Contents are identical to the `stand/` folders (`diff -r`: identical for 01, 03, 04, 04b, 05).
  - 01 contains `notion-export.md` and A1–A5, all *Annahme*, matching the page.
  - 04b contains the guide and four notes I1–I4 with „Ausgewertet: nein“. The pitch in I2 is in the notes, as Teil B step 1 asks.
  - The snacks row (I4), the cold chain (I1) and question A-3 (missing from the notes) are all present.
  - ZIPs unpack flat, so `unzip start.zip` in the new folder gives the project files directly.
- **Unit 1 bash block, executed.** Run with a `file://` stand-in URL: `mkdir`/`cd`/`curl -L -o`/`unzip && rm` works and yields 13 files.
- **Solution claims, checked in the files.**
  - Unit 1: every statement in PROBLEM.md has an ID; „Weiß ich nicht“ appears under *Noch offen*; 12 *Annahme* and 3 *recherchiert* with links; the agent-wording entry is in DECISIONS.md.
  - Unit 2: A16–A30 present; A4 stays *Annahme* with I2 marked as pitched; *belegt* rows are narrow and have an `I…` source; the rejected snacks row is in DECISIONS.md; INTERVIEWS.md has an *Auswertung* section.
- **`check_project.py`, executed on copies of 01, 03, 04b and 05.** No FEHLER. The outputs match the transcript.
- **`render_canvas.py`, executed on a fresh template and on the snapshots.** It writes `build/canvas.html` with 11 blocks: 7 „Team entscheidet“ (purple #534AB7), 4 „Agent entwirft“ (green #0F6E56), and the empty markers „Noch nicht entschieden/entworfen“. With no previous results all blocks are empty, as unit 0 §8 says.
- **What the pages say the agent will ask, compared with SKILL.md.**
  - setup-model asks the three questions in order A → B → C, then shows the AGENTS.md section.
  - grill-problem works in rounds with ❓/➡️, runs the 5 Whys one at a time, sends „Weiß ich nicht“ to *Noch offen*, and pushes back on „keine App“.
  - to-interview-guide asks about experienced situations, adds no pitch, maps each question to an assumption, and lets the team decide whom to ask.
  - log-evidence uses sections of at most 5 rows, never applies „passt“ to *belegt*, and accepts ID lists.
  - All quotes on pages 1 and 2 match `transcript.md` word for word.
- **Commands.**
  - `claude --version` gives 2.1.330.
  - `claude plugin marketplace add <source>` and `claude plugin install <plugin>` (with `plugin@marketplace`) exist, as does `claude doctor`.
  - The plugin and marketplace names in `.claude-plugin/` match the commands.
  - The commands are identical to README:73–74.
  - The `npx skills@latest add -g …` form matches README:70.
- **External links (curl, 200).**
  - Handbook root, „Problemanalyse“, „Zielgruppe“ and „Problem-Interviews“ (real page titles, which differ from the GitBook fallback).
  - claude.com/pricing ($20 found).
  - claude.ai/install.sh and .ps1 (redirect to downloads.claude.ai).
  - code.claude.com/docs/en/setup.
  - opencode.ai/v2/install, /docs and /docs/skills; /docs/zen redirects to /docs/console/models/ (check the wording).
  - nodejs.org.
  - The Codex pages and installers (redirect to learn.chatgpt.com and releases.openai.com).
- **Local link targets exist:** `canvas/README.md`, all 3 ZIPs, the 3 `stand/` folders, and `3-annahme-oder-beleg.md`.

## Executed vs. read

- **Executed:** unzip and diff of 5 ZIPs; the unit-1 download block (local URL stand-in); `check_project.py` and `render_canvas.py` on the snapshots and the template; `claude --version` and the plugin/marketplace/install/doctor `--help` output; curl on all external links and on the github.com links (404).
- **Read only, not executed:**
  - Installing Claude Code, OpenCode, Codex and Node.
  - Logging in, paid plans.
  - `claude plugin marketplace add`/`install` (would add a marketplace; the repo is private).
  - Running the five skills with an agent (the drafts and dialogues were compared against SKILL.md and the transcript).
  - Windows PowerShell commands (`Invoke-WebRequest`, `Expand-Archive`, `irm | iex`).
  - Whether `marketplace add` needs Git on the learner's machine (the docs do not say).
  - Python availability on Windows and macOS.
  - Notion export.
  - Opening HTML or .md files on a learner OS.

## Workload (200 words/min; exercise steps estimated)

| Unit | Page reading | Extra reading the unit asks for | Exercise (steps) | Self-check + transfer | Estimate | Plan |
|---|---|---|---|---|---|---|
| 0 | 1151 words ≈ 6 min (+ index 297 ≈ 1.5) | canvas guide 1108 words ≈ 5.5 (optional link) | ~10 steps (install, check, folder, login, 2 plugin commands, restart, `/setup-model` with 3 questions, `/show-canvas`, open, read): Lena 35–50, Jonas ~10 | 5 + transfer 10–15 (not in plan) | Lena 60–80 min (more if Python or an account is needed) | 55 |
| 1 | 1133 ≈ 6 | handbook Problemanalyse („Vorher“, not budgeted); PROBLEM.md 466 + ASSUMPTIONS/DECISIONS ≈ 1000 words for comparing ≈ 7 | folder setup 5; ~11 answer turns + app test + confirm ≈ 25; compare with 5-point checklist ≈ 10 → ~40 | 5 + 30 | ≈ 80 min | 75 |
| 2 | 1040 ≈ 5 | handbook Zielgruppe + Problem-Interviews (not budgeted); 04b INTERVIEWS 992 ≈ 5; comparing 05 ASSUMPTIONS 1144 + INTERVIEWS 1380 ≈ 12 | two folders ≈ 6; Teil A 4 steps ≈ 12; Teil B 6 steps over 6 agent sections ≈ 20; reading and comparing ≈ 17 → ~55 | 5 + 30 | ≈ 95–100 min | 75 (exercise 30) |

Unit 2's exercise is about twice the planned 30 minutes: two parts, two start states and two comparisons. Unit 0 holds only if Python and the account are already settled. The handbook chapters required as „Vorher“ (2 and 3) are counted nowhere.

## Knowledge assumed outside the boundary (instructor decides: gap in the material, or entry in block 6)

1. Python 3 is installed and callable as `python3` (needed by `/show-canvas`, `grill-problem` and `log-evidence`).
2. A paid Claude plan or course access. Otherwise: installing Node.js for the OpenCode route (block 6 open question).
3. Handling Claude Code's first-run, trust and permission prompts (English UI).
4. Opening local files: an HTML page in the browser, a .md file in an editor; finding a folder made with `mkdir` in Finder or Explorer.
5. Exporting a Notion page as Markdown and placing it in the project folder (unit 0 transfer).
6. Handbook chapters 2 and 3 read before units 1 and 2. Block 6 has only chapter 1; the pages link the chapters but the time is not budgeted.
7. Skills installed globally, not per project (for the ZIP exercise folders).
8. Git, only for the optional commit box.
9. The word „Pitch“ (unit 2 self-check).
10. Where the course pages are read: the Pages site, or GitHub with raw MkDocs syntax.

## Counts (for SIGNALS.md; not appended: the instruction was not to edit course files)

- Lena: unit 0: 2 blockers (+1 Windows-only), 4 friction, 5 notes; unit 1: 1 (+1) / 2 / 3; unit 2: 1 (+1) / 3 / 2.
- Jonas: unit 0: 1 / 1 / 2; unit 1: 1 / 1 / 2; unit 2: 1 / 1 / 2.
- Proposed entry: „2026-11-23 · walkthrough · Lena, Jonas · Einheiten 0–2 · see report“.
- Next: `/review-unit` for fixes; `/course-retro` for a check that catches „Python/tool prerequisites of invoked skills“ and „links into a private repo“.
