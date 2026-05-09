---
name: knowledge-base
version: 1.0.0
description: >
  Search Christian's personal knowledge base using semantic RAG retrieval.
  Use this skill when the user says "what do I know about X", "find in my
  notes", "search knowledge base", "what did I write about X", "look up X",
  "do I have anything on X", "find that document about X", "search my docs",
  "what's in my context log about X", or any phrase implying search across
  stored documents and notes. Uses ChromaDB local vector store — no API key
  required. Falls back to keyword search if vector store unavailable.
metadata:
  openclaw:
    emoji: "🔍"
    requires:
      bins:
        - python
---

# Knowledge Base Skill

You are NAMI searching Christian's personal knowledge base — a local ChromaDB
vector store indexed from workspace documents including SOUL.md, CONTEXT_LOG.md,
PROJECTS.md, and all skill files.

---

## SEARCH

### Run semantic search
```powershell
cd "C:\Users\Christian Kusi\.openclaw\workspace\rag"
python search.py "USER QUERY HERE" --results 5
```

### Search with type filter
```powershell
# Search only context log entries
python search.py "USER QUERY" --type context_log

# Search only project information
python search.py "USER QUERY" --type projects

# Search only skills
python search.py "USER QUERY" --type skill
```

### Format the results for Christian
Present results as:

```
🔍 KNOWLEDGE BASE — "[query]"
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[1] filename.md — 94% match
    Relevant excerpt from the document...

[2] CONTEXT_LOG.md — 87% match
    Relevant logged entry...
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[N] results from [X] total chunks
```

---

## INDEX MANAGEMENT

### Initialize or reindex everything
```powershell
cd "C:\Users\Christian Kusi\.openclaw\workspace\rag"
python indexer.py
```

### Reindex after changes
```powershell
python indexer.py --file "C:\Users\Christian Kusi\.openclaw\workspace\CONTEXT_LOG.md"
```

### Full reset and reindex
```powershell
python indexer.py --reset
```

### Check index status
```powershell
python search.py "test" --results 1
```

---

## BEHAVIOR RULES

- **Search before answering** — always run the search script, don't rely on
  session memory alone for knowledge base queries
- **Show relevance scores** — always show the percentage match so Christian
  knows how confident the result is
- **Surface the source** — always show which file the result came from
- **Offer to log** — if search finds nothing, offer to create a note via
  context-logger skill
- **Suggest reindex** — if results seem stale or incomplete, suggest running
  `python indexer.py` to update the index

---

## INTEGRATION WITH OTHER SKILLS

### Daily Briefing
When daily-briefing runs, optionally search for:
```powershell
python search.py "today priorities" --type context_log --results 3
python search.py "blockers" --type context_log --results 3
```

### Context Logger
After context-logger writes a new entry, trigger reindex:
```powershell
python indexer.py --file "C:\Users\Christian Kusi\.openclaw\workspace\CONTEXT_LOG.md"
```

### Catch-up Skill (M6)
Catch-up uses knowledge base as its primary data source — search for recent
context log entries and project updates to build the session summary.

---

## FALLBACK (No ChromaDB)

If ChromaDB is not installed or the index doesn't exist:

1. Tell Christian: "Knowledge base not initialized yet."
2. Offer to set it up: "Run `pip install chromadb` then `python indexer.py`"
3. Fall back to reading files directly:
```powershell
Get-Content "C:\Users\Christian Kusi\.openclaw\workspace\CONTEXT_LOG.md"
Get-Content "C:\Users\Christian Kusi\.openclaw\workspace\PROJECTS.md"
```

---

## FIRST TIME SETUP

If this is the first run, guide Christian through setup:

```powershell
# Step 1 - Install ChromaDB
pip install chromadb

# Step 2 - Create rag directory
mkdir "C:\Users\Christian Kusi\.openclaw\workspace\rag"

# Step 3 - Copy scripts
copy indexer.py "C:\Users\Christian Kusi\.openclaw\workspace\rag\"
copy search.py "C:\Users\Christian Kusi\.openclaw\workspace\rag\"

# Step 4 - Build the index
cd "C:\Users\Christian Kusi\.openclaw\workspace\rag"
python indexer.py

# Step 5 - Test
python search.py "NAKAMA robot"
```
