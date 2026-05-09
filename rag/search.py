"""
NAMI Knowledge Base Search
Semantic search across indexed documents.

Usage:
    python search.py "query here"
    python search.py "query" --type context_log
    python search.py "query" --results 10
"""

import os
import sys
import argparse
from pathlib import Path

try:
    import chromadb
    from chromadb.utils import embedding_functions
except ImportError:
    print("ERROR: chromadb not installed. Run: pip install chromadb")
    sys.exit(1)

WORKSPACE  = Path(os.environ.get(
    "OPENCLAW_WORKSPACE",
    Path.home() / ".openclaw" / "workspace"
))
CHROMA_DIR = WORKSPACE / "rag" / "chroma_db"
COLLECTION = "nami_knowledge"

def search(query: str, n_results: int = 5, doc_type: str = None):
    if not CHROMA_DIR.exists():
        print("❌ Knowledge base not initialized.")
        print("   Run: python indexer.py")
        sys.exit(1)

    client = chromadb.PersistentClient(path=str(CHROMA_DIR))
    ef     = embedding_functions.DefaultEmbeddingFunction()

    try:
        col = client.get_collection(COLLECTION, embedding_function=ef)
    except Exception:
        print("❌ Collection not found. Run: python indexer.py")
        sys.exit(1)

    where = {"type": doc_type} if doc_type else None

    results = col.query(
        query_texts=[query],
        n_results=min(n_results, col.count()),
        where=where,
        include=["documents", "metadatas", "distances"]
    )

    docs      = results["documents"][0]
    metas     = results["metadatas"][0]
    distances = results["distances"][0]

    if not docs:
        print(f"No results found for: '{query}'")
        return

    print(f"🔍 Search: \"{query}\"")
    if doc_type:
        print(f"   Filter: type={doc_type}")
    print(f"   {len(docs)} result(s)\n")
    print("━" * 60)

    for i, (doc, meta, dist) in enumerate(zip(docs, metas, distances), 1):
        relevance = round((1 - dist) * 100, 1)
        filename  = meta.get("filename", "unknown")
        dtype     = meta.get("type", "document")
        preview   = doc[:300].replace("\n", " ").strip()
        if len(doc) > 300:
            preview += "..."

        print(f"\n[{i}] {filename} ({dtype}) — {relevance}% match")
        print(f"    {preview}")

    print("\n" + "━" * 60)
    print(f"📊 {col.count()} total chunks indexed")

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("query",             type=str, help="Search query")
    p.add_argument("--results", "-n",   type=int, default=5)
    p.add_argument("--type",    "-t",   type=str, help="Filter: identity|context_log|projects|skill|document")
    a = p.parse_args()
    search(a.query, a.results, a.type)
