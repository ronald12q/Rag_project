# RAG ANDA

RAG over the ANDA knowledge base. FastAPI API that retrieves
context with Jina AI embeddings + Pinecone and generates the answer with Groq.

## Requirements

- Python 3.10+
- Jina AI, Groq and Pinecone API keys

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example app/.env   # then fill in your keys
```

Environment variables (`app/.env`):

| Key              | Usage             |
| ---------------- | ----------------- |
| jina_ai_key      | embeddings (Jina AI) |
| groq_api_key     | generation (Groq) |
| pinecone_api_key | vector index      |

## Indexing

```bash
# 1. Create the index in Pinecone (only once)
python scripts/createIndex.py

# 2. Load data/source.csv into the index
python scripts/indexar.py
```

## Running the API

```bash
uvicorn app.main:app --reload
```

- `GET /` — root, `{"message": "server running"}`
- `GET /health` — health check, `{"status": "ok"}`
- `POST /chat` — `{"pregunta": "..."}` → `{"respuesta": "..."}`
