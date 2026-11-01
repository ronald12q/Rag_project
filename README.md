# RAG ANDA

RAG sobre la base de conocimiento de ANDA. API en FastAPI que recupera
contexto con embeddings de Jina AI + Pinecone y genera la respuesta con Groq.

## Requisitos

- Python 3.10+
- Claves de Jina AI, Groq y Pinecone

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example app/.env   # y completa tus claves
```

Variables de entorno (`app/.env`):

| Key              | Uso                    |
| ---------------- | ---------------------- |
| jina_ai_key      | embeddings (Jina AI)   |
| groq_api_key     | generación (Groq)      |
| pinecone_api_key | índice vectorial       |

## Indexar

```bash
# 1. Crear el índice en Pinecone (solo una vez)
python scripts/createIndex.py

# 2. Cargar data/source.csv al índice
python scripts/indexar.py
```

## Correr la API

```bash
uvicorn app.main:app --reload
```

- `GET /` — health check
- `POST /chat` — `{"pregunta": "..."}` → `{"respuesta": "..."}`
