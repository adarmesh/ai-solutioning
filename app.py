"""
Employee Knowledge Portal.

Serves the internal document corpus (HR policies, IT/security guidelines,
operational runbooks) through a simple browse-and-read web UI.

Run with:
    pip install -r requirements.txt
    uvicorn app:app --reload
Then open http://127.0.0.1:8000
"""

from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

DOCS_DIR = Path(__file__).parent / "docs"
STATIC_DIR = Path(__file__).parent / "static"

app = FastAPI(title="Employee Knowledge Portal")
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


class Document(BaseModel):
    doc_id: str
    title: str
    text: str


def load_corpus() -> list[Document]:
    """Loads every .md file in /docs into memory as a Document."""
    documents = []
    for path in sorted(DOCS_DIR.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        title = text.splitlines()[0].lstrip("# ").strip() if text else path.stem
        documents.append(Document(doc_id=path.stem, title=title, text=text))
    return documents


CORPUS = load_corpus()


@app.get("/")
def index():
    return FileResponse(STATIC_DIR / "index.html")


@app.get("/api/docs")
def list_docs():
    """Returns corpus metadata so the UI can list what's available."""
    return [{"doc_id": d.doc_id, "title": d.title} for d in CORPUS]


@app.get("/api/docs/{doc_id}")
def get_doc(doc_id: str):
    """Returns the full text of a single document."""
    for doc in CORPUS:
        if doc.doc_id == doc_id:
            return doc
    raise HTTPException(status_code=404, detail="Document not found")
