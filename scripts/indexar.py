from pathlib import Path

import pandas as pd

from app.config import settings
from app.rag.clients import clients


def EmbeddingFun(array: list[str]):
    vector = []
    response = clients.jinaAIclient.embeddings.create(
        model=settings.embeddingModel,
        input=array,
        extra_body={"task": "retrieval.passage"},
    )
    vector = [item.embedding for item in response.data]
    return vector


def embeddedFun(arrayEmbedded: list[str], batchSize: int = 10):
    embeddingVector = []
    for start in range(0, len(arrayEmbedded), batchSize):
        lote = arrayEmbedded[start : start + batchSize]
        response = EmbeddingFun(lote)
        for vector in response:
            embeddingVector.append(vector)
    return embeddingVector


def createVector(
    arrayEmbedding: list[str], contenido: list[str], titulo: list[str], ID: list[str]
):
    vectors = embeddedFun(arrayEmbedding)
    vectorsPinecone = []
    for i, vector in enumerate(vectors):
        vectorsPinecone.append(
            {
                "id": ID[i],
                "values": vector,
                "metadata": {"titulo": titulo[i], "contenido": contenido[i]},
            }
        )
    return vectorsPinecone


if __name__ == "__main__":
    pathData = Path(settings.dataPath)
    df = pd.read_csv(pathData)
    df = df.dropna(subset=["texto_embedding", "id", "contenido", "titulo"])

    textEmbedding = df["texto_embedding"].astype(str).tolist()
    ragID = df["id"].astype(str).tolist()
    ragContenido = df["contenido"].astype(str).tolist()
    ragTitulo = df["titulo"].astype(str).tolist()

    index = clients.pc.index(settings.indexName)

    Vectors = createVector(textEmbedding, ragContenido, ragTitulo, ragID)

    for start in range(0, len(Vectors), 100):
        lote = Vectors[start : start + 100]
        index.upsert(vectors=lote, namespace=settings.pineconeNamespace)
    print("datos cargados")
