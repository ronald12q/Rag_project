from openai import OpenAI
from pinecone import Pinecone

from ..config import settings


class Clients:
    jinaAIclient = OpenAI(
        base_url=settings.jinaAI_Base_url,
        api_key=settings.jina_ai_key.get_secret_value(),
    )
    groqAIclient = OpenAI(
        base_url=settings.groq_Base_url,
        api_key=settings.groq_api_key.get_secret_value(),
    )
    pc = Pinecone(api_key=settings.pinecone_api_key.get_secret_value())


clients = Clients()
