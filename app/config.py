from pathlib import Path

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = BASE_DIR.parent


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=BASE_DIR / ".env", extra="ignore")
    jina_ai_key: SecretStr
    groq_api_key: SecretStr
    pinecone_api_key: SecretStr
    top_k: int = 3
    scoreThreshold: float = 0.50
    pineconeNamespace: str = "ANDA-RAG"
    groqModel: str = "openai/gpt-oss-120b"
    embeddingModel: str = "jina-embeddings-v5-omni-small"
    jinaAI_Base_url: str = "https://api.jina.ai/v1"
    groq_Base_url: str = "https://api.groq.com/openai/v1"
    pineconeDimension: int = 1024
    pineMetric: str = "cosine"
    indexName: str = "rag-anda"
    dataPath: str = str(PROJECT_ROOT / "data" / "source.csv")


settings = Settings()
