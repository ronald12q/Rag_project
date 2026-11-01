import time

from pinecone import ServerlessSpec

from app.config import settings
from app.rag.clients import clients


def main():
    existing = [i.name for i in clients.pc.list_indexes()]
    if settings.indexName in existing:
        print(f"el index: {settings.indexName} ya existe")
        return
    clients.pc.create_index(
        name=settings.indexName,
        dimension=settings.pineconeDimension,
        metric=settings.pineMetric,
        spec=ServerlessSpec(cloud="aws", region="us-east-1"),
    )

    while not clients.pc.describe_index(settings.indexName).status["ready"]:
        time.sleep(1)

    print("indice creado exitosamente")


if __name__ == "__main__":
    main()
