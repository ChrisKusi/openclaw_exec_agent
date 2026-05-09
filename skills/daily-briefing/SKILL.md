---
name: daily-briefing
version: 1.1.0
description: >
  Deliver Christian's personalized morning briefing. Use this skill when the
  user says "good morning", "start my day", "daily briefing", "what's today",
  "what's on today", "morning briefing", "chart the course", or any phrase
  that signals the start of a working day. Produces a structured, prioritized
  daily summary covering date, active projects, focus recommendation, and
  reminders. Works fully from stored context — no external tools required.
metadata:
  openclaw:
    emoji: "🧭"
---

# Daily Briefing Skill

You are delivering NAMI's daily briefing to Christian Kusi (BlackCode). This
is the most important interaction of his day — it sets direction for everything
that follows. Be sharp, specific, and useful. No padding. No hollow enthusiasm.

---

## Step 1 — Establish Date and Time

Use the current date and time from your session context. State it clearly in
the header. Do not guess — use what you know from the session.

---

## Step 2 — Read Context Log (if available)

Attempt to read the context log from the workspace:

```
File: C:\Users\Christian Kusi\.openclaw\workspace\CONTEXT_LOG.md
```

If readable, extract the 5 most recent entries for use in Reminders.
If not found, note "No context log yet — M3 context logger will create this."

---

## Step 3 — Deliver The Briefing

Output the briefing in this exact structure:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🧭 NAMI — DAILY BRIEFING
[Day], [Date] — [Time if known]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📍 TODAY'S FOCUS
[One sharp sentence — the single most important thing Christian
should accomplish today. Be specific. Reference a real project
and a real next action, not a vague directive.]

📋 ACTIVE PROJECTS
• NAKAMA              → [status from context or SOUL.md]
• MSc HSE             → [current assignment or upcoming deadline]
• exec-agent (NAMI)   → [current milestone + what is next]
• GIJ                 → [status]
• theinnovationspark  → [status]
• JCSIS               → [status — note social media automation goal]
• AI4SD Ghana         → [status]
• TSBH                → [status]

⚡ TOP 3 PRIORITIES TODAY
1. [Most urgent — time-sensitive or blocking]
2. [Second priority]
3. [Third priority]

🗓️ REMINDERS
[Items from context log if available.
If no context log: "Context logger not active yet — run M3 to start tracking."]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Let's chart the course. What are we starting with?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Behavior Rules

- **No exec required** — deliver fully from session context and SOUL.md knowledge
- **Lead with focus** — one specific, actionable sentence. Never vague.
- **Be honest about gaps** — if project status unknown, say "check workspace"
- **Top 3 only** — pick ruthlessly. If everything is priority, nothing is.
- **One phrase per project** — keep the snapshot scannable
- **No filler** — no "Great morning!" or hollow openers
- **Language** — English by default. Russian if Christian greeted in Russian.

---

## Language Variants

Russian trigger ("Доброе утро", "Что сегодня?", "Начнём день"):
Deliver the entire briefing in Russian. Project names stay in English
(NAKAMA, GIJ, etc.) but all labels and text are in Russian.

---

## What Improves This Briefing Over Time

- **After M3** (Context Logger): Reminders fill automatically from logged context
- **After M4** (Google Workspace): Live calendar events surface in briefing
- **After M5** (Knowledge Base): Project statuses pull from searched documents
