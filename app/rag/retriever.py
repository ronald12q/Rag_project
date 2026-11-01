from ..config import settings
from .clients import clients


def get_index():
    return clients.pc.index(settings.indexName)


def queryEmbedding(query: str):
    response = clients.jinaAIclient.embeddings.create(
        model=settings.embeddingModel,
        input=[query],
        extra_body={"task": "retrieval.query"},
    )
    return response.data[0].embedding


def executeQuery(query: str):
    index = get_index()
    vectorQuery = queryEmbedding(query)
    res = index.query(
        vector=vectorQuery,
        top_k=settings.top_k,
        include_metadata=True,
        namespace=settings.pineconeNamespace,
    )
    relevantes = [e for e in res.matches if e.score >= settings.scoreThreshold]
    return relevantes
