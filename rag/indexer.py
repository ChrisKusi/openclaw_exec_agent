"""
NAMI Knowledge Base Indexer
Indexes workspace documents into ChromaDB for semantic search.

Usage:
    python indexer.py              # index all documents
    python indexer.py --file X.md  # index a single file
    python indexer.py --reset      # wipe and reindex everything
"""

import os
import sys
import argparse
import hashlib
from pathlib import Path
from datetime import datetime

try:
    import chromadb
    from chromadb.utils import embedding_functions
except ImportError:
    print("ERROR: chromadb not installed. Run: pip install chromadb")
    sys.exit(1)

# ── Config ────────────────────────────────────────────────────────────────────
WORKSPACE = Path(os.environ.get(
    "OPENCLAW_WORKSPACE",
    Path.home() / ".openclaw" / "workspace"
))
RAG_DIR     = WORKSPACE / "rag"
CHROMA_DIR  = RAG_DIR / "chroma_db"
COLLECTION  = "nami_knowledge"

SOURCES = [
    WORKSPACE / "SOUL.md",
    WORKSPACE / "AGENTS.md",
    WORKSPACE / "CONTEXT_LOG.md",
    WORKSPACE / "PROJECTS.md",
    WORKSPACE / "skills",
]

# ── Helpers ───────────────────────────────────────────────────────────────────
def chunk_text(text: str, size: int = 500, overlap: int = 50) -> list:
    words = text.split()
    chunks, i = [], 0
    while i < len(words):
        chunks.append(" ".join(words[i:i + size]))
        i += size - overlap
    return [c for c in chunks if len(c.strip()) > 50]

def file_hash(path: Path) -> str:
    return hashlib.md5(path.read_bytes()).hexdigest()

def doc_type(path: Path) -> str:
    n = path.stem.lower()
    if "soul" in n or "agent" in n: return "identity"
    if "context" in n:              return "context_log"
    if "project" in n:              return "projects"
    if "skill" in n:                return "skill"
    return "document"

def collect_docs(single_file=None) -> list:
    if single_file:
        return [Path(single_file)]
    docs = []
    for src in SOURCES:
        src = Path(src)
        if src.is_file() and src.suffix == ".md":
            docs.append(src)
        elif src.is_dir():
            docs.extend(src.rglob("*.md"))
    return docs

# ── Main ──────────────────────────────────────────────────────────────────────
def build_index(reset=False, single_file=None):
    print("🧠 NAMI Knowledge Base Indexer")
    print(f"📁 Workspace : {WORKSPACE}")
    print(f"💾 Vector DB : {CHROMA_DIR}\n")

    CHROMA_DIR.mkdir(parents=True, exist_ok=True)
    client = chromadb.PersistentClient(path=str(CHROMA_DIR))
    ef     = embedding_functions.DefaultEmbeddingFunction()

    if reset:
        print("🗑️  Resetting collection...")
        try: client.delete_collection(COLLECTION)
        except Exception: pass

    col = client.get_or_create_collection(
        name=COLLECTION,
        embedding_function=ef,
        metadata={
            "description": "NAMI personal knowledge base",
            "hnsw:space": "cosine"
        }
    )

    docs = collect_docs(single_file)
    print(f"📄 {len(docs)} documents found\n")

    indexed = skipped = 0
    for path in docs:
        if not path.exists():
            print(f"  ⚠️  Missing: {path.name}"); skipped += 1; continue
        try:
            content = path.read_text(encoding="utf-8", errors="ignore")
            if len(content.strip()) < 10:
                skipped += 1; continue
            chunks = chunk_text(content)
            h = file_hash(path)
            for i, chunk in enumerate(chunks):
                did = f"{h}_{i}"
                try: col.delete(ids=[did])
                except Exception: pass
                col.add(
                    ids=[did],
                    documents=[chunk],
                    metadatas=[{
                        "source":     str(path),
                        "filename":   path.name,
                        "type":       doc_type(path),
                        "chunk":      i,
                        "indexed_at": datetime.now().isoformat(),
                    }]
                )
            print(f"  ✅ {path.name} ({len(chunks)} chunks)")
            indexed += 1
        except Exception as e:
            print(f"  ❌ {path.name}: {e}")

    print(f"\n✨ Indexed: {indexed} | Skipped: {skipped}")
    print(f"📊 Total chunks in store: {col.count()}")

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--reset", action="store_true")
    p.add_argument("--file",  type=str)
    a = p.parse_args()
    build_index(reset=a.reset, single_file=a.file)
