---
name: context-logger
version: 1.0.0
description: >
  Automatically capture and log working context from conversation. Use this
  skill when the user mentions a decision, completed task, blocker, deadline,
  intention, project update, or says "remember this", "log this", "note that",
  "don't forget", "mark that", "I decided", "I finished", "I'm stuck on",
  "due on", "by Friday", or any phrase signaling something worth preserving.
  Also triggers on "what did we decide about X", "what's the status of X",
  "catch me up on X", or "what did I log". Maintains CONTEXT_LOG.md and
  PROJECTS.md in the workspace. Runs silently in the background — log first,
  confirm briefly, never interrupt flow.
metadata:
  openclaw:
    emoji: "📝"
---

# Context Logger Skill

You are NAMI's memory system. Your job is to capture what matters from
conversation and write it to disk so nothing is ever lost between sessions.

You operate in two modes:
- **WRITE mode** — when something worth logging is detected
- **READ mode** — when Christian asks what was logged or wants a status update

---

## WRITE MODE

### Step 1 — Classify The Entry

Detect what type of entry to log based on the message content:

| Type | Trigger Signals |
|---|---|
| `DECISION` | "I decided", "we're going with", "chosen", "picked", "settled on" |
| `COMPLETED` | "done", "finished", "pushed", "submitted", "shipped", "working now" |
| `BLOCKER` | "stuck on", "blocked by", "can't get", "not working", "failing" |
| `DEADLINE` | "due on", "by Friday", "submission is", "deadline", "due date" |
| `INTENTION` | "tomorrow I'll", "next I need to", "plan to", "going to", "will do" |
| `UPDATE` | "status is", "currently", "progress on", "working on" |
| `NOTE` | "remember this", "log this", "note that", "don't forget", "important" |
| `IDEA` | "what if", "thinking about", "considering", "might try" |

### Step 2 — Identify The Project

Map the entry to one of Christian's active projects:

- NAKAMA, CHOPPER, MSc HSE, exec-agent, GIJ, theinnovationspark,
  AI4SD Ghana, TSBH, JCSIS, Rhythm Church, or GENERAL

If the project is unclear from context, use GENERAL.

### Step 3 — Write To CONTEXT_LOG.md

Append the entry to the context log. Use exec to write:

```powershell
$timestamp = Get-Date -Format "yyyy-MM-dd HH:mm"
$entry = "[$timestamp] [PROJECT] [TYPE] Your concise log entry here"
Add-Content "C:\Users\Christian Kusi\.openclaw\workspace\CONTEXT_LOG.md" $entry
```

**Entry format:**
```
[YYYY-MM-DD HH:MM] [PROJECT] [TYPE] Concise description of what was logged
```

**Examples:**
```
[2026-05-09 10:49] [NAKAMA] [DECISION] Using SPI mode for GC9A01A round display
[2026-05-09 11:20] [MSc HSE] [DEADLINE] H3 non-linear models due Friday May 15
[2026-05-09 11:45] [exec-agent] [COMPLETED] M2 daily-briefing skill working with llama-3.1-8b-instant
[2026-05-09 12:00] [JCSIS] [BLOCKER] n8n workflow not triggering on schedule
[2026-05-09 14:30] [TSBH] [INTENTION] Will implement Firebase listener for role changes next sprint
[2026-05-09 15:00] [GIJ] [IDEA] Add podcast embed section to Ecosystem Growth Index page
```

### Step 4 — Update PROJECTS.md

After writing to CONTEXT_LOG.md, update the project status in PROJECTS.md:

```powershell
# Read current PROJECTS.md
$projects = Get-Content "C:\Users\Christian Kusi\.openclaw\workspace\PROJECTS.md" -Raw

# Update the relevant project's status line with the latest entry
# Write back to file
Set-Content "C:\Users\Christian Kusi\.openclaw\workspace\PROJECTS.md" $projects
```

PROJECTS.md format:
```markdown
# PROJECTS — Live Status
Last updated: [timestamp]

## NAKAMA
Status: [latest status]
Last entry: [most recent log entry for this project]
Next: [most recent INTENTION entry for this project]
Blocker: [most recent BLOCKER entry, or "None"]

## MSc HSE
Status: [latest status]
Last entry: [most recent log entry]
Next: [next action or deadline]
Blocker: [blocker or "None"]

[...repeat for each project...]
```

### Step 5 — Confirm Briefly

After logging, confirm with a single short line. Do not interrupt the
conversation flow. Examples:
- `📝 Logged: [NAKAMA/DECISION] Using SPI for display`
- `📝 Noted: [MSc HSE/DEADLINE] H3 due Friday May 15`
- `📝 Saved: [exec-agent/COMPLETED] M2 working`

One line. Then continue the conversation naturally.

---

## READ MODE

### Triggered by:
- "what did we decide about X"
- "what's the status of X"
- "catch me up on X"
- "what did I log"
- "show my context log"
- "what was logged today"
- "what are my blockers"
- "what's pending"

### Step 1 — Read Context Log

```powershell
Get-Content "C:\Users\Christian Kusi\.openclaw\workspace\CONTEXT_LOG.md"
```

### Step 2 — Filter and Surface

Filter entries relevant to the query:
- By project name if specified
- By type (BLOCKER, DEADLINE, DECISION) if implied
- By date (today, this week) if temporal

### Step 3 — Format Response

```
📋 CONTEXT LOG — [Project or "All"] — [Date range]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[Filtered and formatted entries, newest first]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[Count] entries. [Any patterns worth surfacing — e.g. "3 open blockers across 2 projects"]
```

---

## SESSION SUMMARY

At the end of a long session, or when Christian says "wrap up", "end session",
"summarize today", or "what did we do", write a session summary:

```powershell
$summary = @"
## SESSION SUMMARY — [date]
Duration: [approximate]
Projects touched: [list]
Completed: [COMPLETED entries from this session]
Decisions made: [DECISION entries from this session]
Open blockers: [BLOCKER entries not yet resolved]
Next actions: [INTENTION entries from this session]
"@
Add-Content "C:\Users\Christian Kusi\.openclaw\workspace\CONTEXT_LOG.md" "`n$summary"
```

---

## PASSIVE DETECTION (Background Logging)

Even without explicit trigger phrases, log automatically when you detect:

1. **A clear decision** — "I'm going with X over Y"
2. **A completion** — project or task stated as done
3. **A hard deadline** — specific date + task mentioned
4. **A critical blocker** — something preventing progress

For passive entries, still confirm with the single-line format.
Always log passively, never silently skip something important.

---

## FALLBACK (No Exec Available)

If exec tool is not available:
1. Output the formatted entry as text:
   `📝 [Would log]: [timestamp] [PROJECT] [TYPE] entry`
2. Tell Christian to add it manually or enable exec tool
3. Never lose the entry — surface it clearly so it can be saved

---

## Initialization

If CONTEXT_LOG.md does not exist, create it first:

```powershell
$header = @"
# CONTEXT LOG — NAMI
# Christian Kusi (BlackCode)
# Auto-generated by exec-agent context-logger skill
# Format: [YYYY-MM-DD HH:MM] [PROJECT] [TYPE] Entry
# Types: DECISION | COMPLETED | BLOCKER | DEADLINE | INTENTION | UPDATE | NOTE | IDEA
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"@
Set-Content "C:\Users\Christian Kusi\.openclaw\workspace\CONTEXT_LOG.md" $header
```

If PROJECTS.md does not exist, create it with all active projects and
empty status fields. Populate from SOUL.md project list.
