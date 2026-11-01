from fastapi import APIRouter

from .rag.pipeline import pipelineResponse
from .schemas import query

router = APIRouter()


@router.post("/pregunta")
def pregunta(body: query):
    respuesta = pipelineResponse(body.pregunta)
    return {"respuesta": respuesta}
