# Employee Knowledge Portal

An internal web app for browsing company documentation - HR policies, IT/
security guidelines, and operational runbooks. These documents are only
published here; there is no other system that holds them.

## Run it

```bash
pip install -r requirements.txt
uvicorn app:app --reload
```

Open <http://127.0.0.1:8000>

## What's here

- `docs/` - the document corpus (Markdown), served as-is.
- `app.py` - FastAPI app that loads the corpus and exposes it via
  `GET /api/docs` (list) and `GET /api/docs/{doc_id}` (full text).
- `static/index.html` - the portal UI: a document list and a reading pane.
