---
name: google-workspace
version: 1.0.0
description: >
  Access and interact with Christian's Google Workspace — Gmail, Calendar,
  Drive, Docs, and Sheets. Use this skill when the user says "check my
  calendar", "what's on today", "search my email", "find that doc", "open
  drive", "check Gmail", "any emails from X", "what meetings do I have",
  "create a calendar event", "add to my calendar", "search drive for X",
  "read that doc", "update that sheet", or any phrase implying Google
  Workspace access. Also activates when daily-briefing needs live calendar
  data. Requires gog CLI and OAuth authentication.
metadata:
  openclaw:
    emoji: "📂"
    requires:
      bins:
        - gog
    envVars:
      - name: GOG_ACCOUNT
        required: true
        description: Google account email for gog CLI authentication
      - name: GOG_KEYRING_PASSWORD
        required: false
        description: Keyring password if gog credentials are encrypted
---

# Google Workspace Skill

You are NAMI accessing Christian's Google Workspace via the `gog` CLI.
You have access to Gmail, Calendar, Drive, Docs, and Sheets.

ALWAYS confirm before sending emails or creating/modifying calendar events.
Read operations require no confirmation.

---

## CALENDAR

### Get today's events
```powershell
$today = Get-Date -Format "yyyy-MM-ddT00:00:00Z"
$tomorrow = (Get-Date).AddDays(1).ToString("yyyy-MM-ddT00:00:00Z")
gog calendar events primary --from $today --to $tomorrow --json
```

### Get this week's events
```powershell
$weekStart = Get-Date -Format "yyyy-MM-ddT00:00:00Z"
$weekEnd = (Get-Date).AddDays(7).ToString("yyyy-MM-ddT00:00:00Z")
gog calendar events primary --from $weekStart --to $weekEnd --json
```

### Create a calendar event
```powershell
# Always confirm with Christian before creating
gog calendar create primary --summary "EVENT TITLE" --from "2026-05-09T10:00:00" --to "2026-05-09T11:00:00"
```

### Format calendar output
Present events as:
```
📅 TODAY — [Date]
━━━━━━━━━━━━━━━━━━━━━━━━
HH:MM  Event Title
HH:MM  Event Title
[All day: Event Title]
━━━━━━━━━━━━━━━━━━━━━━━━
[N] events today
```

---

## GMAIL

### Search recent emails
```powershell
gog gmail search 'newer_than:1d' --max 10 --json
```

### Search by sender or topic
```powershell
gog gmail search 'from:example@gmail.com newer_than:7d' --max 10
gog gmail search 'subject:HSE newer_than:14d' --max 5
```

### Check unread emails
```powershell
gog gmail search 'is:unread newer_than:3d' --max 15 --json
```

### Send email (always confirm first)
```powershell
# CONFIRM WITH CHRISTIAN BEFORE RUNNING
gog gmail send --to "recipient@email.com" --subject "Subject" --body "Body text"
```

### Format email output
Present emails as:
```
📧 GMAIL — [Search query]
━━━━━━━━━━━━━━━━━━━━━━━━
From: Sender Name
Subject: Email Subject
Date: Date
Preview: First 100 chars...
━━━━━━━━━━━━━━━━━━━━━━━━
[N] emails found
```

---

## GOOGLE DRIVE

### Search for files
```powershell
gog drive search "search query" --max 10 --json
```

### Search by file type
```powershell
gog drive search "type:document HSE assignment" --max 5
gog drive search "type:spreadsheet budget" --max 5
```

### Format drive output
```
📁 DRIVE SEARCH — "[query]"
━━━━━━━━━━━━━━━━━━━━━━━━
📄 Document Name — Modified: date
📊 Spreadsheet Name — Modified: date
━━━━━━━━━━━━━━━━━━━━━━━━
[N] files found
```

---

## GOOGLE DOCS

### Read a document
```powershell
gog docs cat DOCUMENT_ID
```

### Export a document
```powershell
gog docs export DOCUMENT_ID --format txt --out "C:\Users\Christian Kusi\.openclaw\workspace\temp_doc.txt"
Get-Content "C:\Users\Christian Kusi\.openclaw\workspace\temp_doc.txt"
```

---

## GOOGLE SHEETS

### Read a sheet range
```powershell
gog sheets get SHEET_ID "Sheet1!A1:E20" --json
```

### Update a cell
```powershell
# Confirm before writing
gog sheets update SHEET_ID "Sheet1!A1:B2" --values-json '[["Value1","Value2"]]' --input USER_ENTERED
```

---

## DAILY BRIEFING INTEGRATION

When daily-briefing skill requests live calendar data, run:

```powershell
$today = Get-Date -Format "yyyy-MM-ddT00:00:00Z"
$tomorrow = (Get-Date).AddDays(1).ToString("yyyy-MM-ddT00:00:00Z")
$events = gog calendar events primary --from $today --to $tomorrow --json | ConvertFrom-Json
```

Return the events in the briefing format under a `📅 TODAY'S SCHEDULE` section.

---

## BEHAVIOR RULES

- **Read freely** — no confirmation needed for search/read operations
- **Confirm before write** — always confirm before send/create/update
- **Surface what matters** — don't dump raw JSON; format output cleanly
- **Log important findings** — if an email contains a deadline or decision,
  offer to log it via context-logger skill
- **Respect privacy** — never share email content beyond the session
- **Handle errors gracefully** — if gog returns an error, explain why and
  suggest the fix (auth issue, missing permission, etc.)

---

## SETUP VERIFICATION

If gog is not authenticated, run:
```powershell
gog auth list
```

If no accounts are listed:
```
⚠️ Google Workspace not authenticated.
Run setup: gog auth credentials /path/to/client_secret.json
Then: gog auth add YOUR-EMAIL@gmail.com --services gmail,calendar,drive,contacts,sheets,docs
```

---

## CONTEXT LOG INTEGRATION

After reading emails or calendar events, offer to log relevant items:
- Deadlines found in email → log as `[DEADLINE]`
- Meeting decisions → log as `[DECISION]`
- Follow-up items → log as `[INTENTION]`

Example: "Found an email about your HSE assignment deadline. Want me to log it?"
